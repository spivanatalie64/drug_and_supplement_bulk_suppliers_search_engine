"""Curated seed dataset: legitimate bulk/wholesale suppliers of drugs & supplements.

Categories:
  ingredient   - bulk raw ingredients for supplements/nutraceuticals
  finished     - wholesale finished supplements / OTC products
  pharma_dist  - licensed pharmaceutical wholesale distribution
  api          - active pharmaceutical ingredients / fine chemicals
  botanical    - bulk herbs & botanicals

MOQ values are typical published minimums; always confirm with the supplier.
"""

SUPPLIERS = [
    # ---------------- Bulk supplement ingredients (US/EU) ----------------
    {
        "name": "BulkSupplements.com",
        "category": "ingredient",
        "website": "https://www.bulksupplements.com",
        "country": "USA",
        "location": "Henderson, NV",
        "moq": "From 100 g; kg quantities standard",
        "certifications": ["cGMP", "FDA-registered facility", "Third-party tested"],
        "products": ["amino acids", "vitamins", "minerals", "creatine monohydrate", "caffeine anhydrous", "herbal extracts", "sweeteners"],
        "description": "Pure bulk powder ingredients sold direct-to-consumer and B2B by the gram to metric ton.",
        "tags": ["powders", "sports nutrition", "no minimum cases"],
    },
    {
        "name": "PureBulk Inc",
        "category": "ingredient",
        "website": "https://purebulk.com",
        "country": "USA",
        "location": "Roseburg, OR",
        "moq": "Gram to multi-kg sizes",
        "certifications": ["GMP", "Third-party lab tested (COA per lot)"],
        "products": ["creatine", "BCAAs", "vitamin powders", "nootropic compounds", "extracts"],
        "description": "Pure bulk nutritional powders and capsules with per-lot certificates of analysis.",
        "tags": ["powders", "COA", "sports nutrition"],
    },
    {
        "name": "NutriScience Innovations LLC",
        "category": "ingredient",
        "website": "https://www.nutriscienceusa.com",
        "country": "USA",
        "location": "Mystic, CT",
        "moq": "Kilogram scale; drum lots available",
        "certifications": ["GMP", "ISO 9001", "FDA-registered facility"],
        "products": ["NAC", "alpha-GPC", "CoQ10", "amino acids", "specialty actives"],
        "description": "Supplier of specialty nutraceutical and pharmaceutical-grade raw materials to manufacturers.",
        "tags": ["specialty chemicals", "branded ingredients"],
    },
    {
        "name": "IngredientsOnline.com",
        "category": "ingredient",
        "website": "https://www.ingredientsonline.com",
        "country": "USA",
        "location": "La Palma, CA",
        "moq": "Case/pallet via RFQ",
        "certifications": ["Vetted factory network", "GMP factories"],
        "products": ["vitamins", "minerals", "botanical extracts", "functional ingredients"],
        "description": "B2B marketplace connecting manufacturers with vetted ingredient factories; transparent pricing and COAs.",
        "tags": ["marketplace", "RFQ", "supply chain"],
    },
    {
        "name": "Prinova Global Solutions",
        "category": "ingredient",
        "website": "https://www.prinovaglobal.com",
        "country": "USA",
        "location": "Carol Stream, IL",
        "moq": "Pallet/distributor scale",
        "certifications": ["GMP warehouses", "Food safety certified"],
        "products": ["vitamins", "sweeteners", "proteins", "flavors", "custom premixes"],
        "description": "Global ingredient distributor offering blending, premixes and supply-chain services.",
        "tags": ["distributor", "premix", "blending"],
    },
    {
        "name": "Glanbia Nutritionals",
        "category": "ingredient",
        "website": "https://www.glanbianutritionals.com",
        "country": "USA",
        "location": "Chicago, IL",
        "moq": "Commercial volumes",
        "certifications": ["GMP", "FSMA compliant", "Organic options"],
        "products": ["proteins", "vitamin premixes", "functional ingredients", "grains/seeds"],
        "description": "Ingredient solutions provider: custom premix, micronization and agglomerated nutrient systems at scale.",
        "tags": ["premix", "large volume", "co-development"],
    },
    {
        "name": "Blue California",
        "category": "ingredient",
        "website": "https://www.bluecal-ingredients.com",
        "country": "USA",
        "location": "Rancho Santa Margarita, CA",
        "moq": "Kg to ton scale",
        "certifications": ["GMP", "ISO", "Fermentation-based actives"],
        "products": ["ergothioneine", "preservatives", "natural actives", "fermentation ingredients"],
        "description": "Developer and manufacturer of fermentation-derived and natural functional ingredients.",
        "tags": ["biotech", "actives", "clean label"],
    },
    {
        "name": "AIDP Inc",
        "category": "ingredient",
        "website": "https://www.aidp.com",
        "country": "USA",
        "location": "City of Industry, CA",
        "moq": "Kg to pallet",
        "certifications": ["GMP", "Branded ingredient science"],
        "products": ["Magtein magnesium L-threonate", "goFAT", "specialty nutrients"],
        "description": "Supplier of clinically researched branded nutraceutical ingredients.",
        "tags": ["branded ingredients", "clinical research"],
    },
    {
        "name": "Jiaherb Inc",
        "category": "ingredient",
        "website": "https://www.jiaherb.com",
        "country": "USA",
        "location": "Totowa, NJ",
        "moq": "Kg to drum",
        "certifications": ["GMP", "NSF-audited factories", "Organic options"],
        "products": ["botanical extracts", "fruit/vegetable powders", "standardized extracts"],
        "description": "Manufacturer-distributor of botanical extracts with in-house labs and vertically integrated farms.",
        "tags": ["botanicals", "extracts", "vertically integrated"],
    },

    # ---------------- Wholesale finished supplements ----------------
    {
        "name": "NOW Natural Foods (Wholesale)",
        "category": "finished",
        "website": "https://www.nowfoods.com",
        "country": "USA",
        "location": "Bloomingdale, IL",
        "moq": "Case quantities via distributors",
        "certifications": ["GMP", "UL-certified facilities", "Non-GMO Project", "In-house labs"],
        "products": ["vitamins", "supplements", "sports nutrition", "personal care", "essential oils"],
        "description": "Family-owned natural products manufacturer selling wholesale through authorized distributors.",
        "tags": ["brand owner", "authorized distributors"],
    },
    {
        "name": "Piping Rock Health Products",
        "category": "finished",
        "website": "https://www.pipingrock.com",
        "country": "USA",
        "location": "Ronkonkoma, NY",
        "moq": "Low case minimums; private label available",
        "certifications": ["GMP", "In-house quality control"],
        "products": ["supplements", "essential oils", "vitamins", "herbal products"],
        "description": "Vertically integrated manufacturer offering finished supplements plus private-label programs.",
        "tags": ["private label", "own manufacturing"],
    },
    {
        "name": "Hard Rhino / BulkSupplements Private Label",
        "category": "finished",
        "website": "https://www.hardrhino.com",
        "country": "USA",
        "location": "Henderson, NV",
        "moq": "Small case minimums",
        "certifications": ["cGMP", "Lot-tested"],
        "products": ["capsules", "bulk powders", "private label supplements"],
        "description": "Finished-goods arm for private label sports nutrition and supplement products.",
        "tags": ["private label", "capsules"],
    },

    # ---------------- Botanical / herb wholesalers ----------------
    {
        "name": "Starwest Botanicals",
        "category": "botanical",
        "website": "https://www.starwest-botanicals.com",
        "country": "USA",
        "location": "Sacramento, CA",
        "moq": "Ounce to bulk sack",
        "certifications": ["USDA Organic", "cGMP", "Kosher"],
        "products": ["dried herbs", "spices", "essential oils", "teas", "powdered botanicals"],
        "description": "One of the largest bulk herb suppliers in the US; organic-certified processing facility.",
        "tags": ["organic herbs", "spices", "tea"],
    },
    {
        "name": "Mountain Rose Herbs",
        "category": "botanical",
        "website": "https://www.mountainroseherbs.com",
        "country": "USA",
        "location": "Eugene, OR",
        "moq": "No true minimum; bulk discounts",
        "certifications": ["USDA Organic", "Fair Trade partner", "Zero-waste facility"],
        "products": ["bulk herbs", "extracts", "essential oils", "clays", "carrier oils"],
        "description": "Certified organic processor of botanical goods emphasizing sustainability.",
        "tags": ["organic", "sustainable", "aromatherapy"],
    },
    {
        "name": "Monterey Bay Spice Co.",
        "category": "botanical",
        "website": "https://www.herbco.com",
        "country": "USA",
        "location": "Watsonville, CA",
        "moq": "Quarter-pound up",
        "certifications": ["Organic options", "Quality-tested botanicals"],
        "products": ["culinary herbs", "spices", "tea blends", "capsules"],
        "description": "Bulk herbs and spices for food, cosmetic and supplement makers.",
        "tags": ["culinary", "small business friendly"],
    },
    {
        "name": "Atlantic Spice Company",
        "category": "botanical",
        "website": "https://www.atlanticspice.com",
        "country": "USA",
        "location": "North Truro, MA",
        "moq": "Pound quantities",
        "certifications": ["Food-grade handling"],
        "products": ["spices", "herbs", "baking ingredients", "sea vegetables"],
        "description": "Wholesale spice and herb house serving small manufacturers since 1990.",
        "tags": ["spices", "food service"],
    },
    {
        "name": "San Francisco Herb & Natural Food Co.",
        "category": "botanical",
        "website": "https://www.sfherb.com",
        "country": "USA",
        "location": "San Leandro, CA",
        "moq": "Pound quantities",
        "certifications": ["Organic lines available"],
        "products": ["bulk herbs", "spices", "potpourri botanicals"],
        "description": "Long-running West Coast wholesaler of herbs, spices and botanicals.",
        "tags": ["herbs", "crafters"],
    },

    # ---------------- Research / fine chemicals & APIs ----------------
    {
        "name": "Cayman Chemical",
        "category": "api",
        "website": "https://www.caymanchem.com",
        "country": "USA",
        "location": "Ann Arbor, MI",
        "moq": "mg to kg (research to pilot)",
        "certifications": ["GMP contract manufacturing", "ISO 13485 devices line"],
        "products": ["reference standards", "bioactive small molecules", "assay kits"],
        "description": "Chemical supplier and GMP contract manufacturer for pharmaceutical R&D.",
        "tags": ["research chemicals", "standards", "GMP scale-up"],
    },
    {
        "name": "Sigma-Aldrich (Merck KGaA)",
        "category": "api",
        "website": "https://www.sigmaaldrich.com",
        "country": "Germany/USA",
        "location": "Darmstadt, DE / St. Louis, MO",
        "moq": "Gram to ton",
        "certifications": ["ISO 9001", "Pharmacopeia grade (USP/EP)", "GMP sites"],
        "products": ["pharmaceutical excipients", "analytical standards", "fine chemicals", "buffers"],
        "description": "Global life-science catalog supplier covering lab through production volumes.",
        "tags": ["catalog giant", "excipients", "global"],
    },
    {
        "name": "Alfa Chemistry",
        "category": "api",
        "website": "https://www.alfa.com",
        "country": "USA",
        "location": "Stony Brook, NY",
        "moq": "Gram to kg",
        "certifications": ["Analytical COAs provided"],
        "products": ["organic reagents", "pharmaceutical impurity standards", "intermediates"],
        "description": "Catalog supplier of organic and analytical chemistry reagents worldwide.",
        "tags": ["reagents", "impurities", "intermediates"],
    },
    {
        "name": "Suanfarma",
        "category": "api",
        "website": "https://www.suanfarma.com",
        "country": "Spain/USA",
        "location": "Madrid, ES / Rocky Hill, NJ",
        "moq": "Commercial API volumes",
        "certifications": ["EU GMP", "US FDA-inspected plants", "CEP/DMF filings"],
        "products": ["APIs", "HPAPIs", "intermediates", "CDMO services"],
        "description": "API manufacturer and CDMO with FDA/EMA-inspected facilities on both continents.",
        "tags": ["CDMO", "DMF", "regulated markets"],
    },
    {
        "name": "PharmaCompass",
        "category": "api",
        "website": "https://www.pharmacompass.com",
        "country": "India",
        "location": "Hyderabad, IN",
        "moq": "Quote-based",
        "certifications": ["Directory of DMF/CEP holders"],
        "products": ["API sourcing", "supplier discovery", "regulatory intelligence"],
        "description": "Sourcing platform listing verified API manufacturers with DMF/CEP documentation status.",
        "tags": ["marketplace", "sourcing", "directory"],
    },
    {
        "name": "Xi'an Natural Field Biotechnology",
        "category": "api",
        "website": "https://www.naturalfield.com",
        "country": "China",
        "location": "Xi'an, CN",
        "moq": "Kg scale; samples available",
        "certifications": ["ISO 9001", "Halal/Kosher lines", "Export COA per batch"],
        "products": ["plant extracts", "nutraceutical raws", "cosmetic actives"],
        "description": "Chinese extract manufacturer exporting standardized botanical and synthetic ingredients.",
        "tags": ["exporter", "extracts"],
    },
    {
        "name": "Hunan Nutramax Inc.",
        "category": "api",
        "website": "https://www.nutramax.com.cn",
        "country": "China",
        "location": "Changsha, CN",
        "moq": "Kg to drum",
        "certifications": ["ISO 9001", "GMP workshops", "Kosher/Halal"],
        "products": ["botanical extracts", "monomer actives", "fruit powders"],
        "description": "High-volume botanical extraction plant supplying global supplement brands.",
        "tags": ["extracts", "high volume"],
    },

    # ---------------- Licensed pharmaceutical distribution ----------------
    {
        "name": "McKesson Corporation",
        "category": "pharma_dist",
        "website": "https://www.mckesson.com",
        "country": "USA",
        "location": "Irving, TX",
        "moq": "Account-based; daily order cycles",
        "certifications": ["State pharmacy licenses", "DEA registration", "VAWD-accredited DCs"],
        "products": ["full-line Rx distribution", "OTC", "generics", "pharmacy supplies"],
        "description": "Largest US pharmaceutical distributor serving pharmacies, health systems and providers.",
        "tags": ["big three distributor", "licensed wholesale"],
    },
    {
        "name": "Cencora (formerly AmerisourceBergen)",
        "category": "pharma_dist",
        "website": "https://www.cencora.com",
        "country": "USA",
        "location": "Conshohocken, PA",
        "moq": "Account-based",
        "certifications": ["DEA registration", "State licensing", "PDURS compliance"],
        "products": ["full-line Rx distribution", "specialty drugs", "vaccines", "generics"],
        "description": "Global pharmaceutical sourcing and distribution services company.",
        "tags": ["big three distributor", "specialty"],
    },
    {
        "name": "Cardinal Health (Pharmaceutical Segment)",
        "category": "pharma_dist",
        "website": "https://www.cardinalhealth.com",
        "country": "USA",
        "location": "Dublin, OH",
        "moq": "Account-based",
        "certifications": ["DEA registration", "Licensed wholesale", "Accredited DC network"],
        "products": ["Rx distribution", "OTC", "nuclear pharmacy services"],
        "description": "Distributor and manufacturer of medical/pharmaceutical products to care sites.",
        "tags": ["big three distributor"],
    },
    {
        "name": "Morris & Dickson Co., LLC",
        "category": "pharma_dist",
        "website": "https://www.morrisdickson.com",
        "country": "USA",
        "location": "Shreveport, LA",
        "moq": "Independent-pharmacy friendly",
        "certifications": ["DEA registration", "State licenses", "VAWD accreditation"],
        "products": ["full-line Rx", "OTC", "veterinary lines"],
        "description": "Family-owned full-line pharmaceutical wholesaler serving independent pharmacies since 1841.",
        "tags": ["independent pharmacies", "family owned"],
    },
    {
        "name": "Smith Drug Company",
        "category": "pharma_dist",
        "website": "https://www.smithdrug.com",
        "country": "USA",
        "location": "Spartanburg, SC",
        "moq": "Regional account terms",
        "certifications": ["DEA registration", "State wholesale licenses"],
        "products": ["Rx distribution", "OTC", "front-end store supplies"],
        "description": "Southeastern regional drug wholesaler for independent community pharmacies.",
        "tags": ["regional wholesaler"],
    },
]


