<!-- fleet job=event-infer id=vtcg-tournaments-v6 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[9033, 10919, 6, 3378] model=claude-haiku-5-5 -->
# TCG Tournaments

{"event": {"name": "Snow Days", "aliases": ["Snow Days holiday season", "Snow Days Are Back! (news title, locale:1653)"]},
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "Dec 18, 2009 through Jan 3, 2010 (daily events; TCG tournaments held throughout the day)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
  {"year": 2013, "when": "Dec 1, 2013 through Jan 14, 2014", "source": "wiki: Snow Days (opening line: 'Snow Days 2013 runs from December 1, 2013 through January 14, 2014')"},
  {"year": 2012, "when": "Season existed (no Snow Days 2012 dates sourced). 12 Days of Presents sub-series: Dec 13-24, presents opened Dec 25", "source": "http://www.freerealms.com/article/detail.action?articleId=2827 (12 Days of Presents only; does not name Snow Days); wiki: Snow Days ('Snow Days 2012 includes all of the awesomeness from previous Snow Days')"}
 ],
 "recurring": "Yearly in winter (December into early January). Dated seasons exist for 2009-10 and 2013-14; the wiki Snow Days page says it includes previous years' content, and the wiki Events page calls it an annual December event.",
 "zones": ["Snowhill"],
 "npcs": ["Candi Ivy"],
 "quests": ["Snowmen Disassembly", "The Great Robgoblin Robbery Ring", "Present Problems", "Holiday Cheer", "Guarding the Gifting Tree"],
 "activities": [
  "Daily community events, Dec 2009 - Jan 2010 (article 705)",
  "TCG / JCC tournaments held throughout the day inside Snow Days (article 705). This is an activity, not the event name",
  "Fight greedy Robgoblins to earn Snow Days clothing (articleId 2429, 1950, 2808)",
  "Complete daily 12 Days of Presents challenges, open presents Dec 25 (articleId 2827; wiki Events)"
 ],
 "items": [
  {"name": "Snow Days Present", "price": null, "currency": null, "source": "locale:1729"},
  {"name": "Snow Days outfits", "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=2429 (Marketplace or quest/present rewards; no price stated)"},
  {"name": "Icy Snowflake Glasses", "price": null, "currency": null, "source": "wiki: Icy Snowflake Glasses (12 Days of Presents 2013)"},
  {"name": "Hot Cocoa Mug", "price": null, "currency": null, "source": "wiki: Hot Cocoa Mug (12 Days of Presents 2013)"},
  {"name": "Figgy Pudding Critter", "price": null, "currency": null, "source": "wiki: Figgy Pudding Critter (12 Days of Presents 2013)"},
  {"name": "Holigoblin Mask", "price": null, "currency": null, "source": "wiki: Holigoblin Mask (12 Days of Presents 2013)"},
  {"name": "Arctic Cat", "price": null, "currency": null, "source": "wiki: Arctic Cat (12 Days of Presents 2013)"},
  {"name": "Subarctic Winterwear Jacket", "price": null, "currency": null, "source": "wiki: Subarctic Winterwear Jacket (Snowmen Disassembly reward)"},
  {"name": "Subarctic Winterwear Hat", "price": null, "currency": null, "source": "wiki: Subarctic Winterwear Hat (Robgoblin Robbery Ring reward)"}
 ],
 "rewards": ["Snow Days Present (locale:1729; articleId 2808)", "Snow Days clothing from Robgoblins (articleId 2429)", "Daily 12 Days of Presents presents, opened Dec 25 (articleId 2827)", "Subarctic Winterwear Jacket and Hat (wiki)"],
 "evidence": [
  {"claim": "Snow Days ran daily Dec 18, 2009 through Jan 3, 2010, with community events and TCG tournaments held throughout the day. 'TCG Tournaments' is an activity inside the event.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
  {"claim": "Snow Days 2013 runs Dec 1, 2013 through Jan 14, 2014.", "source": "wiki: Snow Days"},
  {"claim": "12 Days of Presents: one quest per day Dec 13-24, presents opened Dec 25. The wiki describes it as part of SOE's 12 Days of Holidays and an annual event.", "source": "http://www.freerealms.com/article/detail.action?articleId=2827; wiki: Events"},
  {"claim": "Fighting Robgoblins during Snow Days earns special Snow Days clothing (verified in lookup).", "source": "http://www.freerealms.com/article/detail.action?articleId=2429; articleId 1950"},
  {"claim": "Snowmen Disassembly is locale-named (420292 per prior pack; 420288 'The Great Robgoblin Robbery Ring' verified by locale).", "source": "locale:420288; locale:420602"},
  {"claim": "'Snow Days Present' is a client item named with the event.", "source": "locale:1729"}
 ],
 "confidence": 0.6,
 "open": [
  "Name/identity: the pack's 'TCG Tournaments' is an activity inside Snow Days (article 705), not a separate event. The pack's alias '12 Days of Presents' is treated as a sub-series of Snow Days sourced only to the wiki and articleId 2827; articleId 2827 does not name Snow Days. Confirm before merging.",
  "2012 Snow Days season dates: no source gives them. Only the 12 Days of Presents window (Dec 13-24, opened Dec 25) is sourced.",
  "2011: articleId 2428 (community webcast) was not verified in this pass and is dropped. The 2011 SOE 12 Days of Holidays promo (articleId 2431) is excluded because no source ties it to Snow Days.",
  "Quest title: 'Robgoblin Robbery Ring' (locale:420602) and 'The Great Robgoblin Robbery Ring' (locale:420288) both exist in the client. Confirm which the rebuild uses. 'Snowmen Disassembly' not re-read in this pass.",
  "Prices and currencies are not stated in any verified source; all price and currency fields are null. Article 828 (Marketplace sale, Bonus Wheel, Mayor of Snow Hill) was not re-verified.",
  "Start time conflicts: article 705 says 3pm PST; 718 and 771 say 15:00 Pacific. Not used.",
  "Zones: only Snowhill is tied to Snow Days by a source. NPCs: only Candi Ivy is named.",
  "Not listed as items: Snow Days Floor, Snow Days Pillar, Snow Days Lot, Snow Days Wheel (activity). No sale status sourced. Snow Days Unicorn Sweater, Icy Snow Days Flair Shard, Snow Days Builders Pack, Fruit Cake Critter (2012 wiki items) were not opened and are omitted.",
  "April 2013 TCG promos (articleId 2815, 2912) are separate TCG events and excluded."
 ]
}
