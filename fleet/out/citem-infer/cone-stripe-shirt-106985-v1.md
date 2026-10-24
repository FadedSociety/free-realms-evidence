<!-- fleet job=citem-infer id=cone-stripe-shirt-106985-v1 status=done turns=6 usd=0.0044 tokens(read,write,in,out)=[48803, 18591, 14, 3261] model=claude-haiku-5-5 -->
# One Stripe Shirt

{"item": {"name": "One Stripe Shirt", "locale_id": 106985, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale of One Stripe Shirt variants (definition ids 7299, 7300, 33903; tint groups 1, 2, 3). Selling vendor/NPC not identified in our data.", "where": null, "price": "270 coins (member price 243 coins, 10% member discount; sell-back 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 7299 (line 6256), item 7300 (line 6257), item 33903 (line 7766)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'One Stripe Shirt' is locale 106985; the description line is locale 150485 ('This is an One Stripe Shirt item.'), with no real description.", "source": "locale:106985; locale:150485"},
  {"claim": "The item has 37 client definitions across 12 definition ids, slot 3 (chest), class 1, model freestyle_<race>_m_chest_rolledslvshirt.adr.", "source": "refs:quest-lines/citem-packs.json cone-stripe-shirt-106985 (client definition block)"},
  {"claim": "Three of the 12 definition ids (7299, 7300, 33903) are in our coin store data at 270 coins each (category 103, the clothing category). The other nine definition ids (33904-33912) have no store row.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6256, 6257, 7766"},
  {"claim": "Wiki job-outfit lists (Farmer, Adventurer pages) include 'One Stripe Shirt' among clothing items, but those pages do not state an acquisition source for it.", "source": "wiki page:Farmer; wiki page:Adventurer"},
  {"claim": "No wiki article, article fact, video frame, quest reward, drop or event answer names this item; no vendor stock list in the pack includes it.", "source": "pack fields: wiki_page null, article_facts [], video [], vendor_stock [], mentioned_by_other_answers []"}
 ],
 "confidence": 0.5,
 "open": [
  "The coin store that sells it is not named. Stores.json tags (L1, L2, L4, R2, T633, R1) are not resolved to a vendor or shop here; confirm which NPC/shop sells category 103 at 270 coins.",
  "Only 3 of 12 definition ids have a store row. Whether the other nine tints/variants were ever sold for coins, or were given by another source, is unknown.",
  "Sell-back price of 27 coins comes from the same store rows; not a source, just a note.",
  "Live status rests on the legacy store data (FreeRealms-Legacy), not a dated wiki or article confirmation. The pack's 'live: yes' first pass is a hint only.",
  "No wiki 'Coin Shop' or 'SC Marketplace' category evidence was found for this item, so those source types are not listed.",
  "No critiques were carried in the pack to fix."
 ]}
