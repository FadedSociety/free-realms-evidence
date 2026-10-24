<!-- fleet job=event-infer id=vsummer-camp-weekly-schedule-v6 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[7859, 9366, 6, 3160] model=claude-haiku-5-5 -->
# Summer Camp weekly schedule

{
 "event": {
  "name": "Summer Camp",
  "aliases": ["Summer Camp Racing Week (sub-event, article 1700)", "Summer Camp community event season (2010, per Ten Ton Hammer node/85170 summary, not re-read)"]
 },
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Thursday July 29, 2010, 3pm Pacific (US/Latin America server 1), with the following Friday (Racing Week)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1700"},
  {"year": 2010, "when": "Summer Camp season, 2010, about 13 weeks. Start and end dates not established. Announcement likely June 2010, not confirmed.", "source": "http://www.tentonhammer.com:80/node/85170 (summary only, not re-read)"}
 ],
 "recurring": "Unconfirmed as a yearly event. Article 1628 (undated, Spanish) gives an expected in-season weekly pattern: Tuesdays 09:00 and 16:00 Pacific, Thursdays 15:00 Pacific, Fridays 09:00 Pacific.",
 "zones": ["Greenwood Forest camp (counselors around the lake near the Greenwood Forest warpstone, locale:4420157)", "Wildwood Speedway, just south of the Crossroads Warpstone (Racing Week, article 1700)"],
 "npcs": ["Counselor Amira (locale:4420161, locale:441837)", "Jojo (chugawug, locale:441715)"],
 "quests": ["Chatty's Summer Camp Party (locale:7037)", "Robbie's Summer Camp Party (locale:7039)"],
 "activities": [
  "Kart racing at Wildwood Speedway during Racing Week (article 1700)",
  "Daily camp questlines with the counselors (locale:4420157, locale:441832)",
  "Buy marshmallow items and decorations in the Summer Camp Marketplace (article 1502)"
 ],
 "items": [
  {"name": "Marshmallow animal pets", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1502; wiki: Pet Pals (only available during Summer Camp)"},
  {"name": "Spooky Campfire (temporary ghost pet when clicked)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1502"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Racing Week was a Summer Camp kart race at Wildwood Speedway on Thursday July 29, 2010, 3pm Pacific, with a party and the following Friday.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1700"},
  {"claim": "Marketplace items at Summer Camp include marshmallow animals and a Spooky Campfire that grants a temporary ghost pet.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1502"},
  {"claim": "Marshmallow pets are only available during Summer Camp.", "source": "wiki: Pet Pals"},
  {"claim": "Expected in-season event times: Tuesdays 09:00 and 16:00 PT, Thursdays 15:00 PT, Fridays 09:00 PT. Article is undated in the capture ('Posted 10 months, 3 weeks ago'), so this pattern is not anchored to a season date.", "source": "http://www.freerealms.com/article/detail.action?articleId=1628"},
  {"claim": "Chatty's Summer Camp Party and Robbie's Summer Camp Party are quest titles naming the event.", "source": "locale:7037; locale:7039"},
  {"claim": "Jojo, the littlest chugawug at Summer Camp, is the subject of the Jojo quest chain; objective text names Summer Camp.", "source": "locale:441715; locale:4420157"},
  {"claim": "Counselor Amira runs the camp's daily activities.", "source": "locale:4420161; locale:441837"},
  {"claim": "Summer Camp is also a permanent client place name, so zone references need care.", "source": "locale:442124"}
 ],
 "confidence": 0.5,
 "open": [
  "Season start and end dates for 2010 are not established. Do not use article 1628 (undated) or the June 7, 2010 virtual camp date (node/86237, unverified) as a season start.",
  "Ten Ton Hammer node/85170 (June 2010 announcement, 13 weeks, 14 camp land quests) was not re-read in full. Treat the season length and quest count as unverified.",
  "Jojo quest titles Jojo's Mojo (441714), Jojo's Dojo (441718) and Jojo's Ninjato (441722) are not re-read here. Their titles are from the pack only and are left out of quests until checked. Objective 441719 is also unverified.",
  "Jojo A-go-go (441710) and locale:441709 may belong to a Wilds South chain rather than Summer Camp. Not counted.",
  "Pirate's Plunder Party / Pirate Week, Arts and Crafts Week, Treasure Hunting Week, Sports Week, Pet Week and the Activity Calendar are named in the pack but their articles (1624, 1757, 1596, 1775, 1780, 1661, 1637) were not read. They may be separate community events and are not included.",
  "Glugmort is not tied to the event by a verified source and is left out of npcs.",
  "Spooky Campfire availability window is not confirmed beyond article 1502.",
  "Rewards and prices are not sourced. Marshmallow price and currency are null.",
  "Name ambiguity: 'Summer Camp' is a permanent client place name (locale:442124) and the wiki lists Greenwood [Camp] and Robgoblin [Camp]. Zone references may not belong to the event alone.",
  "Pack's alias 'Camp Chatty / Robbie's Summer Camp Party' is a quest-name list, not an event alias, and is dropped.",
  "Schedule is not wireable as a dated calendar: only Racing Week has an absolute date. The weekly pattern lacks a dated season source."
 ]
}
