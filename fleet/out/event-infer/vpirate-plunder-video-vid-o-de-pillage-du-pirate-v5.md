<!-- fleet job=event-infer id=vpirate-plunder-video-vid-o-de-pillage-du-pirate-v5 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[17997, 11804, 8, 4501] model=claude-haiku-5-5 -->
# Pirate plunder video (Vidéo de Pillage du Pirate)

```json
{
  "event": {
    "name": "Pirate's Plunder Party",
    "aliases": [
      "Pirates Plunder Party (wiki 'Community Events' page)",
      "Community Event: Pirate Party! (article 1170, linked by fact label only)",
      "Community Event: Pirates Plunder Party! (article 1668)",
      "Fête de Pillage Pirate (French, article 2027)",
      "Pirate plunder video (Vidéo de Pillage du Pirate), NOT CONFIRMED as an alias: article 1190 is an undated video post with no event details"
    ]
  },
  "kind": "community",
  "live": "yes",
  "occurrences": [
    {"year": 2010, "when": "Friday 26 March 2010, 3:00pm Pacific Daylight Time, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1170"},
    {"year": 2010, "when": "Thursday 22 July 2010, 3:00pm Pacific Time (U.S. and Latin America), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1668"},
    {"year": 2010, "when": "Friday 23 July 2010, 9:00am Pacific Time (= 4:00pm GMT = 6:00pm CEST), UK and Europe, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1668"},
    {"year": 2011, "when": "Thursday 3 February 2011, 3:00pm Pacific, US and Latin America, Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2027&request_locale=en_US"},
    {"year": 2011, "when": "Friday 4 February 2011, 9:00am Pacific (= 5:00pm GMT = 6:00pm CET), UK and Europe, Server 1. Article 2027 gives '18:00 CET (4:00pm GMT)', which is internally inconsistent; 4:00pm GMT is wrong for February.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2020"}
  ],
  "recurring": null,
  "zones": ["Seaside", "Criqueville (article 2027 only)"],
  "npcs": [],
  "quests": [],
  "activities": [
    "Played the Pirate's Plunder minigame to collect gold (articles 1668, 2020, 2027)",
    "Tried for a prize at the Pirate's Plunder minigame (articles 2020, 2027)",
    "Partied on the Seaside shore, pier and beach (articles 1170 summary, 1668, 2020)",
    "Celebrated on the Criqueville quay (article 2027 only)"
  ],
  "items": [],
  "rewards": ["A prize from the Pirate's Plunder minigame (prize not named in any source)"],
  "evidence": [
    {"claim": "A Pirate's Plunder community event ran Friday March 26, 2010, 3:00pm Pacific Daylight Time, Server 1. Article summary places it on the Seaside shores with a beach party.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1170"},
    {"claim": "A Pirate's Plunder Party was held on the Seaside pier; two scheduled sessions by region on Server 1: Thu July 22 2010 3pm Pacific (US/LatAm) and Fri July 23 2010 9:00am Pacific / 4:00pm GMT (UK/Europe). Verified in the article's facts.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1668"},
    {"claim": "Feb 3 2011 3pm Pacific (US/LatAm) session on Server 1 and a Pirate Plunder party with the minigame on the Criqueville quay.", "source": "http://www.freerealms.com/article/detail.action?articleId=2027&request_locale=en_US"},
    {"claim": "Feb 4 2011 9:00am Pacific UK/Europe session on Server 1; Seaside pier and beach party with the minigame to collect gold and capture a prize.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2020"},
    {"claim": "Wiki Community Events page: the Pirates Plunder Party was an event where players gathered to play the Pirate's Plunder minigame in Seaside, the main focus of the Summer Camp 'Pirate Week'. No year given.", "source": "Community Events (wiki, ns0)"},
    {"claim": "Article 1214 (undated) reports a party on the Seaside docks to celebrate opening of the Pirate's Plunder minigame. Not counted as an occurrence because it is undated and is a minigame-opening party, not a Plunder Party session.", "source": "http://www.freerealms.com/article/detail.action?articleId=1214"},
    {"claim": "Article 1190 is a short undated French news post linking a video of the pirate plunder feature. It gives no dates, mechanics or rewards and is not a party occurrence.", "source": "http://www.freerealms.com/article/detail.action?articleId=1190"}
  ],
  "confidence": 0.45,
  "open": [
    "NAME MISMATCH: The pack's only named item, 'Pirate plunder video (Vidéo de Pillage du Pirate)' (article 1190), is an undated video post. It is not tied to the party by any source, so it is NOT confirmed as this event. It may be a promotional video for the Pirate's Plunder feature or minigame. Treat the event as the pack's subject only if the pack confirms this.",
    "The pack may merge the Pirate's Plunder minigame (launch preview article 1142, 19 Mar 2010, a members-only treasure game; not a party) with the party events. Only the party sessions are counted above.",
    "Article 2023 ('Evento Comunitario: ¡Batalla Pirata!', Seaside docks, Pirate Battle minigame, 3 Jan 2011 15:00 PT and 4 Jan 2011 09:00 PT, Server 1) was reported as article 2022 by the critique; the facts file records it as articleId 2023. It was not re-read here. It is not merged: its title differs and it may be a separate run or a Spanish-language alias of this event. Unresolved.",
    "Location conflict for Feb 2011: article 2027 places the party on the Criqueville quay; article 2020 places it at Seaside. Unknown whether this is one event with an article mismatch or two parallel events. Seaside is the best-supported zone (articles 1170, 1668, 2020).",
    "Time-zone labels: article 2020 says 9:00am Pacific = '4:00pm GMT', which is wrong for February (PST is UTC-8, so 17:00 GMT). Article 2027 gives '18:00 CET (4:00pm GMT)', also inconsistent. The July 2010 label of 4:00pm GMT is correct, since PDT is UTC-7. For July, 9:00am PDT = 16:00 GMT = 18:00 CEST (an earlier critique's 17:00 CEST was wrong).",
    "Recurrence: Runs are dated in Mar 2010, Jul 2010 and Feb 2011 (and possibly Jan 2011). No source says the party recurs, so recurring is null. Whether these form one recurring series, or separate events under the same name, is unresolved.",
    "Articles 1214 (Seaside docks party at minigame opening) and 1229 (Criqueville docks release party with naval battles) are undated and not counted. Their dates are needed before they can be placed.",
    "No NPC, quest, item or price is tied to the party by any source. Client strings such as 'Win a Pirate's Plunder Match' belong to the minigame and are not counted. Article 1585 (pirate theme products) is a different promotion and is not counted.",
    "The prize is not named in any source. Rewards list is therefore generic.",
    "Confidence is about 0.45 because of the unconfirmed name link to the pack's video item, the Seaside/Criqueville conflict, the unresolved Jan 2011 article, and the inconsistent GMT labels."
  ]
}
```
