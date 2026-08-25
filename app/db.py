"""SQLite persistence + FTS5 full-text search layer."""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "suppliers.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS suppliers (
    id           INTEGER PRIMARY KEY,
    name         TEXT NOT NULL UNIQUE,
    category     TEXT NOT NULL CHECK (category IN ('ingredient','finished','botanical','api','pharma_dist')),
    website      TEXT NOT NULL,
    country      TEXT NOT NULL,
    location     TEXT NOT NULL DEFAULT '',
    moq          TEXT NOT NULL DEFAULT '',
    certifications TEXT NOT NULL DEFAULT '[]',
    products     TEXT NOT NULL DEFAULT '[]',
    description  TEXT NOT NULL,
    tags         TEXT NOT NULL DEFAULT '[]'
);
CREATE VIRTUAL TABLE IF NOT EXISTS suppliers_fts USING fts5(
    name, description, products, tags, certs,
    content='suppliers', content_rowid='id'
);
CREATE TRIGGER IF NOT EXISTS suppliers_ai AFTER INSERT ON suppliers BEGIN
    INSERT INTO suppliers_fts(rowid, name, description, products, tags, certs)
    VALUES (new.id, new.name, new.description, new.products, new.tags, new.certifications);
END;
CREATE TRIGGER IF NOT EXISTS suppliers_ad AFTER DELETE ON suppliers BEGIN
    INSERT INTO suppliers_fts(suppliers_fts, rowid, name, description, products, tags, certs)
    VALUES ('delete', old.id, old.name, old.description, old.products, old.tags, old.certifications);
END;
CREATE TRIGGER IF NOT EXISTS suppliers_au AFTER UPDATE ON suppliers BEGIN
    INSERT INTO suppliers_fts(suppliers_fts, rowid, name, description, products, tags, certs)
    VALUES ('delete', old.id, old.name, old.description, old.products, old.tags, old.certifications);
    INSERT INTO suppliers_fts(rowid, name, description, products, tags, certs)
    VALUES (new.id, new.name, new.description, new.products, new.tags, new.certifications);
END;
"""

CATEGORY_LABELS = {
    "ingredient": "Bulk ingredients",
    "finished": "Finished goods",
    "botanical": "Botanicals",
    "api": "APIs & chemicals",
    "pharma_dist": "Pharma distribution",
}


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(seed_rows: list[dict[str, Any]] | None = None) -> int:
    """Create schema; seed only when table empty. Returns row count."""
    with connect() as conn:
        conn.executescript(SCHEMA)
        count = conn.execute("SELECT COUNT(*) FROM suppliers").fetchone()[0]
        if count == 0 and seed_rows:
            for row in seed_rows:
                conn.execute(
                    """INSERT INTO suppliers
                       (name, category, website, country, location, moq,
                        certifications, products, description, tags)
                       VALUES (?,?,?,?,?,?,?,?,?,?)""",
                    (
                        row["name"], row["category"], row["website"], row["country"],
                        row.get("location", ""), row.get("moq", ""),
                        json.dumps(row.get("certifications", [])),
                        json.dumps(row.get("products", [])),
                        row["description"],
                        json.dumps(row.get("tags", [])),
                    ),
                )
            count = len(seed_rows)
        return count


def _row_to_dict(r: sqlite3.Row) -> dict[str, Any]:
    d = dict(r)
    d.pop("rank", None)
    d["category_label"] = CATEGORY_LABELS.get(d["category"], d["category"])
    d["certifications"] = json.loads(d.pop("certifications") or "[]")
    d["products"] = json.loads(d.pop("products") or "[]")
    d["tags"] = json.loads(d.pop("tags") or "[]")
    return d


def sanitize_query(q: str) -> str:
    """Make user text safe for FTS5 MATCH: strip operators/quotes/reserved keywords."""
    cleaned = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in q)
    return " ".join(
        t + "*" for t in cleaned.split() if t and t.upper() not in {"AND", "OR", "NOT", "NEAR"}
    )


def search(
    q: str = "",
    category: list[str] | None = None,
    country: list[str] | None = None,
    cert: list[str] | None = None,
    limit: int = 50,
    offset: int = 0,
) -> tuple[list[dict[str, Any]], int]:
    """Return (results, total). FTS5 relevance ranking when q given; alphabetical otherwise."""
    where: list[str] = []
    params: list[Any] = []
    if category:
        where.append(f"s.category IN ({','.join('?' * len(category))})")
        params += category
    if country:
        where.append(f"s.country IN ({','.join('?' * len(country))})")
        params += country
    if cert:
        likes = " OR ".join(["s.certifications LIKE ?"] * len(cert))
        where.append(f"({likes})")
        params += [f'%"{c}"%' for c in cert]

    if q.strip():
        match = sanitize_query(q)
        join = "JOIN suppliers_fts f ON f.rowid = s.id"
        cond = " AND ".join(["suppliers_fts MATCH ?", *where])
        total_args = [match, *params]
        rows_args = [match, *params, limit, offset]
        total_sql = f"SELECT COUNT(*) FROM suppliers s {join} WHERE {cond}"
        sql = (
            f"SELECT s.*, bm25(suppliers_fts) AS rank FROM suppliers s {join} "
            f"WHERE {cond} ORDER BY rank LIMIT ? OFFSET ?"
        )
    else:
        cond = ("WHERE " + " AND ".join(where)) if where else ""
        total_args = [*params]
        rows_args = [*params, limit, offset]
        total_sql = f"SELECT COUNT(*) FROM suppliers s {cond}"
        sql = (
            f"SELECT s.* FROM suppliers s {cond} "
            f"ORDER BY s.name COLLATE NOCASE LIMIT ? OFFSET ?"
        )

    with connect() as conn:
        total = conn.execute(total_sql, total_args).fetchone()[0]
        rows = conn.execute(sql, rows_args).fetchall()
    return [_row_to_dict(r) for r in rows], total


def get_supplier(supplier_id: int) -> dict[str, Any] | None:
    with connect() as conn:
        r = conn.execute("SELECT * FROM suppliers WHERE id=?", (supplier_id,)).fetchone()
        return _row_to_dict(r) if r else None


def facets() -> dict[str, list]:
    with connect() as conn:
        cats = [
            {"value": r["value"], "label": CATEGORY_LABELS.get(r["value"], r["value"]), "count": r["n"]}
            for r in conn.execute(
                "SELECT category AS value, COUNT(*) AS n FROM suppliers GROUP BY category ORDER BY n DESC"
            ).fetchall()
        ]
        countries = [
            {"value": r["value"], "count": r["n"]}
            for r in conn.execute(
                "SELECT country AS value, COUNT(*) AS n FROM suppliers GROUP BY country ORDER BY n DESC"
            ).fetchall()
        ]
        counts: dict[str, int] = {}
        for (raw,) in conn.execute("SELECT certifications FROM suppliers"):
            for c in json.loads(raw or "[]"):
                counts[c] = counts.get(c, 0) + 1
        certs = sorted(
            ({"value": k, "count": v} for k, v in counts.items()), key=lambda x: -x["count"]
        )
    return {"categories": cats, "countries": countries, "certifications": certs}


if __name__ == "__main__":
    from .seed_data import SUPPLIERS

    print(f"seeded/loaded: {init_db(SUPPLIERS)} suppliers at {DB_PATH}")
