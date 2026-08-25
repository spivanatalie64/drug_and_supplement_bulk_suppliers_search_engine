"""MCP server exposing the BulkSource supplier index as tools.

Run via stdio transport; used by opencode (and any MCP client):
    .venv/bin/python mcp_server.py
"""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

try:  # standalone FastMCP (fastmcp>=2) or SDK-bundled (mcp<2)
    from fastmcp import FastMCP
except ImportError:
    from mcp.server.fastmcp import FastMCP

from app.db import CATEGORY_LABELS, facets, get_supplier, init_db, search, search_drugs
from app.seed_data import ALL_SUPPLIERS as SUPPLIERS
from app.seed_data import DRUGS

init_db(SUPPLIERS, DRUGS)  # auto-create/seed index on startup

mcp = FastMCP(
    "bulksource",
    instructions=(
        "Search engine for bulk/wholesale suppliers of drugs & supplements. "
        "Use search_suppliers for queries, get_facets to discover filter values, "
        "get_supplier_details for a single company."
    ),
)


@mcp.tool()
def search_suppliers(
    q: str = "",
    category: list[str] | None = None,
    country: list[str] | None = None,
    cert: list[str] | None = None,
    limit: int = 20,
) -> dict:
    """Full-text search of bulk drug/supplement suppliers.

    Args:
        q: free-text query (e.g. "creatine", "organic herbs", "gmp capsules")
        category: filter by one or more of ingredient|finished|botanical|api|pharma_dist
        country: filter by country name (e.g. "USA", "China")
        cert: filter by certification substring (e.g. "GMP", "USDA Organic", "DEA")
        limit: max results (default 20)
    Returns {"total": int, "results": [...]} with relevance-ranked suppliers.
    """
    results, total = search(q=q, category=category, country=country,
                            cert=cert, limit=min(max(limit, 1), 100))
    drug_matches = search_drugs(q) if q.strip() else []
    return {"total": total, "drugs": drug_matches, "results": results}


@mcp.tool()
def get_supplier_details(supplier_id: int) -> dict:
    """Fetch full record (website, MOQ, certifications, products) for one supplier by id."""
    s = get_supplier(supplier_id)
    return s if s else {"error": f"no supplier with id {supplier_id}"}


@mcp.tool()
def get_facets() -> dict:
    """List available filter values with counts: categories, countries, certifications."""
    return facets()


@mcp.resource("bulksource://categories")
def categories() -> str:
    """Category codes and labels."""
    return "\n".join(f"{k} = {v}" for k, v in CATEGORY_LABELS.items())


if __name__ == "__main__":
    mcp.run()
