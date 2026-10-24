<!-- fleet job=citem-infer id=cn-elite-pink-alley-fighter-gloves-pl-elite-pink-alley-fighte-44479-v2 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[5574, 12065, 6, 2263] model=claude-haiku-5-5 -->
# {n}Elite Pink Alley Fighter Gloves{pl="Elite Pink Alley Fighter Gloves"}

{"item": {"name": "Elite Pink Alley Fighter Gloves", "locale_id": 44479, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store purchase, store category 102, purchase price 9453 coins (10% member price 8507 coins). The store row does not name the vendor or shop, and this is a standard purchase price, not a sale. Price is unverified: no second source confirms it.", "where": null, "price": "9453 coins (member price 8507 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:2735 (item_id 9478, category_id 102, purchase_price_coins 9453, member_price_coins 8507, sell_price_coins 945; no price_provenance block)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for definition 9478 is locale 44479 'Elite Pink Alley Fighter Gloves'.", "source": "locale:44479"},
  {"claim": "Store row for item_id 9478 exists in category 102 with purchase price 9453 coins and member price 8507 coins (10% discount, 9453 x 0.9 = 8507.7, truncated).", "source": "repo:prototype/osfr-tools/data/content/stores.json:2735"},
  {"claim": "Client definition 9478 carries coin_store_prices 9453, matching the store row.", "source": "client definition for definition id 9478 (same store data, so not independent corroboration)"},
  {"claim": "Slot 2, class 25, and a brawler hands gauntlet model indicate worn gloves, so kind is clothing.", "source": "client definition for definition id 9478"},
  {"claim": "No wiki page, article fact, image, or video frame names this item; the lookup returns only the client locale line.", "source": "lookup (wiki, articles, client) for 'Elite Pink Alley Fighter Gloves'"},
  {"claim": "The stores.json row for 9478 has no price_provenance block, unlike rows marked reconstructed (e.g. item 69478), so it is not flagged as a reconstructed price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:2735 vs :14883"},
  {"claim": "Critique note that 9453 repeats across many unrelated item ids was checked in part: item 29478 in the same file has a different price (270), so the value is not universal, but the full repetition claim was not verified.", "source": "repo:prototype/osfr-tools/data/content/stores.json:10655"}
 ],
 "confidence": 0.35,
 "open": [
  "Vendor, shop and location are not identified. Store category 102 is not decoded in the repo, so 'where' stays null.",
  "The 9453-coin price is supported only by the store row and the client's coin_store_prices field, which come from the same data. No wiki, article, or video source confirms it.",
  "Source tags L1/L2/L4/R2/T633/R1 are not decoded to vendor names; they look store-wide and are not vendor evidence.",
  "Live status is unconfirmed: the store row has no date and no live listing was found. Retirement status is unknown.",
  "The previous answer called this a 'Coin store sale'; the row is a standard purchase price, so the detail is corrected here.",
  "The sibling sets (Rowdy Rumbler 44475, Alley Fighter 44476, Elite Black Alley Fighter 44481) have no quest, drop, or vendor-stock evidence in the pack, so no source is inferred from them."
 ]}
