<!-- fleet job=citem-infer id=cfresh-sand-dollar-1413-v2 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[17572, 12990, 8, 2461] model=claude-haiku-5-5 -->
# Fresh Sand Dollar

{"item": {"name": "Fresh Sand Dollar", "locale_id": 1413, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 8 of 8 in the 'Sand Dollars' collection (catalogue id 30; entries locale 1406-1413). Membership only: the collection is where this item is used, not an acquisition method. Collection completion reward listed as 2 coins + 50 XP (sanctuary-derived, unverified against live).", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1133-1228 (id 30, name_id 38698, description_id 38699, entry id 180 = locale 1413 / item_definition 3265; entries carry item_link 'sanctuary'); repo:prototype/osfr-tools/data/content/collections.json:11694 ('Sand Dollars'); wiki page List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections) lists '[Sand] [Dollars]'; locale:38698, locale:38699 ('Sand Dollars found in Seaside.')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 1413 'Fresh Sand Dollar'; sibling entries are locale 1406 Fancy, 1407 Salty, 1408 Smelly, 1409 Slimy, 1410 Dried, 1411 Sandy, 1412 Ordinary, 1413 Fresh Sand Dollar.", "source": "locale:1406-1413 (locale lookup 'Sand Dollar')"},
  {"claim": "Fresh Sand Dollar is entry 180 of collection id 30 ('Sand Dollars'), item_definition_id 3265.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1133-1228 (item_definition_id 3265 at line 1211)"},
  {"claim": "The collection is named 'Sand Dollars' on the wiki's List of Collections page.", "source": "wiki: List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections); locale:38698"},
  {"claim": "Collection description text is 'Sand Dollars found in Seaside.' This describes the collection as a whole, not a drop or gather source for Fresh Sand Dollar specifically.", "source": "locale:38699"},
  {"claim": "Item description text 'This item can be added to the Sand Dollars Collection' is a client string; it confirms collection membership only.", "source": "locale:132291"},
  {"claim": "No coin vendor sells item 3265: no coin store price in the client definition and no item 3265 in stores.json.", "source": "client definition (coin_store_prices empty); repo:prototype/osfr-tools/data/content/stores.json (no item 3265)"},
  {"claim": "No wiki article, video, or article fact names a way to obtain Fresh Sand Dollar.", "source": "lookup over client, wiki, articles, video for 'Sand Dollar'"},
  {"claim": "Critique fix applied: the earlier cited locale:2502242177 does not exist and is dropped; the Seaside text is locale:38699.", "source": "id_check; locale:38699"},
  {"claim": "Cheap-model first pass (live=yes) is a hint only; the catalogue rows are tagged item_link 'sanctuary', so live status is not confirmed.", "source": "jev_first_pass; collection_catalogue.json item_link fields"}
 ],
 "confidence": 0.4,
 "open": [
  "No acquisition source is evidenced. The collection entry is membership, not how a player gets the item. Where Fresh Sand Dollar drops, is gathered, or is bought is unknown; 'found in Seaside' (locale 38699) is a collection-level hint only. Not wireable as a drop until a source line exists.",
  "The collection completion reward (2 coins, 50 XP) comes from the Sanctuary-derived catalogue and has no wiki or live check.",
  "Retirement status unknown: the wiki List of Collections (rev 27852, 2013-07-13) is the only dated source and does not say whether the collection was still obtainable.",
  "Live status is 'unsure': the entry data carries item_link 'sanctuary'; the cheap-model 'live=yes' is not evidence."
 ]}
