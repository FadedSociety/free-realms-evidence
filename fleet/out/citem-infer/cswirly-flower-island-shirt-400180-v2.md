<!-- fleet job=citem-infer id=cswirly-flower-island-shirt-400180-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5552, 7808, 6, 1656] model=claude-haiku-5-5 -->
# Swirly Flower Island Shirt

{"item": {"name": "Swirly Flower Island Shirt", "locale_id": 400180, "kind": "clothing"},
 "sources": [
  {"type": "other", "detail": "Unnamed coin store price row (stores.json category 103), tint group 1, item 60005. Price data only: no vendor, NPC or stock row maps category 103, and the row is marked no_sale. Not confirmed as a vendor sale.", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 8384 (item 60005); same 270 price on items 59970-59972, 60006, 60007, 60040 in lines 8381-8387"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Swirly Flower Island Shirt', description 'Sweet swirling flowers!', slot 3, class ids 1 and 173, 36 definitions (listed ids 60005-60016)", "source": "locale:400180; client definition pack"},
  {"claim": "Store row for item 60005 (category 103, tint group 1): purchase_price_coins 270, member_price_coins 243, sell_price_coins null, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json line 8384 (re-read and confirmed)"},
  {"claim": "source_tags [L1,L2,L4,R2,L3,L3] are identical on every category 103 row and on category 6 rows, so they are a shared template, not per-item sale evidence", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 8378-8392"},
  {"claim": "no_sale true on every store row checked, including this one, so the row does not show the item is currently sold", "source": "repo:prototype/osfr-tools/data/content/stores.json line 8384"},
  {"claim": "lookup of the item name across client, wiki, articles and video returns only the client locale line; no wiki page, article, video frame, quest, drop or event names it", "source": "lookup 'Swirly Flower Island Shirt' (all four sources)"}
 ],
 "confidence": 0.3,
 "open": [
  "No vendor is identified. Stores.json category 103 is not mapped to any NPC or stock row, so the 270-coin price cannot be attributed to a vendor or shop.",
  "no_sale: true on the row, with sell_price null, is unexplained in the repo. It may mean the item is not sold, so the coin price may not be a live purchase.",
  "Definitions 60008-60016 have no store row, so sale coverage for the other tints is unknown.",
  "No wiki, article or video source gives a live date, sale period or retirement. live is 'unsure' and retired is null.",
  "The Island Shirt Friday and Summer membership promos (locale 400320, 813, 834) concern the Dark Flower Island Shirt, not this item. No promo source is attributed here.",
  "Critique fixes applied: the source is labelled as an unnamed price row, not a vendor; no_sale and source_tags are stated as recorded and not interpreted; the sale status is left unresolved."
 ]}
