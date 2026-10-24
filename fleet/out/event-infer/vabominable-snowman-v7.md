<!-- fleet job=event-infer id=vabominable-snowman-v7 status=done turns=1 usd=0.0039 tokens(read,write,in,out)=[0, 12007, 4, 4760] model=claude-haiku-5-5 -->
# Abominable Snowman

```json
{
 "event": {
  "name": "Snow Days",
  "aliases": ["Snowy Days (article 1955, French 'Jours Enneigés')", "Días de Nieve (Spanish posts 1956, 1957)", "Snow Days Returns (article 2429)", "Snow Days Are Here Again! (article 2808)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "Dec 18 2009 to Jan 3 2010 (daily holiday events, community events, JCC tournaments) - window cited from the Spanish post, not re-verified in this pass", "source": "http://www.freerealms.com/article/detail.action?articleId=718"},
  {"year": 2011, "when": "Season discussed in a community webcast on Dec 8 2011; no start or end date given. Not confirmed as running that day.", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
  {"year": 2012, "when": "Late Dec 2012 or early Jan 2013 (relative-age only: 'posted about 3 weeks 6 days' before a January 2013 capture; no absolute date)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2808"}
 ],
 "recurring": "Yearly, December into early January. Articles 1955 ('chaque année') and 2808 ('every year') say it recurs; article 892 says Snow Days ended and was to return the following year. Exact window is not stated in any source for any year.",
 "zones": ["Snowhill"],
 "npcs": ["Candi Ivy", "Everett", "Zena Lierre (article 1955 only)", "Trina Turtledove (client text only, locale:441091)", "The Abominable Snowman"],
 "quests": [],
 "activities": [
  "Talk to Candi Ivy daily to get a present from under the Gifting Tree (articles 828, 2429)",
  "Spin the Snow Days prize wheel (article 828)",
  "Defend the Gifting Tree from the Abominable Snowman and his snowmen by throwing snowballs from the nearest snowball pile when a warning appears (articles 1950, 1955, 1956, 1957, 2429, 2808)",
  "Fight Robgoblins to earn Snow Days clothing (articles 2429, 2808)",
  "Pelt snowmen with snowballs to collect coal for Everett (locale:420816; name-level tie only)",
  "Eat one of each Snow Days cookie for Trina Turtledove (locale:441091; client text only)"
 ],
 "items": [
  {"name": "Snow Days Present", "price": null, "currency": "reward", "source": "locale:1729 (name); article 828 (daily Gifting Tree presents)"},
  {"name": "Snow Days outfits", "price": null, "currency": null, "source": "article 828 (Marketplace, limited time)"},
  {"name": "Snow Days clothing (Robgoblin drop)", "price": null, "currency": "reward", "source": "article 2429; article 2808"},
  {"name": "Snow Days Toys", "price": null, "currency": "reward", "source": "wiki: Snow Days Toys (prize wheels and combat/crafting rewards; wiki only)"}
 ],
 "rewards": [
  "Snow Days Present (daily from the Gifting Tree; article 828)",
  "Snow Days outfits (Marketplace; article 828)",
  "Snow Days clothing from Robgoblin fights (articles 2429, 2808)",
  "Snow Days Toys (wiki only)"
 ],
 "evidence": [
  {"claim": "Snow Days holiday events ran Dec 18 2009 to Jan 3 2010", "source": "http://www.freerealms.com/article/detail.action?articleId=718"},
  {"claim": "Snow Days 2011 was discussed in a community webcast on Dec 8 2011; the event's window is not given", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
  {"claim": "Snow Days ended and was to return the following year", "source": "http://www.freerealms.com:80/article/detail.action?articleId=892"},
  {"claim": "Candi Ivy daily Gifting Tree presents, Snow Days prize wheel, Snow Days outfits limited to Marketplace", "source": "http://www.freerealms.com:80/article/detail.action?articleId=828"},
  {"claim": "Abominable Snowman and snowmen steal Gifting Tree presents each Snow Days; players throw snowballs from the nearest snowball pile when warned", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1950"},
  {"claim": "The Abominable Snowman attacks recur each year (French post)", "source": "http://www.freerealms.com/article/detail.action?articleId=1955"},
  {"claim": "They show up every year to steal the presents from under the Gifting Tree", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2808"},
  {"claim": "Robgoblin fights earn Snow Days clothing", "source": "http://www.freerealms.com/article/detail.action?articleId=2429; http://www.freerealms.com:80/article/detail.action?articleId=2808"},
  {"claim": "Pelt snowmen to collect coal for Everett", "source": "locale:420816 (name-level only)"}
 ],
 "confidence": 0.5,
 "open": [
  "Pack title is 'Abominable Snowman', but the Abominable Snowman is a raid inside the Snow Days event, so the event is recorded as Snow Days. The pack's own 'Abominable Snowman' names_seen is the only hit for that name.",
  "MERGE: 12 Days of Presents / 12 Days of Holidays is NOT merged here. Articles 2813 and 2827 describe it with daily challenges Dec 13-24 and presents opened Dec 25, and never mention Snow Days. The only link is the wiki category (Category:Snow Days). Keep it as a separate event until a source ties them. Its items (Snow Days Lot, Snow Days Builders Pack, Snow Days Unicorn Sweater, Icy Snowflake Glasses, Figgy Pudding Critter, Icy Snow Days Flair Shard) belong to 12 Days, not Snow Days, and are removed from this record.",
  "2009 window rests on article 718 (Spanish); English 705 was not re-verified, and a lookup for those dates returned no matches. Treat as cited but unverified in this pass.",
  "2010 is not used: articles 1950, 1955, 1956, 1957 are undated. The year is only inferred from relative post ages.",
  "2011: no start or end date in any source; article 2428 gives only the webcast date.",
  "2012/13 season start from article 2808 is relative-age only (late Dec 2012 or early Jan 2013). Wiki Template:News/Archive ('[Snow Days] has ended' under the Jan 12 2012 update) and Game Update 122.1 (12/04/2013) were cited by the critique but not re-read here, so they are not used as evidence.",
  "The Dec 1 2013 to Jan 14 2014 window has no article or client confirmation and is dropped.",
  "Quest titles: none is tied to Snow Days by a source. The Gifting Tree daily and Snow Days quest titles are unresolved. 'An Unexpected Gift' (locale:420296), 'Snowmen Disassembly' (locale:420292), 'Guarding the Gifting Tree' (locale:420280), 'Snowman Showdown' (locale:5102788, 5102791) are unconfirmed.",
  "Snowball defense is sourced to articles, not the locale lines. Locale 441097, 441121, 441305, 441317 describe the same theft and could be checked as in-client text. Locale 441200 is not used (it names the 12 Days 2013 quest).",
  "Zone and NPC lists may be incomplete: the wiki Category:Snow Days member list was empty in the pack.",
  "Prices and currency: no source gives any; all null.",
  "Snow Days Floor (locale:441325), Snow Days Pillar (locale:441326), Mini Holiday Tree, Tacky Reindeer Sweater, Snowman Coals are not listed: no event-linked source.",
  "Recurring pattern is annual, December into January, from articles 1955, 2808 and 892. The 'annual during December through January' wording on the wiki Events page was cited by the critique but not re-read here.",
  "The calendar is not wireable as a single schedule: only 2009 (article 718) and 2011 (webcast only) are article-dated, and 2012/13 is relative-age only. No 2014 or later occurrence is in the pack."
 ]
}
```
