<!-- fleet job=event-infer id=vsummer-camp-in-game-v4 status=done turns=2 usd=0.0037 tokens(read,write,in,out)=[8714, 10985, 6, 4499] model=claude-haiku-5-5 -->
# Summer Camp in-game events

## Record A (parent): Summer Camp, 2010 community season

```json
{"event": {"name": "Summer Camp (2010 community season)", "aliases": ["Campamento de Verano (Spanish article title)", "Greenwood Camp (probable, unverified as a formal name)"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [{"year": 2010, "when": "Summer 2010. Virtual Summer Camp released June 7, 2010; themed events ran 13 weeks from the announcement week. End date not in pack (partial window).", "source": "http://www.tentonhammer.com:80/node/86237 (June 7, 2010 release); http://www.tentonhammer.com:80/node/85170 (13 weeks beginning that week)"}],
 "recurring": null,
 "zones": ["Summer Camp (client place, locale:442124)", "Greenwood Forest camp, reached through a newly activated Warpstone (http://www.freerealms.com:80/article/detail.action?articleId=1510)", "Seaside (Pirate's Plunder minigame, wiki Community Events)"],
 "npcs": ["Chatty (created the camp, articleId=1510)", "Jojo, a young chugawug (locale:441709, locale:441711)", "Glugmort, Jojo's father (locale:441832, locale:441711)", "Counselor Amira (locale:4420161, handles daily kids' activities)"],
 "quests": ["Jojo A-go-go (locale:441710 title; objective locale:441832)", "Jojo's Mojo (locale:441714)", "Jojo's Dojo (locale:441718)", "Jojo's Ninjato (locale:441722)"],
 "activities": ["Weekly themed community weeks: Fashion Week (articleId=1593, undated), Arts and Crafts Week (articleId=1624), Pirate Week (wiki Community Events), Pet Parade as last event (articleId=1780)", "Pirate's Plunder minigame in Seaside (Pirate Week focus, wiki Community Events)", "Printable weekly Activity Calendar for completing activities alone or with friends (articleId=1661, 1737)", "Summer Camp Marketplace shopping (articleId=1502)", "Jojo quest chain: Ninja Apprentice mojo, obstacle course items, Ninjato from Taka in Danger Peaks (locale:441715, 441719, 441723)"],
 "items": [
  {"name": "Marshmallow pet (pet pal)", "price": null, "currency": null, "source": "articleId=1498 (Marshmallow pets in various colors sold in the Summer Camp Marketplace); wiki Pet Pals ('Only available during [Summer] [Camp]'). Price not sourced."},
  {"name": "Marshmallow animal pets (other colors)", "price": null, "currency": null, "source": "articleId=1502"},
  {"name": "Chatty and Robby inflatable decorations", "price": null, "currency": null, "source": "articleId=1502 (decorations, not NPCs)"},
  {"name": "Spooky Campfire", "price": null, "currency": null, "source": "articleId=1502 (grants a temporary ghost pet when clicked; whether the ghost pet is a separate item is unconfirmed)"},
  {"name": "Talent Fragments with marshmallow campfire variants", "price": null, "currency": null, "source": "articleId=1502"}],
 "rewards": [],
 "evidence": [
  {"claim": "Virtual Summer Camp released June 7, 2010.", "source": "http://www.tentonhammer.com:80/node/86237"},
  {"claim": "Summer Camp themed events ran in summer 2010 for 13 weeks beginning the week of the announcement; 14 new camp land quests plus daily questlines and events were added. Re-checked in the articles index.", "source": "http://www.tentonhammer.com:80/node/85170"},
  {"claim": "Chatty created a camp in Greenwood Forest, reached through a newly activated Warpstone.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1510"},
  {"claim": "Each week celebrated a different theme; Arts and Crafts Week was one.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1624"},
  {"claim": "A printable Summer Camp Activity Calendar was released, new each week.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1661 and articleId=1737"},
  {"claim": "Pet Parade was the last Summer Camp event (date not sourced).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"},
  {"claim": "Marshmallow pets were sold in the Summer Camp Marketplace; they are only available during Summer Camp. Re-checked in the articles and wiki indexes.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498; wiki Pet Pals"},
  {"claim": "Marketplace Summer Camp items include marshmallow animals, Chatty and Robby inflatables, a Spooky Campfire, and Talent Fragments with marshmallow campfire variants. Re-checked in the articles index.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1502"},
  {"claim": "Jojo quests name Summer Camp in their text: Jojo A-go-go (441711: 'currently attending Summer Camp'), Jojo's Mojo (441715), Jojo's Dojo (441719), Jojo's Ninjato (441723). Titles are client locale text; the SGRevamp-prefixed titles (441831-441853) are internal labels and are not used.", "source": "locale:441710, 441711, 441714, 441715, 441718, 441719, 441722, 441723"},
  {"claim": "Glugmort's package goes to Jojo at the Summer Camp counselors.", "source": "locale:441832; locale:441709"}],
 "confidence": 0.6,
 "open": [
  "Merge: 'Summer Camp in-game events' (the pack name) is not an alias of this record. It is the child schedule (Record B below), linked to this parent only by the shared Summer Camp name, which is an inference.",
  "Timing: start 2010-06-07 is sourced. The end is not sourced: 13 weeks from the announcement week, and the announcement date is not in the pack. Window is partial, so the record cannot be placed on a calendar with a fixed end.",
  "Article 1593 (Fashion Week) is undated. Its summary places it about 11 months before the 2011-06-04 capture (roughly mid-2010), which fits the 2010 season but does not prove the year. Fashion Week is therefore not counted as a sourced 2010 activity; it is moved to Record B.",
  "Articles 1502, 1780 and 1498: 1498 and 1502 were re-checked in lookup. 1780 (Pet Parade) was not re-checked; its date is unknown.",
  "Pirate Week dates are not sourced (wiki Community Events only).",
  "Greenwood camp alias is probable only (wiki World list; wiki user blog 'Greenwood Forest [technically [Summer] [Camp] as well]'; articleId=1510). Robgoblin [Camp] is a separate wiki place and is not an alias.",
  "Chatty's Summer Camp Party (locale:7037) and Robbie's Summer Camp Party (locale:7039) are title matches only, with no date or event flag, so they are not listed as quests. Robbie is named only as an inflatable decoration subject (articleId=1502), not as an NPC. Jintaka and Taka appear in objective text only and are not listed as NPCs. Counselor Amira is named only in dialog (locale:4420161).",
  "Marshmallow pet and other items: prices and currency are unknown (wiki price stripped). Bigfoot pages listing Camp banners and tents are monster reward pages and are not counted as Summer Camp items.",
  "Rewards: none sourced.",
  "Parent is not wireable as a calendar entry: no end date, no recurrence, and the only schedule is undated (Record B)."]}
```

