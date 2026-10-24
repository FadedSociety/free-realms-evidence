<!-- fleet job=citem-infer id=cexplorer-s-backpack-29103-v3 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[15584, 9571, 8, 2331] model=claude-haiku-5-5 -->
# Explorer's Backpack

{"item": {"name": "Explorer's Backpack", "locale_id": 29103, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin store sale of Explorer's Backpack (store row item_id 29103, category 105, tint group 2, not no_sale); item_id-to-locale-id mapping assumed, not confirmed", "where": "Coin Shop (shop name not stated in stores.json)", "price": "270 coins (member price 243 coins, 10% member discount); sell-back 27 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:10464; client coin_store_prices [270]"}],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "locale:29103 is \"Explorer's Backpack\" (zone-free base name; other locale names in the family: 29078 Ayani Tree, 29085 Seaside, 29108 Blackspore, 29111 Briarwood, 29150 Memorial Caverns, 29164 Snowhill Explorer's Backpack).", "source": "locale:29103 and locale family lookup"},
  {"claim": "stores.json has a row for item_id 29103: category 105, purchase 270 coins, member 243, sell 27, no_sale false. Matches client coin_store_prices [270].", "source": "repo:prototype/osfr-tools/data/content/stores.json:10464"},
  {"claim": "The 270 price is shared by most rows in the 29084-29298 block, so it supports but does not by itself confirm the item identity. The store row is the only item-specific price tie.", "source": "repo:prototype/osfr-tools/data/content/stores.json:10455-10470"},
  {"claim": "Store rows with item_id equal to other Explorer backpack locale ids exist with no_sale true (e.g. 29085 = Seaside Explorer's Backpack), so item_id/locale-id equality is plausible but unverified.", "source": "repo:prototype/osfr-tools/data/content/stores.json:10456; locale:29085"},
  {"claim": "Wiki lookup returned only collection/zone index pages (Adventurer, Blackspore Rare Exploration, Briarwood [Explorer], Sacred Grove [Explorer], etc.); no page for this item. Article lookup returned nothing usable.", "source": "lookup wiki/articles 'Explorer Backpack'"},
  {"claim": "Item appears in shipped inventory screenshots alongside zone variants. Presence only, not an acquisition source.", "source": "video:MzxfUBdIIGU/00032.jpg; video:JNEzUHfmocc/00026.jpg; video:22IH8XFo6R4/00024.jpg"}
 ],
 "confidence": 0.5,
 "open": [
  "item_id 29103 to locale 29103 mapping is unconfirmed; no source names both ids. The coin_shop source rests on that assumption.",
  "Shop name not stated in stores.json; 'Coin Shop' is the label used for category 105 by convention, not confirmed.",
  "No quest, drop, collection, or event source found for the base Explorer's Backpack. Zone variants (Ayani Tree, Blackspore, Briarwood, Seaside, Snowhill, Memorial Caverns) are separate items; their sources do not transfer. Pathfinder's Backpack (locale 29102) sits in the Rare Exploration collection in collections.json:1982, a sibling item only.",
  "Retirement unknown: no source says retired. live 'yes' rests only on the store row with no_sale false in the data snapshot; it is not a current price."
 ]}
