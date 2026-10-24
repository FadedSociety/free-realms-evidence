<!-- fleet job=citem-infer id=cextra-large-flutterfish-407642-v1 status=done turns=5 usd=0.0033 tokens(read,write,in,out)=[33695, 11624, 12, 3046] model=claude-haiku-5-5 -->
# Extra Large Flutterfish

{"item": {"name": "Extra Large Flutterfish", "locale_id": 407642, "kind": "other"},
 "sources": [
  {"type": "drop", "detail": "Caught by fishing (reel-in catch) as the largest size of Flutterfish; the species is catchable at level 1 with Frostflies lure bonus", "where": "Sacred Grove Shallows (Stillwater Crossing boat) and Rainbow Lake (Lakeshore boat)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/fishing_spots.json:206-211 (flutterfish item ids 68041-68044, XL = 68044); wiki page Sacred Grove Shallows and Rainbow Lake (Types of Fish: Flutterfish catchable at level 1); repo:notes/Build Guides/Content/Jobs/Fisherman.md:188-189, 221"},
  {"type": "collection", "detail": "Collection 'Extra Large Catch of the Day' (collection id 308, name locale 419595, description locale 419587 'A collection of extra large fish.'); this item is entry 6 of 7, reward is client item 2735 x1", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:23106-23114 (entry name_id 407642, item_definition_id 68044); locale:419587; wiki page Sacred Grove Shallows and Rainbow Lake list 'Extra Large Catch of the Day' under Collections"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 407642 'Extra Large Flutterfish' is definition 68044, the XL tier of the Flutterfish fish family (68041-68044)", "source": "locale:407642; repo:prototype/osfr-tools/data/content/fishing_spots.json:206-211; repo:prototype/osfr-tools/data/content/collection_catalogue.json:23112"},
  {"claim": "Flutterfish is catchable by fishing at Sacred Grove Shallows and Rainbow Lake from level 1", "source": "wiki: Sacred Grove Shallows; wiki: Rainbow Lake; repo:notes/Build Guides/Content/Jobs/Fisherman.md:188-189"},
  {"claim": "Quest 'Shallows: Catch of the Day' (Melanie, Sacred Grove Shallows, Fisherman 20) requires reeling in an extra large Flutterfish; it is an objective, not a reward, and the reward line reads '30 stars and 16 coins'", "source": "video:0LCKMQz3zMs/00298, 00304, 00306; repo:notes/Build Guides/Content/Jobs/Fisherman.md:171"},
  {"claim": "Flutterfish is a Frostflies lure target (10% better chance)", "source": "wiki: Fisherman; repo:notes/Build Guides/Content/Jobs/Fisherman.md:269"},
  {"claim": "Client has a 'Flutterfish Medley' cooking dish that uses Flutterfish as ingredient (Chef fish-dish quest for Merri De'Flor); the XL fish is not named as the ingredient", "source": "locale:412849; repo:notes/Build Guides/Content/Jobs/Chef.md:191"}
 ],
 "confidence": 0.8,
 "open": [
  "No coin store price in client definition or stores.json; no coin vendor sale found, so no vendor/coin_shop/marketplace source is listed.",
  "Client definition has empty description, no slots/models beyond a single class; the item is not a wiki-article item and no wiki page names this exact size.",
  "Per-size catch rates for XL Flutterfish are not in the data; the fishing_spots.json entry only proves the item id is in the spot's pool.",
  "Collection reward item 2735 was not resolved to a name, and the collection's exact display name (locale 419595) was not read in the locale table.",
  "The Catch of the Day quest is listed as a source of the item only as a consumer (objective), not a reward; if the rebuild needs quest-reward rows, none apply.",
  "Whether the XL Flutterfish is still obtainable on live servers is not confirmed by a dated source; treated as live based on the first-pass tag and the wiki Fishing listings."
 ]}
