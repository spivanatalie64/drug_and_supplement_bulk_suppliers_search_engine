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
- **Drug-name lookup** — search `sertraline`, `melatonin`, `ibuprofen`… and get
  a drug card (kind, description, legitimate sourcing channels) plus matching
  licensed distributors; 38 molecules/actives indexed
- **64-supplier index** — real companies across CN/KR/IN/US/CA/UK/DE/EU:
  BulkSupplements, Divi's Labs, Dr. Reddy's, CSPC, Hisun, Celltrion, Apotex,
  Jamieson, PHOENIX group, Evonik, McKesson, Cencora, Cardinal Health and more
- **Pricing & quantities** — indicative bulk price examples ($/kg etc.), pack sizes
  and MOQ notes per supplier; searchable ("$45 kg", "25 kg drum")
- **B2B marketplaces indexed** — Alibaba.com, Made-in-China.com, IndiaMART,
  Global Sources, DHgate, ThomasNet, EC21

## Quick start

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m app.db          # build + seed data/suppliers.db (idempotent)
.venv/bin/uvicorn app.main:app --reload --port 8010
```

Open http://localhost:8010 — try queries like `creatine`, `organic herbs`, `gmp capsules`.

## Run as a service (auto-start)

```bash
cp deploy/bulksource.service ~/.config/systemd/user/
systemctl --user daemon-reload && systemctl --user enable --now bulksource
loginctl enable-linger $USER   # keep it running across reboots without login
```

Web UI: http://localhost:8010

A desktop launcher (`bulksource.desktop`) can be installed for one-click browser access:

```bash
cp deploy/bulksource.desktop ~/.local/share/applications/
cp deploy/bulksource.desktop ~/Desktop/ && chmod +x ~/Desktop/bulksource.desktop
```

## MCP server (use from AI agents / opencode)

`mcp_server.py` exposes the index as MCP tools over stdio — `search_suppliers`,
`get_supplier_details`, `get_facets`. It auto-seeds the DB on startup.
Register in opencode (`~/.config/opencode/opencode.jsonc`):

```jsonc
{
  "mcp": {
    "bulksource": {
      "type": "local",
      "command": ["<project>/.venv/bin/python", "<project>/mcp_server.py"],
      "enabled": true,
      "environment": {}
    }
  }
}
```

Smoke-test by hand:

```bash
printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"t","version":"0"}}}\n' | \
  .venv/bin/python mcp_server.py | head -1

## API examples

```bash
curl 'localhost:8010/api/search?q=creatine'
curl 'localhost:8010/api/search?category=botanical&cert=USDA%20Organic'
curl 'localhost:8010/api/suppliers/1'
curl 'localhost:8010/api/facets'
```

Query params for `/api/search`: `q`, `category` (repeatable), `country` (repeatable),
`cert` (repeatable), `limit` ≤ 100, `offset`. Responses include `drugs` (molecule
matches) alongside supplier `results`.

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
mcp_server.py      MCP stdio server (search_suppliers / get_supplier_details / get_facets)
static/index.html  frontend (vanilla JS)
tests/test_api.py  pytest suite (TestClient)
```

## Disclaimer

The seed dataset is an informational starting point for B2B sourcing research.
Minimum order quantities are typical published values and may change.
**Always verify** FDA registration / DEA licensing / state wholesale licenses and
certifications directly with a supplier before transacting. Nothing here is medical,
legal or purchasing advice; intended for lawful sourcing only.
