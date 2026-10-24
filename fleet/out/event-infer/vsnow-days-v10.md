<!-- fleet job=event-infer id=vsnow-days-v10 status=done turns=1 usd=0.0032 tokens(read,write,in,out)=[0, 12469, 4, 3341] model=claude-haiku-5-5 -->
# Community Events (Snow Days)

```json
{
 "event": {
  "name": "Snow Days",
  "aliases": ["Días de Nieve", "Les Jours de Neige", "Snow Days community events", "Colina Nevada (Snowhill, Spanish posts)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "Dec 18, 2009 through Jan 3, 2010, daily in-game community events at 3pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705 (Spanish: articleId=709)"},
  {"year": 2010, "when": "Member reward pack began Wed 15 Dec 2010 at 21:00 CET, delivered over 2-3 days (year stated in the French quote)", "source": "http://www.freerealms.com/article/detail.action?articleId=1966&request_locale=en_US"}
 ],
 "recurring": "Yearly in winter (December into early January). Basis: two dated winter occurrences (2009-10, 2010) plus article 892's line 'Snow Days is over until next year.' (article 892's 2010-01-26 date is pack metadata only).",
 "zones": ["Snowhill (town centre, Gifting Tree)", "Wintery Basin (fishing area above Snowhill; season party, per article 1953 summary)"],
 "npcs": ["Candi Ivy (daily Gifting Tree present, article 828)", "Abominable Snowman (attacks the Gifting Tree, article 2815)", "Calvin Coldcastle (snowball fights, locale:441081)"],
 "quests": ["The Gifting Tree"],
 "activities": [
  "Daily in-game community events at 3pm Pacific, a different event each day, including snowball battles and jump-platform games (articles 705, 770, 771)",
  "Talk to Candi Ivy each day to get a present from under the Gifting Tree (article 828)",
  "Spin the Snow Days prize wheel (article 828)",
  "Repel Abominable Snowman attacks on the Gifting Tree with snowballs (article 2815)"
 ],
 "items": [
  {"name": "Snow Days Lot", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
  {"name": "Snow Days Builders Pack", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
  {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
  {"name": "Icy Snow Days Flair Shard", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
  {"name": "Snow Days Toys", "price": null, "currency": null, "source": "wiki category 'Snow Days'"},
  {"name": "Snow Days Present", "price": null, "currency": "reward", "source": "locale:1729"},
  {"name": "Snow Days Wheel", "price": null, "currency": null, "source": "locale:426650; article 828"}
 ],
 "rewards": [
  "Snow Days present from under the Gifting Tree, daily (article 828)",
  "Snow Days prize wheel bonus prizes (article 828)",
  "Snow Days outfits, limited time (article 809)",
  "Snow Days member reward pack, tiered by membership, Dec 2010 (articles 1966, 1967)"
 ],
 "evidence": [
  {"claim": "Snow Days ran daily Dec 18, 2009 through Jan 3, 2010 with in-game community events", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
  {"claim": "Community events took place each day at 3pm Pacific", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
  {"claim": "A different event each day, with snowball battles and jump platforms, until 3 January", "source": "http://www.freerealms.com/article/detail.action?articleId=770"},
  {"claim": "Member reward pack began Wed 15 Dec 2010 at 21:00 CET, arriving in 2-3 days", "source": "http://www.freerealms.com/article/detail.action?articleId=1966&request_locale=en_US"},
  {"claim": "Snowhill is decorated and presents are under the Gifting Tree in the town centre", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1950"},
  {"claim": "Talk to Candi Ivy every day for a present; spin the Snow Days prize wheel; holiday ending", "source": "http://www.freerealms.com:80/article/detail.action?articleId=828"},
  {"claim": "Abominable Snowman attacks the Gifting Tree during Snow Days", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2815; locale:433669"},
  {"claim": "Snow Days is over until next year", "source": "http://www.freerealms.com:80/article/detail.action?articleId=892"},
  {"claim": "Snow Days is HERE! (community webcast recap, undated in text)", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"}
 ],
 "confidence": 0.6,
 "open": [
  "Critique fix: the 2011 occurrence and the 'Snow Days 2011' alias are dropped. Article 2428 ('Snow Days is HERE!') has no date in its text, and the year came only from the pack title.",
  "The winter 2010 return posts (articleId 1950, 1953, 1956, 1957) print no year. They are used as context only, not as dated occurrences. The Dec 9/10 season-party dates are inferred from capture dates and are not used.",
  "Article 892's 2010-01-26 date is pack metadata; its body says only 'over until next year'.",
  "Recurrence rests on two dated winters plus the 'until next year' line. No third dated year is confirmed.",
  "NPC conflict: Spanish posts 1956/1957 name Alana Yedra as the daily Gifting Tree giver; English posts name Candi Ivy. Not resolved whether these are one NPC.",
  "Everett (coal request) appears only in the article 1950 summary, not in article text, so it is excluded.",
  "Quests: only 'The Gifting Tree' is tied to Snow Days by a source (articles 828, 2808; locale:419835). Other Gifting Tree quest answers (Guarding the Gifting Tree, Holiday Cheer, Present Problems, Silversnow's Sapling, The Perfect Disguise, The Great Robgoblin Robbery Ring, Holiday Recital, Bye-Bye Supplies!, Snowmen Disassembly) have no Snow Days tie in a source, so they are excluded. 'Snow Days Are Back!' (locale:1653) is unconfirmed.",
  "Possible merged event: 12 Days of Presents (Dec 2012; articles 2813/2827; locale:441946) is a separate event and is not merged. The '2013 Snow Days Toy Collector Pack' and 'Day 9: Snow Days Soccer' (locale:441181) may belong to 12 Days and are not counted.",
  "Item prices are not in any source and are all null. Only the wiki-category items are listed; individual outfit names are not tied to the event by article text.",
  "Desktop wallpaper promotion (article 820, Radiocasetera de Días de Nieve) is tied to the event but is not listed as an item.",
  "Activities at Wintery Basin (season party, bring boomboxes, ice fishing; article 1953 and locale:15043/15044/15048) and client events (House Party tour, Dance Party; locale:436455/436457) are noted but not tied to a dated occurrence."
 ]
}
```
