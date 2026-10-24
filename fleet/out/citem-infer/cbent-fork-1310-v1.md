<!-- fleet job=citem-infer id=cbent-fork-1310-v1 status=done turns=9 usd=0.0073 tokens(read,write,in,out)=[119943, 29159, 20, 4915] model=claude-haiku-5-5 -->
# Bent Fork

{"item": {"name": "Bent Fork", "locale_id": 1310, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Forks collection (collection id 33, name locale 38710 'Forks', category 6 = Robgoblin Junk / wiki 'Various Robgoblin Junk'). Bent Fork is entry 1 of 8 (locale 1310-1317: Bent Fork, Silver Fork, Rusty Fork, Primitive Fork, Fancy Fork, Plastic Fork, Spork, +1). Completing the collection grants 10 coins and item definition 3177 (unnamed in the pack). Bent Fork itself is one collectible piece; the collection is the source.", "where": null, "price": null, "currency": null, "source": "wiki: List of Collections (the 'Various Robgoblin Junk' group lists 'Forks'); repo:prototype/osfr-tools/data/content/collection_catalogue.json:1325-1420 (collection id 33, entries 1310 = item 3162 'Bent Fork'); locale:38710 = 'Forks'; repo:prototype/osfr-tools/data/content/collections.json:11845-11847 (category 6 'Robgoblin Junk' = wiki 'Various Robgoblin Junk'); client description locale:132293 'This item can be added to the Forks Collection'"},
  {"type": "drop", "detail": "Pieces of Robgoblin junk collected from the world (the wiki groups the Forks under 'Various Robgoblin Junk' collections; the per-spawn pickup location for this piece is not recorded)", "where": null, "price": null, "currency": null, "source": "wiki: List of Collections ('Various Robgoblin Junk'); repo:prototype/osfr-tools/data/content/collections.json:11845-11846. Spawn mechanics not verified: see open."}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Bent Fork is client item definition 3162 with name locale 1310 and description locale:132293 'This item can be added to the Forks Collection'; no coin store price and no model files.", "source": "client definition in pack; locale:1310; locale:132293"},
  {"claim": "Bent Fork is entry 1 of collection id 33, named 'Forks' (locale 38710), with 8 entries and a completion reward of 10 coins and item 3177.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1325-1420; locale:38710"},
  {"claim": "The wiki's List of Collections shows 'Forks' under the Various Robgoblin Junk group, alongside Spoons, Knives and Plates.", "source": "wiki: List of Collections (page:ns0)"},
  {"claim": "Client category 6 is labelled 'Robgoblin Junk' and the wiki label is 'Various Robgoblin Junk'.", "source": "repo:prototype/osfr-tools/data/content/collections.json:11843-11848"},
  {"claim": "The shipped client's item 3162 is in the collection catalogue as entry 1310 with item_definition_id 3162.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1337-1341"},
  {"claim": "The cheap first-pass tag (live yes, kind collection, source drop) is consistent with the wiki listing, but the drop part is only a guess.", "source": "jev_first_pass (hint only)"}
 ],
 "confidence": 0.55,
 "open": [
  "No wiki article or video frame names Bent Fork or the Forks collection directly; the only wiki evidence is the List of Collections group entry.",
  "Source type for the individual forks is not confirmed: 'drop' (Robgoblin junk pickups) is inferred from the 'Various Robgoblin Junk' group label, not from a recorded spawn or enemy table. Where (zone) is unknown.",
  "Collection reward item 3177 is not named in the pack; its identity and whether it is a further source for Bent Fork are unverified.",
  "The collection_catalogue rows are (R) reconstructions from the wiki and Legacy data (collections.json gaps note: no first-party reward IDs or amounts). Treat the 10 coins and item 3177 as unverified.",
  "Collection entry 8 in the catalogue (index 7-8: Spork and one more) and the total of 8 entries were not fully cross-checked against the wiki's Forks list.",
  "No coin store price exists, so no coin-vendor sale is claimed. Retirement status is not recorded in any source in the pack."
 ]}
