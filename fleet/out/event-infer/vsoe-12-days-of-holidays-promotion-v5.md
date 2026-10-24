<!-- fleet job=event-infer id=vsoe-12-days-of-holidays-promotion-v5 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[8005, 12584, 6, 3666] model=claude-haiku-5-5 -->
# SOE 12 Days of Holidays promotion

```json
{
 "event": {
  "name": "12 Days of Presents (Free Realms, SOE 12 Days of Holidays)",
  "aliases": [
   "12 Days of Holidays (article 2827 uses it for this Free Realms event)",
   "Snow Days (wiki and articles 892, 1953, 2428 use it for a winter Snowhill event; link to 12 Days of Presents NOT settled, open)"
  ]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Dec 13 to Dec 24, 2012 (one challenge per day; presents opened Dec 25)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813 (dated 2012-12-13 in articles/facts.json); content also in articleId=2827 (undated)"}
 ],
 "recurring": null,
 "zones": ["Snowhill"],
 "npcs": ["Trina Turtledove (named as the Present Tracker NPC in client text, locale:392128125; no article ties her to a year)"],
 "quests": ["12 Days of Presents"],
 "activities": [
  "Log in each day from Dec 13 to Dec 24 and complete that day's challenge to earn a present with its bow (article 2813)",
  "Complete a challenge on the day it is offered; the present is only earned on its first day (article 2813)",
  "Track progress with Trina Turtledove's Present Tracker (locale:392128125)",
  "Log in on Dec 25 to open the presents (article 2813)",
  "Each 4 daily presents opened earns a bonus Big Present; completing all 12 challenges gives 12 bows and 15 presents in total (article 2813)"
 ],
 "items": [
  {"name": "Icy Snow Days Flair Shard", "price": null, "currency": "reward", "source": "wiki: Icy Snow Days Flair Shard (claims 12 Days of Presents 2012). UNVERIFIED: not seen on the wiki event page in this check."},
  {"name": "Snow Days Unicorn Sweater", "price": null, "currency": "reward", "source": "wiki: Snow Days Unicorn Sweater (claims 12 Days of Presents 2012)"},
  {"name": "Snow Days Lot", "price": null, "currency": "reward", "source": "wiki: Snow Days Lot (claims 12 Days of Presents 2012)"},
  {"name": "Snow Days Builders Pack", "price": null, "currency": "reward", "source": "wiki: Snow Days Builders Pack (claims 12 Days of Presents 2012)"},
  {"name": "Snowglobe Helmet", "price": null, "currency": "reward", "source": "wiki: Snowglobe Helmet (acquired in the 12 Days of Presents 2012 Snow Days series, as a daily present; NOT the Big Present)"}
 ],
 "rewards": [
  "Daily present with a bow for each challenge completed on its first day (article 2813)",
  "Bonus Big Present for every 4 daily presents opened; 15 presents total for all 12 (article 2813)",
  "Daily 2012 item rewards listed above (wiki)"
 ],
 "evidence": [
  {"claim": "The 12 Days of Presents ran one daily challenge per day Dec 13-24, with presents opened Dec 25; dated 2012-12-13.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "Each daily challenge completed on its first day gives a present with its bow; presents open on the 25th.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "A bonus Big Present is awarded per 4 daily presents opened; completing all 12 gives 12 bows and 15 presents.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "Article 2827 (Day 12 post) repeats the Dec 13-24 challenge and Dec 25 opening structure; it has no year, so it is content support only.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2827"},
  {"claim": "Client text names the Snowhill event, the 13th-24th window, Trina Turtledove's Present Tracker, and the '12 Days of Presents' quest and Big Present objectives.", "source": "locale:392128125; locale:2109814218; locale:2976893817"},
  {"claim": "Snow Days Unicorn Sweater, Snow Days Lot and Snow Days Builders Pack are tied to 12 Days of Presents 2012 by wiki pages.", "source": "wiki pages: Snow Days Unicorn Sweater; Snow Days Lot; Snow Days Builders Pack"}
 ],
 "confidence": 0.6,
 "open": [
  "2013 occurrence NOT established. Client 'Day N' names and wiki tags (2013) are undated; no article dates it. Not scheduled.",
  "Recurring is null. The wiki calls the event annual, but no article says so, and only one dated occurrence (2012) exists.",
  "Exact clock times (e.g. 12:01 am / 11:59 pm PST) are not verified in article 2813's text reviewed here. Only the Dec 13-24 window is kept.",
  "Big Present names not settled. Earlier pack said 2012 Big Present = St. Bernard Pet and later one = Polar Bear Ride (wiki 12 Days of Presents); not re-checked here. Snowglobe Helmet was wrongly listed as the Big Present; it is a daily reward.",
  "Icy Snowflake Glasses and Figgy Pudding Critter are tagged 2013 on the wiki and are left out as unconfirmed. The wiki page also lists 'Snowflake Glasses' as a Day 7 2012 present; may be the same or a different item.",
  "Icy Snow Days Flair Shard: wiki tie to 2012 not verified on the event page; treat as unverified.",
  "Snow Days vs 12 Days of Presents is unsettled. The 2012 link comes from wiki item pages; the wider Snow Days event (articles 892, 1953, 2428; 2011 per 2428; NPCs Candi Ivy and Snow Hill Mayor from article 828) is a separate, undated candidate. Its NPCs are withheld here.",
  "SOE-wide 12 Days of Holidays promotions are a separate calendar entry and not merged here: article 2433, 2440, 2441, 2442, 2455 (Free Realms-hosted, dated Dec 17 2011 PST per pack), 2457 (day 8 double Station Cash until 21 Dec 08:59 CET, no year, undated), 2826 (Free Realms-hosted generic triple Station Cash, no year, unplaced), 2431 (preview, not live). Dates for these come from the pack, not re-read in full.",
  "Prices unknown for all items; no station_cash prices sourced. 'Purchase Bow' is client UI only and is not listed as an item.",
  "Quest titles are locale text only; quest ids unknown. Locale 441964 is keyed 'Snowhill 12 Days of Presents' but its text reads '12 Days of Presents'.",
  "Snowhill make-up claim from article 2827 was not confirmed and is omitted."
 ]
}
```