def validate(rows):
    seen = set()
    for r in rows:
        assert r["name"] not in seen, f"Duplicate: {r['name']}"
        seen.add(r["name"])
        assert r["category"] in {
            "ingredient", "finished", "pharma_dist", "api", "botanical", "marketplace"
        }, r["name"]
    return rows


# ---------------------------------------------------------------------------
# Pricing & pack-size enrichment.
# Prices are INDICATIVE list/range figures for typical bulk quantities, meant
# for comparison shopping only; confirm current quotes with the supplier.
# ---------------------------------------------------------------------------
PRICE_AND_PACKS: dict[str, dict] = {
    "BulkSupplements.com": {
        "pack_sizes": ["100 g", "500 g", "1 kg", "5 kg", "25 kg"],
        "pricing_note": "Per-kg price drops sharply at 5 kg+ tiers",
        "price_examples": [
            {"item": "Creatine monohydrate", "price": "$16–26", "unit": "kg"},
            {"item": "Caffeine anhydrous", "price": "$12–20", "unit": "kg"},
            {"item": "L-Glutamine", "price": "$14–22", "unit": "kg"},
        ],
    },
    "PureBulk Inc": {
        "pack_sizes": ["100 g", "250 g", "1 kg", "5 kg", "20 kg"],
        "pricing_note": "COA per lot included in price",
        "price_examples": [
            {"item": "Creatine monohydrate (Creapure)", "price": "$45–65", "unit": "kg"},
            {"item": "Creatine monohydrate (generic)", "price": "$18–30", "unit": "kg"},
            {"item": "Beta-alanine", "price": "$20–32", "unit": "kg"},
        ],
    },
    "NutriScience Innovations LLC": {
        "pack_sizes": ["1 kg", "5 kg", "25 kg drum"],
        "pricing_note": "Quote-based above 25 kg",
        "price_examples": [
            {"item": "NAC", "price": "$28–45", "unit": "kg"},
            {"item": "Alpha-GPC 50% powder", "price": "$60–95", "unit": "kg"},
        ],
    },
    "IngredientsOnline.com": {
        "pack_sizes": ["25 kg carton", "50 lb fiber drum", "pallet"],
        "pricing_note": "Transparent tiered list pricing on site; RFQ for pallets",
        "price_examples": [
            {"item": "Vitamin C ascorbic acid", "price": "$8–15", "unit": "kg"},
            {"item": "Magnesium glycinate", "price": "$14–24", "unit": "kg"},
        ],
    },
    "Prinova Global Solutions": {
        "pack_sizes": ["bag", "box", "pallet", "bulk truckload"],
        "pricing_note": "Contract/distributor pricing via account reps",
        "price_examples": [
            {"item": "Sweeteners & proteins", "price": "Quote", "unit": "per lot"},
        ],
    },
    "Glanbia Nutritionals": {
        "pack_sizes": ["custom premix batches", "tote/pallet"],
        "pricing_note": "Custom-quoted premix programs",
        "price_examples": [
            {"item": "Vitamin premix blends", "price": "Quote", "unit": "per batch"},
        ],
    },
    "Blue California": {
        "pack_sizes": ["1 kg", "5 kg", "25 kg"],
        "pricing_note": "Premium fermentation-derived actives",
        "price_examples": [
            {"item": "L-Ergothioneine", "price": "$800–1500", "unit": "kg"},
        ],
    },
    "AIDP Inc": {
        "pack_sizes": ["1 kg", "5 kg", "25 kg drum"],
        "pricing_note": "Branded ingredients carry premium vs commodity",
        "price_examples": [
            {"item": "Magtein (Mg L-threonate)", "price": "$90–140", "unit": "kg"},
        ],
    },
    "Jiaherb Inc": {
        "pack_sizes": ["1 kg", "5 kg", "25 kg drum"],
        "pricing_note": "Standardization ratio drives price",
        "price_examples": [
            {"item": "Curcuminoids 95% extract", "price": "$30–55", "unit": "kg"},
            {"item": "Green tea extract 50% EGCG", "price": "$25–45", "unit": "kg"},
        ],
    },
    "NOW Natural Foods (Wholesale)": {
        "pack_sizes": ["case of 6–12 units", "master case"],
        "pricing_note": "Wholesale ~40-50% off MSRP via distributors",
        "price_examples": [
            {"item": "Finished bottles (typ. 60–120 ct)", "price": "$6–25", "unit": "bottle wholesale"},
        ],
    },
    "Piping Rock Health Products": {
        "pack_sizes": ["case packs", "private label runs from ~1k units"],
        "pricing_note": "Private label quoted per SKU and run length",
        "price_examples": [
            {"item": "Stock supplements wholesale", "price": "$2–12", "unit": "bottle"},
        ],
    },
    "Hard Rhino / BulkSupplements Private Label": {
        "pack_sizes": ["cases", "pallets"],
        "pricing_note": "Low case minimums; label setup fee may apply",
        "price_examples": [
            {"item": "Capsules (stock formulas)", "price": "$3–10", "unit": "bottle"},
        ],
    },
    "Starwest Botanicals": {
        "pack_sizes": ["4 oz", "1 lb", "5 lb", "25 lb sack"],
        "pricing_note": "Organic line priced above conventional",
        "price_examples": [
            {"item": "Organic chamomile flowers whole", "price": "$12–22", "unit": "lb"},
            {"item": "Organic turmeric powder", "price": "$6–12", "unit": "lb"},
        ],
    },
    "Mountain Rose Herbs": {
        "pack_sizes": ["4 oz", "1 lb", "5 lb", "25 lb"],
        "pricing_note": "No minimum order; bulk pricing tiers online",
        "price_examples": [
            {"item": "Organic nettle leaf c/s", "price": "$9–16", "unit": "lb"},
            {"item": "Organic lavender flowers", "price": "$14–26", "unit": "lb"},
        ],
    },
    "Monterey Bay Spice Co.": {
        "pack_sizes": ["1/4 lb", "1 lb", "5 lb", "25 lb"],
        "pricing_note": "Small-business friendly pack ladder",
        "price_examples": [
            {"item": "Hibiscus flowers c/s", "price": "$5–10", "unit": "lb"},
        ],
    },
    "Atlantic Spice Company": {
        "pack_sizes": ["1 lb", "5 lb", "25 lb box"],
        "pricing_note": "Volume breaks at 5/25 lb",
        "price_examples": [
            {"item": "Cinnamon powder (cassia)", "price": "$3–7", "unit": "lb"},
        ],
    },
    "San Francisco Herb & Natural Food Co.": {
        "pack_sizes": ["1 lb", "5 lb", "25 lb"],
        "pricing_note": "Long-standing flat wholesale tiers",
        "price_examples": [
            {"item": "Rosemary leaf whole", "price": "$4–9", "unit": "lb"},
        ],
    },
    "Cayman Chemical": {
        "pack_sizes": ["mg vials", "g lots", "multi-kg GMP campaigns"],
        "pricing_note": "Research mg-g; GMP scale-up separately quoted",
        "price_examples": [
            {"item": "Bioactive reference standards", "price": "$50–400", "unit": "vial"},
        ],
    },
    "Sigma-Aldrich (Merck KGaA)": {
        "pack_sizes": ["g bottles", "kg pails", "ton IBC"],
        "pricing_note": "Catalog list prices; volume contracts via sales",
        "price_examples": [
            {"item": "USP-grade excipients", "price": "$40–200+", "unit": "kg catalog"},
        ],
    },
    "Alfa Chemistry": {
        "pack_sizes": ["g", "100 g", "kg"],
        "pricing_note": "Impurity standards often $100+/10 mg",
        "price_examples": [
            {"item": "Pharmaceutical impurity standards", "price": "$100–600", "unit": "10 mg–1 g"},
        ],
    },
    "Suanfarma": {
        "pack_sizes": ["kg commercial packs", "drum (25–50 kg)", "container"],
        "pricing_note": "Contract API pricing with DMF support",
        "price_examples": [
            {"item": "Commercial APIs", "price": "Quote / contract", "unit": "kg"},
        ],
    },
    "PharmaCompass": {
        "pack_sizes": ["n/a (RFQ platform)"],
        "pricing_note": "Free RFQ to multiple DMF-holding factories",
        "price_examples": [
            {"item": "API quotes", "price": "Quote", "unit": "per RFQ"},
        ],
    },
    "Xi'an Natural Field Biotechnology": {
        "pack_sizes": ["1 kg foil bag", "25 kg drum"],
        "pricing_note": "FOB China; samples free with freight collect",
        "price_examples": [
            {"item": "Plant extracts (standardized)", "price": "$10–80", "unit": "kg FOB"},
        ],
    },
    "Hunan Nutramax Inc.": {
        "pack_sizes": ["1 kg", "25 kg drum"],
        "pricing_note": "High-volume export pricing",
        "price_examples": [
            {"item": "Botanical extracts", "price": "$8–60", "unit": "kg FOB"},
        ],
    },
    "McKesson Corporation": {
        "pack_sizes": ["each", "case"],
        "pricing_note": "WAC + contract pricing; requires pharmacy license/account",
        "price_examples": [
            {"item": "Brand & generic Rx", "price": "WAC/contract", "unit": "per account"},
        ],
    },
    "Cencora (formerly AmerisourceBergen)": {
        "pack_sizes": ["each", "case"],
        "pricing_note": "WAC/contract; specialty buy-side programs",
        "price_examples": [
            {"item": "Rx distribution", "price": "WAC/contract", "unit": "per account"},
        ],
    },
    "Cardinal Health (Pharmaceutical Segment)": {
        "pack_sizes": ["each", "case"],
        "pricing_note": "WAC/contract; generics programs available",
        "price_examples": [
            {"item": "Rx distribution", "price": "WAC/contract", "unit": "per account"},
        ],
    },
    "Morris & Dickson Co., LLC": {
        "pack_sizes": ["each", "case"],
        "pricing_note": "Independent-pharmacy generic programs",
        "price_examples": [
            {"item": "Rx distribution", "price": "Account terms", "unit": "per account"},
        ],
    },
    "Smith Drug Company": {
        "pack_sizes": ["each", "case"],
        "pricing_note": "Regional account terms",
        "price_examples": [
            {"item": "Rx distribution", "price": "Account terms", "unit": "per account"},
        ],
    },

    # ---------------- B2B marketplaces ----------------
    "Alibaba.com": {
        "pack_sizes": ["seller-defined: 1 kg bags → FCL containers"],
        "pricing_note": "Tiered per-MOQ pricing listed live; Trade Assurance escrow",
        "price_examples": [
            {"item": "Bulk supplement powders", "price": "$2–60", "unit": "kg (MOQ-dependent)"},
            {"item": "Finished softgels/capsules OEM", "price": "$0.01–0.05", "unit": "capsule"},
        ],
    },
    "Made-in-China.com": {
        "pack_sizes": ["seller-defined: kg drums → containers"],
        "pricing_note": "Onsite-check verified suppliers; negotiated pricing",
        "price_examples": [
            {"item": "Botanical extracts", "price": "$5–70", "unit": "kg (MOQ-dependent)"},
        ],
    },
    "IndiaMART": {
        "pack_sizes": ["seller-defined: kg → tons"],
        "pricing_note": "Quote-based; huge Indian pharma/excipient base",
        "price_examples": [
            {"item": "APIs & excipients", "price": "Quote", "unit": "kg lots"},
        ],
    },
    "Global Sources": {
        "pack_sizes": ["seller-defined"],
        "pricing_note": "Verified-manufacturer program; RFQ workflow",
        "price_examples": [
            {"item": "Health products & ingredients", "price": "Quote", "unit": "varies"},
        ],
    },
    "DHgate": {
        "pack_sizes": ["small-lot wholesale (1–100 units)"],
        "pricing_note": "Escrow protected small-batch pricing",
        "price_examples": [
            {"item": "Small-lot supplements", "price": "$1–15", "unit": "unit"},
        ],
    },
    "ThomasNet": {
        "pack_sizes": ["n/a (directory)"],
        "pricing_note": "US manufacturer directory with direct RFQ",
        "price_examples": [
            {"item": "Co-man/co-pack quotes", "price": "Quote", "unit": "per project"},
        ],
    },
    "EC21": {
        "pack_sizes": ["seller-defined"],
        "pricing_note": "Korea-based global B2B offers board",
        "price_examples": [
            {"item": "Chemical & pharma offers", "price": "Quote", "unit": "varies"},
        ],
    },
    "Pharmaoffer": {
        "pack_sizes": ["pilot kg → commercial tons"],
        "pricing_note": "Multi-supplier RFQ comparison, free for buyers",
        "price_examples": [
            {"item": "API quotes", "price": "Quote", "unit": "kg lots"},
        ],
    },
    "Knowde": {
        "pack_sizes": ["sample → drum → tote"],
        "pricing_note": "List pricing or quote carts set by producers",
        "price_examples": [
            {"item": "Nutraceutical actives", "price": "$10–200", "unit": "kg (typical range)"},
        ],
    },
    "CPHI Online": {
        "pack_sizes": ["n/a (RFQ platform)"],
        "pricing_note": "Buyer membership free tiers; quotes from verified GMP sites",
        "price_examples": [
            {"item": "API/excipient RFQs", "price": "Quote", "unit": "per RFQ"},
        ],
    },
    "EudraGMDP Database (EMA)": {
        "pack_sizes": ["n/a — register"],
        "pricing_note": "Free public access",
        "price_examples": [],
    },
    "NABP Accredited Distributor Search (VAWD)": {
        "pack_sizes": ["n/a — directory"],
        "pricing_note": "Free public lookup",
        "price_examples": [],
    },
    "FDA Establishment Registration & Listing": {
        "pack_sizes": ["n/a — register"],
        "pricing_note": "Free public access",
        "price_examples": [],
    },
}

