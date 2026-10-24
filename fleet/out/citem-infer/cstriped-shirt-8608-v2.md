<!-- fleet job=citem-infer id=cstriped-shirt-8608-v2 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[5290, 11714, 6, 2193] model=claude-haiku-5-5 -->
# Striped Shirt

{"item": {"name": "Striped Shirt", "locale_id": 8608, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin-store vendor: store category 103 row for item 422 (tint group 1). The repo names no vendor for this row, so the vendor is unplaced. Category 103 also holds items priced 291, 320, 715, 9453 and others, so it is a price category rather than a single store.", "where": null, "price": "270 coins (member price 243 coins, 10% member discount; sell-back 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:203 (item_id 422, category_id 103, tint_group_id 1, purchase_price_coins 270, member_price_coins 243, sell_price_coins 27); same 270 price on item 970 and 971 (stores.json:5731-5732); client coin_store_prices [270] for the definition"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 'Striped Shirt' is locale 8608, slot 3, class 1, model freestyle_<race>_m_chest_longsleevecuffed.adr, 69 definitions across definition_ids 422, 970-974, 17056-17061", "source": "locale:8608; client definition pack"},
  {"claim": "Store data lists definition 422 at 270 coins purchase, 243 member price (10% discount), 27 sell-back, in store category 103", "source": "repo:prototype/osfr-tools/data/content/stores.json:203; 5731, 5732"},
  {"claim": "Mystery Reward lines (8609) sit next to the item name in client text but do not name the shirt, so no link to this item", "source": "locale:8609"},
  {"claim": "Wiki pages Farmer and Adventurer list a '[Striped Shirt]' entry in their clothing lists. These pages do not name it as a reward or acquisition route, so they are not acquisition evidence", "source": "lookup wiki ns0 Farmer; ns0 Adventurer"},
  {"claim": "Tentonhammer guide describes clothing rewards for duel and quest wins while leveling Ralsu, but does not name Striped Shirt, so it is not used as a source", "source": "http://www.tentonhammer.com:80/node/69806"}
 ],
 "confidence": 0.45,
 "open": [
  "Vendor for the 270-coin store row (category 103) is not named in the repo data. The vendor source is unplaced, and the 'coin store' label is an inference from the store row. The category-to-store mapping is not evidenced.",
  "No wiki article for 'Striped Shirt'. File:Striped Shirt.png has no transcribed text.",
  "Locales 8611 and 8613 are dropped: the id check flags them as duplicates of 8609, so they are not live evidence. The Mystery Reward cluster is unlinked to this item.",
  "Tentonhammer 'striped tee shirt' at level 4 and 'single-striped shirt' are not confirmed as this item. 'Striped T-Shirt' (locale 2497), 'Striped Longsleeve Shirt' (locale 2896) and the daily login Striped T-Shirt (locale 384) are different items.",
  "Retired status unknown; no retirement source found. Store row has no_sale false, so the price row is not marked as withdrawn in the repo."
 ]}
