<!-- fleet job=event-infer id=vspring-chicken-pack-sale-v4 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[8496, 9259, 6, 3138] model=claude-haiku-5-5 -->
# Spring Chicken Pack sale

{
 "event": {"name": "Memorial Day Pack and Spring Chicken Pack sale", "aliases": ["Spring Chicken Pack sale", "Memorial Day Pack sale"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [{"year": 2011, "when": "May 27-30 (sale starts 7:00 AM PDT Fri May 27, ends 11:59 PM PDT Mon May 30)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146"}],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy the Memorial Day Pack (400 Station Cash)", "Buy the Spring Chicken Pack (500 Station Cash)"],
 "items": [
  {"name": "Memorial Day Pack", "price": "400", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (price and contents); locale:435553, locale:435555 (descriptions)"},
  {"name": "Spring Chicken Pack", "price": "500", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (price); locale:435357 (item name); locale:435358 (description)"},
  {"name": "Spring Chick Pet Pal", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (pack contents); locale:435321 (item name); wiki page Spring Chick"},
  {"name": "Spring Chicken Costume", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (pack contents); locale:435322"},
  {"name": "Uncle Sam Top Hat", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (pack contents); locale:399120"},
  {"name": "Uncle Sam Jacket", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (pack contents); locale:399085"},
  {"name": "Uncle Sam Pants", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (pack contents); locale:399155"},
  {"name": "Uncle Sam Shoes", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (pack contents); locale:400359"},
  {"name": "USA Flags (5)", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (pack contents); locale:435553"},
  {"name": "USA T-Shirt", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (pack contents); locale:435553"}
 ],
 "rewards": ["Memorial Day Pack (400 SC, stated 1300 SC value): Uncle Sam Top Hat, Jacket, Pants, Shoes, 5 USA Flags, 1 USA T-Shirt", "Spring Chicken Pack (500 SC, stated 2000 SC value): Spring Chicken Costume, Spring Chicken pet, Spring Chick Pet Pal, 20 each of Chick and Chicken house items"],
 "evidence": [
  {"claim": "The Memorial Day and Spring Chicken pack sale ran from 7:00 AM PDT Friday May 27 to 11:59 PM PDT Monday May 30, 2011.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146"},
  {"claim": "The Memorial Day Pack cost 400 Station Cash and contained Uncle Sam Top Hat, Jacket, Pants, Shoes, 5 USA Flags and 1 USA T-Shirt.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146; locale:435553; locale:435555"},
  {"claim": "The Spring Chicken Pack cost 500 Station Cash and its client description names a Chicken Costume, a Chick and Chicken Pet Pal, and 20 Chicks and Chickens for the house.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146; locale:435358"},
  {"claim": "The Uncle Sam item names (Top Hat, Jacket, Pants, Shoes) are client item names.", "source": "locale:399120; locale:399085; locale:399155; locale:400359"}
 ],
 "confidence": 0.6,
 "open": [
  "Memorial Mania is a separate promotion in the same article (articleId=2146, 12:01 AM PDT May 27 to 11:59 PM PDT May 30, 2011; triple Station Cash for an SOE Pre-Paid Station Cash Card). It is not part of this entry and needs its own object. Article 2144 calls the card an 'SOE Pre-Paid Game Card'; confirm the name.",
  "Pack-title mismatch: article 2146 is titled 'Memorial Mania May 27th through May 30th'. The name 'Memorial Day Pack and Spring Chicken Pack sale' is the pack-sale name, not the article title. The pack sale and Memorial Mania may share the article, not the event.",
  "Article 2146 has a null date. 2011 comes only from the quote; the weekdays (Fri May 27, Mon May 30) match 2011. A re-lookup of article 2146 in this session returned no matches, so the quote was not re-verified here.",
  "'Spring Chicken pet' in article 2146 is not confirmed as an item. Name match only to locale:435323 'Spring Chicken'. Client item locale:435320 'Spring Chicken Pet Pal' is tied only through the description locale:435358 ('a Chick and Chicken Pet Pal'). Confirm which client object is the pack's pet before wiring.",
  "The article says 'Uncle Sam Top Hat'; the Memorial Day Pack description (locale:435553, locale:435555) says 'Uncle Sam Hat'. These are observed strings; I have not asserted an alias relationship.",
  "Wiki claims 'USA T-shirt acquired during May 2011' and 'Spring Chick acquired through the Spring Chicken Pack' were not reproduced in lookups, so they are not cited as evidence here. The Spring Chick pet pal link rests on article 2146 and locale:435321.",
  "Spring Chicken Housing Item (wiki Holiday category) is not tied to this sale by a source; excluded.",
  "Spring Fever (April 2011) returned the Spring Chicken Pack per an earlier note. That is a different event, so this entry is not recurring. Only one dated occurrence is supported.",
  "Spring 2012 double-SC promotion (articleId=2557) is a different event; excluded.",
  "Bare 'Memorial' matches the zone Memorial Caverns; excluded.",
  "No zones, NPCs or quests tie to this sale in the pack or lookups."
 ]
}
