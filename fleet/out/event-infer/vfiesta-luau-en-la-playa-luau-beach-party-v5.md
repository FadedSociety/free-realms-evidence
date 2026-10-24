<!-- fleet job=event-infer id=vfiesta-luau-en-la-playa-luau-beach-party-v5 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[8499, 10143, 6, 3325] model=claude-haiku-5-5 -->
# Fiesta Luau en la Playa (Luau Beach Party)

{"event": {"name": "Luau Beach Party (Fiesta Luau en la Playa)", "aliases": ["Fiesta Luau en la Playa", "Community Event: Luau Beach Party", "Luau Party (community event)"]},
"kind": "community",
"live": "yes",
"occurrences": [
 {"year": 2011, "when": "late March 2011; Thursday 24 March 2011, 15:00 PST (US and Latin America), Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2065 (days/times, Spanish quote: \"Jueves 24 de marzo, 2011 15:00hrs. PST (23:00 CET) (EE.UU. y Latino America) Servidor 1\"); year/month also per http://www.freerealms.com:80/article/detail.action?articleId=2062 summary"},
 {"year": 2011, "when": "Friday 25 March 2011, 09:00 PST / 17:00 UTC (UK and Europe), Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2065 (Spanish quote: \"viernes 25 de marzo, 2011 09:00hrs. PST / 17:00hrs. UTC (UK y Europa) Servidor 1\")"}
],
"recurring": null,
"zones": ["Seaside (per article 2062)", "Playa Azul (per article 2065; treated as the same beach, inferred link)"],
"npcs": ["Community Ambassadors (unnamed group; article 2065)", "Tiger the Party Animal (client only: locale:422874 ties him to a Luau Party; not stated as event host in any dated source)"],
"quests": [],
"activities": ["dance on the beach/sea", "turn into crabs", "light fireworks", "trade collections", "socialize", "trivia and Q&A with Community Ambassadors"],
"items": [],
"rewards": [],
"evidence": [
 {"claim": "A community event called Luau Beach Party took place in Seaside, where players danced, turned into crabs, lit fireworks and traded collections (past tense).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
 {"claim": "Article 2062 is dated late March 2011 on Server 1 (per its summary; the posting date itself is not in the pack).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
 {"claim": "Spanish article announces the luau at Playa Azul with two sessions: Thu 24 Mar 2011 15:00 PST (US/Latin America) and Fri 25 Mar 2011 09:00 PST / 17:00 UTC (UK/Europe), Server 1.", "source": "http://www.freerealms.com/article/detail.action?articleId=2065"},
 {"claim": "Community Ambassadors hosted trivia, dancing and questions at the luau.", "source": "http://www.freerealms.com/article/detail.action?articleId=2065"},
 {"claim": "Client text for a Luau Party exists: 'A luau party has started in Seaside/Sanctuary/Blackspore/Greenwood Forest' (generic, undated; not used as proof of this run).", "source": "locale:419938; locale:419939; locale:419940; locale:419941"},
 {"claim": "Quest objective text: 'Equip a luau outfit and speak to Tiger the Party Animal during a Luau Party.' Quest availability outside luau events is not verified.", "source": "locale:422874; locale:422865"},
 {"claim": "Luau Party Ticket text: 'Purchasing this item will immediately begin a Luau Party for your current zone.' Ticket is not confirmed as event-only.", "source": "locale:5102399"}
],
"confidence": 0.55,
"open": [
 "Posting date unknown for articles 2062 and 2065 (no absolute date in pack). Year and month come from article 2062's summary ('late March 2011'); the days come from 2065's Spanish text.",
 "Article 2062 body was not re-read in full; Seaside and the activity list rest on its summary and lookup fact. Playa Azul (2065) vs Seaside (2062) is an inferred same-beach link.",
 "Time-zone conflict in 2065: '15:00 PST (23:00 CET)' matches PDT, while '09:00 PST / 17:00 UTC' matches PST. Store the Pacific wall-clock times as given; do not derive UTC.",
 "Live status: 2062 is written in past tense and the client has Luau Party strings, but no dated post confirms the run. Treated as live with moderate confidence.",
 "Quest 'A Luau' (locale:422865) is a related quest, not an event quest: no source shows it is restricted to luau events. Tiger also appears in other party contexts (Pet and Winter parties per the earlier pack's locale:422870 and 424776; not re-verified here).",
 "Luau Party Ticket (locale:5102398/5102399), Luau Outfit ids (156883, 156882, 5102139, 5102140) and the 18000 price (store frame, regular price unconfirmed) are possibly related but not tied to the event by any source. Excluded from items. Girls outfit has two candidate ids unresolved.",
 "Outfits can be obtained by quests, web codes, in-game currency and Station Cash (article 2065 summary); not event-only.",
 "Possible earlier run of the same format: article 1092 (Friday March 5 2010, 3pm Pacific Server 1, Seaside beach party with dancing, crabs, fireworks, trade, trivia). It is called a beach party, not a luau, so it is not counted as an occurrence. If it is the same event, recurrence would be yearly-ish in March, but that is unproven.",
 "Separate events not merged: Seaside Beach Party Luau (locale:5525, 5528; Hula outfits, below the Abandoned Dojo), article 1136 (pet-swimming beach party), article 194 (Seaside Beach Party, Aug 14 2009; same boilerplate activities), nighttime beach party (article 1118), Back to School Beach Party (locale:436158), referee-hosted Luau Party (locale:31354, 31368, 31369; schedule not read).",
 "Luau Tiki Torch (locale:420140) and Luau Spit Fire (locale:423111) not tied to the event; excluded.",
 "Wiki category for this event is empty in the pack; no wiki source ties items or NPCs to the event. Tiger retirement wiki note is undated and not used.",
 "Recurrence is null: only one dated run (two sessions, 24-25 March 2011) is evidenced."
]}
