<!-- fleet job=citem-infer id=cgold-feather-1450-v2 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[17872, 14233, 8, 2789] model=claude-haiku-5-5 -->
# Gold Feather

{"item": {"name": "Gold Feather", "locale_id": 1450, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Member of collection 196 (Feather set: Yellow, Green, Blue, Black, Gold, White, Purple, Red Feather; entry index 5). Membership only: the collection is completed with these pieces and pays a reward (7 coins, item definition 23579, unlocks collection 197). No evidenced way to obtain the feather itself.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:15888-15984 (collection 196; entry 1450 at lines 15932-15940)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Gold Feather' is locale 1450; the client's Feather/Spring cluster is locale 1446-1456.", "source": "locale:1450"},
  {"claim": "Collection 196 entry id 1450 (index 5) is 'Gold Feather' by id match, with name_id 67188 and item_link 'legacy-unique-name'. Entry name_id 67188 has no locale text found (locale lookup ^67188 returned nothing), so the name link is by entry id only.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:15932-15940"},
  {"claim": "Collection 196 (name_id 67562, description_id 67674) reward: 7 coins, item 23579, collection_add 197. Locale lookups for 67562 and 67674 returned no text, so the set name and rules are unconfirmed.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:15888-15984"},
  {"claim": "Catalogue gives Gold Feather item_definition_id 23575; the client definition in the pack lists definition_ids [3302]. Searching the repo for 23575 and 3302 found no item-definition link to the feather. The ids conflict and are unresolved.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:15938; pack client definition"},
  {"claim": "No coin store price for the feather. The previous answer's stores.json:466 row is item_id 1454 (270 coins, category 102), not Gold Feather; item 1454 is a different item (client name 'Tightly Coiled Spring'). Verified by reading the line.", "source": "repo:prototype/osfr-tools/data/content/stores.json:466"},
  {"claim": "No wiki page, article or video names Gold Feather; lookup returns only the client locale entry.", "source": "lookup client/wiki/articles/video 'Gold Feather'"}
 ],
 "confidence": 0.3,
 "open": [
  "Wireable as an acquisition source: false. The only evidence is collection 196 membership and the set's reward; no vendor, drop, quest, event, or coin sale of the feather itself is evidenced.",
  "Definition id conflict: pack says 3302, catalogue says 23575 for entry 1450. Confirm which item definition the client uses for Gold Feather before wiring any source.",
  "Entry 1450 matches locale 1450 by id, but the catalogue's own name_id for that entry is 67188, which has no locale text found. The client name link may be coincidental; verify.",
  "Collection 196's name (67562) and description (67674) do not resolve to locale text, so the set rules and reward wording are unconfirmed.",
  "Live status unsure: the item and collection exist in the client and catalogue, but no player, wiki or video evidence shows it is obtainable now or was retired.",
  "The pack's 'live: yes' and 'collection' tags from the cheap model were not used as evidence."
 ]}
