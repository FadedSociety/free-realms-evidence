<!-- fleet job=event-infer id=vspring-chicken-pack-sale-v5 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[7713, 9731, 6, 3423] model=claude-haiku-5-5 -->
# Spring Chicken Pack sale

{"event": {"name": "Memorial Day and Spring Chicken Pack promotion", "aliases": ["Spring Chicken Pack sale", "Memorial Day Pack sale"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [{"year": 2011, "when": "May 27-30 (7:00 AM PDT Fri May 27 to 11:59 PM PDT Mon May 30)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (quote: \"The promotion begins at 7:00 AM PDT on Friday, May 27 and ends at 11:59 PM PDT on Monday, May 30.\" Article date field is null; 2011 comes from the quote and matching weekdays)"}],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy the Memorial Day Pack (400 Station Cash)", "Buy the Spring Chicken Pack (500 Station Cash)"],
 "items": [
  {"name": "Memorial Day Pack", "price": "400", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (price, contents via fact:economy); locale:435553, locale:435555 (descriptions)"},
  {"name": "Spring Chicken Pack", "price": "500", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (price); locale:435357 (name); locale:435358 (description)"},
  {"name": "Spring Chicken Costume", "price": null, "currency": "reward", "source": "locale:435358 (pack description names a Chicken Costume); locale:435322 (name). Pack contents also listed in articleId=2146"},
  {"name": "Spring Chick Pet Pal", "price": null, "currency": "reward", "source": "locale:435358 (\"a Chick and Chicken Pet Pal\"); locale:435320 'Spring Chicken Pet Pal'; article 2146 lists 'Spring Chick Pet Pal'; wiki page Spring Chick says acquired through the Spring Chicken Pack"},
  {"name": "Uncle Sam Top Hat", "price": null, "currency": "reward", "source": "articleId=2146 (fact:economy); locale:399120"},
  {"name": "Uncle Sam Jacket", "price": null, "currency": "reward", "source": "articleId=2146 (fact:economy); locale:399085"},
  {"name": "Uncle Sam Pants", "price": null, "currency": "reward", "source": "articleId=2146 (fact:economy); locale:399155"},
  {"name": "Uncle Sam Shoes", "price": null, "currency": "reward", "source": "articleId=2146 (fact:economy); locale:400359"},
  {"name": "USA Flags (5)", "price": null, "currency": "reward", "source": "articleId=2146; locale:435553"},
  {"name": "USA T-Shirt", "price": null, "currency": "reward", "source": "articleId=2146; locale:435553"}
 ],
 "rewards": ["Memorial Day Pack (400 SC, stated 1300 SC value): Uncle Sam Top Hat, Jacket, Pants, Shoes, 5 USA Flags, 1 USA T-Shirt", "Spring Chicken Pack (500 SC, stated 2000 SC value): Spring Chicken Costume, Spring Chick Pet Pal, 20 each of Chick and Chicken house items (per articleId=2146 and locale:435358)"],
 "evidence": [
  {"claim": "The Memorial Day and Spring Chicken Pack promotion ran 7:00 AM PDT Fri May 27 to 11:59 PM PDT Mon May 30, 2011 (re-verified via articles fact:event).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146"},
  {"claim": "The Memorial Day Pack cost 400 Station Cash, stated 1300 SC value, with Uncle Sam Top Hat, Jacket, Pants, Shoes, 5 USA Flags, 1 USA T-Shirt (re-verified via articles fact:economy).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146; locale:435553; locale:435555"},
  {"claim": "The Spring Chicken Pack cost 500 Station Cash (stated 2000 SC value), described as returning from the Spring Fever promotion (re-verified via articles fact:economy).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146; locale:435357; locale:435358"},
  {"claim": "The Spring Chicken Pack's client description names a Chicken Costume, a Chick and Chicken Pet Pal, and 20 Chicks and Chickens for the house.", "source": "locale:435358"},
  {"claim": "Spring Chick is a pet pal acquired through the Spring Chicken Pack in the SC Marketplace during spring.", "source": "wiki page: Spring Chick; wiki page: Pet Pals"}
 ],
 "confidence": 0.5,
 "open": [
  "Name conflict: article articleId=2146 is titled 'Memorial Mania May 27th through May 30th'. The pack sale name here is the sale's own wording, not the article title. Aliases were not invented beyond the pack names in the prior entry.",
  "Memorial Mania (triple Station Cash for an SOE Pre-Paid Station Cash Card, 12:01 AM PDT May 27 to 11:59 PM PDT May 30, 2011; articleId=2146 and 2144) is a separate promotion in the same article and needs its own object. Its card name differs between articles (2144 says 'SOE Pre-Paid Game Card'); not resolved.",
  "The article 2146 date field is null. The 2011 year rests on the quote and on weekday matching (Fri May 27, Mon May 30 fall in 2011). Not confirmed from an article dateline.",
  "'Spring Chicken' (locale:435323) vs 'Spring Chicken Pet Pal' (locale:435320): which client object is the pack's pet is not confirmed; the article says 'Spring Chicken Pet' and the description says 'Chick and Chicken Pet Pal'.",
  "Uncle Sam hat naming: article says 'Uncle Sam Top Hat' (item locale:399120); the Memorial Day Pack descriptions (locale:435553, 435555) say 'Uncle Sam Hat'. Recorded as observed; alias status not asserted.",
  "Spring Fever (April 2011) is a different event that the Spring Chicken Pack returned from; not merged. Spring 2012 double-SC promotion (articleId=2557) excluded. Only one dated occurrence is supported, so recurring is null.",
  "Wiki claim 'USA T-shirt acquired during May 2011' was not reproduced in lookups; not cited.",
  "Spring Chicken Housing Item (wiki Holiday category) has no source tying it to this sale; excluded.",
  "No zones, NPCs or quests tie to this sale."
 ]}
