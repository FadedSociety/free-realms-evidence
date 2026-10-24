<!-- fleet job=event-infer id=vsummer-camp-weekly-schedule-v7 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[16950, 10104, 8, 3518] model=claude-haiku-5-5 -->
# Summer Camp weekly schedule

{"event": {"name": "Summer Camp", "aliases": ["Summer Camp Racing Week (sub-event, article 1700)", "Summer Camp Crafting Week (articles 1627/1628, Spanish; undated)"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Thursday July 29, 2010, 3pm Pacific (Racing Week kart race, Server 1; party and following Friday)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1700 (articles summary; Friday's date cut off in the summary)"}
 ],
 "recurring": null,
 "zones": ["Greenwood Forest summer camp (camp counselors around the lake near the Greenwood Forest warpstone, locale:4420157)", "Wildwood Speedway, just south of the Crossroads Warpstone (Racing Week, article 1700)"],
 "npcs": ["Counselor Amira (locale:441915 name; locale:4420161 and locale:441837 objective text: she handles the camp's daily activities)", "Jojo, the chugawug (locale:441715, 441709)"],
 "quests": ["Chatty's Summer Camp Party (locale:7037)", "Robbie's Summer Camp Party (locale:7039)"],
 "activities": ["Kart racing at Wildwood Speedway during Racing Week (article 1700)", "Daily camp questlines with the counselors (locale:4420157, locale:441832)", "Buying marshmallow items and decorations in the Summer Camp Marketplace (article 1502)"],
 "items": [
  {"name": "Marshmallow animal pets", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1502 (marshmallow animals in several colors sold in Summer Camp Marketplace); availability limit to Summer Camp: wiki page Pet Pals"},
  {"name": "Spooky Campfire", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1502 (grants a temporary ghost pet when clicked)"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Racing Week was a Summer Camp kart race at Wildwood Speedway, just south of the Crossroads Warpstone, on Thursday July 29, 2010, 3pm Pacific, with a party and the following Friday.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1700"},
  {"claim": "Summer Camp Marketplace sells marshmallow animals in several colors, inflatable Chatty and Robby decorations, and a Spooky Campfire that grants a temporary ghost pet.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1502"},
  {"claim": "Marshmallow pets are only available during Summer Camp.", "source": "wiki: Pet Pals"},
  {"claim": "Chatty's Summer Camp Party and Robbie's Summer Camp Party are quest titles naming the event.", "source": "locale:7037; locale:7039"},
  {"claim": "Jojo is the littlest chugawug attending Summer Camp near Greenwood Forest; the Jojo quest objectives direct players to the camp counselors.", "source": "locale:441715; locale:441709; locale:4420157"},
  {"claim": "Counselor Amira handles the camp's daily activities.", "source": "locale:441915; locale:4420161; locale:441837"},
  {"claim": "Article 1628 (Spanish, undated in capture) describes expected in-game community event times during the camp: Tuesdays 09:00 and 16:00 PT, Thursdays 15:00 PT, Fridays 09:00 PT. Used as an undated in-season expectation only, not as a dated or recurring schedule.", "source": "http://www.freerealms.com/article/detail.action?articleId=1628"},
  {"claim": "Summer Camp is also a permanent client place name, so zone references need care.", "source": "locale:442124"}
 ],
 "confidence": 0.5,
 "open": [
  "Season start and end dates for 2010 are not established. The Ten Ton Hammer node/85170 summary (about 13 weeks, June 2010 announcement) was not re-read and is not used as an occurrence. The June 7, 2010 virtual camp date (node/86237) is unverified.",
  "Article 1628 is undated, so its Tue/Thu/Fri schedule is not anchored to any season or year and is not a recurrence.",
  "Article 1700 summary cuts off before the Friday date. The Friday date is not stated.",
  "Recurrence: only one dated occurrence (2010) is sourced. Whether Summer Camp recurs yearly is unknown.",
  "Jojo quest titles Jojo's Mojo (441714), Jojo's Dojo (441718) and Jojo's Ninjato (441722) were not looked up, so they are not listed as quests. The Jojo objective text (441715, 441719, 441723, 441727) names Summer Camp, so the chain is client-tied but its titles are unverified.",
  "Jojo A-go-go (441710) and locale:441709/441711 may belong to a Glugmort or Wilds South chain. Glugmort is not tied to the event by a verified source and is left out of npcs.",
  "Pet Pals wiki page is the only source for the marshmallow-pet availability limit; article 1502 supports sale in the Marketplace only.",
  "Spooky Campfire availability window is unconfirmed beyond article 1502. Article 1502's date is not known.",
  "Prices and currency for all items are unsourced and left null. Rewards are unsourced.",
  "Other pack-named events (Pirate's Plunder Party / Pirate Week, Arts and Crafts Week, Treasure Hunting Week, Sports Week, Pet Week, Activity Calendar; articles 1624, 1757, 1596, 1775, 1780, 1661, 1637) were not read. Whether they belong to the 2010 Summer Camp season or are separate community events is unknown; they are excluded.",
  "Name ambiguity: 'Summer Camp' is a permanent client place name (locale:442124), and the wiki lists Greenwood [Camp] and Robgoblin [Camp]. Zone references may not belong to the event alone.",
  "Pack alias 'Camp Chatty / Robbie's Summer Camp Party' is a quest-name list, not an event alias, and is dropped.",
  "The pack's schedule cannot be wired as a dated calendar: only Racing Week has an absolute date."
 ]}