## Record B (child): Summer Camp in-game event schedule (plan-like, unconfirmed)

```json
{"event": {"name": "Summer Camp in-game event schedule", "aliases": ["Semana de Moda / Fashion Week (article 1593 title)"]},
 "kind": "weekly",
 "live": "unsure",
 "occurrences": [{"year": null, "when": "Expected Tuesdays 09:00 and 16:00 Pacific, Thursdays 15:00 Pacific, Fridays 09:00 Pacific. Year not stated (article undated; about 11 months before the 2011-06-04 capture, roughly mid-2010).", "source": "http://www.freerealms.com/article/detail.action?articleId=1593"}],
 "recurring": "weekly on Tuesdays (09:00, 16:00), Thursdays (15:00) and Fridays (09:00) Pacific, as expected in the article; not confirmed as live timing",
 "zones": ["Summer Camp"], "npcs": [], "quests": [],
 "activities": ["Fashion Week fashion shows and friend activities (articleId=1593)", "Game Guide calendar and Go button used to reach events (articleId=1593)"],
 "items": [], "rewards": [],
 "evidence": [{"claim": "Expected in-game event times for Summer Camp, marked as expected, from a Spanish official post with the Fashion Week theme.", "source": "http://www.freerealms.com/article/detail.action?articleId=1593"}],
 "confidence": 0.3,
 "open": ["Plan-like: the source describes expected times, not confirmed live timing. Date null.", "Link to Record A (2010 season) is an inference from the shared Summer Camp name; the article does not say 2010.", "The Spanish text was read as given; time zone is Pacific as written."]}
```

Status: the 2010 Summer Camp season is supported by Ten Ton Hammer (June 7, 2010 release; 13 weeks; 14 camp land quests). The recurring schedule is undated and plan-like, so it is kept separate. The calendar should not wire the parent until an end date is found.
