<!-- fleet job=citem-infer id=cgold-star-1462-v1 status=done turns=9 usd=0.0071 tokens(read,write,in,out)=[136756, 26007, 20, 5044] model=claude-haiku-5-5 -->
# Gold Star

{"item": {"name": "Gold Star", "locale_id": 1462, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 3314 is named Gold Star (NameId 1462), description 'This item can be added to a collection.', DescriptionId 24229, icon 519, CategoryId 19, Cost 1, MemberDiscount 10.", "source": "refs:Sanctuary/src/Resources/ClientItemDefinitions.json:61553-61560 (Comment 'Gold Star'); also Lxzxrus-Free-Realms-Server and TCG-Files copies"},
  {"claim": "locale:1462 = 'Gold Star'; locale:1466 = 'Silver Star'; locale:1467 = 'Bronze Star'; 1463 'Medal of Honor'; 1464 'Distinguished Service'; 1465 'Commendation'; 1457-1461 are the Bronze/Copper/Steel/Rusted/Broken Spring items.", "source": "locale:1462, locale:1466, locale:1467, locale:1463-1465, locale:1457-1461"},
  {"claim": "Gold Star is a collection-fill item (its own description says it can be added to a collection), so its real use is as a collection member; the pack's first-pass kind 'collection' agrees.", "source": "client definition description (definition 3314)"},
  {"claim": "No coin store price for definition 3314 in our store data; no stores.json row references 3314.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no match for 3314)"},
  {"claim": "Name-matching collection row in our catalogue is not this item: collection_catalogue.json entry id 1462 (collection 198, name 'Ninja Magical Sword Essences') points at item_definition_id 23587, not 3314. Do not use that row as Gold Star's collection.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:16084-16100"},
  {"claim": "The earlier citem pack for this same item (cgold-star-1462) carries the same client facts and no source, so it adds no new source evidence.", "source": "refs:quest-lines/citem-packs.json:143562-143610"}
 ],
 "confidence": 0.3,
 "open": [
  "No collection is identified that Gold Star feeds. The Spring/Medal/Star cluster (locale 1457-1467) has no collection, wiki, article or video match in any root, so the collection and its reward are unknown.",
  "No acquisition source found: no vendor stock, no coin-store price, no quest reward, no drop, no event, no wiki page. Sources list is empty on purpose.",
  "Live status unsure: the item definition exists in several community client-definition copies (Sanctuary, Lxzxrus, TCG-Files, Sanctuary-PC2009), which shows it shipped, but no proof it was ever obtainable by players. The jev first pass said live 'yes'; that is a hint only.",
  "Sanctuary definition shows Cost 1 and MemberDiscount 10. These are client/server fields, not a coin store price, so no price is recorded.",
  "Next step: find which collection lists item definition 3314 (search client collection tables for item_definition_id 3314 or its locale 1462 entry in a different collection id), or check the Silver Star (1466) and Bronze Star (1467) siblings for a shared collection."
 ]}
