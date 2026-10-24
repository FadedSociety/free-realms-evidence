<!-- fleet job=citem-infer id=cclump-of-bat-fur-23236-v1 status=nothing_found turns=10 usd=0.0075 tokens(read,write,in,out)=[158196, 25998, 22, 5326] model=claude-haiku-5-5 -->
# Clump of Bat Fur

{"item": {"name": "Clump of Bat Fur", "locale_id": 23236, "kind": "other"},
 "sources": [{"type": "collection", "detail": "Entry index 2 of collection id 154 (collection name locale 67520 'Knives'); the entry is labelled 'Hunting Knife' (locale 66849). No drop, vendor, quest or event source found.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11827-11845 (item_definition_id 23236, entry id 1111)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item definition 23236 is named 'Clump of Bat Fur' in the client (locale 23236); the client has no description for it and no model files.", "source": "locale:23236"},
  {"claim": "Item 23236 appears in the collection catalogue as a member of collection 154, the one named 'Knives' (locale 67520), at entry index 2.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:11819-11845"},
  {"claim": "The entry name for that slot is 'Hunting Knife' (locale 66849), which does not match the item name 'Clump of Bat Fur', so the catalogue link is suspect.", "source": "locale:66849; repo:prototype/osfr-tools/data/content/collection_catalogue.json:11843"},
  {"claim": "The neighbouring items 23231-23233 (Wooly Underpants, Regal Bat Loincloth, Fashionable Troll Shirt) and 23234-23235, 23237-23240 form a same-named cluster of fur/bat/yeti/troll costume-style items; in the catalogue 23231-23233 are attached to collection 153 (name 'Sanctuary Mixture', locale 67519) whose entries are named 'Boiling Sanctuary Mixture' etc.", "source": "locale:23231-23240; locale:67519; repo:collection_catalogue.json:11774-11792"},
  {"claim": "No coin store price: 23236 does not appear in data/content/stores.json. No wiki page, article fact, or video frame names the item. No vendor, quest reward, or enemy drop in the repo lists it.", "source": "repo search for 23236 and 'Bat Fur' (only collection_catalogue.json matched); lookup of wiki/articles/video returned no hits"},
  {"claim": "The first-pass tag 'drop' is not supported by any evidence in the pack.", "source": "jev_first_pass (hint only)"}
 ],
 "confidence": 0.25,
 "open": [
  "Real acquisition source is unknown. Likely candidates are a crafting/mining or event drop, but none is evidenced. Needs a wiki page, a video frame, or a quest/drop table that names the item.",
  "The collection catalogue ties item 23236 to collection 154 'Knives' with an entry labelled 'Hunting Knife'. Either the item id or the entry name is wrong; resolve before treating the collection as a source.",
  "Live status is unknown. The client defines the item, but no store, wiki, or source evidence confirms it was ever obtainable, so retired status is unknown too.",
  "The client definition has an empty description and no models, so this may be an unused or placeholder definition. Check the client flags before treating it as live content.",
  "Jev's first-pass 'drop' guess is unverified and was not used as evidence."
 ]}
