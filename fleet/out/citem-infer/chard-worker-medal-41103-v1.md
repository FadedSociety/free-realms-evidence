<!-- fleet job=citem-infer id=chard-worker-medal-41103-v1 status=done turns=12 usd=0.0073 tokens(read,write,in,out)=[187432, 25107, 26, 4572] model=claude-haiku-5-5 -->
# Hard Worker Medal

{"item": {"name": "Hard Worker Medal", "locale_id": 41103, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item definition 3887 is entry 1 of the 'Honorable Mention Medals' collection (collection id 113, name_id 7764, category 6), with name_id 41103 and item_link 'sanctuary'.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9344-9361"},
  {"claim": "The collection's 8 entries are the Hard Worker through Honesty/Bravery medals (items 3887-3894, name_ids 41103-41110). The collection's completion reward is 8 coins plus item 3850 and 50 XP.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9352-9440"},
  {"claim": "The collection name 'Honorable Mention Medals' is listed on the wiki's List of Collections page (with the other medal and ring collections).", "source": "wiki: List of Collections (revid 27852, 2013-07-13), https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "Client text for the collection: 'This item can be added to the Honorable Mention Medals Collection' (description of the medal).", "source": "locale:389474415 / locale:132372 (client text table)"},
  {"claim": "No coin store price exists for definition 3887 in stores.json, and no vendor, quest, drop or event in the pack stocks or gives it.", "source": "client definition (coin_store_prices empty); repo search for 3887 in data/content returns only collection_catalogue.json"},
  {"claim": "The wiki's List of Collections has the Honorable Mention Medals entry but no entry list, so no per-medal acquisition method is documented.", "source": "wiki: List of Collections; collection_catalogue.json wiki:6:178 entries [] and entries_known false"}
 ],
 "confidence": 0.3,
 "open": [
  "The first-pass guess 'quest_reward' is not supported by any evidence in the pack or the repo. No quest, vendor, drop or event that gives item 3887 was found. Do not seed a quest_reward source until one is found.",
  "How players obtain the individual medal is unknown. The collection catalogue marks the entries item_link 'sanctuary', which may mean they are tied to a Sanctuary-side source, but no source text confirms this.",
  "The 'Honorable Mention Medals' collection's completion reward (8 coins, item 3850, 50 XP) is recorded in collection_catalogue.json, but the reward is for the collection, not for the medal, so it is not listed as a source.",
  "Live status is unverified: the first-pass tag says live 'yes', but the only support is the wiki category listing. No retirement or price evidence exists.",
  "Wiki has no article for the item or the collection's entries. Check the wiki's Honorable Mention Medals section (if any) or the forum for how the medals were earned."
 ]}
