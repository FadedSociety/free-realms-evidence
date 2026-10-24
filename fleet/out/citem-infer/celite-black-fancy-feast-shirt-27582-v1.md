<!-- fleet job=citem-infer id=celite-black-fancy-feast-shirt-27582-v1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[12651, 15037, 8, 1884] model=claude-haiku-5-5 -->
# Elite Black Fancy Feast Shirt

{"item": {"name": "Elite Black Fancy Feast Shirt", "locale_id": 27582, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Elite Black Fancy Feast Shirt' is locale 27582, item class, slot 3 (chest), one definition (id 13717), model freestyle_<race>_<gender>_chest_tuckedlongslvapron.adr.", "source": "locale:27582"},
  {"claim": "Sibling items share the Fancy Feast set: Fancy Feast Shirt (locale 5893), Elite Pink Fancy Feast Shirt (locale 8310), Fancy Feast Hat/Shoes/Pants and Elite Black variants (locale 5907, 5909, 27639, 27641, 27642, 28375, 28729, 28731, 28732). The set's acquisition path is not documented in any source I could query.", "source": "locale:5893, locale:8310, locale:27582"},
  {"claim": "Client definition lists coin store price 9453 for this item. Repo stores.json has 9453-coin rows (e.g. item_id 87, 100, 102, 104), but no row with item_id 13717 exists, so the price cannot be tied to this item in our store data. 9453 is a common price shared by many items.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 80-83 (price rows); no item 13717 row found"},
  {"claim": "No wiki page, article fact, video frame, or vendor stock entry names this item. Searches for 'Fancy Feast' across wiki, articles and video returned no matches.", "source": "lookup (wiki, articles, video): no matches"}
 ],
 "confidence": 0.15,
 "open": [
  "No verified source. The first-pass guess of 'vendor' is unsupported: the 9453-coin price in the client definition is not linked to item 13717 in stores.json.",
  "Check whether the Fancy Feast set came from a coin vendor, a promotion, or an event (the set name suggests a themed event or holiday item). No source in the pack says which.",
  "Check the store data for a row keyed to definition 13717 or to the item's store id, and confirm the coin price, before accepting the 9453 price.",
  "Live status and retirement are unknown. The first-pass tag of 'live' is a hint only and is not confirmed by any source.",
  "Client cluster neighbour 'Rookie Demo Derby Shirt' (locale 27577) is not evidence of the same source."
 ]}
