<!-- fleet job=citem-infer id=czippy-walk-shirt-6000-v1 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[20155, 13731, 10, 3018] model=claude-haiku-5-5 -->
# Zippy Walk Shirt

{"item": {"name": "Zippy Walk Shirt", "locale_id": 6000, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale (coin vendor, category 103); the store row is for definition 436 (tint group 1), with sibling rows for definitions 1730 (tint 2) and 1733 (tint 3)", "where": null, "price": "270 coins (member price 243 coins, 10% member discount; sell-back 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:205 (item_id 436), :5821 (item_id 1730), :5824 (item_id 1733)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name locale 6000 is 'Zippy Walk Shirt', slot 3, class 3, model courier_<race>_<gender>_chest_shortslvbag.adr", "source": "locale:6000"},
  {"claim": "Our coin store data prices definition 436 at 270 coins, the same price in the client definition's coin_store_prices", "source": "repo:prototype/osfr-tools/data/content/stores.json:205"},
  {"claim": "Definitions 1730 and 1733 are also listed at 270 coins in the same category (tint groups 2 and 3)", "source": "repo:prototype/osfr-tools/data/content/stores.json:5821, :5824"},
  {"claim": "Its client cluster is the Courier delivery-runner set (Speedy Sprint Jacket, Amateur/All-Star Postman Jacket, Hasty Mailing Shirt, Express Delivery Shirt, Hasty Trot Shirt); the set's sibling pieces (Zippy Walk Hat, Zippy Walk Wristbands, Zippy Walk Shorts) appear in the client text", "source": "locale:5995, locale:5996, locale:5998, locale:5999, locale:6004, locale:6005; client text 'Zippy Walk Hat', 'Zippy Walk Wristbands', 'Zippy Walk Shorts'"},
  {"claim": "No wiki page, article, video frame or other answer names the Zippy Walk Shirt, so no second price, sale, drop or quest source could be confirmed", "source": "lookup client/wiki/articles/video: only locale:6000 returned"}],
 "confidence": 0.5,
 "open": ["Which coin vendor (NPC or shop name and zone) sells category 103 item 436; stores.json gives the price but not the vendor name or location, and the source_tags (L1, L2, L4, R2, T633, R1) are not decoded here.",
  "The pack says 17 definitions but lists 12 definition_ids. Only 436, 1730 and 1733 appear in stores.json at 270 coins; definitions 12801, 12802, 12808, 12809, 12811, 12813, 12814, 12816, 12817 have no store row and no source, so their sources are unknown.",
  "Retired status is unknown. The store row has no_sale false and no retirement note, and no wiki page confirms it is still sold. Live is marked 'unsure' until a vendor or wiki source confirms it.",
  "The first-pass tag said source 'vendor' and live 'yes'. The vendor part is supported by the store price. The live part is not confirmed by a source beyond the store row.",
  "The client description is empty, and the item has no wiki page, images or video frames, so no in-game description or appearance confirms the item."]}
