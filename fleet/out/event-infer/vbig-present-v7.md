<!-- fleet job=event-infer id=vbig-present-v7 status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[24434, 10050, 10, 3631] model=claude-haiku-5-5 -->
# Big Present

{
 "event": {
  "name": "12 Days of Holidays (Free Realms, 2012 edition)",
  "aliases": ["12 Days of Presents (the presents sub-system of the event, per article 2827)", "Snow Days (wiki and client label, 2012)", "Big Present (bonus reward component; not a separate event)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Dec 13-24, 2012 (daily challenges, 12:01 am PST Dec 13 through 11:59 pm PST Dec 24); presents opened Dec 25, 2012", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"}
 ],
 "recurring": null,
 "zones": ["Snowhill"],
 "npcs": ["Trina Turtledove (client strings locale:441963, 441965 tie her to Snowhill presents; the 2012 article does not name her, so treat as client-sourced)"],
 "quests": ["Big Present 1", "Big Present 2", "Big Present 3"],
 "activities": [
  "Log in each day Dec 13-24 and complete that day's holiday challenge at Snowhill; completing it on its first day gives a present with a bow (article 2813; locale:441441)",
  "Track progress with Trina Turtledove's Present Tracker and collect bows (locale:441963)",
  "Open presents on Dec 25, 2012 with Trina in Snowhill (locale:441965, 441927)",
  "Earn a Big Present for every 4 daily presents, 8 and 12 presents as tiers (locale:441944-441946)"
 ],
 "items": [
  {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki page Snow Days Unicorn Sweater (labelled 2012; no wiki category or article tie, weak)"},
  {"name": "Snow Days Lot", "price": null, "currency": null, "source": "wiki page Snow Days Lot (labelled 2012, Day 11; weak)"},
  {"name": "Snow Days Builders Pack", "price": null, "currency": null, "source": "wiki page Snow Days Builders Pack (labelled 2012; weak)"},
  {"name": "Snowflake Glasses", "price": null, "currency": null, "source": "wiki page Snowflake Glasses (labelled 2012; weak)"}
 ],
 "rewards": [
  "A present with a bow for each daily challenge completed on its first day (article 2813; locale:441441)",
  "A bonus Big Present for every 4 daily presents opened (article 2813; locale:441441)",
  "Complete all 12 daily challenges: 12 bows and 15 presents in total (article 2813)",
  "Big Present 1-3 reward presents (locale:441947-441949)"
 ],
 "evidence": [
  {"claim": "The 2012 event is named '12 Days of Holidays', ran Dec 13 2012 12:01 am PST to Dec 24 2012 11:59 pm PST, with a daily challenge and reward, and a present-opening step on Dec 25", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "Each day Dec 13-24 a new challenge is offered; completing it on its first day gives a present with its bow; presents open on the 25th; an extra Big Present is earned per 4 daily presents", "source": "locale:441441"},
  {"claim": "Big Present tiers: complete 4, 8 or 12 daily presents to open a Big Present on Dec 25", "source": "locale:441944, 441945, 441946"},
  {"claim": "Presents system rules (daily challenge, first-day present, Dec 25 opening, bows bought for missed days) are restated; the article is undated", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2827"},
  {"claim": "Client text 'SOE 12 Days of Holidays is Here!' is a 2011 cross-game SOE promotion, a different event with the same name", "source": "locale:831, locale:832"},
  {"claim": "The 2012 posting date 2012-12-13 is inferred from a 'Posted 4 days, 9 hours ago' stamp against a 2012-12-18 capture; the event dates come from the article body", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"}
 ],
 "confidence": 0.7,
 "open": [
  "The pack's name 'Big Present' is a reward component. The 2012 event is '12 Days of Holidays'. The pack merged the component with the event; the prior answer's name '12 Days of Presents' was the presents sub-system, and the 2012 article names the event '12 Days of Holidays'.",
  "The 12:01 am / 11:59 pm PST times are now sourced from article 2813 (lookup fact:event excerpt). The article's full body was not re-read beyond that excerpt.",
  "Locale 441513-441524 ('12 Days Present - Day 1..12') and locale 441525 ('12 Days Bow - Day 1') are client quest titles that carry the 12 Days name. No article ties them to a year, so they are not listed as quests of the 2012 occurrence. Confirm against the 2012 quest list before wiring.",
  "2013 edition: NOT article-confirmed. Client strings '12 Days 2013 - Day 1..12' (locale:441125-441199) and Trina Turtledove challenge strings have no dated source. Not listed as an occurrence.",
  "Recurrence: 'annual' is not established by any source in the pack. recurring is null.",
  "The four 'Snow Days' items are tied only by wiki page labels; no wiki category membership was found. Prices are unsourced.",
  "Excluded: 2013 wiki-only rewards (Figgy Pudding Critter, Icy Snowflake Glasses, Arctic Cat, Snow Days Gift Box, Holigoblin Mask); per-day rewards read only from a lookup excerpt (St. Bernard pet, Snowman Mask, 5,000 Coins, Temporary Snowflake Parachute); Snowglobe Helmet, Icy Snow Days Flair Shard, Winter Holiday Present (locale:132588); '12 Days of Sales' banners; Candi Ivy and Alana Yedra (Gifting Tree NPCs, not tied to this event).",
  "The 2011 SOE '12 Days of Holidays' cross-game promotion (articles 2442, 2441, 2433, 2457; Dec 13-25, 2011) is a separate event with the same name and is not an occurrence here.",
  "Article 2827 is undated and supports rules only; it gives no year."
 ]
}
