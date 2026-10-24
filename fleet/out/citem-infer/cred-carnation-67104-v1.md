<!-- fleet job=citem-infer id=cred-carnation-67104-v1 status=done turns=7 usd=0.0052 tokens(read,write,in,out)=[71915, 19007, 16, 4121] model=claude-haiku-5-5 -->
# Red Carnation

{"item": {"name": "Red Carnation", "locale_id": 67104, "kind": "collection"},
 "sources": [{"type": "other", "detail": "Flora gathering: the Carnations flower line (Tulips/Orchids/Carnations/Roses/Daisies/Lilies/Sunflowers/Daffodils) on the wiki's Flora table; Red Carnation is one entry of the Carnations collection. Inferred from the collection page, not a confirmed per-item source.", "where": null, "price": null, "currency": null, "source": "freerealms-wiki/wikitext/2038-27852-f0e36d086ea8.wiki lines 371-378 (List of Collections, Flora table, rev 27852, 2013-07-13); refs freerealms-wiki/harvest/lists/tables.json:3494"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client definition: item 23491, name_locale_id 67104 'Red Carnation', description 'This item can be added to the Carnations Collection'; no coin store price (coin_store_prices empty), no model files.", "source": "locale:67104; pack client_definition"},
  {"claim": "Red Carnation is entry index 1 of collection 186 (name_id 67552, 'Carnations'), with item_definition_id 23491, flag6=1, category 3; sibling entries Pink Carnation (23492) and others.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:14912-14929"},
  {"claim": "The 'Carnations' collection is listed on the wiki's List of Collections page (wiki:3:71, Flora-type collection, page id 2038, rev 27852), with a separate Snowhill Carnations collection.", "source": "repo:prototype/osfr-tools/data/content/collections.json:5303-5326; freerealms-wiki/wikitext/2038-27852-f0e36d086ea8.wiki:92,103"},
  {"claim": "Flora stage-1 items include Carnations, which progress to Golden Flowers and an Exotic Golden Flower final reward; Snowhill carnations go to Rare Snowhill Flowers.", "source": "freerealms-wiki/wikitext/2038-27852-f0e36d086ea8.wiki lines 371-387"},
  {"claim": "Client text for the item name and its sibling flower names (Yellow Orchid through Yellow Carnation, ids 67099-67109) sit together as one collection cluster; no other line names a Red Carnation source.", "source": "locale:67099-67109"},
  {"claim": "No vendor stock, wiki article, article facts, or video frames name Red Carnation; the earlier pack for this item (quest-lines/citem-packs.json 'cred-carnation-67104') has the same empty data.", "source": "refs quest-lines/citem-packs.json:304313-304361"}],
 "confidence": 0.35,
 "open": ["No source names Red Carnation directly: the Flora harvest-to-collection mapping is inferred from the collection table and the wiki's Flora table, not from a per-item drop or gather record.",
  "The wiki's Flora row gives Carnations as a stage-1 item but not whether the Red tint is a separate gather or a tint of the base Carnation (the client has 'Carnations' as a collection with tinted entries).",
  "The collection_catalogue entry carries item_link 'sanctuary' and icon_tint 95 (vs 92 for other entries); the meaning of that link is unverified.",
  "No price, vendor, crafting, or prize-wheel source found. The 2013 wiki revision is the newest collection page in the refs, so later changes are unknown.",
  "The jev first-pass tag 'live: yes' is unverified; the collection entry exists in the client but no live-server evidence was found.",
  "No critiques were carried in this pack, so none needed fixing."]}
