<!-- fleet job=event-infer id=vsummer-camp-printable-calendar-v6 status=done turns=2 usd=0.0033 tokens(read,write,in,out)=[8285, 11406, 6, 3664] model=claude-haiku-5-5 -->
# Summer Camp printable calendar

{
 "event": {"name": "Summer Camp", "aliases": ["Summer Camp community event season (2010)", "Campamento de Verano (articleId=1628, Spanish)", "Camp Chatty vs Camp Robbie event", "Summer Camp Activity Calendar (printable sub-item, not a separate event)"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Start June 2010 (week of June 4-8); runs through Labor Day 2010 (articleId=1510 says 'Now through Labor Day'). Labor Day 2010 = Monday Sept 6 (calendar fact, not from a source).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498 (June 4, 2010 update); http://www.tentonhammer.com:80/node/85170 ('will run for 13 weeks beginning this week'; June 2010); http://www.freerealms.com:80/article/detail.action?articleId=1510 ('through Labor Day')"}
 ],
 "recurring": null,
 "zones": ["Greenwood Forest (Chatty's camp, reached by a newly activated Warpstone)", "Robgoblin camp across the lake (Robbie's rival camp)"],
 "npcs": ["Chatty", "Robbie the Robgoblin", "Jojo (chugawug)"],
 "quests": ["Chatty's Summer Camp Party (locale:7037)", "Robbie's Summer Camp Party (locale:7039)", "Jojo's Mojo (locale:441715 'Summer Camp Jojo's Mojo')", "Jojo's Dojo (locale:441719 'Summer Camp Jojo's Dojo')", "Jojo's Ninjato (locale:441723; objective prefixed 'Danger Peaks', so the zone differs from the Summer Camp prefix)"],
 "activities": [
  "Competing for Camp Chatty vs Camp Robbie (articleId=1498, 1502, 1510)",
  "Following the weekly printable Summer Camp Activity Calendar (articleId=1661, 1737: 'Print out the Summer Camp Activity Calendar. There will be a new one each week!')",
  "Weekly Community Team themed in-game events through Labor Day (articleId=1510)",
  "Jojo ninja-training quest chain (locale:441715, 441716, 441719, 441721, 441723, 441727)"
 ],
 "items": [
  {"name": "Camp Chatty and Camp Robbie banners, campfires, tents, stackable totems, playgrounds", "price": null, "currency": "coins", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498 (sold in the Summer Camp Coin Shop); articleId=1502 (Camp Store)"}
 ],
 "rewards": ["Camp Chatty / Camp Robbie decorations (sold, see items)"],
 "evidence": [
  {"claim": "The June 4, 2010 update introduced Summer Camp with competing camps run by Chatty and Robbie near the new Greenwood Forest Warpstone.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498"},
  {"claim": "Camp Chatty and Camp Robbie banners, campfires, tents, stackable totems and playgrounds were sold in the Summer Camp Coin Shop.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498"},
  {"claim": "Chatty and Robbie set up summer camps near the Greenwood Forest warpstone; French notes dated 04/06/2010.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1502"},
  {"claim": "Summer Camp ran as themed events for 13 weeks beginning the week of the announcement, dated June 2010 (pack metadata: 2010-06-08), with 14 new camp land quests.", "source": "http://www.tentonhammer.com:80/node/85170"},
  {"claim": "Community Team themed in-game events and activities ran weekly through Labor Day, with a new printable Summer Camp Activity Calendar each week.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1510"},
  {"claim": "A printable Summer Camp Activity Calendar was released with a new one each week.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1661; http://www.freerealms.com:80/article/detail.action?articleId=1737"},
  {"claim": "Jojo's Mojo and Jojo's Dojo are Summer Camp quests (client prefix 'Summer Camp'), and Jojo is described as the littlest chugawug at Summer Camp.", "source": "locale:441715; locale:441719; locale:441716; locale:441723"},
  {"claim": "Jojo's Ninjato objective is prefixed 'Danger Peaks', and its text places the sword quest at Danger Peaks ninjas.", "source": "locale:441723; locale:441721"},
  {"claim": "Jojo is found near the lake in Greenwood Forest.", "source": "locale:4420163"}
 ],
 "confidence": 0.6,
 "open": [
  "Start day within June 2010 is not pinned: June 4 (update notes) and June 7 (virtual camp release, tentonhammer node/86237) are both 2010. The 13-week run is anchored to the June 2010 announcement week.",
  "End: 'through Labor Day' (articleId=1510) gives early September 2010; the 13-week count and Labor Day are consistent but the exact last day is not stated.",
  "Recurring: null. Only the 2010 season is evidenced; no second year is sourced.",
  "Removed 'Jojo A-go-go' from quests: the title was not found in client text.",
  "Glugmort package delivery (locale:441709) names Summer Camp but was not checked this pass; left out of quests.",
  "Sports Week (articleId=1621), Adventure Week and Bigfoot (articleId=1552), Robbie's treasure (articleId=1637), Crafting Week (articleId=1624/1628), Pirate Week / Pirate's Plunder (wiki: Community Events) and Treasure Hunting (articleId=1757) were cited in the pack but not confirmed in my lookups. They are not listed as event activities or weeks until a quote is in hand.",
  "Fashion Week (articleId=1592, dated 2010-07-01 in the pack) would show weekly themes running into July; not verified here.",
  "Marshmallow pet (wiki: Pet Pals, 'Only available during Summer Camp') is availability-only; price and currency are unsourced and left null.",
  "Weekly Tue/Thu/Fri Pacific schedule (articleId=1628) is undated and was not used.",
  "Wilds South: removed as a zone; it appears only in 'SGRevamp - Wilds South' quest-name prefixes (441831-441853), which suggest a later revamp of the chain, not the 2010 event.",
  "Locale 442124 'Summer Camp' is a place name, a possible alias overlap; the printable calendar is kept as a sub-item of the event.",
  "Shaggy Mysterychaser and Bigfoot items are not tied to this event by a source here."
 ]
}
