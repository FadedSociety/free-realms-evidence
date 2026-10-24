<!-- fleet job=event-infer id=vspring-chicken-pack-sale-v7 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[7297, 8023, 6, 3173] model=claude-haiku-5-5 -->
# Spring Chicken Pack sale

{
 "event": {
  "name": "Memorial Mania 2011 Station Cash pack sale (Memorial Day / Spring Chicken packs)",
  "aliases": ["Spring Chicken Pack sale", "Memorial Day Pack sale", "Memorial Mania", "Memorial Day and Spring Chicken Pack promotion"]
 },
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [
  {"year": 2011, "when": "May 27-30 (article quote: 7:00 AM PDT Fri May 27 to 11:59 PM PDT Mon May 30); year inferred from weekdays, article date null", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146 (quote: \"The promotion begins at 7:00 AM PDT on Friday, May 27 and ends at 11:59 PM PDT on Monday, May 30.\")"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy the Memorial Day Pack with Station Cash", "Buy the Spring Chicken Pack with Station Cash"],
 "items": [
  {"name": "Memorial Day Pack", "price": null, "currency": "station_cash", "source": "locale:435553 (contents); locale:435554/435555 (name, per prior answer); article 2146 listing not re-read. Price 400 SC is unverified."},
  {"name": "Spring Chicken Pack", "price": null, "currency": "station_cash", "source": "locale:435357 (name); locale:435358 (contents). Article 2146 listing not re-read. Price 500 SC is unverified."},
  {"name": "Spring Chicken Costume", "price": null, "currency": "reward", "source": "locale:435358"},
  {"name": "Spring Chick Pet Pal (client also reads 'Spring Chicken Pet Pal')", "price": null, "currency": "reward", "source": "locale:435320 ('Spring Chicken Pet Pal'); locale:435358 ('a Chick and Chicken Pet Pal'). Single reward, name unresolved."},
  {"name": "Uncle Sam Hat / Top Hat", "price": null, "currency": "reward", "source": "locale:435553 ('Uncle Sam Hat'); article 2146 as reported by prior reading ('Uncle Sam Top Hat'), unconfirmed"},
  {"name": "Uncle Sam Jacket", "price": null, "currency": "reward", "source": "locale:435553"},
  {"name": "Uncle Sam Pants", "price": null, "currency": "reward", "source": "locale:435553"},
  {"name": "Uncle Sam Shoes", "price": null, "currency": "reward", "source": "locale:435553"},
  {"name": "USA T-Shirt", "price": null, "currency": "reward", "source": "locale:435553"},
  {"name": "USA Flags (5)", "price": null, "currency": "reward", "source": "locale:435553"}
 ],
 "rewards": [
  "Memorial Day Pack contents: Uncle Sam Hat, Jacket, Pants, Shoes, 1 USA T-Shirt, 5 USA Flags for the home (locale:435553)",
  "Spring Chicken Pack contents: Chicken Costume, Chick and Chicken Pet Pal, 20 Chicks and Chickens for the house (locale:435358)"
 ],
 "evidence": [
  {"claim": "Article 2146 (titled Memorial Mania May 27th through May 30th) states the promotion window 7:00 AM PDT Fri May 27 to 11:59 PM PDT Mon May 30, 2011 (year inferred from weekdays).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146"},
  {"claim": "Article 2146 is summarized as promoting Memorial Mania May 27-30, 2011 and listing two Station Cash item packs.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146"},
  {"claim": "Memorial Day Bundle contents are in the client.", "source": "locale:435553"},
  {"claim": "Spring Chicken Pack name and contents are in the client.", "source": "locale:435357; locale:435358"}
 ],
 "confidence": 0.35,
 "open": [
  "Lookup of the articles index returned no matches this session, so article 2146 could not be re-read. Its window, pack prices (400 SC, 500 SC) and the Uncle Sam Top Hat naming come from a prior reading and are unverified.",
  "Window conflict: article 2146's quote gives 7:00 AM PDT May 27 to 11:59 PM PDT May 30; the prior pack notes article 2144 gives 12:01 AM PDT May 27 to 11:59 PM PDT May 30 for Memorial Mania (triple Station Cash with an SOE Pre-Paid card). It is not established which window governs the pack sale. Memorial Mania is likely the parent event; the pack sale is a part of it per the 2146 summary, not a separate dated event.",
  "Year 2011 is inferred from weekdays (Fri May 27, Mon May 30); no dateline confirms it. Live status is therefore unsure.",
  "Spring Chicken fever (locale:435358) is not dated in the client. It is not merged with Spring Fever (April 2011) or the Spring 2012 double-SC promotion (articleId=2557).",
  "Pet name unresolved: 'Spring Chick Pet Pal' vs 'Spring Chicken Pet Pal'. Wiki Spring Chick was not checked, so not cited.",
  "Wiki category members, zones, NPCs and quests: none found in the pack; none claimed.",
  "Spring Chicken Housing Item excluded (no source tying it to this sale)."
 ]
}
