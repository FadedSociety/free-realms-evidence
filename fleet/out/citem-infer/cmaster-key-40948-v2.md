<!-- fleet job=citem-infer id=cmaster-key-40948-v2 status=done turns=5 usd=0.0033 tokens(read,write,in,out)=[44191, 14140, 12, 2166] model=claude-haiku-5-5 -->
# Master Key

{"item": {"name": "Master Key", "locale_id": 40948, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Master Key' (definition 3732, name locale 40948); no coin store price, no model files, one variant.", "source": "locale:40948; client definition in pack"},
  {"claim": "Keys Collection description: 'This item can be added to the Keys Collection'.", "source": "locale:132352"},
  {"claim": "The Keys collection (name locale 7744 'Keys', description 7820) has eight entries; entry index 3 is name_id 40948 with item_definition_id 3732, item_link 'sanctuary'. The collection's reward is 4 coins/50 XP-type entries with no item rewards for the collection itself; it is a membership list, not an acquisition route.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 7317-7397 (collection id 93, entries id 664)"},
  {"claim": "Wiki Keys collection lists [master] [key] beside chest, spare, shackles and do-not-duplicate keys; the page does not say how to obtain any of them.", "source": "wiki File:Free Realms- Key locations D-0"},
  {"claim": "No vendor stock, store price, quest reward, drop, or event text names the Master Key in the client lookup, wiki, or articles.", "source": "lookup over client, wiki, articles, video for 'Master Key'; repo search for 3732"}
 ],
 "confidence": 0.25,
 "open": [
  "No acquisition source found. Collection membership (Keys collection, id 93) is not a way of obtaining the item, so it is recorded as a fact, not a source.",
  "Live status unknown: the wiki key-locations page is undated and nothing in the pack dates the Keys collection. Do not treat as live or retired without a dated source.",
  "Previous answer's locale 390930417 was wrong; the Keys description is locale 132352 (siblings 132353 Fancy, 132451-132454 Everyday/Useful/Special/Sacred).",
  "Previous claim about ClientItemDefinitions.json line 68431 comment entries in Lxzxrus and FreeRealms-Legacy was not verified in this pass and is dropped.",
  "The Keys collection reward is listed in the catalogue as coins 0 with no items (the 4-coin value belongs to the preceding collection id 92 block), so no item reward is confirmed for this collection.",
  "Next step: find how the Keys collection entries are earned (chest or Snowhill key drops, quest rewards), which the wiki page does not state."
 ],
 "critiques_addressed": ["Cited locale 132352 instead of 390930417", "Removed collection as acquisition source", "Live/retired left unknown", "Dropped unverified refs claim"]
}
