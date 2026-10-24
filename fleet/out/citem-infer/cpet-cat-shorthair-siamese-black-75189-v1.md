<!-- fleet job=citem-infer id=cpet-cat-shorthair-siamese-black-75189-v1 status=done turns=4 usd=0.0040 tokens(read,write,in,out)=[25161, 18329, 10, 2899] model=claude-haiku-5-5 -->
# Pet: Cat: Shorthair: siamese_black

{"item": {"name": "Pet: Cat: Shorthair: siamese_black", "locale_id": 75189, "kind": "pet"},
 "sources": [
  {"type": "marketplace", "detail": "Cat pet line, Shorthair siamese_black variant. Sold for Station Cash as part of the Cats category (wiki says cats are only available for Station Cash; no per-variant SC price or listing given)", "where": "SC Marketplace (inferred from the Station Cash-only wiki statement; venue not named)", "price": null, "currency": "station_cash", "source": "wiki page Cats (text: 'Cats are only available to be purchased with Station Cash.'), as quoted in quest-lines/item-packs.json:9162 and confirmed by lookup on wiki page Cats"},
  {"type": "vendor", "detail": "Legacy coin store record for item 24039 (no named vendor in the store data; no wiki or client source names a coin vendor for this cat)", "where": null, "price": "540 coins (member price 486 coins, 10% member discount; sell price 54 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 24039 (line 6916)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client definition: Pet: Cat: Shorthair: siamese_black, locale 75189, definition id 24039, model cat_shorthair.adr, one definition, coin store price 540", "source": "locale:75189; repo:prototype/osfr-tools/data/content/stores.json item 24039 (line 6916)"},
  {"claim": "The store record for 24039 has no price_provenance block, unlike the Station Cash items reconstructed from wiki prices (e.g. 24021 Mojo, 24022 Mittens, 24027 Pooky, 24032 Zinx, 24041 Gizmo), so its 540 coin price is the plain legacy coin cost", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6898-6918"},
  {"claim": "Wiki Cats page says cats are only available to be purchased with Station Cash, which conflicts with the 540-coin legacy store price for this cat", "source": "wiki page Cats (lookup result; quest-lines/item-packs.json:9162)"},
  {"claim": "Sibling cat variants 75184-75194 share the Cat pet hint and the Shorthair naming; the cluster has no separate wiki page or price", "source": "client_cluster in pack; quest-lines/flags.tsv:7727-7738"},
  {"claim": "Cat pet lines in the client are tagged only as dev asset keys (internal asset key, not display text), so they give no sale or drop evidence", "source": "quest-lines/flags.tsv:7733"}
 ],
 "confidence": 0.4,
 "open": [
  "The Station Cash-only wiki statement and the 540-coin legacy store price contradict each other. The coin price is the only per-variant price, but no coin vendor is named for it. Confirm which channel sold the siamese_black cat before using the coin price.",
  "No wiki page names this variant, no SC price is given for it, and no marketplace listing was found. The SC Marketplace venue is inferred from the Cats category text only.",
  "The tag on the pack said 'vendor'. The coin store record supports a legacy coin sale, but no vendor name, zone or shop is in the data, so the vendor entry has no where field.",
  "Live status and retirement are not verified: no wiki or article source says whether this cat was retired. The source tags on store item 24039 (L1, L2, L4, R2, T633, R1) are not decoded in the pack and were not used as evidence.",
  "Only the client's coin store price and the category-level wiki text were found. No images, article facts, video frames or drop/quest/event answers name this cat."
 ]}
