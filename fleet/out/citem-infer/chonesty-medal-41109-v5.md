<!-- fleet job=citem-infer id=chonesty-medal-41109-v5 status=nothing_found turns=3 usd=0.0029 tokens(read,write,in,out)=[20116, 15353, 8, 1610] model=claude-haiku-5-5 -->
# Honesty Medal

{"item": {"name": "Honesty Medal", "locale_id": 41109, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Honesty Medal' is locale 41109.", "source": "locale:41109"},
  {"claim": "Client description 'This item can be added to the Honorable Mention Medals Collection' is locale 132372; the collection name 'Honorable Mention Medals' is locale 7764.", "source": "locale:132372; locale:7764"},
  {"claim": "Collection id 113 (name_id 7764) entry index 7 is id 825, name_id 41109, icon_id 455, icon_tint_id 117, item_definition_id 3893, item_link 'sanctuary'.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 9407-9415"},
  {"claim": "Repo search for 3893 and 'Honesty Medal' finds only the collection entry and collections.json name 'Honorable Mention Medals' (line 10014); no coin store row, vendor stock, quest, drop or event for definition 3893.", "source": "repo search, prototype/osfr-tools/data/content"},
  {"claim": "Lookup of 'Honesty Medal' across client, wiki, articles and video returns only locale:41109; no wiki page, article or video names it.", "source": "lookup (all sources)"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. Sources are empty rather than guessed. The item stays unwireable until a real source is found.",
  "Correction to the prior answer: the description locale is 132372 in the live locale table. The id 389474415 appears in older locale dumps in the repo, but it is not in the current client table, so it is dropped as a citation here. The 'open[2]' citation to 389474415 is removed.",
  "The collection completion reward (8 coins, item 3850, 50 XP) in collection_catalogue.json lines 9426-9445 is unverified and is not a source for the medal.",
  "item_link 'sanctuary' on the collection entries is a lead for checking Sanctuary-era data; it is not a status claim.",
  "Live status is unsure: the client still defines the item and the collection, but no post-2013 source confirms it is obtainable and no retirement source was found."
 ]}
