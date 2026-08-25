# BulkSource — Drug & Supplement Bulk Suppliers Search Engine

Full-text search engine over a curated index of **legitimate bulk/wholesale suppliers** of
dietary supplements, raw ingredients, botanicals, APIs and licensed pharmaceutical distribution.

FastAPI + SQLite FTS5 backend, zero-dependency vanilla JS frontend.

## Features

- **Relevance search** — SQLite FTS5 with bm25 ranking across name, description,
  products, tags *and* certifications (typo-tolerant prefix matching)
- **Faceted filtering** — category, country, certification (multi-select)
- **REST API** — `/api/search`, `/api/suppliers/{id}`, `/api/facets`, `/healthz`
- **Web UI** — single-page dark UI served at `/`
- **29-company seed index** — real companies: BulkSupplements, PureBulk, Prinova,
  Glanbia Nutritionals, Starwest Botanicals, Cayman Chemical, Suanfarma, McKesson,
  Cencora, Cardinal Health and more

## Quick start

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m app.db          # build + seed data/suppliers.db (idempotent)
.venv/bin/uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000 — try queries like `creatine`, `organic herbs`, `gmp capsules`.

## API examples

```bash
curl 'localhost:8000/api/search?q=creatine'
curl 'localhost:8000/api/search?category=botanical&cert=USDA%20Organic'
curl 'localhost:8000/api/suppliers/1'
curl 'localhost:8000/api/facets'
```

Query params for `/api/search`: `q`, `category` (repeatable), `country` (repeatable),
`cert` (repeatable), `limit` ≤ 100, `offset`.

Categories: `ingredient` · `finished` · `botanical` · `api` · `pharma_dist`

## Tests

```bash
.venv/bin/pytest -q
```

## Project layout

```
app/main.py        FastAPI routes + static mounting
app/db.py          schema, FTS5 triggers, sanitize_query, search/facets
app/seed_data.py   curated supplier dataset (edit to extend the index)
static/index.html  frontend (vanilla JS)
tests/test_api.py  pytest suite (TestClient)
```

## Disclaimer

The seed dataset is an informational starting point for B2B sourcing research.
Minimum order quantities are typical published values and may change.
**Always verify** FDA registration / DEA licensing / state wholesale licenses and
certifications directly with a supplier before transacting. Nothing here is medical,
legal or purchasing advice; intended for lawful sourcing only.
