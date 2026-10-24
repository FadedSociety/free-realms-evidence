<!-- fleet job=event-infer id=vreferee-heliotrope-party-v5 status=done turns=2 usd=0.0039 tokens(read,write,in,out)=[6875, 11964, 6, 4578] model=claude-haiku-5-5 -->
# Referee Heliotrope party

{"event": {"name": "Luau Beach Party (community event, March 2011)", "aliases": ["Luau Beach Party", "Luau Party", "Luau Community Event", "Beach Party Luau", "Community Event: Luau Beach Party"]},
"kind": "community",
"live": "yes",
"occurrences": [
 {"year": 2011, "when": "Thursday 24 March 2011, 3pm Pacific (US and Latin America), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062 (English); http://www.freerealms.com/article/detail.action?articleId=2065 (Spanish, 'Jueves 24 de marzo, 2011 15:00hrs. PST')"},
 {"year": 2011, "when": "Friday 25 March 2011, 9:00am Pacific / 5:00pm UTC (UK and Europe), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062 (English); http://www.freerealms.com/article/detail.action?articleId=2064 and 2065 (Spanish, 'viernes 25 de marzo, 2011 09:00hrs. PST / 17:00hrs. UTC')"}
],
"recurring": null,
"zones": ["Seaside", "Sanctuary", "Blackspore", "Greenwood Forest", "Playa Azul (unresolved, see open)"],
"npcs": ["Tiger the Party Animal", "Community Ambassadors", "Referees (client dialog only)"],
"quests": ["A Luau"],
"activities": ["dance", "turn into crabs", "set off fireworks", "trade collections", "socialize", "trivia and Q&A with Community Ambassadors", "equip a luau outfit and speak to Tiger the Party Animal (A Luau quest)", "buy Luau Party Ticket to start a party in your current zone"],
"items": [
 {"name": "Luau Party Ticket", "price": null, "currency": null, "source": "locale:5102398 (name); locale:5102399 (purchasing begins a Luau Party for current zone); wiki: Luau Party Ticket and Tiger the Party Animal (sold by Tiger in Blackspore, Sanctuary, Seaside; price fields blank in excerpt)"},
 {"name": "Luau Party Favor", "price": null, "currency": "reward", "source": "locale:4548 and locale:422849 / 422864 (Tiger gives a party favor for wearing a luau outfit); name-tied only"},
 {"name": "Luau Party Outfit (Female)", "price": null, "currency": null, "source": "locale:156862 (name); locale:422876 (buy a luau outfit from the marketplace); name-tied only"},
 {"name": "Luau Outfit (Girls)", "price": null, "currency": null, "source": "locale:156882 (name); name-tied only"},
 {"name": "Luau Outfit (Boys)", "price": null, "currency": null, "source": "locale:156883 (name); name-tied only"},
 {"name": "Luau Tiki Torch", "price": null, "currency": null, "source": "locale:420140 (name); name-tied only"}
],
"rewards": ["Luau Party Favor (from Tiger the Party Animal when wearing a luau outfit, per locale 422864)"],
"evidence": [
 {"claim": "Luau Beach Party ran Thu 24 Mar 2011 3pm Pacific for US/Latin America on Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
 {"claim": "Luau Beach Party UK/Europe session Fri 25 Mar 2011 9:00am Pacific / 5:00pm UTC on Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062; http://www.freerealms.com/article/detail.action?articleId=2064"},
 {"claim": "Activities: dance, turn into crabs, fireworks, trade collections, socialize; Community Ambassadors ask trivia and answer questions", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062; http://www.freerealms.com/article/detail.action?articleId=2065"},
 {"claim": "Event place given as Seaside in the English article", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
 {"claim": "Event place given as Playa Azul in the Spanish articles", "source": "http://www.freerealms.com/article/detail.action?articleId=2064; http://www.freerealms.com/article/detail.action?articleId=2065"},
 {"claim": "Quest title 'A Luau'; objective text is 'Equip a luau outfit and speak to Tiger the Party Animal during a Luau Party.' (quoted as written)", "source": "locale:422865; locale:422874"},
 {"claim": "Wiki says A Luau is only available during Luau Community Events and Tiger spawns during them", "source": "wiki: Quest:A Luau"},
 {"claim": "Luau Party Ticket description: purchasing begins a Luau Party for the current zone", "source": "locale:5102399"},
 {"claim": "Client has per-zone start messages 'A luau party has started in Seaside / Sanctuary / Blackspore / the Greenwood Forest'", "source": "locale:419938, 419939, 419940, 419941"},
 {"claim": "Client dialog links Referees to Luau Party ('Join your favorite referees for a Luau Party!'); no article confirms Referee-hosted luau parties", "source": "locale:31354; locale:31369"},
 {"claim": "Wiki Parties section says Referees host a Luau themed party during the summer (wiki only)", "source": "wiki: Tiger the Party Animal"},
 {"claim": "Wiki news says Tiger has retired from Luau duty to prepare for Snow Days (undated)", "source": "wiki: Template:News"}
],
"confidence": 0.6,
"open": [
 "Pack mismatch: the evidence pack (n191) holds only articleId 1118 'Referees Party Too!' (Referee Heliotrope party in Sanctuary, undated, captured March 2010). It does not contain any Luau content. The pack title merges a Referee party with the Luau event. The Referee party is a different event and is not described by this object; it stays unscheduled.",
 "Place conflict: articleId 2062 (English) says Seaside; articleId 2064 and 2065 (Spanish) say Playa Azul. Both are sourced and unresolved. Zones list both until a calendar owner settles it.",
 "Session 2 citation: the Friday 25 March session is stated in 2064 and 2065 and in the English 2062 summary; earlier citation of 2062 alone for Session 2 was only partly right, since 2062 also has the English wording.",
 "Live: articles are past-tense and confirm the March 2011 run. Whether the event still runs is not known. The Template:News retirement is undated.",
 "Recurring is null. The two sessions are one run over two days. A 2010 Seaside beach party (articleId 1092, Friday 5 March 2010) and a 'Seaside Beach Luau' with pets swimming (articleId 1136, undated) are related but are not confirmed as the same event. No article says the luau recurs.",
 "Referee-hosted status: client strings 31354/31369 and the wiki say Referees host luau parties, but no article confirms it.",
 "Item prices and currency are null: the wiki price fields are blank in the excerpt and no locale gives a price. Luau Party Outfit (Girls) 156864 is a duplicate and 156881 is DEPRECATED, so they are not listed. Luau items other than the ticket are tied by name only.",
 "Quest 'Luau Party' (locale 31368, quest_title) may be a second quest title; it is not confirmed as a distinct quest. The 'repeatable' wording comes from the wiki only."
]}
