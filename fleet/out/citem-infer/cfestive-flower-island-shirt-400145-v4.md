<!-- fleet job=citem-infer id=cfestive-flower-island-shirt-400145-v4 status=no_submit turns=2 usd=0.0026 tokens(read,write,in,out)=[5904, 11336, 6, 2306] model=claude-haiku-5-5 -->
# Festive Flower Island Shirt

```json
{"item": {"name": "Festive Flower Island Shirt", "locale_id": 400145, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store price row only. Selling NPC not identified; no stock row names this item. stores.json has no_sale: true and sell_price: null, so purchase status is unverified.", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 59970 (line 8381); same row shape for items 59971, 59972, 60005, 60006, 60007 and 60040 (lines 8382-8387)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 400145 'Festive Flower Island Shirt', description 'For occasions when non-festive flowers just don't cut it.', slot 3, class 1, 35 definitions (12 listed IDs 59970-59981).", "source": "locale:400145; client definition pack"},
  {"claim": "Store rows for the Festive shirt are category 103 at 270 coins, member 243, no_sale true, sell_price null: items 59970 (tint 1), 59971 (tint 2), 59972 (tint 3), 60005-60007 (tints 1-3), and 60040 (tint 2).", "source": "repo:prototype/osfr-tools/data/content/stores.json:8381-8387"},
  {"claim": "Category 103 is mixed. Other category 103 rows carry sell_price values and no_sale false, and the 270-coin rows share the same six-tag set as bulk rows (items 58217-58219, 58426-58428 at 50 coins). That makes the category a weak basis for a sale claim.", "source": "repo:prototype/osfr-tools/data/content/stores.json:8370-8380"},
  {"claim": "The client name search returns only the Festive shirt, the Dark Flower Island Shirt (locale 5239) and the Swirly Flower Island Shirt (locale 400180). No wiki page, article or video frame names the Festive shirt.", "source": "lookup (client, wiki, articles), this run; locale query 'Flower Island Shirt'"},
  {"claim": "The sibling Dark Flower Island Shirt is a Station Cash / SC Marketplace item (available in the Summer event and as a bonus with the June 4-25, 2013 Summer Pass). It is not a coin-store row, so it does not evidence the Festive shirt's source.", "source": "wiki page 'Dark Flower Island Shirt' (SC Marketplace); wiki page 'Summer Pass' (Category:Membership, Category:Station Cash); locale:813, locale:834; articles http://www.freerealms.com:80/article/detail.action?articleId=1521 and articleId=1532"},
  {"claim": "notes/Autopilot/T634.md:61 lists 'Dark Flower Island Shirt' among ambiguous Station Cash articles. This conflicts with nothing for the Festive shirt, but it shows the family was Station Cash-sold in 2013 and the Festive shirt's status is still unknown.", "source": "notes/Autopilot/T634.md:61"}
 ],
 "confidence": 0.3,
 "open": [
  "Selling vendor NPC, zone and sale period are unidentified. Nothing in the pack proves a coin vendor stocks this shirt, so the vendor source is a store-data price row only and is not wireable as an acquisition yet.",
  "no_sale: true with sell_price null on every row may mean the item is not sold for coins at all. Treat the 270/243 coin price as a row value, not a confirmed sale.",
  "Sibling Dark Flower Island Shirt is Station Cash / SC Marketplace (wiki and articles). Whether the Festive shirt was also an SC Marketplace or Summer event item is unverified and needs a wiki or article check on 'Festive Flower Island Shirt'.",
  "Items 59973-59981 and about 23 other definitions have no store row. Whether they share this source is unverified.",
  "No wiki category (Coin Shop, SC Marketplace, holiday) or wiki page names this item. Retirement date is unknown."
 ],
 "confidence_note": "wireable: false"}
```
