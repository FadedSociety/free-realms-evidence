<!-- fleet job=event-infer id=vpirates-theme-video-v7 status=done turns=6 usd=0.0053 tokens(read,write,in,out)=[59182, 17740, 14, 4927] model=claude-haiku-5-5 -->
# Pirates theme video

```json
{
 "event": {
  "name": "Pirate's Plunder Party (community event)",
  "aliases": ["Pirates Plunder Party", "Pirate Plunder Party", "Fête de Pillage Pirate (French title)", "Community Event: Pirate's Plunder!"]
 },
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Thursday July 22, 2010, 3pm Pacific, Server 1 (U.S. and Latin America session)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1668"},
  {"year": 2010, "when": "Friday July 23, 2010, 9:00am Pacific / 4:00pm GMT, Server 1 (UK and Europe session)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1668"},
  {"year": 2011, "when": "Thursday February 3, 2011, 3pm Pacific, Server 1 (U.S. and Latin America session)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2020"},
  {"year": 2011, "when": "Friday February 4, 2011, 9:00am Pacific / 4:00pm GMT, Server 1 (UK and Europe session)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2020"},
  {"year": 2011, "when": "Thursday 3 February 2011 3pm Pacific and Friday 4 February 2011 18:00 CET / 4:00pm GMT, Server 1 (French-language repost of the same two sessions, Criqueville quay)", "source": "http://www.freerealms.com/article/detail.action?articleId=2027&request_locale=en_US"}
 ],
 "recurring": null,
 "zones": ["Seaside (pier and shores)", "Criqueville (quay / docks, article 2027 and 16644)"],
 "npcs": [],
 "quests": [],
 "activities": [
  "Play the Pirate's Plunder minigame on the Seaside pier/shores and collect gold (article 1668, article 2020)",
  "Play the Pirates Plunder minigame at the Criqueville quay party, collect gold and try for a prize (article 2027, article 16644)"
 ],
 "items": [],
 "rewards": ["Gold (pièces d'or) collected in the minigame; a prize was offered (article 2027 summary, article 16644 summary). Prize not named."],
 "evidence": [
  {"claim": "The July 22 (Thu, 3pm Pacific, Server 1, US/LatAm) and July 23, 2010 (Fri, 9am Pacific / 4pm GMT, Server 1, UK/Europe) sessions of the Pirate's Plunder Party on the Seaside pier are stated explicitly in the article text. Only the article's posting date (about July 2010) is inferred from the relative stamp.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1668"},
  {"claim": "A community event on the Seaside shores/pier let members play the Pirate's Plunder minigame and collect gold.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1668"},
  {"claim": "The February 3 (Thu, 3pm Pacific, US/LatAm) and February 4, 2011 (Fri, 9am Pacific / 4pm GMT, UK/Europe) sessions of 'Community Event: Pirate's Plunder!' on Server 1 are stated explicitly in the article text. The page is undated; the 2011 year comes from the quoted text.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2020"},
  {"claim": "A French-language post for the Criqueville quay 'Fête de Pillage Pirate' gives the same Feb 3 and Feb 4, 2011 sessions on Server 1 (Thu 3 Feb 2011 3pm Pacific; Fri 4 Feb 2011 18:00 CET / 4pm GMT). Undated post; the dates are from the quoted text.", "source": "http://www.freerealms.com/article/detail.action?articleId=2027&request_locale=en_US"},
  {"claim": "Members could play the Pirates Plunder minigame to collect gold and claim a prize at a Pirate Plunder party on the Criqueville docks, on Server 1 on two dates (French post). Dates not extracted in this pack; treat as a probable third run to verify.", "source": "http://www.freerealms.com/article/detail.action?articleId=16644"},
  {"claim": "'Pirates theme video' (Referee Ruby's video guide on looting and gold doubloons/pièces d'or with the Pirates theme products) is a promo post, not an event. It is undated.", "source": "http://www.freerealms.com/article/detail.action?articleId=1585"},
  {"claim": "Pirates Week (Summer Camp theme week, pirate-costume dressing, member-only Pirates Plunder game, Seaside pier NPC) is a separate themed week. Its article is undated, so it has no dated occurrence here.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1661"}
 ],
 "confidence": 0.6,
 "open": [
  "Name merge: the pack name 'Pirates theme video' is a promo video post (article 1585, undated), not an event. Removed from aliases; it is only related promo context.",
  "Pirates Week / Summer Camp 2010 is a separate theme week (article 1661, undated, title 'Summer Camp - Pirates Week'). The earlier claim that it was the July 22-23 sessions rests on a wiki line (Community Events) and article 1668 does not name it. Pirates Week has no dated occurrence and its week number is unknown. Do not merge it with the Plunder Party.",
  "Jolly Roger and the Seaside pier NPC are tied only to the undated Pirates Week article (1661). They are not attached to the Plunder Party sessions. Client text (locale:33796) ties Jolly Roger to Pirate's Plunder minigame rounds generally, not to this event.",
  "Criqueville quay/docks (articles 2027 and 16644) is a second location; the Seaside sessions (1668, 2020) and Criqueville sessions (2027, 16644) may be the same Feb 2011 runs or different ones. Article 16644 dates were not extracted, so its occurrences are not listed. Verify before wiring.",
  "Recurring: two separate dated run-sets (July 2010, February 2011) show the same format, but no article says it recurs. Left null.",
  "Related but separate: 'Pirate Party and Invasion' (article 331, Aug 18, 2009) and 'Pirate Party!' (article 1170, March 26, 2010, Pirate's Plunder event at 3pm PDT, Server 1, listed in facts) are not verified here as part of this entry; the March 2010 one may be an earlier run of the same party and should be checked.",
  "Pirate's Plunder minigame launch (article 1661/Ahoy! post, March 2010) is the game itself, a members-only minigame, not the community event.",
  "Items, prices and currencies: none tied to this event by a source. Client items (Pirate Ship Bed locale:7914, Pirate Flag Wall Hanging locale:16141, Pirate King's Treasure Pile locale:16147, Pirates and Snakes locale:4944) and quest 'Plunder the Pirates' (locale:433040) are unlinked. locale:31028 is a flagged menu fragment, not evidence.",
  "Referee Ruby appears only in undated promo articles (1585, 1577, 15062); not an event NPC.",
  "The wiki category for this event is absent; prizes and reward items are unknown."
 ]
}
```
