<!-- fleet job=event-infer id=vfestival-of-hearts-wheel-v4 status=done turns=3 usd=0.0042 tokens(read,write,in,out)=[19777, 11516, 8, 5207] model=claude-haiku-5-5 -->
# Festival of Hearts Wheel

```json
{
 "event": {
  "name": "Festival of Hearts",
  "aliases": ["Valentine's Day event (wiki alias, not an in-game name)", "Festival of Hearts Wheel (daily prize wheel feature, locale:400039, not a separate event)"]
 },
 "kind": "holiday",
 "live": "unsure",
 "occurrences": [
  {"year": 2010, "when": "live starting with the February 12, 2010 update", "source": "http://www.freerealms.com:80/article/detail.action?articleId=967 (article fact: 'live in Merry Vale starting with the February 12, 2010 update'; summary: update notes for February 12, 2010 announcing the Festival of Hearts)"},
  {"year": 2011, "when": "year only, day not stated", "source": "wiki: Gifting Basket; wiki: Cupid; wiki: Heart Critter"},
  {"year": 2012, "when": "February 7, 2012 (Festival text, Cudip quests) and February 9, 2012 (holiday items added to Marketplace)", "source": "wiki: Template:News/Archive"},
  {"year": 2014, "when": "began February 4, 2014 (week #1 listed); window length not read", "source": "wiki: Festival of Hearts (2014 section)"}
 ],
 "recurring": "Annual, each February (wiki says an annual Valentine's Day-themed event; wiki Cudip says it 'take places annually each February'). Confirmed dated runs: 2010, 2012, 2014; 2011 year-only. The undated articles 969, 2016, 2498-2501 say 'annual' and 'returned' but cannot be placed in a year. Wiki Events says the event was introduced in 2012, which conflicts with article 967 (2010) and is unresolved.",
 "zones": ["Merry Vale"],
 "npcs": ["Cudip", "Stone Heart (villain)", "Heartbreakers / Heart Breakers (enemies)"],
 "quests": ["Petal Picker", "A Bundle of Love", "Ooey, Gooey Love", "Potion Testing: Version 6.0", "Potion Testing: Version 7.0"],
 "activities": [
  "Spin the daily Festival of Hearts prize wheel",
  "Do the daily and Members Only Festival quests",
  "Collect flowers in Stone Heart's Hideaway (Cudip objective, locale:427513)",
  "Fight the Heartbreakers in Merry Vale"
 ],
 "items": [
  {"name": "Gifting Basket", "price": null, "currency": null, "source": "wiki: Gifting Basket (sold on the SC Marketplace during the 2011 Festival; no longer acquirable)"},
  {"name": "Holiday Basket", "price": null, "currency": null, "source": "locale:6942 ('A final gift from the Festival of Heart's Gifting Basket.'). Only tie is the description text; currency not sourced."},
  {"name": "She-Rex", "price": null, "currency": "station_cash", "source": "wiki: She-Rex (Festival item on the SC Marketplace; article 967 says new holiday items added to Marketplace). Currency is an inference from 'SC Marketplace'."},
  {"name": "Snowheart", "price": null, "currency": "station_cash", "source": "wiki: Snowheart (Festival SC Marketplace item)"},
  {"name": "Lovelectric Boombox", "price": null, "currency": "station_cash", "source": "wiki: Lovelectric Boombox (Festival SC Marketplace item)"},
  {"name": "Stone Heart's Gummy Bear", "price": null, "currency": "station_cash", "source": "wiki: Stone Heart's Gummy Bear (Festival SC Marketplace item)"},
  {"name": "King of Hearts Costume", "price": null, "currency": "station_cash", "source": "wiki: King of Hearts Costume (Festival SC Marketplace item)"},
  {"name": "Love Struck Piano", "price": null, "currency": "station_cash", "source": "wiki: Love Struck Piano (Festival category)"},
  {"name": "Cupid (pet pal)", "price": null, "currency": "reward", "source": "wiki: Cupid; wiki: Pet Pals (random prize from the Gifting Basket, 2011 Festival only)"},
  {"name": "Heart Critter (pet pal)", "price": null, "currency": "reward", "source": "wiki: Heart Critter; wiki: Pet Pals (2011 Gifting Basket)"},
  {"name": "Dove (pet pal)", "price": null, "currency": "reward", "source": "wiki: Dove (Members Only pet pal from the Sleeping Pixie quest). Tie to the Festival is from the pack only."},
  {"name": "Festival of Hearts Semi-Formal (outfit)", "price": null, "currency": null, "source": "locale:31033 (pack-listed; not re-checked)"}
 ],
 "rewards": ["Daily prize wheel prizes", "Coin Wheel prizes (article 967 summary: for players logged in 30+ minutes a day)", "Festival pet pals Cupid and Heart Critter (2011)", "Dove pet pal (Sleeping Pixie quest, pack only)"],
 "evidence": [
  {"claim": "Festival of Hearts was live in Merry Vale from the February 12, 2010 update, with Cudip helping players", "source": "http://www.freerealms.com:80/article/detail.action?articleId=967 (re-read by lookup this run: article fact and summary)"},
  {"claim": "Festival of Hearts is an annual Valentine's Day-themed event in Merry Vale; Stone Heart and the Heart Breakers try to ruin love", "source": "wiki: Festival of Hearts; wiki: Events"},
  {"claim": "Cudip appears during the Festival each February and starts the Petal Picker and other quests", "source": "wiki: Cudip"},
  {"claim": "Festival of Hearts 2014 began February 4, 2014", "source": "wiki: Festival of Hearts (2014 section)"},
  {"claim": "Festival updates February 7 and February 9, 2012 (Festival text; new holiday items on the Marketplace)", "source": "wiki: Template:News/Archive"},
  {"claim": "Gifting Basket was sold on the SC Marketplace during the 2011 Festival and is no longer acquirable", "source": "wiki: Gifting Basket; wiki: Pet Pals"},
  {"claim": "Daily prize wheel exists in the Festival", "source": "http://www.freerealms.com:80/article/detail.action?articleId=969 (quote: 'There is a daily prize wheel'; article undated)"},
  {"claim": "Festival of Hearts TCG bundle offer was available only until the Festival ended", "source": "http://www.freerealms.com/article/detail.action?articleId=1009 (re-checked by lookup this run: 'available only until the Festival of Hearts ended')"},
  {"claim": "Heartbreakers are the Festival enemies in Merry Vale (on-screen text)", "source": "wiki: Heart Breakers; video:p5sDafXSQtQ/00086.jpg; video:jAKl4y_BzH4/00010.jpg"},
  {"claim": "Quest titles exist in the client: Petal Picker, A Bundle of Love, Ooey, Gooey Love, Potion Testing: Version 6.0 / 7.0", "source": "locale:426990, locale:427041, locale:427117, locale:427046, locale:427141"},
  {"claim": "Holiday Basket description names the Festival's Gifting Basket", "source": "locale:6942"},
  {"claim": "Festival window is February through March (wiki)", "source": "wiki: Festival of Hearts; wiki: Events. Wiki Merry Vale says 'During February' (wiki: Merry Vale). Conflict unresolved; no end date fixed."}
 ],
 "confidence": 0.5,
 "open": [
  "Live status for 2026 is unknown. The newest dated run is 2014. Live is 'unsure'. No evidence dates a run after 2014, so this record is not wireable as a current event.",
  "Window end is contested: wiki Events and Festival of Hearts say February through March; wiki Merry Vale says 'During February'. No end date is fixed. Start days per run: Feb 12 2010, Feb 7/9 2012, Feb 4 2014.",
  "Origin conflict: article 967 gives a live start of February 12, 2010, but wiki Events says the event was introduced in 2012. The 2010 date is the article's own text; the 2012 'introduced' line is recorded as a conflicting wiki claim.",
  "Articles 969, 2016, 2498, 2499, 2500, 2501 are undated; their 'annual', 'returned', 'launched for PS3' and daily/Members Only quest wording cannot be placed in a year.",
  "The community semi-formal dance (articles 957 and 960, claimed February 12, 2010) is not an activity here. Those articles were not re-read. Client locale:2778 ('Community Event: Festival of Hearts Dance Party') and locale:6672 ('Scheduled: Community Event: Festival of Hearts Semi-formal') may be one event or two; merge question open.",
  "Festival of Hearts Semi-Formal (locale:31033) and Festival of Hearts Mystery Gift (locale:4418) were pack-listed and not re-checked; the Semi-Formal outfit's tie to the Festival rests on the pack only.",
  "Prices are blank in every source checked (TCG bundle, SC Marketplace items, costumes, pianos, Gifting Basket, Holiday Basket). Currency for SC Marketplace items is inferred from 'SC Marketplace' wording.",
  "Holiday Basket currency is not sourced and is left null. Its only tie to the event is locale:6942 text.",
  "Dove pet pal's Festival tie is pack-only (wiki Dove, Sleeping Pixie quest); not confirmed as a Festival reward in a dated source.",
  "Stone Heart's Hideaway (locale:427513) is a Cudip objective, not a quest title, so not listed as a quest. Dubawug's Sweetheart is unchecked.",
  "Stone Heart's Wing Pattern Card (locale:4781) and Stone Heart's Candy (locale:134675) are excluded: no source ties them to the event.",
  "Stone Hearted Furniture Bundle (locale:3574, 3575) is excluded: its only tie (locale:3559) does not name the Festival.",
  "The Valentine's Day alias is a wiki alias only, not an in-game name.",
  "Wiki Festival of Hearts 2014 section is cut off; the 2014 window length is unknown.",
  "Article 1009 was re-checked for the TCG bundle ending with the Festival; article 967 supports Marketplace holiday items. The 'Festival of Hearts Marketplace items' claim cites 967 and the 2012 archive."
 ]
}
```
