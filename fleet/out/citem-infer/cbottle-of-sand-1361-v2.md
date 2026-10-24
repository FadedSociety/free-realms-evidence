<!-- fleet job=citem-infer id=cbottle-of-sand-1361-v2 status=done turns=8 usd=0.0048 tokens(read,write,in,out)=[88824, 17104, 18, 3471] model=claude-haiku-5-5 -->
# Bottle of Sand

{"item": {"name": "Bottle of Sand", "locale_id": 1361, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Member of the Bottles collection (catalogue collection id 38, name_id 38729, entry id 241, index 4, item_definition_id 3213, item_link 'sanctuary'); the collection's description text is the one that reads 'This item can be added to the Bottles Collection'", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1975-1979 (entry for 3213 inside collection 38, which starts at line 1833); locale:132299 ('This item can be added to the Bottles Collection'); wiki: List of Collections (lists '[Bottles]')"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 3213 is 'Bottle of Sand' (locale 1361) and is entry 4 of collection 38 in the collection catalogue.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1975-1979; locale:1361"},
  {"claim": "The item's description text 'This item can be added to the Bottles Collection' resolves to locale:132299. The id 3113583733 cited in the earlier answer is not a locale id; it is the hash key for that same string in the client locale data file (locale/en_us_data.dat, ucdt 3113583733).", "source": "locale:132299; client locale/en_us_data.dat line 82194"},
  {"claim": "The wiki's List of Collections page lists a '[Bottles]' collection, consistent with the catalogue's Bottles collection.", "source": "wiki: List of Collections (lookup result)"},
  {"claim": "The catalogue's Bottles collection (38) holds sibling bottle items at entries 230-242 (locale 1350-1362 range), including 1359 Perfume Bottle (3211), 1360 Water Bottle (3212), 1361 Bottle of Sand (3213), 1362 Baby Bottle (3214). Sibling descriptions were not separately checked.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1950-1989"},
  {"claim": "The collection's reward block grants items and collection_add 36/37 for other collections, but no reward or vendor in the pack lists Bottle of Sand as an acquisition. No coin store price exists (stores.json has no item 3213 entry).", "source": "repo:prototype/osfr-tools/data/content/stores.json (no match); evidence pack client definition"}
 ],
 "confidence": 0.35,
 "open": [
  "Acquisition path is unknown. Membership in the Bottles collection does not say how a player obtained the physical item (drop, quest, event, prize wheel, or collection-only). Not wireable until a source is found.",
  "The Bottles collection's own name (locale 38729) did not resolve in the locale table, so the link between catalogue collection 38 and the wiki's '[Bottles]' entry is inferred from the matching description text, not confirmed.",
  "Retired/live status is unconfirmed. The first-pass 'live: yes' is only a hint and is not used here.",
  "Sibling descriptions (1356-1366) were not each checked for the Bottles text; only the item's own description (132299) is confirmed."
 ]}
