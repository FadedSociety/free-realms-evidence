<!-- fleet job=event-infer id=vfree-realms-1st-birthday-v4 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[8019, 8998, 6, 3731] model=claude-haiku-5-5 -->
# Free Realms 1st birthday

{
 "event": {
  "name": "Free Realms Birthday (yearly anniversary party; 2010 '1st Birthday', later 'Birthday Bash')",
  "aliases": ["Free Realms 1st birthday", "Free Realms 1st birthday celebration", "Birthday Bash", "Free Realms Turns Three!"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "April 29, 2010 (anniversary) through May 10, 2010 (scheduled end)", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 ; http://www.freerealms.com:80/article/detail.action?articleId=1268 (German, states 29 April start and end on 10 May) ; preview only: http://www.tentonhammer.com:80/node/83604 (posted 2010-04-22, future tense)"},
  {"year": 2012, "when": "from 4/28/2012, Bash ran through May 24, 2012 (called the 3rd birthday)", "source": "http://www.freerealms.com/article/detail.action?articleId=2578 ; http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"year": 2013, "when": "April 29, 2013 (4th birthday)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"}
 ],
 "recurring": "yearly, around April 29 (Free Realms' anniversary); the wiki lists Birthday Bash under Annual events",
 "zones": ["Sanctuary", "Sacred Grove"],
 "npcs": ["Camellia (wiki: royal party planner, Sanctuary)", "Cakenstein (boss/enemy)", "Cakelings (enemies)", "Ambassadors (2013 dancing area, per article 2924)"],
 "quests": ["Free Realms Turns Three! (client quest_title, locale:706; dialog locale:707 mentions the cake bake-off in Sacred Grove and names Camellia as contact; article 2580 names Queen Valerian for the bake-off)"],
 "activities": ["Visit birthday party areas in eight zones (2010, articles 1267 and 1268)", "Complete birthday quests from Camellia (2010, article 1267)", "Fight Cakenstein, boss fight (2010, article 1268)", "Cake bake-off in Sanctuary (2012, article 2580)", "Dance with the Ambassadors in the Birthday Bash area in Sanctuary (2013, article 2924)"],
 "items": [
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "http://www.freerealms.com/article/detail.action?articleId=2578 (login reward, 2012)"},
  {"name": "Birthday Bash Furniture Bundle (Dining Table, Bed, Chair, Sofa)", "price": null, "currency": null, "source": "locale:691 ; locale:692 ; locale:436980-436983 (names only; year and price not in evidence)"},
  {"name": "Boss Birthday Cake", "price": null, "currency": "reward", "source": "http://www.freerealms.com/article/detail.action?articleId=2100 (collecting all 8 zone-themed cakes awards it); locale:30109"},
  {"name": "Birthday Cake / Big Birthday Cake / Large Birthday Cake", "price": null, "currency": null, "source": "locale:427853 ; locale:428028 ; locale:428031 (names only)"}
 ],
 "rewards": ["Birthday Cake Hat (2012 login)", "Boss Birthday Cake (collect all 8 zone cakes, article 2100)", "Birthday party prizes and new in-game events (2010, article 83604 preview)"],
 "evidence": [
  {"claim": "Free Realms' first anniversary fell on April 29, 2010, and a birthday party was held in-game from the announcement until May 10, 2010.", "source": "http://www.freerealms.com/article/detail.action?articleId=1267"},
  {"claim": "The 2010 party was scheduled to end May 10, 2010; the German post states it started on the posting day and ended 10 May.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1268 ; http://www.freerealms.com/article/detail.action?articleId=1261"},
  {"claim": "The 1st birthday celebration was previewed to start April 29, 2010 (future tense, pre-launch).", "source": "http://www.tentonhammer.com:80/node/83604 (2010-04-22)"},
  {"claim": "A 2010 Ten Ton Hammer podcast listed Free Realms' 1st birthday as a topic (2010-04-13); it gives no event details.", "source": "http://www.tentonhammer.com:80/node/83296"},
  {"claim": "The 2012 Birthday Bash ran from 4/28/2012 through May 24, 2012, with a login Birthday Cake Hat and tripled Station Cash purchases.", "source": "http://www.freerealms.com/article/detail.action?articleId=2578 ; http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "The 2013 (4th birthday) event was April 29, 2013, with a Birthday Bash area in Sanctuary.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"},
  {"claim": "Eight zone-themed cakes; collecting all eight awards the Boss Birthday Cake for free. (Collect rule only; no buy option is sourced.)", "source": "http://www.freerealms.com/article/detail.action?articleId=2100 ; wiki: Cake"},
  {"claim": "Cakenstein and Cakelings are Birthday Bash enemies.", "source": "wiki: Cakenstein ; wiki: Cakeling ; locale:4732 ; locale:4949"},
  {"claim": "Quest 'Free Realms Turns Three!' exists in the client with cake bake-off dialog.", "source": "locale:706 ; locale:707"}
 ],
 "confidence": 0.5,
 "open": [
  "MERGE: the pack merges two series. The 2010 '1st birthday' (Flitter invitations, balloons, Cakenstein fight, eight zone parties) and the 2012-2013 'Birthday Bash' (Cake Hat, Ambassadors, Furniture Bundle) share a yearly date but are not shown to be one calendar event. Recommend splitting into a 2010 '1st Birthday' record and a 'Birthday Bash' 2012-2013 record. This record is kept merged per the schema, and items are not year-tagged beyond what the sources say.",
  "2010 live start is unverified: articles 1267 and 1268 say the party began at announcement/posting day, but the posting dates are not in the pack. Only the April 29 anniversary and May 10 end are sourced.",
  "Furniture Bundle price (1350 Station Cash) was removed: no article in the corpus states it. Year of the bundle is unknown.",
  "Boss Cake: the 'or buying' wording was removed. Only collect-all-8 is sourced (article 2100). The 'SC Marketplace' sale location rests on the wiki Cake page only and is not stated here.",
  "Camellia's Sanctuary presence during the Bash rests on the wiki page only. Quest dialog (locale:707) names Camellia as contact; article 2580 names Queen Valerian for the bake-off. Both are cited, and they disagree on the contact.",
  "Quest 'Birthday Bash!' (locale:29341) is linked only by objective locale:4952; not listed as a confirmed quest. Wiki quest names 'A Piece of Cake', 'Undelivered Confections', 'Birthday Cake Bake-off' have no client title match.",
  "Only four cakes are named in the client; the other four of the eight are not enumerated. No cake prices are sourced.",
  "Birthday Invitation (locale:4951), Birthday Pinata and 2010 balloon weapons are excluded: no source ties them to the event.",
  "Prices missing for Birthday Cake Hat, Wall Sconce, Birthday Crates, and T-shirts.",
  "2010 articles 1261, 1267, 1268 are undated in the pack; their 2010 year comes from the April 29, 2010 date in 1267 and 1268 plus the self-description '1st birthday'.",
  "Confidence is limited by the merged name, thin 2010 record, and unenumerated cake set."
 ]
}
