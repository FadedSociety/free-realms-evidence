<!-- fleet job=citem-infer id=cstrawberry-surge-helmet-106214-v2 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5034, 6483, 6, 1818] model=claude-haiku-5-5 -->
# Strawberry Surge Helmet

{"item": {"name": "Strawberry Surge Helmet", "locale_id": 106214, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin Store sale, store category 101, tint group 1 (item 33132); variants 33133 (tint group 2) and 33134 (tint group 3) carry the same price in the same category", "where": "Coin Store", "price": "270 coins purchase (member price 243 coins, 10% member discount; sell-back 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 33132 (line 11092); item 33133 (line 11093); item 33134 (line 11094)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Strawberry Surge Helmet' (locale 106214), with the item line 'This is a Strawberry Surge Helmet item.' (locale 150480).", "source": "locale:106214; locale:150480"},
  {"claim": "The coin store table lists item 33132 at 270 coins purchase, 243 coins member price (10% member discount), 27 coins sell price, category 101, tint group 1, no_sale false, source tags L1, L2, L4, R2, T633, R1. This is the only price source; it is the project's own data table, not a live listing.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 11092"},
  {"claim": "Items 33133 (tint group 2) and 33134 (tint group 3) are in the same category at the same 270-coin price. Items 33167 and 33168 (tint groups 2 and 3) also appear there, so the helmet has more variants than the 12 ids in the pack.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 11093, 11094, 11095, 11096"},
  {"claim": "No wiki page, article fact, video frame, vendor stock entry or other answer names this helmet beyond the client text and the store row.", "source": "lookup wiki/articles/video (no matches for 'Strawberry Surge Helmet'); vendors.json has no entry for 33132 (per pack)"}
 ],
 "confidence": 0.5,
 "open": [
  "The 270/243/27 coin prices come only from repo stores.json (lines 11092-11094). The critique is right that the FreeRealms-Legacy CoinStoreItems.json entry gives category 101 and tint group only, so it is not a second price source. I did not re-check that file's line numbers.",
  "No wiki or article confirms the Coin Store listing, its sale dates, or that the helmet was sold live. Live status is unsure; the first-pass 'live: yes' is a hint only.",
  "Retirement is unknown: no source states whether or when the Coin Store sale ended.",
  "Quest, drop, event, crafting, collection and prize-wheel sources were not checked against any data; none are named in the evidence pack.",
  "Only tint groups 1-3 in category 101 are confirmed in stores.json for this name. The 35 definitions (33132-33143 plus others) are not all mapped to a store row or tint, so the full variant list is open.",
  "The store row's source tags (L1, L2, L4, R1, R2, T633) are not decoded in the evidence, so the exact channel is unconfirmed.",
  "The pack's 'standard clothing tier' reading of the same-price pattern is not supported by the table and is not used here."
 ]}
