<!-- fleet job=citem-infer id=cmost-effective-trophy-66974-v1 status=nothing_found turns=5 usd=0.0037 tokens(read,write,in,out)=[39324, 16511, 12, 2418] model=claude-haiku-5-5 -->
# Most Effective Trophy

{"item": {"name": "Most Effective Trophy", "locale_id": 66974, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text for the name is locale 66974 'Most Effective Trophy'; the item's description is locale 132428 'This item can be added to the Combat Trophies Collection' (the 'Combat Trophies Collection' is the collection it feeds).", "source": "locale:66974; locale:132428"},
  {"claim": "The client definition is item definition 23361 with no models, no class and no coin store price, so it has no coin vendor sale.", "source": "client definition in evidence pack; repo:data/content/stores.json has no entry (no price field)"},
  {"claim": "The name sits in a cluster of trophy items (Team, Capture The Flag, Dueling, Most Time Played, Most Improved, Highest Ranked) that are all defined with the same collection-style description. Other trophies in this cluster are also undocumented on the wiki.", "source": "locale:66969-66975; Sanctuary/src/Resources/ClientItemDefinitions.json:480275 (Comment 'Most Effective Trophy'); FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:480275"},
  {"claim": "The item is present in the client definitions of several community server copies (Sanctuary, Lxzxrus-Free-Realms-Server, FreeRealms-Legacy, TCG-Files), so it existed in the shipped data. None of those copies gives a source or a price.", "source": "refs ClientItemDefinitions.json comment lines (above)"},
  {"claim": "The wiki has a 'List of Collections' page, but it shows only collection names and no trophy item or source list.", "source": "wiki: List of Collections"}
 ],
 "confidence": 0.2,
 "open": [
  "No source found. No wiki page, article, video frame, coin vendor, quest reward, enemy drop, or event names this trophy. Neither the coin store data nor the prize wheel data lists it.",
  "The trophy is probably a reward for a combat achievement or minigame placement (its name matches the 'Trophy' tier idea in Rewards and Collections.md). That is an inference, not evidence, so it is not listed as a source.",
  "The 'Combat Trophies' collection name is confirmed (locale 132428), but the collection's member list and the trophy's award condition are not in the sources provided.",
  "Liveness is unsure: the client defines it, but no evidence shows it was ever awarded on live servers.",
  "The first-pass tag said 'live: yes, kind: collection'. That is a hint only and is not confirmed here.",
  "Locale ids do not line up with the names in the pack's cluster in one place: locale 66973 reads 'Combat Trophies' in the en_us_data.dat extract, while the pack names it 'Most Improved Trophy'. Verify the id mapping before using the cluster."
 ]}
