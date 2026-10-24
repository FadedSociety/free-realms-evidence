<!-- fleet job=event-infer id=vsummer-camp-sports-week-v5 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[7831, 9340, 6, 3022] model=claude-haiku-5-5 -->
# Summer Camp Sports Week

```json
{"event": {"name": "Summer Camp (2010)", "aliases": ["Virtual Summer Camp (tentonhammer node/86237 per pack, not re-fetched)", "Campamento de Verano (article 1601 title)", "Summer Camp (client place name, locale:442124)"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Summer 2010 season, starting June 2010 and running through Labor Day (13 weeks). Exact start/end days not confirmed beyond June 7 release.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1510; http://tentonhammer.com/node/86237 (June 7 release, pack-sourced; not re-fetched in lookup)"}
 ],
 "recurring": null,
 "zones": ["Greenwood Forest (Summer Camp, near the Greenwood Forest warpstone; locale:4420157)", "Snowy Hill field (Sports Week soccer, article 1601 only; 'Colina Nevada' not a client string)"],
 "npcs": ["Chatty (camp creator; article 1510)", "Robbie the Robgoblin (rival camp; article 1637)", "Jojo (chugawug, Summer Camp; locale:441709, 441711)"],
 "quests": ["Chatty's Summer Camp Party (locale:7037)", "Robbie's Summer Camp Party (locale:7039)", "Jojo's Mojo (Summer Camp id locale:441714; title shared with a Southern Wilds quest, locale:441841, which is NOT part of this event)", "Jojo's Dojo (Summer Camp id locale:441718; title shared with Southern Wilds locale:441995 'Jojo's Mojo Dojo', NOT part of this event)"],
 "activities": ["Weekly themed community events through Labor Day", "Printable Summer Camp Activity Calendar, new each week (articles 1661, 1737, 1510)", "Sports Week (Semana Deportiva): soccer challenges at the Snowy Hill field during the week and a sports-themed party on Tuesday (article 1601)", "Arts and Crafts Week as one weekly theme (article 1624)", "Pirate Week: Pirate's Plunder minigame in Seaside (article 1661 summary; wiki Community Events)", "Robbie's hidden treasure: visit his tent to try to recover part of it (articles 1637 and 1644)", "Jojo quest chain (client locale:441709-441832)"],
 "items": [{"name": "Marshmallow (pet)", "price": null, "currency": null, "source": "wiki: Pet Pals ('only available during Summer Camp'), pack-sourced, not re-checked"}],
 "rewards": [],
 "evidence": [
  {"claim": "Chatty created a Summer Camp near Greenwood Forest with weekly themed events through Labor Day.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1510"},
  {"claim": "Summer Camp is a client place name; the Jojo quest text names Summer Camp near the Greenwood Forest warpstone.", "source": "locale:442124; locale:4420157"},
  {"claim": "Sports Week included soccer challenges at the Snowy Hill field during the week and a sports-themed party on Tuesday. Party date is not given beyond Tuesday.", "source": "http://www.freerealms.com/article/detail.action?articleId=1601 (Spanish; article is undated)"},
  {"claim": "Robbie used Summer Camp to get people to find his treasure; players visit his tent to try to recover some of it.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1637; http://www.freerealms.com/article/detail.action?articleId=1644&request_locale=en_US"},
  {"claim": "Quest titles Chatty's Summer Camp Party and Robbie's Summer Camp Party exist in the client.", "source": "locale:7037; locale:7039"},
  {"claim": "Virtual Summer Camp released June 7, 2010; ran 13 weeks.", "source": "http://tentonhammer.com/node/86237; http://www.tentonhammer.com:80/node/85170 (pack summaries; not re-fetched)"}
 ],
 "confidence": 0.5,
 "open": [
  "MERGE: The pack title 'Summer Camp Sports Week' combines the season (Summer Camp 2010) with one child theme (Sports Week / Semana Deportiva). It should not be stored as a standalone event. Sports Week is a week inside this season.",
  "Sports Week dates UNVERIFIED: the July 8-9, 2010 Server 1 soccer dates from article 1621 and team/jersey details from article 1622 did not return in lookup. Not stated here. Needs article re-fetch before wiring any date.",
  "Sports Week party day is only 'Tuesday' (article 1601, undated). The week's calendar date is not known.",
  "The June 4, 2010 'update' date from article 1498 did not return in lookup; dropped. Start date rests on the June 7 release (tentonhammer 86237, pack-sourced).",
  "Season end is 'Labor Day' per article 1510; exact final date not confirmed.",
  "Adventure Week (La Semaine d'Aventure, article 1552, Bigfoot sighting near Camp Chatty) was named in the prior critique as a Summer Camp theme. Not verified in this pass; not listed as a theme here.",
  "Pet Parade (article 1780) is said to be the last Summer Camp event. Undated; not included as a dated occurrence.",
  "Article 1601 scheduled times for community events were not read; not available.",
  "Pack item 'Chatty's and Robbie's Summer Camp' removed: it is an inference from quest titles, not a sourced alias.",
  "Pack said article 1637 did not support the treasure claim; lookup shows it does (1637 and 1644 both support it).",
  "Pirate Week is a separate theme inside the season, not an alias.",
  "Item prices and currency: none sourced. Rewards: none sourced.",
  "Recurring: only the 2010 season is evidenced; recurring is null.",
  "Jojo's Mojo and Jojo's Dojo: same titles as Southern Wilds quests (locale:441841, 441995). Only the Summer Camp ids 441714 and 441718 belong to this event; the id-to-title pairing was not re-verified in this pass."
 ]}
```
