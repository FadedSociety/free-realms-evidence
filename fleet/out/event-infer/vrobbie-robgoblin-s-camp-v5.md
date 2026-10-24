<!-- fleet job=event-infer id=vrobbie-robgoblin-s-camp-v5 status=done turns=2 usd=0.0032 tokens(read,write,in,out)=[8547, 10075, 6, 3760] model=claude-haiku-5-5 -->
# Robbie the Robgoblin's camp

```json
{
 "event": {
  "name": "Summer Camp 2010 (Community Team event season)",
  "aliases": ["Summer Camp (2010)"]
 },
 "kind": "community",
 "live": "no",
 "occurrences": [
  {
   "year": 2010,
   "when": "Season started with the June 4, 2010 update; weekly Community Team themed events ran through Labor Day 2010 (exact end date approximate, about Sept 6; not quoted)",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=1510 (announces weekly themed events 'through Labor Day'); http://www.freerealms.com:80/article/detail.action?articleId=1498 (June 4, 2010 start, per pack; not re-verified in this pass)"
  }
 ],
 "recurring": null,
 "zones": [
  "Greenwood Forest (Chatty's Summer Camp, reached by a newly activated Warpstone)",
  "Camp Robbie (Robbie the Robgoblin's rival camp across the lake from Chatty's camp)",
  "Seaside (Pirate's Plunder minigame, Pirate Week; wiki: Community Events)"
 ],
 "npcs": ["Chatty", "Robbie the Robgoblin", "Edmond (Camp Chatty counselor)", "Kaela (Camp Chatty counselor)", "Tyra (Camp Chatty counselor)", "Jake (Camp Chatty counselor)"],
 "quests": [
  "Chatty's Summer Camp Party (client name match only: locale:7037; event link unsourced)",
  "Robbie's Summer Camp Party (client name match only: locale:7039; event link unsourced)"
 ],
 "activities": [
  "Weekly themed in-game Community Team events (e.g. Arts and Crafts Week, Pirate Week, Pet Week) (articleId=1510, articleId=1624)",
  "Pet Parade from Crossroads toward the Sanctuary area, Server 1, Sept 2 and 3, 2010 (articleId=1780; the route wording comes from the articleId=1775 summary)",
  "Printable Summer Camp Activity Calendar each week (articleId=1510 summary)"
 ],
 "items": [
  {"name": "Robbie Totem", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498 (sold in Summer Camp Coin Shop, per pack); client locale:23410 (not re-verified)"},
  {"name": "Chatty and Robbie banners, campfires, tents, playgrounds", "price": null, "currency": "coins", "source": "articleId=1498 and articleId=1502 (Camp Store), per pack; coin currency rests on the Coin Shop mention only"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Summer Camp community season: Chatty's camp in Greenwood Forest (new Warpstone) and Robbie the Robgoblin's rival camp across the lake, with weekly themed events through Labor Day.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1510"},
  {"claim": "The season began with the June 4, 2010 update (per pack; single source, not re-verified this pass).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498"},
  {"claim": "Pet Week was the final weekly theme of the 2010 Summer Camp community event season.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1775"},
  {"claim": "Pet Parade held on Server 1 on September 2 and 3, 2010, from Crossroads toward the Sanctuary warpstone area. The article describes it as the last Summer Camp event.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"},
  {"claim": "Each week celebrates a different theme (Arts and Crafts Week).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1624"},
  {"claim": "14 new camp land quests with daily questlines and events over a 13-week run (no calendar dates).", "source": "http://www.tentonhammer.com:80/node/85170"},
  {"claim": "Quest titles 'Chatty's Summer Camp Party' and 'Robbie's Summer Camp Party' exist in the client.", "source": "locale:7037; locale:7039"},
  {"claim": "Camp Chatty counselors Edmond, Kaela, Tyra and Jake named in client text.", "source": "locale:429029; locale:429031"},
  {"claim": "'Summer Camp' is a client place name (also used in Jojo quest text as the camp near Greenwood Forest).", "source": "locale:442124; locale:441709; locale:441715"},
  {"claim": "Robbie is linked to treasure in client text ('treasure to Camp Master Robbie').", "source": "locale:7327"},
  {"claim": "Marshmallow pet is available only during Summer Camp (wiki claim, no price or route).", "source": "wiki page: Pet Pals"},
  {"claim": "Pirate's Plunder minigame in Seaside was the focus of Pirate Week.", "source": "wiki page: Community Events"}
 ],
 "confidence": 0.6,
 "open": [
  "Merge risk: the pack's sources cover Chatty's Summer Camp community season and Robbie's rival camp. Robbie's camp is treated as a sub-location, not a separate event. 'Robbie's Camp', 'Camp Robbie', 'Robgoblin Camp' and 'Greenwood Summer Camp' are not aliases because no source uses them as the event name. 'Virtual Summer Camp' was dropped (no source). 'Summer Camp' alone is a place name (locale:442124), so it is not used as the event name.",
  "Start date 2010-06-04 rests on articleId=1498, which was not re-verified in this pass. The article date for articleId=1510 is not in the pack, so the 'through Labor Day' wording is undated; the Sept 6 end is calendar knowledge, not a sourced quote.",
  "Only one 2010 season occurrence is recorded. Pet Week and the Pet Parade (Sept 2-3, 2010) are the season's final items, not a second occurrence.",
  "Live is 'no': no source says it runs now. Recurrence is null. Later years (2011+) were not checked for a repeat.",
  "Quests 'Chatty's Summer Camp Party' and 'Robbie's Summer Camp Party' match client names only; no source ties them to the 2010 dates. Camp quest id locale:429030 ('Camp Chatty Meet and Greet') was not confirmed, so it is left out.",
  "Jojo quests (Jojo's Mojo, Dojo, Ninjato, A-go-go; locale 441709-441727, 441832) are a SGRevamp Wilds questline that only uses Summer Camp as a location. Not event content. Locale 441831/441832 were not confirmed by search. Counselor Amira (locale:4420161) is left out because her text does not name Summer Camp.",
  "Bigfoot quests and Bigfoot Defender NPCs (including Edmond as an enemy) are not part of this event. Robbie Backpack is a Treasure War reward, not Summer Camp.",
  "Prices are not sourced for any item. The 'coins' currency for camp decor rests only on the Coin Shop mention in articleId=1498. Robbie Totem's sale location is unverified (locale:23410 not re-checked).",
  "Marshmallow pet: wiki-only claim (Pet Pals), no price, route or date. Do not schedule from it.",
  "Robbie treasure: the 'hide treasure / tent recovery' mechanic is dropped; no source confirms it. Only locale:7327 is cited.",
  "Camp Robbie Shirt (locale:16978) is removed: articleId=1534 does not name an item.",
  "Pet Parade route ('Crossroads to Sanctuary') comes from the articleId=1775 summary, not a full article read.",
  "Wireable now: season start (2010-06-04, pending re-verification of articleId=1498) and Pet Parade dates (Sept 2-3, 2010). Everything else stays open until sourced."
 ]
}
```
