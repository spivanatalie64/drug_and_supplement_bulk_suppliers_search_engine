"""FastAPI application: bulk drug & supplement supplier search engine."""
from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .db import facets, get_supplier, init_db, search, search_drugs
from .seed_data import ALL_SUPPLIERS as SUPPLIERS
from .seed_data import DRUGS

BASE_DIR = Path(__file__).resolve().parent.parent


@asynccontextmanager
async def lifespan(_app: FastAPI):
    count = init_db(SUPPLIERS, DRUGS)
    print(f"[startup] {count} suppliers in index")
    yield


app = FastAPI(
    title="Drug & Supplement Bulk Suppliers Search Engine",
    description="Full-text search over a curated index of legitimate bulk/wholesale suppliers "
                "of supplements, ingredients, botanicals, APIs and pharmaceutical distribution.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/api/search")
def api_search(
    q: str = Query("", max_length=200, description="Free-text query"),
    category: list[str] = Query(default=[], description="ingredient|finished|botanical|api|pharma_dist"),
    country: list[str] = Query(default=[]),
    cert: list[str] = Query(default=[], description="Certification substring, e.g. GMP"),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    results, total = search(q=q, category=category or None, country=country or None,
                            cert=cert or None, limit=limit, offset=offset)
    drug_matches = search_drugs(q) if q.strip() else []
    return {"query": q, "total": total, "limit": limit, "offset": offset,
            "drugs": drug_matches, "results": results}


@app.get("/api/suppliers/{supplier_id}")
def api_supplier(supplier_id: int):
    s = get_supplier(supplier_id)
    if not s:
        raise HTTPException(404, "Supplier not found")
    return s


@app.get("/api/facets")
def api_facets():
    return facets()


@app.get("/healthz")
def healthz():
    return {"ok": True}


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(BASE_DIR / "static" / "index.html")


app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
