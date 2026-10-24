<!-- fleet job=citem-infer id=cbooming-bump-jacket-122000-v1 status=done turns=6 usd=0.0040 tokens(read,write,in,out)=[41936, 15118, 14, 3361] model=claude-haiku-5-5 -->
# Booming Bump Jacket

{"item": {"name": "Booming Bump Jacket", "locale_id": 122000, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (coin-store item 42001, tint group 1), purchase price 1266 coins; member price 1139 coins (10% member discount), sell-back 126 coins", "where": "coin store (category 103; the store/vendor NPC is not named in our data)", "price": "1266 coins (member 1139)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 42001 (line 7988)"},
  {"type": "vendor", "detail": "Coin store sale of higher-priced tint variants (coin-store items 42006 tint group 2, 42011 tint group 3, and other variants of the same set, all in category 103)", "where": "coin store (category 103)", "price": "9453 coins (member 8507)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json items 42006 (line 7989) and 42011 (line 7990)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Booming Bump Jacket' is locale 122000, a client item; its set siblings Booming Bump Boots/Gloves/Helmet/Pants are locale 122001-122004", "source": "locale:122000; locale:122001; locale:122002; locale:122003; locale:122004"},
  {"claim": "Coin store entries exist for definition 42001 at 1266 coins and for 42006 and 42011 at 9453 coins, which match the two coin_store_prices in the client definition (the 42xxx definitions are this jacket's tint/race variants)", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 7988-7990"},
  {"claim": "The stores data is from FreeRealms-Legacy (CoinStoreItems), so these prices come from the legacy coin store, not a wiki page", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 1-25 (source_repository)"},
  {"claim": "No wiki page, image, article fact, video frame, or other answer names this item; the 'vendor' guess from the first-pass tag is only a hint", "source": "lookup of 'Booming Bump Jacket' (client, wiki, articles, video) returned only the locale rows"}
 ],
 "confidence": 0.5,
 "open": [
  "Which coin vendor or Coin Shop category sells it is not named: stores.json category 103 has no name in our data, and no wiki page covers the item. Confirm the store/NPC and whether it is a Coin Shop or a vendor sale.",
  "Two prices exist: 1266 coins for tint group 1 (42001) and 9453 coins for tint groups 2-3 (42006, 42011). The wiki has no price to confirm them. 9453 is the common top coin price in this category, so check the tint-to-price mapping in-game.",
  "The client definition lists 12 definition_ids but says 16 definitions. The other 4 definitions were not checked.",
  "Retired status and dates are unknown. The store rows carry R1/R2/T633 tags, which suggest a later sale, but no article or wiki page dates the sale or retirement, so live status is unsure.",
  "No quest, enemy-drop, event, crafting, collection, or prize-wheel source was found. The set's clothing items are not in any pack answer."
 ]}
