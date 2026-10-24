<!-- fleet job=citem-infer id=cship-in-a-bottle-1364-v1 status=done turns=9 usd=0.0055 tokens(read,write,in,out)=[107769, 20101, 20, 3845] model=claude-haiku-5-5 -->
# Ship in a Bottle

{"item": {"name": "Ship in a Bottle", "locale_id": 1364, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Bottles collection (collection id 39, name locale 38734 'Bottles'; description 38735). Ship in a Bottle is entry index 7 (item_definition_id 3216, name_id 1364, icon 1956). Completing the collection gives 6 coins + 50 XP (reward block). This is where the item is filed, not an acquisition source.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1936-2030 (entry at line 2005)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Ship in a Bottle' is locale 1364, definition 3216, with description 'This item can be added to the Bottles Collection'.", "source": "locale:1364; locale:3113583733 (client data); repo:quest-lines/citem-packs.json (cship-in-a-bottle-1364)"},
  {"claim": "The Bottles collection (id 39) lists Ship in a Bottle (3216) as entry 7 of 8 with the same name_id 1364; the collection is in the Sanctuary item_link set.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:2005"},
  {"claim": "Wiki 'List of Collections' lists a Bottles collection heading, so the collection is documented on the wiki index, but no wiki page names this item's acquisition.", "source": "wiki: List of Collections"},
  {"claim": "Client UI string 'This item can be added to the Bottles Collection' is locale 132299 (ui - Bottles Collection).", "source": "locale:132299"},
  {"claim": "The client name cluster (1359-1369: Perfume Bottle, Water Bottle, Message in a Bottle, Lightning in a Bottle, Pine Cones) shares a catalogue grouping, but none of these have a sourced acquisition route in the evidence pack.", "source": "repo:collection_catalogue.json; locale:1359-1369"},
  {"claim": "Store data has no coin store price for definition 3216 (coin_store_prices empty). No vendor stocks it in the pack.", "source": "client definition in evidence pack"}
 ],
 "confidence": 0.3,
 "open": [
  "No source for how a player obtains Ship in a Bottle: no vendor, marketplace, quest reward, drop, event, or crafting evidence found in the pack, wiki, articles, video, or repo. Left unfilled rather than guessed.",
  "The first-pass 'source_guess: drop' has no evidence behind it and is not used.",
  "Live status is unconfirmed: the catalogue entry exists, but no sale, drop, or reward ties it to a live period. The first-pass 'live: yes' is unverified.",
  "The Bottles collection's completion reward (6 coins, 50 XP) is the only sourced reward and is attached to the collection, not the item.",
  "No wiki page exists for Ship in a Bottle or the Bottles collection detail. Checking the wiki Bottles collection page and collection_catalogue reward logic for the other bottle items would be the next step."
 ]}
