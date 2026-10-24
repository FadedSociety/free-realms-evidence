<!-- fleet job=event-infer id=vhouse-tour-visite-de-maison-v4 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[8389, 9984, 6, 3480] model=claude-haiku-5-5 -->
# House Tour (Visite de Maison)

```json
{
 "event": {
  "name": "House Party (House Party Tuesday)",
  "aliases": ["House Party Tuesday", "Community Event: House Party Tuesday (locale:428314)", "House Tour (Visite de Maison) - French article alias, article 1229"]
 },
 "kind": "weekly",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Tuesday March 23, 2010, 4pm Pacific (earliest source-dated session; see open on series start)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1168"},
  {"year": 2010, "when": "Tuesday April 6, 2010, 3pm Pacific (article calls it the first listed session)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1209"},
  {"year": 2010, "when": "April 12, 2010, 3pm Pacific (article says Tuesday April 12th; weekday conflicts with calendar, see open)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1241"},
  {"year": 2010, "when": "Tuesday April 20, 2010, 4pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1263"},
  {"year": 2010, "when": "Tuesday June 15, 2010, 4pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1536"},
  {"year": 2010, "when": "Tuesday June 22, 2010, theme 'Obstacle Course Adventure'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1556"},
  {"year": 2011, "when": "Sunday September 18, 2011, 3pm Pacific (special instance, not a Tuesday)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2269"},
  {"year": 2011, "when": "Tuesday September 20, 2011, Sanctuary, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2270"},
  {"year": 2012, "when": "Tuesday January 31, 2012 (special Wilds Condo Tuesday edition of the weekly event)", "source": "http://www.freerealms.com/article/detail.action?articleId=2492"}
 ],
 "recurring": "Weekly on Tuesdays (articles say every Tuesday; wiki says most Tuesdays)",
 "zones": ["Sanctuary (meeting point)", "player housing (visited homes and lots)"],
 "npcs": ["House Party (Community Team character, Friends List, teleports between featured houses)"],
 "quests": [],
 "activities": ["Meet in Sanctuary on Server 1", "Add the House Party character to Friends List and teleport to him", "Visit player-decorated homes and lots on the tour"],
 "items": [
  {"name": "Futuristic Bicycle", "price": null, "currency": "reward", "source": "wiki page: Community Events; wiki page: Futuristic Bicycle (acquisition conflicts with wiki Rides and Items pages)"}
 ],
 "rewards": ["Futuristic Bicycle via unique code for players whose home was toured (wiki only; membership-exclusive; not every event gives codes)"],
 "evidence": [
  {"claim": "House Party Tuesday is a weekly community event held every Tuesday in Sanctuary on Server 1; players visit decorated homes; the 'House Party' Community Team character teleports to featured houses", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1452"},
  {"claim": "Client UI name is 'Community Event: House Party Tuesday'", "source": "locale:428314"},
  {"claim": "Client UI text: 'Join the Community Team on a tour of homes and lots!'", "source": "locale:428315"},
  {"claim": "Weekly Tuesday house tours starting at the Sanctuary (French recap, undated in pack)", "source": "http://www.freerealms.com/article/detail.action?articleId=1229"},
  {"claim": "First source-dated session Tuesday March 23, 2010, 4pm Pacific, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1168"},
  {"claim": "Tuesday September 20, 2011 regular tour meeting in Sanctuary, Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2270"},
  {"claim": "Tuesday June 22, 2010 featured theme 'Obstacle Course Adventure'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1556"},
  {"claim": "Special Wilds Condo Tuesday edition of the weekly House Party, January 31, 2012, Sanctuary, Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2492"},
  {"claim": "Wiki Community Events: weekly House Party run most Tuesdays by an SOE employee character with occasional Ambassadors; some events give a code for a Futuristic Bicycle", "source": "wiki page: Community Events"},
  {"claim": "Weak 2013 datapoint: wiki screenshot dated 1/4/2013 shows a Community Team [House][Party] character", "source": "wiki image: world_screenshot Ref7.png"}
 ],
 "confidence": 0.6,
 "open": [
  "Name/aliases: the pack title 'House Tour (Visite de Maison)' is the French article alias for House Party. Client name confirmed as 'Community Event: House Party Tuesday' (locale:428314); the 'Seaside' prefix from the earlier index label is not in the string.",
  "Editions, not aliases: Wilds Condo Tuesday (article 2492, 2012-01-31), Pirate House Party (locale 436162/436163, undated), Snow Days and New Year quest/UI variants (locale 436455, 31364, 426815). Not tied to the weekly calendar by any dated source here. Not merged.",
  "Series start unsettled: article 1168 gives Tuesday March 23, 2010 as the first event; article 1209 calls Tuesday April 6, 2010 the first listed session. March 23 kept as earliest source-dated session.",
  "Start times differ: US/Latin America 4pm Pacific in 1168, 1263, 1536, 2262; 3pm Pacific in 1209, 1241, 2269. UK/Europe 9:00am Pacific / 4:00pm GMT in 2010 sources (1241, 1263); 9:30am Pacific / 4:30pm GMT in 2262 (year not stated) and 2492 (from earlier pass, not re-verified).",
  "Article 2286 (Tuesday, October 3) excluded: October 3 was a Tuesday in no year 2009-2014, so the source's weekday or date is wrong or it refers to another year.",
  "Article 1241 says Tuesday April 12th, but April 12, 2010 was a Monday. Date kept as stated, weekday conflict flagged.",
  "Article 1229 (French recap) has no date in the pack; its year is unknown. It is not used as an occurrence.",
  "Article 2269 (Sunday Sept 18, 2011) is a special instance, not a regular Tuesday; kept and marked special.",
  "Live 'yes' rests on dated articles through 2012-01-31 and a weak 1/4/2013 wiki screenshot. No end date found; no evidence after January 2013.",
  "Futuristic Bicycle: no price found; currency set to reward. Acquisition conflicts: wiki Community Events and Futuristic Bicycle say a unique code from a home tour; wiki Rides says a housing contest; wiki Items says SOE Employees. Unresolved. Wiki Futuristic Bicycle text is garbled, so the code mechanic rests on weak wiki-only support.",
  "NPCs: Ambassador Amnerys is mentioned on the wiki as helping run House Party, but no article ties her to it, so she is not listed.",
  "Quests: no exact House Party quest titles tied to the weekly Tuesday event in the pack. Snow Days and New Year titles are not confirmed as part of the weekly event.",
  "Excluded: locale 3545 (Love Struck Armoire) mentions a house party in flavor text only. Pirate party at Criqueville docks (article 1229) is a separate event. Thursday community events (articles 1984, 1987, 1854) and wiki Pet Party are different events, not re-checked.",
  "Article 1556 and 2270 were added from the critique; confirmed by lookup (articles index) but their full text was not re-read. Article 1452 is undated in the pack; its year is unknown and it is used only for the cadence.",
  "Article 2494 repeats the 2012-01-31 Wilds Condo fact and adds no new date."
 ]
}
```
