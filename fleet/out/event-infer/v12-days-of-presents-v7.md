<!-- fleet job=event-infer id=v12-days-of-presents-v7 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[8230, 9604, 6, 3064] model=claude-haiku-5-5 -->
# 12 Days of Presents

{
 "event": {
  "name": "12 Days of Presents",
  "aliases": ["12 Days of Holidays (Free Realms 2012 branding; the same name was used for SOE's cross-game 2011 promotion, which is a different event)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Dec 13-24, 2012: one new challenge per day, each completed on its first day for a present with a bow. Presents open Dec 25, 2012. Missed quests and bows can still be finished or bought until January 3 (year not stated in locale text; read as Jan 3, 2013).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813 (summary: 'December 13 to December 24, 2012'; quote: 'Complete each challenge on the first day it is offered and you get a present with its bow'; 'On December 25th, log in to open your presents!'); http://www.freerealms.com:80/article/detail.action?articleId=2827 ('Every day from December 13th through the 24th'); locale:441441, locale:441963, locale:441965 ('You still have until January 3rd to complete any quests or buy any bows')"}
 ],
 "recurring": "Stated as annual by the wiki page '12 Days of Presents' (not article-confirmed). A 2013 run is suggested only by wiki item notes; no 2013 article is in the pack, so 2013 dates are unsourced.",
 "zones": ["Snowhill"],
 "npcs": ["Trina Turtledove"],
 "quests": ["12 Days of Presents", "Big Present 1", "Big Present 2", "Big Present 3"],
 "activities": [
  "Log in each day from Dec 13 to Dec 24 and complete that day's holiday challenge on the day it is offered (locale:441441)",
  "Use Trina Turtledove's Present Tracker in Snowhill to find presents and collect bows (locale:441963)",
  "Talk to Trina Turtledove in Snowhill to open completed presents (locale:441965)",
  "Log in on Dec 25 to open presents (locale:441963)",
  "Buy bows for missed days from the Marketplace (article 2827 summary only; the sentence is not quoted; no price in pack)"
 ],
 "items": [
  {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki 'Snow Days Unicorn Sweater' (2012 event tie by page text)"},
  {"name": "Snow Days Builders Pack", "price": null, "currency": null, "source": "wiki 'Snow Days Builders Pack' (2012 event tie by page text)"},
  {"name": "Snow Days Lot", "price": null, "currency": null, "source": "wiki 'Snow Days Lot' (2012 event tie by page text; unobtainable housing lot)"},
  {"name": "Icy Snowflake Glasses", "price": null, "currency": null, "source": "wiki 'Icy Snowflake Glasses' (wiki-only 2013 tie)"},
  {"name": "Figgy Pudding Critter", "price": null, "currency": null, "source": "wiki 'Figgy Pudding Critter' (wiki-only 2013 tie)"}
 ],
 "rewards": [
  "A present with a bow for each daily challenge completed on its first day (locale:441441)",
  "Big Present 1, 2, 3: complete 4, 8, or all 12 daily presents to open the matching Big Present on Dec 25 (locale:441944, locale:441945, locale:441946; titles locale:441947, locale:441948, locale:441949)"
 ],
 "evidence": [
  {"claim": "New challenge each day Dec 13-24, 2012; completing it on its first day gives a present with a bow", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813 ; locale:441441"},
  {"claim": "Presents open by logging in on Dec 25", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813 ; locale:441963"},
  {"claim": "Missed quests and bows can be completed or bought until January 3", "source": "locale:441965"},
  {"claim": "Day-by-day run Dec 13 through 24 ('Every day from December 13th through the 24th')", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2827"},
  {"claim": "Big Present tiers at 4, 8, 12 presents, opened Dec 25; titles Big Present 1-3 exist", "source": "locale:441944, locale:441945, locale:441946, locale:441947, locale:441948, locale:441949"},
  {"claim": "Snowhill zone; Trina Turtledove; Present Tracker", "source": "locale:441963"},
  {"claim": "2011 SOE cross-game '12 Days of Holidays' promotion (Dec 13-24/25, 2011, daily offers and Station Cash deals) is a different event; it does not mention Free Realms in the body", "source": "http://www.freerealms.com/article/detail.action?articleId=2442 ; articleId=2441 ; articleId=2433 ; articleId=2440 ; articleId=2455 (verified in this pass via summaries)"},
  {"claim": "Annual recurrence and 2012 start", "source": "wiki '12 Days of Presents' (wiki statement, not an article)"}
 ],
 "confidence": 0.7,
 "open": [
  "Exact 2012 start/end times (e.g. 12:01 am PST / 11:59 pm PST) are NOT verified in the pack. Only 'December 13 to December 24, 2012' is sourced. Fetch article 2813 full text.",
  "Posting date 2012-12-13 for article 2813 is inferred from a relative 'Posted 4 days, 9 hours ago' stamp; the 'Starting today, December 13, 2012' wording was not verified.",
  "The January 3 end date (locale:441965) gives no year; 2013 is inferred from the 2012 run.",
  "2013 run: no 2013 article in the pack; 2013 dates are unscheduled. 15-presents total is wiki-only.",
  "Name collision: '12 Days of Holidays' is also the 2011 SOE cross-game promotion (separate event; excluded from occurrences). The wiki calls 12 Days of Presents part of the same SOE brand.",
  "'Snow Days' is a Snowhill winter-event wiki page, not a confirmed alias; removed from aliases.",
  "Bow price and currency not in the pack; null.",
  "Wiki category members without page text in the pack (Arctic Cat, Hot Cocoa Mug, Holigoblin Mask, Fruit Cake Critter, Icy Snow Days Flair Shard, Polar Bear, Temporary Snowflake Parachute, St. Bernard, Snowman Mask, Snowglobe Helmet, Snowflake Glasses) have no per-item tie to this event and are excluded. Snowflake Glasses vs Icy Snowflake Glasses is unresolved.",
  "No quest answers in the pack mention the event."
 ]
}
