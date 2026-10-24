<!-- fleet job=event-infer id=vjcc-v6 status=done turns=2 usd=0.0040 tokens(read,write,in,out)=[6594, 14497, 6, 4335] model=claude-haiku-5-5 -->
# JCC events

```json
{
 "event": {
  "name": "Snow Days (Días de Nieve)",
  "aliases": ["Snow Days", "Días de Nieve", "Seasonal: Snow Days (client quest title)", "Snow Days! (client locale:5103008)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "Dec 18, 2009 to Jan 3, 2010, daily", "source": "http://www.freerealms.com/article/detail.action?articleId=709"},
  {"year": 2010, "when": "Ended by the Jan 26, 2010 update; article says it was 'over until next year'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=892"},
  {"year": 2011, "when": "Live during the 2011 community webcast ('Snow Days is HERE'); exact dates not in pack", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
  {"year": 2012, "when": "'12 Days of Presents' quest series during 2012 Snow Days; exact dates not in pack", "source": "Wiki: Snow Days Lot; Icy Snow Days Flair Shard; Snow Days Unicorn Sweater"},
  {"year": 2013, "when": "'Snow Days 2013' (2013 Snow Days Toy Collector Pack sold during Snow Days 2013); exact dates not in pack", "source": "Wiki: 2013 Snow Days Toy Collector Pack"}
 ],
 "recurring": "Yearly winter seasonal event (late December into early January). Article 892 says it would return the following year; article 1953 calls it the winter seasonal event.",
 "zones": ["Snowhill"],
 "npcs": ["Candi Ivy (Gifting Tree presents, article 828)", "Mayor of Snow Hill (daily quests, article 828)", "Abominable Snowman (large figure around quest givers in Snowhill, article 2815)", "Robgoblins (fought for special clothing, articles 2429, 1950)"],
 "quests": ["Snow Days (quest_title locale:5102485)", "Seasonal: Snow Days (quest_title locale:4419465)", "12 Days of Presents (2012 quest series, wiki)"],
 "activities": [
  "Talk to Candi Ivy daily for a present from under the Gifting Tree (article 828)",
  "Spin the Snow Days prize wheel (article 828; locale:426650 'Snow Days Wheel')",
  "Complete daily Snow Days quests for the Mayor and Snow Hill residents (article 828)",
  "Fight Robgoblins for special Snow Days clothing (articles 2429, 1950)",
  "Attend daily community events at 15:00 Pacific time (articles 709, 771)",
  "JCC tournaments all day (articles 718, 771; 709 says JCC tournaments)",
  "Complete the 12 Days of Presents quest series for 2012 items (wiki)"
 ],
 "items": [
  {"name": "Snow Days Present", "price": null, "currency": "reward", "source": "locale:1729"},
  {"name": "Snow Days Outfits (clothing)", "price": null, "currency": null, "source": "articles 828, 1956, 1957 (Marketplace for a limited time, also quests and gifts)"},
  {"name": "Snow Globe (exotic ride)", "price": null, "currency": "station_cash", "source": "Wiki: Snow Globe (SC Marketplace during Snow Days)"},
  {"name": "Snow Hog (pet pal)", "price": null, "currency": "coins", "source": "Wiki: Snow Hog (Coin Shop, Members Only)"},
  {"name": "2013 Snow Days Toy Collector Pack", "price": null, "currency": "station_cash", "source": "Wiki: 2013 Snow Days Toy Collector Pack"},
  {"name": "Snow Days Lot (housing lot, 12 Days of Presents 2012)", "price": null, "currency": "reward", "source": "Wiki: Snow Days Lot; locale:441205"},
  {"name": "Icy Snow Days Flair Shard", "price": null, "currency": "reward", "source": "Wiki: Icy Snow Days Flair Shard"},
  {"name": "Snow Days Unicorn Sweater", "price": null, "currency": "reward", "source": "Wiki: Snow Days Unicorn Sweater; locale:441217"},
  {"name": "Snow Days Builders Pack (building materials)", "price": null, "currency": "reward", "source": "Wiki: Snow Days Builders Pack; locale:441209"},
  {"name": "Snow Days Toys (housing miniatures)", "price": null, "currency": "reward", "source": "Wiki: Snow Days Toys (prize wheels, combat and crafting rewards)"}
 ],
 "rewards": ["Snow Days Present", "Snow Days outfits", "Snow Days Toys", "Snow Days Lot", "Icy Snow Days Flair Shard", "Snow Days Unicorn Sweater"],
 "evidence": [
  {"claim": "Snow Days ran daily from Dec 18, 2009 to Jan 3, 2010 with daily community events and JCC tournaments.", "source": "http://www.freerealms.com/article/detail.action?articleId=709"},
  {"claim": "Same run, Dec 18, 2009 to Jan 3, 2010, every day, with community events and JCC tournaments.", "source": "http://www.freerealms.com/article/detail.action?articleId=718"},
  {"claim": "JCC tournaments ran all day during Snow Days; a different community event each day at 15:00 Pacific, running until January 3.", "source": "http://www.freerealms.com/article/detail.action?articleId=771"},
  {"claim": "Snow Days ended and was to return the following year; Snow Days is over until next year.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=892"},
  {"claim": "Snow Days is HERE during the 2011 community webcast recap.", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
  {"claim": "Snow Days is the winter seasonal event; the party was the first Snow Days party of the season.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1953"},
  {"claim": "Daily Mayor/Snow Hill quests; Candi Ivy daily presents from the Gifting Tree; Snow Days prize wheel; Snow Days outfits sold in the Marketplace for a limited time.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=828"},
  {"claim": "Fighting Robgoblins during Snow Days earns special Snow Days clothing; Snowhill decorated, presents under the Gifting Tree.", "source": "http://www.freerealms.com/article/detail.action?articleId=2429"},
  {"claim": "Abominable Snowman towered over players around quest givers in Snowhill during Snow Days.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2815"},
  {"claim": "Snow Days outfits sold through catalog or obtained from quests and opening gifts.", "source": "http://www.freerealms.com/article/detail.action?articleId=1957"},
  {"claim": "Snow Days quest_title, item and place names exist in the client.", "source": "locale:5102485, locale:4419465, locale:1729, locale:426650, locale:441205"},
  {"claim": "12 Days of Presents 2012 quest series produced Snow Days Lot, Icy Snow Days Flair Shard, Snow Days Unicorn Sweater, Snow Days Builders Pack; 2013 Snow Days Toy Collector Pack sold during Snow Days 2013.", "source": "Wiki pages: Snow Days Lot; Icy Snow Days Flair Shard; Snow Days Unicorn Sweater; Snow Days Builders Pack; 2013 Snow Days Toy Collector Pack; Category:Snow Days"}
 ],
 "confidence": 0.7,
 "open": [
  "The pack name 'JCC events' merges several things. This record covers only Snow Days. Generic JCC expectation articles (1552 French, 1592, 1593, 1628 Summer Camp, all undated or 'expected' wording) are not occurrences of any event and are excluded. Article 1628 (Summer Camp Crafting Week) is a separate event with no absolute date.",
  "Article 1861 (Halloween JCC promotion, TCG pack quests) is a separate promotion; excluded.",
  "Articles 640 and 641 (weekly player-vs-player JCC) were not re-verified in this pass; excluded from this record.",
  "Article 770 was dropped as a source for the JCC tournament claim. It is a daily community-event reminder and does not mention JCC tournaments.",
  "Exact 2010 Snow Days dates are not in the pack; 2010 is only inferred from article 892 ('over until next year'). The 2011, 2012 and 2013 runs have no absolute dates in the pack; the year comes from article 2428 and from wiki page titles.",
  "Article 1552 and 1593 were cited in the earlier answer but are not verified here.",
  "Wiki sources for 2012 and 2013 give no run dates. Treat those occurrences as year-only.",
  "Activity 'Learn to play JCC in the lobby' and 'Practise against Kai' (video JA4jxTzqdOg/00090.jpg) are not tied to Snow Days and are dropped.",
  "Prices are null: the pack gives no Snow Days item prices except that the Snow Hog is Coin Shop and the Snow Globe is SC Marketplace; the exact amounts were not captured.",
  "The 'live' field is 'yes' meaning the event ran on the live service. It is not running now.",
  "Article publish dates are not in the pack; 709/718 give run dates and 828 and 2428 have no date."
 ]
}
```