MARKETPLACES = [
    {
        "name": "Alibaba.com",
        "category": "marketplace",
        "website": "https://www.alibaba.com",
        "country": "China",
        "location": "Hangzhou, CN (global reach)",
        "moq": "Set by seller; commonly 1–500 kg or 100+ units",
        "certifications": ["Trade Assurance escrow", "Supplier verification tiers"],
        "products": ["supplement raw materials", "APIs", "herbal extracts", "OEM finished supplements", "packaging"],
        "description": "World's largest B2B marketplace; filter by Verified Supplier, trade assurance and MOQ.",
        "tags": ["b2b", "oem", "global sourcing", "escrow"],
    },
    {
        "name": "Made-in-China.com",
        "category": "marketplace",
        "website": "https://www.made-in-china.com",
        "country": "China",
        "location": "Nanjing, CN (global reach)",
        "moq": "Seller-defined; typically 25–100 kg",
        "certifications": ["Onsite Check factory audits", "Verified Supplier badges"],
        "products": ["botanical extracts", "nutraceutical raws", "pharma machinery", "supplements"],
        "description": "Major Chinese B2B portal with audited-factory listings across nutraceutical supply.",
        "tags": ["b2b", "factory audits", "global sourcing"],
    },
    {
        "name": "IndiaMART",
        "category": "marketplace",
        "website": "https://www.indiamart.com",
        "country": "India",
        "location": "Noida, IN",
        "moq": "Seller-defined; quote-based",
        "certifications": ["Supplier verification levels", "GST-registered sellers"],
        "products": ["APIs", "excipients", "ayurvedic/herbal ingredients", "pharma machinery"],
        "description": "India's largest B2B marketplace with deep pharmaceutical and herbal supplier base.",
        "tags": ["b2b", "india", "quote-based"],
    },
    {
        "name": "Global Sources",
        "category": "marketplace",
        "website": "https://www.globalsources.com",
        "country": "Hong Kong/China",
        "location": "Hong Kong SAR",
        "moq": "Seller-defined",
        "certifications": ["Verified Manufacturer program"],
        "products": ["health supplements", "ingredients", "consumer health devices"],
        "description": "Asia-sourcing B2B platform known for verified-manufacturer vetting and trade shows.",
        "tags": ["b2b", "verified suppliers", "trade shows"],
    },
    {
        "name": "DHgate",
        "category": "marketplace",
        "website": "https://www.dhgate.com",
        "country": "China",
        "location": "Beijing, CN (global reach)",
        "moq": "Very low; single-carton lots common",
        "certifications": ["Buyer-protection escrow"],
        "products": ["small-lot supplements", "vitamins", "sports nutrition"],
        "description": "Small-batch wholesale arm of the Chinese export ecosystem; low MOQs with escrow.",
        "tags": ["b2b", "small lots", "escrow"],
    },
    {
        "name": "ThomasNet",
        "category": "marketplace",
        "website": "https://www.thomasnet.com",
        "country": "USA",
        "location": "New York, NY",
        "moq": "n/a — RFQ directory",
        "certifications": ["North American manufacturer focus"],
        "products": ["co-manufacturers", "co-packers", "ingredient distributors", "private label"],
        "description": "Directory of North American industrial and nutraceutical manufacturers with direct RFQ.",
        "tags": ["b2b", "directory", "rfq", "usa"],
    },
    {
        "name": "EC21",
        "category": "marketplace",
        "website": "https://www.ec21.com",
        "country": "South Korea",
        "location": "Seoul, KR",
        "moq": "Offer-based",
        "certifications": ["Gold/Silver supplier membership tiers"],
        "products": ["chemicals", "pharmaceuticals", "food additives", "herbal materials"],
        "description": "Korean global B2B platform strong in chemicals and pharma trade offers.",
        "tags": ["b2b", "chemicals", "trade offers"],
    },
]


