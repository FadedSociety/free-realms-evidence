<!-- fleet job=citem-infer id=cshort-sleeve-flared-shirt-8639-v4 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[6335, 7547, 6, 1746] model=claude-haiku-5-5 -->
# Short-Sleeve Flared Shirt

{"item": {"name": "Short-Sleeve Flared Shirt", "locale_id": 8639, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Unconfirmed coin store clothing sale. Candidate rows only: stores.json item 2174 (category 103, tint group 3, purchase 270, member 243, sell 27, no_sale false), with 2175 and 2176 (tint groups 2 and 1) matching three definition ids. Row 8639 (category 6, purchase 270, member 243, no_sale true) is a non-sale row. No store-to-definition table or row naming the model confirms the link; the 270 price is shared by many other category-103 clothing rows.", "where": "coin store (category names unconfirmed in repo)", "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2174; repo:prototype/osfr-tools/data/content/stores.json item 2175; repo:prototype/osfr-tools/data/content/stores.json item 2176; repo:prototype/osfr-tools/data/content/stores.json item 8639 (no_sale true); client definition coin_store_prices [270]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Short-Sleeve Flared Shirt' is locale 8639; item class 1, slot 3, 64 definitions, model freestyle_<race>_m_chest_flaredlayeredshirt.adr", "source": "locale:8639"},
  {"claim": "Client definition carries coin store price 270, which is a definition price and not a vendor stock row", "source": "client definition coin_store_prices [270]"},
  {"claim": "Store rows 2174-2176 are category 103 at 270/243 with no_sale false; row 8639 is category 6 with no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 5870 and 13517"},
  {"claim": "Wiki outfit pages Farmer and Adventurer list 'Short Sleeve [Flared] [Shirt]' as a clothing piece; existence only, no acquisition source", "source": "lookup wiki page:ns0 Farmer; page:ns0 Adventurer"},
  {"claim": "Sibling client lines: locale 8524 'Long-Sleeve Flared Shirt'; locale 30768 'Flared Short Sleeve Shirt'; locale 385523 description 'This is a flared short sleeve shirt.' No source names an acquisition.", "source": "locale:8524; locale:30768; locale:385523"}
 ],
 "confidence": 0.3,
 "open": [
  "Store-to-definition mapping is unconfirmed. Store item_ids 2174-2176 match three of 64 definition ids and row 8639 matches the locale id, but neither is proven. Only 3 of 64 definitions have any store row.",
  "Category 6 and category 103 have no names in the repo, so 'Coin Shop' is not confirmed as the label.",
  "Row 8639 is no_sale true; it may mean not sold rather than retired. Retirement status is unknown.",
  "No quest, enemy drop, event, prize wheel, crafting or collection source was found for this shirt or its sibling lines.",
  "live is unsure: no source documents current sale or retirement status. Do not infer current availability from the store rows."
 ]}
