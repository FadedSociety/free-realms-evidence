<!-- fleet job=event-infer id=vambassadors-v6 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[22450, 9569, 10, 3998] model=claude-haiku-5-5 -->
# Community Ambassadors

The pack merged two things, so this is split into two entries. Entry A is the standing program. Entry B is a one-off sub-event.

### Entry A: Community Ambassadors weekly community events (program)

```json
{"event": {"name": "Community Ambassadors weekly community events", "aliases": ["Community Ambassadors", "Ambassador Events", "Community Events (Community Ambassadors)", "Community Team events"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [
   {"year": null, "when": "every Thursday 4pm PST and Friday 9am PST (article gives no year)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854"},
   {"year": null, "when": "every Thursday, the Community Team gathers in a different place (no year)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1984"}
 ],
 "recurring": "weekly: every Thursday 4pm PST and Friday 9am PST, reachable by teleport from the in-game guide (article 1854)",
 "zones": [],
 "npcs": ["Community Ambassadors (Community Team Ambassadors)"],
 "quests": [],
 "activities": ["kart races", "house shows (visiting decorated player homes)", "duels", "hide-and-seek with Ambassadors hiding for players to find", "trivia and questions", "fishing with community staff"],
 "items": [],
 "rewards": [],
 "evidence": [
   {"claim": "The Community Team hosts Community Events every Thursday at 4pm PST and Friday at 9am PST, reachable via teleport from the in-game guide.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854"},
   {"claim": "Every Thursday the Community Team gathers in a different place to hang out and party as a Community Event.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1984"},
   {"claim": "The Free Realms Community Ambassadors throw weekly events where players race karts, show houses, duel and take part in other activities (undated recap).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=877"},
   {"claim": "A weekly Community Event was a winner-takes-all kart race at Thunder Falls Speedway. This is one undated week, not a program zone.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2009"},
   {"claim": "Hide-and-seek with Community Team Ambassadors hiding on Server 3 (Briarwood), sent duel requests, was held Friday 21 August 2009 1pm-3pm Pacific.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=220 and articleId=212"},
   {"claim": "A House Party event was held Tuesday, October 3rd (meeting in Sanctuary to visit decorated homes); the year is not given in the lookup result.", "source": "http://www.freerealms.com/article/detail.action?articleId=2286"},
   {"claim": "Client friends-list text reads 'Add Ambassador Events to your friends list', supporting the alias.", "source": "locale:2777, locale:2779"}
 ],
 "confidence": 0.55,
 "open": [
   "Year of the program is not stated by any source in the pack. Articles 1854 and 1984 give a weekly cadence but no date. Sub-events are dated 2009 (articles 220, 212) and 2011 (article 2062), so the program ran at least across 2009-2011; no start or end year is established.",
   "Live status: the program's last run is not dated. Live is 'unsure' until a 2012-2014 source is found.",
   "Zones: no program zone is sourced. Thunder Falls Speedway (2009), Briarwood (212, 220) and Sanctuary (2286) are single-event locations. Articles 1214 and 1987 say 'a different location' without naming places and were not re-checked here.",
   "Items, quests and rewards: none are tied to the program in this pack. The client event titles are 'Community Event: <name>'; the list of sub-event titles was not enumerated.",
   "Merge warning: the pack's facts mix the program with one-off sub-events (Luau, Snow Days, Robgoblin Rave, Boss Battles). Only the cadence claim above belongs to the program.",
   "Article post dates are null or relative in the pack. The 2009 and 2011 dates come from the article text, not from post dates."
 ]}
```

### Entry B: Luau Beach Party (one-off community event, sub-event of the program)

```json
{"event": {"name": "Luau Beach Party", "aliases": ["Luau Party", "Beach Party"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
   {"year": 2011, "when": "Thursday March 24, 2011, 3pm Pacific (US and Latin America session, Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
   {"year": 2011, "when": "Friday March 25, 2011, 9:00am Pacific / 5pm UTC (UK and Europe session, Server 1)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"}
 ],
 "recurring": null,
 "zones": ["Seaside"],
 "npcs": ["Community Ambassadors (on hand to ask trivia, dance in the surf, answer questions)"],
 "quests": [],
 "activities": ["dance", "turn into crabs", "light fireworks", "trade collections", "trivia questions", "dance in the surf with Ambassadors"],
 "items": [],
 "rewards": [],
 "evidence": [
   {"claim": "The US and Latin America session was on Thursday March 24, 2011, 3pm Pacific, Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
   {"claim": "The UK and Europe session was on Friday March 25, 2011, 9:00am Pacific, Server 1.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
   {"claim": "A community event called Luau Beach Party took place in Seaside, where players could dance, turn into crabs, light fireworks and trade collections.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
   {"claim": "Community Ambassadors were on hand to ask trivia questions and dance in the surf.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2062"},
   {"claim": "A Playa Azul version of the luau beach party event (Spanish/Portuguese localisation) was also held.", "source": "http://www.freerealms.com/article/detail.action?articleId=2064 and articleId=2065"}
 ],
 "confidence": 0.8,
 "open": [
   "The Playa Azul articles (2064, 2065) describe the same party at a different location; their dates were not checked, so they are not used for dates.",
   "Items: Luau Party Ticket, Ballet Boombox and Party for Pets/A Luau are sub-event items named in the earlier pack but not confirmed here against a source tying them to this party. Left out.",
   "Quests: none found in the pack for this party."
 ]}
```

Corrections against the critiques: the previous 'late March 2011' date is replaced by the stated March 24 and 25, 2011 dates from article 2062. The Thursday 4pm PST and Friday 9am PST schedule was re-verified in article 1854 and is now the recurrence. The Thunder Falls Speedway item is a single undated week and is no longer a program zone. Seaside is attached only to the Luau entry. The program now has its own entry with no fixed year. Confidence is 0.55 for the program and 0.8 for the Luau sub-event.
