<!-- fleet job=citem-infer id=cred-doll-1342-v1 status=done turns=9 usd=0.0056 tokens(read,write,in,out)=[105262, 19953, 20, 4010] model=claude-haiku-5-5 -->
# Red Doll

{"item": {"name": "Red Doll", "locale_id": 1342, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 1342 'Red Doll' (item definition 3194) carries the text 'This item can be added to the Dolls Collection', so it is a collection-set member, not a consumable or gear.", "source": "locale:1342; locale:4116032179 ('This item can be added to the Dolls Collection'); repo:prototype/osfr-tools/data/content/collection_catalogue.json:1731-1747 (collection id 37, name_id 38724, entry id 222, index 1, name_id 1342, item_definition_id 3194)"},
  {"claim": "The collection (name_id 38724) is the wiki page 'Toys (Collections)' (revision 31048, 2013-08-21); its Dolls section lists 'Red Doll' among Red, Green, Blue, Brown, Orange, Pink, Purple and Gold Doll, with no acquisition note against Red Doll.", "source": "wiki: Toys (Collections); repo:prototype/osfr-tools/data/content/collections.json:6935-6943"},
  {"claim": "Only Gold Doll on that page has a stated source (reward for completing Army Men). The page gives no reward, vendor, drop, price or event for Red Doll.", "source": "wiki: Toys (Collections) (Gold Doll entry)"},
  {"claim": "The client has no coin store price, no vendor stock entry, and no wiki article or video for Red Doll.", "source": "client definition (coin_store_prices empty); lookup of 'Red Doll' across wiki, client, articles and video returned only the Toys (Collections) listing and locale:1342"},
  {"claim": "Dolls-collection entries 1343-1349 (Green through Purple Doll) and 1342 share one collection set in the client catalogue, so the set is a collection of toy items rather than a single-source reward.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1742-1760; locale 1343-1349"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source for Red Doll (item 3194) is evidenced anywhere in the pack. The wiki Toys (Collections) page lists it in the Dolls set without a reward note. Need the full wiki Dolls section or a legacy/Sanctuary source that names how Red Doll was earned (quest, drop, event, or collection-set reward).",
  "The 'Dolls Collection' itself is a collection set, so it is where the item is stored, not a source. Do not record the set as a source of Red Doll unless a reward link is found.",
  "Liveness is unsure: the wiki page is a 2013 revision and no retirement note exists for Red Doll. The jev first pass said live: yes, but that is a hint only.",
  "Client shows a duplicate Red Doll name in ugdt strings (1910416303, 3654784091). These are likely other-language or different-category entries, not a second item; not verified."
 ]}
