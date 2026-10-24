<!-- fleet job=event-infer id=vspring-chicken-pack-sale-v6 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[7014, 7673, 6, 3383] model=claude-haiku-5-5 -->
# Spring Chicken Pack sale

{"event": {"name": "Memorial Day and Spring Chicken Pack promotion (May 2011 Station Cash pack sale)", "aliases": ["Spring Chicken Pack sale", "Memorial Day Pack sale", "Memorial Mania (article 2146 title; the pack sale is one part of it, see open)"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "May 27-30 (quoted as 7:00 AM PDT Fri May 27 to 11:59 PM PDT Mon May 30)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (quote: \"The promotion begins at 7:00 AM PDT on Friday, May 27 and ends at 11:59 PM PDT on Monday, May 30.\"). Article date field is null; year 2011 is inferred from the quote and weekdays, not from a dateline."}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy the Memorial Day Pack with Station Cash", "Buy the Spring Chicken Pack with Station Cash"],
 "items": [
  {"name": "Memorial Day Pack", "price": "400", "currency": "station_cash", "source": "articleId=2146 (price as reported in prior pack; re-check not possible in this session: articles lookup returned no matches); locale:435553 (\"A special Memorial Day Bundle! Get your Uncle Sam Hat, Jacket, Pants and Shoes! Also includes 1 USA T-Shirt and 5 USA Flags\")"},
  {"name": "Spring Chicken Pack", "price": "500", "currency": "station_cash", "source": "articleId=2146 (price as reported in prior pack; not re-verified); locale:435358 (\"Spring Chicken fever has come to Free Realms! Get ... a Chicken Costume, a Chick and Chicken Pet Pal, and 20 Chicks and Chickens for your house!\")"},
  {"name": "Spring Chicken Costume", "price": null, "currency": "reward", "source": "locale:435358; locale:435322"},
  {"name": "Spring Chick Pet Pal", "price": null, "currency": "reward", "source": "locale:435358 (\"a Chick and Chicken Pet Pal\"); locale:435320 reads \"Spring Chicken Pet Pal\". The name is unresolved (see open); one reward, two client spellings."},
  {"name": "Uncle Sam Top Hat", "price": null, "currency": "reward", "source": "articleId=2146 (as reported); locale:399120"},
  {"name": "Uncle Sam Jacket", "price": null, "currency": "reward", "source": "articleId=2146 (as reported); locale:399085"},
  {"name": "Uncle Sam Pants", "price": null, "currency": "reward", "source": "articleId=2146 (as reported); locale:399155"},
  {"name": "Uncle Sam Shoes", "price": null, "currency": "reward", "source": "articleId=2146 (as reported); locale:400359"},
  {"name": "USA Flags (5)", "price": null, "currency": "reward", "source": "locale:435553"},
  {"name": "USA T-Shirt", "price": null, "currency": "reward", "source": "locale:435553"}
 ],
 "rewards": [
  "Memorial Day Pack (400 SC): Uncle Sam Hat/Top Hat, Jacket, Pants, Shoes, 1 USA T-Shirt, 5 USA Flags (locale:435553)",
  "Spring Chicken Pack (500 SC): Chicken Costume, Chick and Chicken Pet Pal, 20 Chicks and Chickens for the house (locale:435358)"
 ],
 "evidence": [
  {"claim": "The promotion window is quoted as 7:00 AM PDT Fri May 27 to 11:59 PM PDT Mon May 30, 2011. The quote is from the article, but the article's title is 'Memorial Mania May 27th through May 30th', so the window is attributed to this promotion by inference.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146"},
  {"claim": "The Memorial Day Bundle contents (Uncle Sam Hat, Jacket, Pants, Shoes, 1 USA T-Shirt, 5 USA Flags) are in the client description.", "source": "locale:435553"},
  {"claim": "The Spring Chicken Pack contents (Chicken Costume, Chick and Chicken Pet Pal, 20 Chicks and Chickens) are in the client description, which ties the pack to a 'Spring Chicken fever' promotion.", "source": "locale:435358"},
  {"claim": "The Spring Chicken Pet Pal name exists in the client.", "source": "locale:435320"}
 ],
 "confidence": 0.5,
 "open": [
  "Prices (400 SC and 500 SC) and the stated values (1300 SC and 2000 SC) come only from the prior pack's reading of articleId=2146. The articles lookup returned no matches in this session, so they are not re-verified. Treat prices as unconfirmed until the article text is read.",
  "The 7 AM window is quoted from articleId=2146, which is titled 'Memorial Mania May 27th through May 30th'. Memorial Mania (triple Station Cash for an SOE Pre-Paid Station Cash Card, 12:01 AM PDT May 27 to 11:59 PM PDT May 30, 2011; articleId=2146 and 2144) is a separate offer. Whether the 7 AM window governs the pack sale or Memorial Mania is not shown; it is not resolved. Memorial Mania needs its own object. Its card name differs between articles (2144 says 'SOE Pre-Paid Game Card').",
  "Year 2011 is inferred from weekday matching (Fri May 27 and Mon May 30 fall in 2011). The article date is null, so no dateline confirms it.",
  "Pet name is unresolved: 'Spring Chick Pet Pal' (prior article reading, wiki Spring Chick) vs 'Spring Chicken Pet Pal' (locale:435320) vs 'a Chick and Chicken Pet Pal' (locale:435358). Listed once as one reward. The wiki Spring Chick claim was not checked here, so the wiki source is not cited.",
  "Uncle Sam hat naming: article says 'Uncle Sam Top Hat' (locale:399120); locale:435553 says 'Uncle Sam Hat'. Recorded as observed; not merged.",
  "Spring Chicken Pack is described in the client as returning from 'Spring Chicken fever' (locale:435358). The prior answer tied it to Spring Fever (April 2011). That is a different event and is not merged here. The Spring 2012 double-SC promotion (articleId=2557) is excluded.",
  "Spring Chicken Housing Item (wiki Holiday category) has no source tying it to this sale; excluded.",
  "Only one dated occurrence is supported, so recurring is null. No zones, NPCs or quests tie to this sale."
 ]}
