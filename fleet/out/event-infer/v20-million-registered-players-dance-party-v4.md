<!-- fleet job=event-infer id=v20-million-registered-players-dance-party-v4 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[13142, 7075, 8, 2852] model=claude-haiku-5-5 -->
# 20 million registered players celebration dance party

The pack covers two sourced occurrences from the same October 2011 celebration. The schema holds one event, so I return both as an array of two objects, as the calendar critique asked. I did not merge them.

```json
[
 {
  "event": {"name": "Community Event: 20 Million Dance Party", "aliases": ["20 Million Dance Party", "20 Million Celebration (umbrella, not the event name)"]},
  "kind": "community",
  "live": "yes",
  "occurrences": [
   {"year": 2011, "when": "October 21, 2011 (one day; sessions listed as raw hours 9.5-10.5 and 16-18, timezone unconfirmed)", "source": "http://www.freerealms.com/article/detail.action?articleId=2308", "sessions": ["9.5-10.5 (raw hours, unconfirmed timezone)", "16-18 (raw hours, unconfirmed timezone)"]}
  ],
  "recurring": null,
  "zones": ["Sanctuary (Server 1)"],
  "npcs": [],
  "quests": [],
  "activities": ["Attend a dance party hosted by the Community Team"],
  "items": [],
  "rewards": [],
  "evidence": [
   {"claim": "Client event name is 'Community Event: 20 Million Dance Party'.", "source": "locale:436428"},
   {"claim": "Client description: join the Community Team for a dance party celebrating over 20 million registered players, SERVER 1.", "source": "locale:436429"},
   {"claim": "Community Team held dance parties in Sanctuary on October 21, 2011 to celebrate the 20 million registration milestone (article summary).", "source": "http://www.freerealms.com/article/detail.action?articleId=2308"},
   {"claim": "Session numbers 9.5-10.5 and 16-18 come from the pack's fact numbers for article 2308. No source in the pack gives a clock time or timezone, so they are not published as clock times.", "source": "http://www.freerealms.com/article/detail.action?articleId=2308 (pack fact numbers)"},
   {"claim": "SOE announced more than 20 million registered users since the April 28, 2009 launch.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2305"}
  ],
  "confidence": 0.6,
  "open": [
   "Session hours are raw decimal numbers from the pack, with timezone unconfirmed. Clock times are not established.",
   "Live is inferred from past-tense article text (article 2308 summary). The pack shows no pre-launch plan for the dance party.",
   "Host NPC is not named. Sources say only 'the Community Team'.",
   "Article 2308 'date' field is null in the pack. The year and day come from the summary text.",
   "Other Community Event dance parties (Festival of Hearts locale:2778, Lucky Green locale:2788, Snow Days locale:436457) are separate events and are not merged here."
  ]
 },
 {
  "event": {"name": "20 Million Letterman Jacket Claim", "aliases": ["20 Million Celebration (umbrella)", "Free Realms Letterman Jacket giveaway"]},
  "kind": "community",
  "live": "yes",
  "occurrences": [
   {"year": 2011, "when": "October 21 to October 31, 2011 (claim window; ends 11:59 p.m. PDT on October 31)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2305; http://www.freerealms.com/article/detail.action?articleId=2308"}
  ],
  "recurring": null,
  "zones": ["Sanctuary (Server 1)"],
  "npcs": [],
  "quests": [],
  "activities": ["Log in and claim the free Letterman Jacket during the claim window"],
  "items": [
   {"name": "Free Realms Letterman Jacket", "price": null, "currency": "reward", "source": "locale:8878 (name); article 2308 (claim); wiki page 'Free Realms Letterman Jacket' (description)"}
  ],
  "rewards": ["Free Realms Letterman Jacket (article 2308 claim)", "Special Edition 20 Million Varsity Jacket by in-game message (locale:436431; name not matched to the Letterman Jacket, unresolved)"],
  "evidence": [
   {"claim": "A free Letterman Jacket was given to every player who logged in and claimed it from October 21 through October 31, 2011.", "source": "http://www.freerealms.com/article/detail.action?articleId=2308"},
   {"claim": "The claim window ran Friday October 21, 2011 through Monday October 31, 2011, at 11:59 p.m. PDT.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2305"},
   {"claim": "Client item name is 'Free Realms Letterman Jacket' (verified in locale lookup).", "source": "locale:8878"},
   {"claim": "Client message: 'THANK YOU for helping us reach 20 Million Registered Players' and tells players to receive their Special Edition 20 Million Varsity Jacket from messages.", "source": "locale:436431 (text verified; type label not checked)"},
   {"claim": "Wiki page describes the Free Realms Letterman Jacket as a Freestyle Jobs clothing item created for the 20M celebration and given to players who claimed it in the October 2011 window.", "source": "Free Realms Letterman Jacket (wiki)"}
  ],
  "confidence": 0.6,
  "open": [
   "Category:Unobtainable membership is not verified; the pack's wiki category list is empty, so no category claim is made.",
   "Varsity Jacket (locale:436431) and Letterman Jacket (locale:8878) may be the same item under two names, or two items. Unresolved.",
   "Briarwood Letterman Jacket (locale:17191) has no source tying it to this event and is excluded.",
   "Price and currency are not in the pack. Listed as reward only.",
   "Locale 8879 (description) was not returned by the lookup, so the description text is taken from the pack, not re-verified.",
   "Locale 436430 '20MM Registered Users!' is typed ui, not a quest title. No quest title is confirmed."
  ]
 }
]
```
