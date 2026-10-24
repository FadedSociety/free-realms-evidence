<!-- fleet job=citem-infer id=cbronze-tag-medal-41065-v2 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[5689, 13151, 6, 1984] model=claude-haiku-5-5 -->
# Bronze Tag Medal

{"item": {"name": "Bronze Tag Medal", "locale_id": 41065, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 3 of collection 108 'Bronze Medals' (name_id 7759). The catalogue links item_definition 3849 to this collection. It does not say how a player obtains the medal itself. Completing the 8 entries (41063-41070) grants 3 coins, item 3858 x1, 50 XP (profile 12) and adds collection 109.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8836-8935 (entry id 781 at lines 8864-8871; reward block lines 8918-8935); wiki List of Collections https://freerealms.fandom.com/wiki/List_of_Collections (lists '[Bronze] [Medals]', no entries or sources)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name locale 41065 is 'Bronze Tag Medal', description 'This item can be added to the Bronze Medals Collection'.", "source": "locale:41065; locale:132367"},
  {"claim": "Client definition item_definition_id 3849 has no coin store price. A search of stores.json finds no item 3849, so no coin vendor sale is evidenced.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no match for 3849)"},
  {"claim": "Bronze Tag Medal is entry index 3 of collection 108 'Bronze Medals'. The 8 entries are item definitions 3847-3854 (locale 41063-41070). Every entry carries item_link 'sanctuary', a raw catalogue field that is not evidence of a player location.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8836-8917"},
  {"claim": "Collection completion reward is 3 coins, item 3858 x1, 50 XP (profile 12), and collection_add 109.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8918-8935"},
  {"claim": "The Bronze Medals collection is named on the wiki's List of Collections. No entries or acquisition detail are given.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "Lookup for 'Bronze Tag Medal' across client, wiki, articles and video returns only the client locale line 41065. No wiki page, article or video names the medal or its acquisition.", "source": "lookup 'Bronze Tag Medal' (client, wiki, articles, video)"}
 ],
 "confidence": 0.3,
 "open": [
  "How a player obtains the Bronze Tag Medal itself (quest, minigame, achievement, event or other) is unevidenced. The only sourced link is membership in collection 108. Needs in-game or wiki confirmation.",
  "wireable: false. Collection membership does not give an acquisition route for the medal, and no price, quest, drop or event is evidenced.",
  "The wiki evidence is a name-only entry on List of Collections. collections.json has entries_known: false and no entry count, so the set's contents are not verified from the wiki.",
  "Live status is unconfirmed. The collection appears in the client and the 2013 wiki list, but no post-2013 evidence was found.",
  "Item 3858 (completion reward) is not identified and was not researched.",
  "The critique's fixes were applied: the 'Sanctuary' location was removed (item_link is raw data only), the 'not bought or looted' inference was dropped, the 50 XP and 3 coins were verified at catalogue lines 8919 and 8926-8931, and the wiki evidence was reduced to a name-only citation."
 ]}
