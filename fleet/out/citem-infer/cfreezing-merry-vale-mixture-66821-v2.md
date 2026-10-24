<!-- fleet job=citem-infer id=cfreezing-merry-vale-mixture-66821-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5497, 7564, 6, 1925] model=claude-haiku-5-5 -->
# Freezing Merry Vale Mixture

{"item": {"name": "Freezing Merry Vale Mixture", "locale_id": 66821, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 6 of the Merry Vale Mixture collection (collection id 150). This is a collection component, not an acquisition source; the loose mixture's source is unknown (see open).", "where": "Merry Vale", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11492-11495 (name_id 66821, item_definition_id 23208); repo:prototype/osfr-tools/data/content/collections.json:11526 (Merry Vale Mixture); locale:132409; wiki List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 23208 is named 'Freezing Merry Vale Mixture' (locale 66821) with description 'This item can be added to the Merry Vale Mixture Collection' (locale 132409).", "source": "locale:66821; locale:132409"},
  {"claim": "It is entry 6 of collection 150 'Merry Vale Mixture', alongside Toxic, Clean, Purified, Dirty, Boiling, Magical and Mystical Merry Vale Mixtures.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11435-11500; locale:66816-66823"},
  {"claim": "The wiki List of Collections lists 'Merry Vale Mixture' entries.", "source": "wiki List of Collections"},
  {"claim": "The wiki Merry Vale location page lists '[Merry] [Vale] [Mixture]' among its location items (with Rare Exploration, Water Samples, Liquid Concoction); it does not show a Collections heading. The earlier claim about a Collections heading is withdrawn.", "source": "wiki Merry Vale"},
  {"claim": "Video frames show 'You receive 1 Magical Merry Vale Mixture' near Rich Tin Mining / Gold-Tipped Dragon / Fairy Cultist. They show the Magical colour only, not Freezing; the earlier source entry citing them for Freezing was removed.", "source": "video:9rPMuvwc728/00172; video:9rPMuvwc728/00174"},
  {"claim": "No coin store price (no entry for 23208 in stores.json), no vendor stock, no quest reward, no enemy drop and no event naming the Freezing colour were found.", "source": "repo:data/content/stores.json; lookup client/wiki/video"}
 ],
 "confidence": 0.3,
 "open": [
  "Loose-item acquisition for the Freezing Merry Vale Mixture is unverified. The only video evidence (video:9rPMuvwc728/00172, 00174) shows the Magical colour being received near Rich Tin Mining / Gold-Tipped Dragon / Fairy Cultist, so the method is seen for Magical only. Whether Freezing uses the same method is unknown.",
  "The collection reward for completing the Merry Vale Mixture collection is not recorded (reward: null in collections.json).",
  "The wiki Merry Vale page lists the mixture as a location item, not a collection heading; it does not say how the mixture is obtained.",
  "Wireable: not a schema field. Per the critique, the item is not wireable with a price, quest, enemy or event source. Only collection membership is evidenced."
 ]}
