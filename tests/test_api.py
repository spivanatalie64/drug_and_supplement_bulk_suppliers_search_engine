"""API tests."""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db import init_db, search
from app.seed_data import SUPPLIERS


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
