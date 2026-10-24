<!-- fleet job=citem-infer id=ccasual-doll-cap-40610-v1 status=done turns=7 usd=0.0054 tokens(read,write,in,out)=[84556, 22758, 16, 3368] model=claude-haiku-5-5 -->
# Casual Doll Cap

{"item": {"name": "Casual Doll Cap", "locale_id": 40610, "kind": "collection"},
 "sources": [
  {"type": "drop", "detail": "Robgoblin (enemy) for the Casual Pixie Doll collection; the wiki lists the collection's spawn type as Robgoblin, quality Common, reward column 'Pixie Casual Doll' 21 coins", "where": "Southern Wilds", "price": "21 coins (wiki reward figure for the collection, not a per-item price)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/collections.json:6687-6772 (wiki:4:108 'Casual Pixie Doll', entry 'Casual Doll Cap'; source page 'Toys (Collections)', revision 31048, 2013-08-21); wiki 'Toys (Collections)' via lookup"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client definition: locale 40610 'Casual Doll Cap', description 'This item can be added to the Casual Pixie Doll Collection' (client 1248222261 for the collection line); two definition ids 3394 and 3442, no coin store price", "source": "locale:40610; locale:132310 (ui 'Casual Pixie Doll Collection')"},
  {"claim": "Wiki 'Toys (Collections)' lists 'Casual Doll Cap' as one of the 8 entries of the Casual Pixie Doll collection (Cap, Jacket, Shirt, Accessories, Ring, Shoes, Boots, Pants)", "source": "wiki page 'Toys (Collections)' (lookup); repo:prototype/osfr-tools/data/content/collections.json:6696-6745"},
  {"claim": "Collection listed on the wiki 'List of Collections' page as '[Casual] [Pixie] [Doll]'", "source": "wiki page 'List of Collections' (lookup)"},
  {"claim": "Collection set reward/meta: the 'Pixie Casual Doll' item is listed as 21 (coins) on the wiki; the Elite/Pixie doll meta set is also 21", "source": "repo:prototype/osfr-tools/data/content/collections.json:6750-6759, 8659-8665"}
 ],
 "confidence": 0.5,
 "open": [
  "No wiki page or article names a per-item acquisition for Casual Doll Cap specifically; the Robgoblin drop is inferred from the collection-level spawn_type, not from a per-item drop table.",
  "The 21 figure is attached to the collection reward ('Pixie Casual Doll'), not to the cap; it is not a sale price for the cap and no coin vendor stocks it (no store entry in stores.json, no client coin price).",
  "Two definition ids (3394, 3442) share the name; the tint/variant split was not checked.",
  "Retirement status not stated by any source; the collection is on the wiki list but no date says whether the Robgoblin drop still exists.",
  "The first-pass tag 'collection' is consistent with the evidence; 'live: yes' rests on the wiki listing, not a current-date check."
 ]}
