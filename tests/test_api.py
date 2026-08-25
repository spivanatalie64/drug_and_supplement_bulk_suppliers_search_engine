"""API tests."""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db import init_db, search
from app.seed_data import ALL_SUPPLIERS as SUPPLIERS


@pytest.fixture(scope="module", autouse=True)
def _db():
    init_db(SUPPLIERS)


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_search_finds_creatine():
    results, total = search("creatine")
    names = {r["name"] for r in results}
    assert total >= 2
    assert "BulkSupplements.com" in names and "PureBulk Inc" in names


def test_search_sanitizes_fts_operators():
    # should not raise an FTS syntax error
    results, _total = search('"creatine" AND (monohydrate)')
    assert isinstance(results, list)


def test_category_filter():
    results, total = search("", category=["botanical"])
    assert total == 5
    assert all(r["category"] == "botanical" for r in results)


def test_cert_filter():
    results, total = search("herbs", cert=["USDA Organic"])
    assert total >= 1
    assert any("Starwest" in r["name"] for r in results)


def test_marketplaces_indexed_with_pricing():
    results, total = search("", category=["marketplace"])
    assert total >= 7
    assert any(r["name"] == "Alibaba.com" for r in results)
    assert all("price_examples" in r for r in results)


def test_price_and_pack_fields_returned():
    results, _ = search("creatine")
    top = results[0]
    assert top["pack_sizes"] and top["price_examples"]
    assert "unit" in top["price_examples"][0]


def test_drug_lookup_sertraline():
    from app.db import search_drugs
    hits = search_drugs("sertraline")
    assert hits and hits[0]["name"] == "Sertraline"
    assert hits[0]["kind"] == "rx"

def test_distributors_findable_by_molecule():
    results, total = search("sertraline", category=["pharma_dist"])
    assert total >= 3

def test_api_endpoints(client):
    r = client.get("/api/search", params={"q": "vitamin"})
    assert r.status_code == 200
    body = r.json()
    assert {"query", "total", "results"} <= set(body)
    assert body["total"] >= 1

    r2 = client.get("/api/facets")
    assert r2.status_code == 200
    facets = r2.json()
    assert {"categories", "countries", "certifications"} <= set(facets)

    sid = body["results"][0]["id"]
    r3 = client.get(f"/api/suppliers/{sid}")
    assert r3.status_code == 200
    assert r3.json()["name"]

    r4 = client.get("/api/suppliers/999999")
    assert r4.status_code == 404


def test_healthz(client):
    assert client.get("/healthz").json() == {"ok": True}
