<!-- fleet job=citem-infer id=cbasic-topsoil-100-5103094-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6026, 8462, 6, 1829] model=claude-haiku-5-5 -->
# Basic Topsoil (100)

{"item": {"name": "Basic Topsoil (100)", "locale_id": 5103094, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Pack of 100 Basic Topsoil (farm soil lot, definition 78660), offered at a reduced price in packs of 100, 500 and 1000 per the Jan 15th hotfix. The hotfix gives no per-pack price and no date for when the packs were removed.", "where": "Coin Shop", "price": null, "currency": "coins", "source": "wiki Template:News 'Jan 15th Hotfix'; locale:5103094, locale:5103095 (pack-size names)"},
  {"type": "vendor", "detail": "Farmer Wug sells Basic Topsoil. The single-piece item is the one confirmed; whether he stocks the 100 lot is not shown.", "where": "Sanctuary (outside, near the warpstone)", "price": null, "currency": null, "source": "locale:436183 ('Buy Basic Topsoil'); wiki 'Build Guides/Content/NPCs/NPCs - Sanctuary' Farmer Wug row; repo:prototype/osfr-tools/data/content/npcs/sanctuary.json:19498"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 78660 is 'Basic Topsoil (100)', a lot of 100 pieces for placing on a farm; no coin store price in the client definition, and no stores.json entry for it", "source": "client definition; locale:5103094, locale:5103095; repo search for 78660 finds no store row"},
  {"claim": "Basic Topsoil was made available at a reduced price in packs of 100, 500 and 1000 in the Jan 15th hotfix", "source": "wiki Template:News 'Jan 15th Hotfix'"},
  {"claim": "Basic Topsoil (single item, locale:8070) is bought from the Coin Shop and is needed before planting", "source": "http://www.freerealms.com/article/detail.action?articleId=2087"},
  {"claim": "Basic Topsoil appears under 'Soil' on the Vending Machine page; the page does not say whether it is sold for coins or dispensed, and gives no price", "source": "wiki page 'Vending Machine'"},
  {"claim": "Farmer Wug's quest objective is 'Buy Basic Topsoil' (single item)", "source": "locale:436183; locale:8070"},
  {"claim": "Basic Topsoil is placed on the farm (Humble Beginnings step 'Place Basic Topsoil')", "source": "locale:434736"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin price of the 100 lot is unknown. The only 90-coin figure (video:ljDRabG8Akk/00076.jpg) reads '[Basic] [Topsoil]', which is the single-piece item (locale:8070), not the (100) lot, so it is NOT used as a price for 78660.",
  "The Jan 15th hotfix names only '[Basic] [Topsoil]' and gives no price. Mapping the pack sale to definition 78660 relies on the pack-size names (locale:5103094/5103095) and is unverified.",
  "Farmer Wug: confirmed for the single item only. Whether he sells the 100 lot, and at what price, is unverified.",
  "Vending Machine page lists Basic Topsoil under Soil with no price; treated as unknown mode and not used as coin-shop support.",
  "Article 2087 says Basic Topsoil (single) is bought from the Coin Shop; it supports the single item, not the lot.",
  "Date the reduced-price packs were available and whether they were retired is unknown; retired status not established. Live status 'unsure' pending a dated Coin Shop capture or stock row."
 ]}
