<!-- fleet job=citem-infer id=cgold-softball-trophy-66967-v1 status=done turns=6 usd=0.0036 tokens(read,write,in,out)=[49076, 13511, 14, 2786] model=claude-haiku-5-5 -->
# Gold Softball Trophy

{"item": {"name": "Gold Softball Trophy", "locale_id": 66967, "kind": "collection"},
 "sources": [{"type": "collection", "detail": "Entry 8 of the 'Gold Trophies' collection (catalogue id 168, name locale 67534); the item is a collection member, not a sold or dropped item. Completing the collection pays 10 coins and 50 XP (profile 48).", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13170-13265 (entry id 1229, item_definition_id 23354, name_id 66967); collections.json key wiki:6:197 'Gold Trophies' sourced from wiki 'List of Collections' (revision 27852, 2013-07-13)"}],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name locale 66967 is 'Gold Softball Trophy', definition id 23354, description 'This item can be added to the Gold Trophies Collection' (locale 132427).", "source": "locale:66967; locale:132427"},
  {"claim": "Definition 23354 is entry index 8 of the Gold Trophies collection (catalogue id 168, name locale 67534 'Gold Trophies'), with sibling trophies 23347-23353 at name locales 66960-66966.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13170-13265"},
  {"claim": "The Gold Trophies collection is listed on the wiki 'List of Collections' page; its collection description is 'A collection of gold trophies for being the best!' (locale 67646).", "source": "wiki:List of Collections; locale:67646; repo:prototype/osfr-tools/data/content/collections.json wiki:6:197"},
  {"claim": "Collection reward for completing Gold Trophies: 10 coins and 50 XP.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13252-13264"},
  {"claim": "The item has no coin store price and no coin vendor stock in the pack; the client definition lists coin_store_prices as empty.", "source": "evidence pack client_definition; repo:data/content/stores.json has no entry for 23354"},
  {"claim": "The first-pass tag 'collection' is consistent with the catalogue, which files it under collection category 6.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13170-13174"}
 ],
 "confidence": 0.6,
 "open": [
  "How a player earns an individual Gold Softball Trophy (the sport-event or achievement that grants it) is not documented in any wiki page, article, video or answer in the pack. The 'Gold Trophies' collection is the only source found.",
  "The wiki 'List of Collections' page lists '[Gold] Medals' and 'Silver/Bronze [Trophies]' but I did not confirm the Gold Trophies collection's member list on the wiki; the membership comes from the client catalogue.",
  "Retirement status is unknown: no source states whether the trophy or the collection was retired.",
  "The client's trophy-sibling set (Last Man Standing, Team, CTF, Dueling, Most Time Played Trophy, locales 66968-66972) is a separate achievement-trophy group and was not checked against this item."
 ]}
