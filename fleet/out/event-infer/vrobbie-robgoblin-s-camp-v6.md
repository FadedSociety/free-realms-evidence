<!-- fleet job=event-infer id=vrobbie-robgoblin-s-camp-v6 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[8366, 8865, 6, 3429] model=claude-haiku-5-5 -->
# Robbie the Robgoblin's camp

{"event": {"name": "Summer Camp 2010 (Community Team event season)", "aliases": ["Summer Camp (2010)"]},
"kind": "community",
"live": "no",
"occurrences": [
  {"year": 2010, "when": "Start: June 4, 2010 (season began with the update centered on Summer Camp). Weekly themed events ran through Labor Day 2010; the exact end date is not quoted (about Sept 6 by calendar, unsourced).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498 (dated 2010-06-04 per the critique's check of articles.json; not re-fetched by me); http://www.freerealms.com:80/article/detail.action?articleId=1510 (weekly themed events 'through Labor Day')"}
],
"recurring": null,
"zones": ["Greenwood Forest (Chatty's Summer Camp, reached by a newly activated Warpstone)", "Camp Robbie (Robbie the Robgoblin's rival camp across the lake from Chatty's camp; sub-location of the same season)"],
"npcs": ["Chatty", "Robbie the Robgoblin"],
"quests": [],
"activities": [
  "Weekly themed Community Team in-game events through the season (e.g. Arts and Crafts Week, http://www.freerealms.com:80/article/detail.action?articleId=1624; Pet Week, http://www.freerealms.com:80/article/detail.action?articleId=1775, the last weekly theme per that post)",
  "Pet Parade on Server 1, September 2 and 3, 2010 (http://www.freerealms.com:80/article/detail.action?articleId=1780, described there as the last Summer Camp event)",
  "Printable weekly Summer Camp Activity Calendar and in-game event schedule via the Game Guide calendar (http://www.freerealms.com:80/article/detail.action?articleId=1510)"
],
"items": [
  {"name": "Robbie Totem", "price": null, "currency": null, "source": "client name only: locale:23410. No source in the pack names where it was sold; the earlier Coin Shop attribution is dropped."},
  {"name": "Summer Camp decor (Chatty and Robbie banners, campfires, tents, playgrounds)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498 says the camp items were sold in the Marketplace and Coin Shop (no per-item price or currency given). Individual decor names are from the earlier pack and are not confirmed by the 1498 summary."}
],
"rewards": [],
"evidence": [
  {"claim": "Summer Camp season: Chatty's camp in Greenwood Forest (new Warpstone) and Robbie the Robgoblin's rival camp across the lake, with weekly themed events through Labor Day.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1510"},
  {"claim": "The season began with the June 4, 2010 update, which is centered on the Summer Camp event.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498 (dated 2010-06-04)"},
  {"claim": "Pet Week is the last weekly theme of the 2010 Summer Camp season (undated post, relative posting time).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1775"},
  {"claim": "Pet Parade on Server 1, September 2 and 3, 2010, described as the last Summer Camp event.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"},
  {"claim": "Each week celebrates a different theme (Arts and Crafts Week).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1624"},
  {"claim": "Season had 14 new camp land quests and daily questlines over a 13-week run (no calendar dates).", "source": "http://www.tentonhammer.com:80/node/85170"},
  {"claim": "Robbie the Robgoblin and Chatty appear as camp NPCs in the season.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1510"}
],
"confidence": 0.5,
"open": [
  "Merge risk: the pack mixes Chatty's Summer Camp season with Robbie's rival camp. Robbie's camp is treated as a sub-location of this one event, not a separate event. 'Robbie's Camp', 'Camp Robbie', 'Robgoblin Camp' and 'Greenwood Summer Camp' are not aliases because no source uses them as an event name. 'Virtual Summer Camp' is dropped (no source). 'Summer Camp' alone is a client place name (locale:442124), so it is not the event name.",
  "End date is unsourced: only 'through Labor Day' (articleId=1510, undated in the pack). Do not schedule a hard end date until a second source is found.",
  "Start date 2010-06-04 rests on articleId=1498. The date was confirmed in the critique's check of articles.json, but I did not re-fetch the article in this pass.",
  "Only one 2010 season occurrence is recorded. Pet Week and the Pet Parade are the season's final items, not a second occurrence. Later years (2011+) were not checked for a repeat.",
  "Quests 'Chatty's Summer Camp Party' (locale:7037) and 'Robbie's Summer Camp Party' (locale:7039) match client names only; no source ties them to the 2010 season, so they are left out of quests.",
  "Counselors Edmond, Kaela, Tyra and Jake are removed: locale:429029 and locale:429031 did not resolve as camp counselors, and locale:41267 (Tyra) is a Merry Vale performer. Unverified.",
  "Seaside / Pirate's Plunder / Pirate Week is removed from zones and activities: the wiki page cited (Community Events) did not return a match in the pack, and Pirate Week is not in the 1510 summary.",
  "Marshmallow pet: wiki-only claim (Pet Pals), no price, route or date. Not in items. Do not schedule from it.",
  "Pet Parade route ('Crossroads toward Sanctuary') is removed: no source in the pack quotes it.",
  "Prices are unsourced for all items. Currency is null for every item because only the Marketplace/Coin Shop mention is sourced, with no per-item price.",
  "Robbie treasure / tent recovery mechanic is dropped; only locale:7327 mentions treasure and it does not establish an activity.",
  "Camp Robbie Shirt (locale:16978) is removed: articleId=1534 does not name it.",
  "Bigfoot quests, Bigfoot Defender NPCs, Robbie Backpack and the Jojo quest chain are not part of this event.",
  "Wireable now: 2010 season start (2010-06-04, articleId=1498) and Pet Parade dates (Sept 2-3, 2010, articleId=1780). Everything else stays open until sourced."
]}
