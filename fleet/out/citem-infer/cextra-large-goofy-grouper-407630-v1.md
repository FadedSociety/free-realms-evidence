<!-- fleet job=citem-infer id=cextra-large-goofy-grouper-407630-v1 status=done turns=7 usd=0.0041 tokens(read,write,in,out)=[62880, 13676, 16, 3590] model=claude-haiku-5-5 -->
# Extra Large Goofy Grouper

{"item": {"name": "Extra Large Goofy Grouper", "locale_id": 407630, "kind": "other"},
 "sources": [
  {"type": "drop", "detail": "Caught by fishing: Goofy Grouper fish (minimum level 14, rarity 3, difficulty 3). Extra Large is one of the four size tiers (S/M/L/XL weights; XL is the largest tier). Catchable with the Mega Slider lure (+10% chance).", "where": "Frostbitten Banks (fishing spot)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/fishing.json:1326-1344; repo:notes/Build Guides/Content/Jobs/Fisherman.md:192 and :226; repo:notes/Build Guides/Gameplay/Fishing.md:133; locale:99952 (Goofy Grouper fish name); locale:409557 and locale:412929 / 3475855459 (Mega Slider lure text); freerealms-wiki Fisherman page (Mega Slider lure text)"},
  {"type": "collection", "detail": "Listed as a fish entry in a collection catalogue (catalogue id 2160, index 4, item definition 68032, icon 4269). The collection's name was not resolved in the catalogue file.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:23088-23096"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "The client name 'Extra Large Goofy Grouper' is locale 407630, item definition 68032; it is the XL size of the Goofy Grouper fish.", "source": "locale:407630; repo:prototype/osfr-tools/data/content/collection_catalogue.json:23091-23094; Sanctuary/src/Resources/ClientItemDefinitions.json (comment 'Extra Large Goofy Grouper')"},
  {"claim": "Goofy Grouper is a fish caught at Frostbitten Banks at level 14; the Fisherman wiki/build notes list Goofy Grouper 14 at Banks.", "source": "repo:notes/Build Guides/Content/Jobs/Fisherman.md:192, :226; repo:prototype/osfr-tools/data/content/fishing.json:1328-1331; locale:410545 (Frostbitten Banks fishing NPC text lists goofy grouper)"},
  {"claim": "The Frostbitten Banks Fisherman quest 'Showing Off Your Skills' has the objective 'Catch an extra large Goofy Grouper'. This is a quest objective, not a reward for the item.", "source": "locale:410236; locale:4052517283"},
  {"claim": "The Mega Slider lure gives a 10% higher chance of catching Goofy Grouper, Finless Fish and Fanged Grouper. Lure coin price is not in this pack.", "source": "locale:412929; freerealms-wiki Fisherman page (lure list)"},
  {"claim": "No coin vendor, Station Cash, Coin Shop or prize-wheel entry was found for this item; the client definition has no coin store price.", "source": "client definition (coin_store_prices empty); repo search for 68032 and 407630 returned only the fishing and collection files"}
 ],
 "confidence": 0.6,
 "open": [
  "The fish is a fishing catch, not a fixed drop. The closest source type is 'drop'; the fishing system is not a listed category, so a 'fishing' source type may be better.",
  "The collection that holds catalogue entry 2160 was not named in the repo files. Check which collection it belongs to before recording the collection source.",
  "Catch rate, the XL size weight range, and the exact weight thresholds for XL were not checked against a wiki or video source. Only the size-weight array is in the repo (27/35/27/11 for the size tiers; which tier is XL is not labelled).",
  "No wiki article, image or video frame covers this XL fish directly. The Fishing wiki page lists only the 'Goofy Grouper' fish name.",
  "Whether the fish is still catchable in the live game is not confirmed; no retirement source was found. The live field is 'unsure'.",
  "The first-pass tag said 'drop' and 'live: yes'. The source check does not confirm 'live'; it only shows the item is in the fishing and collection data."
 ]}
