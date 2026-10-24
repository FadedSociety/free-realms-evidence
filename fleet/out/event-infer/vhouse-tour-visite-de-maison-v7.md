<!-- fleet job=event-infer id=vhouse-tour-visite-de-maison-v7 status=done turns=1 usd=0.0031 tokens(read,write,in,out)=[0, 9157, 4, 3923] model=claude-haiku-5-5 -->
# House Tour (Visite de Maison)

```json
{
  "event": {
    "name": "House Party Tuesday",
    "aliases": [
      "House Party",
      "House Tour (Visite de Maison)",
      "Community Event: House Party Tuesday (locale:428314)",
      "[House] [Party] Tuesday (article titles)"
    ]
  },
  "kind": "weekly",
  "live": "unsure",
  "occurrences": [
    {"year": 2010, "when": "Tuesday March 23, 2010, 4pm Pacific (first source-dated session)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1168"},
    {"year": 2010, "when": "Tuesday April 6, 2010, 3pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1209"},
    {"year": 2010, "when": "Tuesday April 20, 2010, 4pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1263"},
    {"year": 2010, "when": "Tuesday June 15, 2010, 4pm Pacific (weekly run; that week's theme Camping)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1536"},
    {"year": 2010, "when": "Tuesday June 22, 2010, Sanctuary, Server 1 (weekly run; that week's theme Obstacle Course Adventure)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1556"},
    {"year": 2011, "when": "Tuesday September 20, 2011, Sanctuary, Server 1 (regular tour)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2270"}
  ],
  "recurring": "Weekly on Tuesdays (time of day varies by source year: 3pm or 4pm Pacific in 2010; not fixed). Stated as recurring/'every Tuesday' in articles 1168, 1209, 1263, 1536, 1556 and 2270; wiki 'Community Events' says 'most Tuesdays'.",
  "zones": [
    "Sanctuary (meeting point, Server 1)",
    "player housing (decorated homes and lots)"
  ],
  "npcs": [
    "Community Team character '[House] [Party]' (add to Friends List; players teleport to him as he moves between featured houses), per article 1452 (undated) and client locale:428315"
  ],
  "quests": [],
  "activities": [
    "Meet in Sanctuary on Server 1",
    "Add the House Party character to Friends List and teleport to him",
    "Tour player-decorated homes and lots",
    "Summer 2010 weeks (June 15 Camping; June 22 Obstacle Course Adventure) were themed weeks of the same weekly run, per articles 1536 and 1556, not separate events"
  ],
  "items": [],
  "rewards": [],
  "evidence": [
    {"claim": "Weekly community house tour on Tuesdays, meeting in Sanctuary, visiting player houses", "source": "http://www.freerealms.com/article/detail.action?articleId=1229 (undated; French recap)"},
    {"claim": "Weekly Tuesday House Party in Sanctuary, Server 1; first source-dated session Tuesday March 23, 2010 4pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1168"},
    {"claim": "Every Tuesday players meet in Sanctuary to visit decorated homes; Tuesday April 6, 2010 3pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1209"},
    {"claim": "Tuesday April 20, 2010 session, 4pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1263"},
    {"claim": "Tuesday June 15, 2010 session; summer houses matched that week's theme (Camping)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1536"},
    {"claim": "Tuesday June 22, 2010 session on Server 1; theme Obstacle Course Adventure", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1556"},
    {"claim": "Tuesday September 20, 2011 regular tour, Sanctuary, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2270"},
    {"claim": "Client UI name 'Community Event: House Party Tuesday'", "source": "locale:428314"},
    {"claim": "Client UI text 'Join the Community Team on a tour of homes and lots!'", "source": "locale:428315"},
    {"claim": "Wiki: weekly House Party run most Tuesdays; 'Wilds Condo Tuesday' is a special edition of it", "source": "wiki page: Community Events"},
    {"claim": "Tuesday January 31, 2012 Wilds Condo special edition of the weekly House Party (a one-off variant, not a weekly occurrence)", "source": "http://www.freerealms.com/article/detail.action?articleId=2492"}
  ],
  "confidence": 0.6,
  "open": [
    "Live status: last dated source is Jan 31, 2012 (article 2492). No end date found. A wiki screenshot dated 1/4/2013 shows a [House][Party] character, but it is weak and unverified. live = 'unsure'.",
    "Wilds Condo Tuesday (Jan 31, 2012; articles 2492, 2493, 2494) is a special edition of this weekly event, not a weekly occurrence and not an alias. Kept out of the occurrence list and aliases. Record it as a separate special-edition entry if the calendar needs it.",
    "Excluded from occurrences: Article 2262 ('Tuesday, September 13'): no year in the text; 2011 is inferred and the time (9:30am) is not in the summary. Not used as a dated occurrence until the full text is checked.",
    "Excluded: Article 1241 says 'Tuesday April 12th', but April 12, 2010 was a Monday. Source-internal inconsistency; not counted as a Tuesday session.",
    "Excluded: Article 2269 (Sunday September 18, 2011, 3pm Pacific) is a special instance, not a regular Tuesday.",
    "Excluded: Article 2286 ('Tuesday, October 3') does not match a Tuesday in the years checked, so it was not used.",
    "Start time conflicts across sources: 4pm Pacific (1168, 1263, 1536), 3pm Pacific (1209, 1241, 2269), 9:30am (2262, unverified). Some 2010 sources give UK times (9am Pacific / 4pm GMT). The time is recorded per source and is not a single fixed time.",
    "Article 1452 is undated and supports cadence and location only. Article 1214 (every Tuesday, Sanctuary, weekly [House][Party]) is cadence evidence cited in a critique but was not re-read in this pass.",
    "Article 1229 (French 'Visite de Maison') is undated. The 'House Tour (Visite de Maison)' title is a French alias of this event. The same article's Criqueville pirate party and Thursday events are different events and are not included.",
    "Name collisions not merged: locale 436162 (Pirate House Party), 436455/436459 (Snow Days House Party), 31364 and 426815 (New Year House Party), 430483 (Treehouse Party). No dated source ties them to the weekly calendar. Locale 3545 (Festival of Hearts house party) is flavor text only.",
    "Items: none sourced to this event. Futuristic Bicycle was dropped (conflicting wiki sources and garbled text). No price or currency found.",
    "Quests: none tied to this event in the pack.",
    "NPC Ambassador Amnerys is named on the wiki as helping run House Party, but no article ties her to it. Not listed.",
    "Wiki 'Community Events' says 'most Tuesdays', so some weeks may have been skipped. The skipped weeks are not identified in the pack."
  ]
}
```