def enrich(rows) -> list[dict]:
    """Attach pack sizes / indicative pricing to each supplier entry."""
    for r in rows:
        extra = PRICE_AND_PACKS.get(r["name"], {})
        r.setdefault("pack_sizes", extra.get("pack_sizes", []))
        r.setdefault("price_examples", extra.get("price_examples", []))
        r.setdefault("pricing_note", extra.get("pricing_note", ""))
    return rows


# ---------------------------------------------------------------------------
# Sourcing platforms & regulatory directories (licensed/verified channels)
# ---------------------------------------------------------------------------
SOURCING_PLATFORMS = [
    {
        "name": "Pharmaoffer",
        "category": "marketplace",
        "website": "https://www.pharmaoffer.com",
        "country": "Netherlands",
        "location": "Leiden, NL",
        "moq": "Quote-based; pilot to commercial",
        "certifications": ["Verified CDMO/API profiles", "DMF/CEP status shown"],
        "products": ["APIs", "excipients", "CDMO services", "finished dose manufacturing"],
        "description": "B2B platform to find and quote vetted API manufacturers and contract manufacturers worldwide.",
        "tags": ["b2b", "api sourcing", "cdmo", "rfq"],
    },
    {
        "name": "Knowde",
        "category": "marketplace",
        "website": "https://www.knowde.com",
        "country": "USA",
        "location": "San Jose, CA",
        "moq": "Supplier-defined; sample requests supported",
        "certifications": ["Direct-from-producer listings", "TDS/SDS docs attached"],
        "products": ["nutraceutical ingredients", "functional actives", "chemicals", "flavors"],
        "description": "Online marketplace where ingredient producers list products with technical documentation and quotes.",
        "tags": ["b2b", "ingredients", "documentation"],
    },
    {
        "name": "CPHI Online",
        "category": "marketplace",
        "website": "https://www.cphi.com",
        "country": "Netherlands",
        "location": "Amsterdam, NL (global network)",
        "moq": "n/a — RFQ platform",
        "certifications": ["Verified supplier profiles", "GMP site info listed"],
        "products": ["APIs", "excipients", "contract manufacturing", "packaging", "machinery"],
        "description": "Informa's pharma supply-chain platform connecting buyers with GMP suppliers year-round plus CPHI trade shows.",
        "tags": ["b2b", "directory", "rfq", "trade shows"],
    },
    {
        "name": "EudraGMDP Database (EMA)",
        "category": "pharma_dist",
        "website": "https://eudragmdp.ema.europa.eu",
        "country": "EU/EEA",
        "location": "Amsterdam, NL (EMA)",
        "moq": "n/a — official register",
        "certifications": ["Official EU database", "GDP certificate status"],
        "products": ["wholesale distribution authorizations", "GMP certificates", "manufacturing authorizations"],
        "description": "EU regulator-run register of licensed wholesale distributors and GDP/GMP certificate status across member states.",
        "tags": ["regulatory", "verify wholesalers", "gdp"],
    },
    {
        "name": "NABP Accredited Distributor Search (VAWD)",
        "category": "pharma_dist",
        "website": "https://nabp.pharmacy",
        "country": "USA",
        "location": "Mount Prospect, IL",
        "moq": "n/a — accreditation directory",
        "certifications": ["VAWD accreditation", "State licensure verified by NABP"],
        "products": ["accredited wholesale distributor lookup", "pharmacy verification"],
        "description": "Search tool from the National Association of Boards of Pharmacy for VAWD-accredited drug wholesalers.",
        "tags": ["regulatory", "verify distributors", "accreditation"],
    },
    {
        "name": "FDA Establishment Registration & Listing",
        "category": "api",
        "website": "https://www.accessdata.fda.gov/scripts/cder/drls/",
        "country": "USA",
        "location": "Silver Spring, MD",
        "moq": "n/a — official register",
        "certifications": ["Official FDA database"],
        "products": ["registered drug manufacturers", "repackers", "contract manufacturers", "API facilities"],
        "description": "Verify that a drug facility is FDA-registered and what operations it is authorized to perform.",
        "tags": ["regulatory", "due diligence", "facility verification"],
    },
]

ALL_SUPPLIERS: list[dict] = validate(enrich(SUPPLIERS + MARKETPLACES + SOURCING_PLATFORMS))


if __name__ == "__main__":
    print(f"{len(ALL_SUPPLIERS)} suppliers validated")
