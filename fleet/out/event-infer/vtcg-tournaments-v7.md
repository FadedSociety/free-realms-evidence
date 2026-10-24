<!-- fleet job=event-infer id=vtcg-tournaments-v7 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[8351, 11012, 6, 3960] model=claude-haiku-5-5 -->
# TCG Tournaments

```json
{
 "event": {
  "name": "Snow Days",
  "aliases": ["Snow Days holiday season", "Snow Days Are Back! (news title, locale:1653)", "Snow Days 2011 / 2012 / 2013 (season names)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "Dec 18, 2009 through Jan 3, 2010 (daily community events; TCG tournaments held throughout the day)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
  {"year": 2011, "when": "Live in December 2011; community webcast aired Dec 8, 2011", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
  {"year": 2012, "when": "Season existed; no 2012 start/end dates sourced", "source": "wiki: Snow Days ('Snow Days 2012 includes all of the awesomeness from previous Snow Days')"},
  {"year": 2013, "when": "Dec 1, 2013 through Jan 14, 2014 (wiki only; no dated article seen)", "source": "wiki: Snow Days"}
 ],
 "recurring": "Yearly in December into January (wiki Events: 'an annual event during the month of December throughout January'). Dated seasons: 2009-10, 2011, 2013-14; 2012 undated.",
 "zones": ["Snowhill"],
 "npcs": ["Candi Ivy", "Gifting Tree (wiki Events: gives presents to all players in Snowhill)"],
 "quests": ["The Great Robgoblin Robbery Ring", "Present Problems", "Holiday Cheer", "Guarding the Gifting Tree"],
 "activities": [
  "Daily community events and TCG/JCC tournaments held throughout the day, Dec 2009 - Jan 2010 (articleId 705). TCG Tournaments is an activity inside Snow Days, not a separate event.",
  "Fight greedy Robgoblins to earn special Snow Days clothing (articleId 1950 'Defeating greedy Robgoblins earns special Snow Days clothing'; also 2429, 2808)",
  "Complete Snow Days quests and open presents for tacky sweaters and winter outfit pieces (articleId 2429)",
  "Daily 12 Days of Presents challenges Dec 13-24, presents opened Dec 25 (articleId 2827; sub-series, see open)"
 ],
 "items": [
  {"name": "Snow Days Present", "price": null, "currency": null, "source": "locale:1729"},
  {"name": "Snow Days outfits / clothing", "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=2429 (Marketplace or quest/present rewards; Robgoblin drops)"},
  {"name": "Icy Snowflake Glasses", "price": null, "currency": null, "source": "wiki: Icy Snowflake Glasses (tagged 12 Days of Presents 2013; item page not re-read)"},
  {"name": "Hot Cocoa Mug", "price": null, "currency": null, "source": "wiki: Hot Cocoa Mug (tagged 12 Days of Presents 2013; not re-read)"},
  {"name": "Figgy Pudding Critter", "price": null, "currency": null, "source": "wiki: Figgy Pudding Critter (tagged 12 Days of Presents 2013; not re-read)"},
  {"name": "Holigoblin Mask", "price": null, "currency": null, "source": "wiki: Holigoblin Mask (tagged 12 Days of Presents 2013; not re-read)"},
  {"name": "Arctic Cat", "price": null, "currency": null, "source": "wiki: Arctic Cat (tagged 12 Days of Presents 2013; not re-read)"},
  {"name": "Subarctic Winterwear Jacket", "price": null, "currency": null, "source": "wiki: Subarctic Winterwear Jacket (Snowmen Disassembly reward; year not stated)"},
  {"name": "Subarctic Winterwear Hat", "price": null, "currency": null, "source": "wiki: Subarctic Winterwear Hat (Robgoblin Robbery Ring reward; year not stated)"}
 ],
 "rewards": [
  "Snow Days Present (locale:1729)",
  "Special Snow Days clothing from Robgoblins (articleId 1950, 2429)",
  "Daily 12 Days of Presents presents, opened Dec 25 (articleId 2827)",
  "Subarctic Winterwear Jacket and Hat (wiki)"
 ],
 "evidence": [
  {"claim": "Snow Days ran daily Dec 18, 2009 through Jan 3, 2010, with community events and TCG tournaments held throughout the day. TCG Tournaments is an activity inside the event.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
  {"claim": "A community webcast on Dec 8, 2011 discussed Snow Days 2011 as live.", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
  {"claim": "Robgoblin defeats earn special Snow Days clothing.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1950; http://www.freerealms.com/article/detail.action?articleId=2429"},
  {"claim": "Snow Days 2013 runs Dec 1, 2013 through Jan 14, 2014 (wiki only).", "source": "wiki: Snow Days"},
  {"claim": "Snow Days is an annual December-January event in Snowhill with the Gifting Tree.", "source": "wiki: Events"},
  {"claim": "'Snow Days Present' is a client item named with the event.", "source": "locale:1729"},
  {"claim": "Quest names 'The Great Robgoblin Robbery Ring' and 'Robgoblin Robbery Ring' both exist in the client.", "source": "locale:420288; locale:420602"}
 ],
 "confidence": 0.6,
 "open": [
  "Identity: 'TCG Tournaments' is an activity inside Snow Days (articleId 705), not its own event. The pack's name is the activity.",
  "'12 Days of Presents' is a sub-series. Its Dec 13-24 / Dec 25 window comes from articleId 2827, which does not name Snow Days; the link rests on the wiki category and the wiki 2012/2013 item pages. Record it separately if the rebuild needs it.",
  "2012 Snow Days dates: no source gives them. Only the wiki's 'includes previous Snow Days' line.",
  "2013 window rests on one wiki opening line; no dated article in the pack confirms it.",
  "Dec 8, 2011 webcast (articleId 2428) confirms 2011 was live but gives no season start/end dates.",
  "Quests: the four quests are client-named (locale 420288, 420268, 420272, 420280) but not tied to a year. 'Snowmen Disassembly' (locale 420292 per prior pack) was not re-verified here, so it is omitted. Which of 'The Great Robgoblin Robbery Ring' (420288) and 'Robgoblin Robbery Ring' (420602) the rebuild uses is unresolved; both exist in the client.",
  "Items: only 'Snow Days Present' is directly client-named with the event. The 2013 wiki items and Subarctic Winterwear items are wiki-tagged with no verified dates and were not re-read. Prices and currencies are unsourced; all null.",
  "Start time conflicts (articleId 705 says 3pm PST; 718 and 771 say 15:00 Pacific) are unresolved and not used.",
  "Not included: April 2013 TCG promos (articleId 2815, 2912) are separate TCG events. Article 828 (Marketplace sale, Bonus Wheel) was not re-verified."
 ]
}
```
