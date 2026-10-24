<!-- fleet job=event-infer id=vweekend-price-cut-v3 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[13912, 8590, 8, 2553] model=claude-haiku-5-5 -->
# Weekend Price Cut

{"event": {"name": "Weekend Price Cuts", "aliases": ["Weekend Price Cut", "Weekend Sale (Station Cash, Marketplace)"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [{"year": 2012, "when": "August 10-12, 2012 (12:01AM PDT 8/10/2012 to 11:59PM PDT 8/12/2012)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2707; corroborated by http://www.freerealms.com/article/detail.action?articleId=2712 (fact: 'during August 10 to 12, 2012') and http://www.freerealms.com/article/detail.action?articleId=2716 (fact: 'from 12:01 AM PDT on 8/10/2012 to 11:59 PM PDT on 8/12/2012')"}],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy Station Cash items in the Marketplace at up to 30% off (memberships excluded)"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Official post: up to 30% off Station Cash items in the Marketplace, memberships excluded, valid 12:01AM PDT 8/10/2012 to 11:59PM PDT 8/12/2012; 'Hurry, ends 8/12/12!'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2707"},
  {"claim": "Spanish article: 30% off Station Cash items in the Marketplace during August 10 to 12, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2712"},
  {"claim": "Spanish article: 30% off Station Cash items in the Marketplace, three days, 12:01 AM PDT 8/10/2012 to 11:59 PM PDT 8/12/2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2716"},
  {"claim": "In-game UI title 'Weekend Price Cuts' (verified by locale ids check)", "source": "locale:862"},
  {"claim": "In-game banner 'Everything in the Marketplace is 30% off!' (verified by locale ids check)", "source": "locale:863"},
  {"claim": "Video frames show the banner 'Weekend Price Cuts / Everything in the Marketplace is 30% off! / Time Left: 2 Days' (live in client; frame does not show the date)", "source": "video:QPhBoJrHSDI/00040.jpg"},
  {"claim": "Article 2707 posted date 2012-08-10 is inferred from a relative stamp at the 2012-08-17 capture; the year and window come from the offer text", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2707"},
  {"claim": "Not counted as occurrences: members-only weekend sale of 30% off Station Cash, May 25-28, 2012 (summary-dated, not re-read); different audience and window", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2609; http://www.freerealms.com/article/detail.action?articleId=2611"},
  {"claim": "Not counted: President's Day weekend 50% housing sale (Feb 17-20, 2012), TCG booster weekend sales, locale:33802 'Weapon Price Cut' (no link to this event)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2528; http://www.freerealms.com/article/detail.action?articleId=2753"}
 ],
 "confidence": 0.6,
 "open": [
  "Only one occurrence is dated (Aug 10-12, 2012). 'first occurrence' is dropped: no source says it was the first, and earlier sales cannot be ruled out. Recurring is null: the members-only sale (May 25-28, 2012) is a different window and audience, and no article says this event recurs.",
  "articleId=2700 is retrievable (Portuguese): 'A Marketplace weekend sale offered up to 30% off Station Cash items.' Its summary gives no dates, so it is not counted. A direct read is needed to date it; it may be the same or a separate sale. Earlier lookup failure was a query-syntax error on '=' and '%', not a source gap.",
  "The 2707 posted date (2012-08-10) is inferred from a relative stamp, so the exact posting day is not confirmed; the offer window itself is quoted.",
  "Items: no named items are tied to this sale by any source. The sale covers the category 'Station Cash items in the Marketplace'. Price, currency and item fields are left empty.",
  "Zones, NPCs and quests: none sourced for this event.",
  "The pack's merged 'Weekend Sale' label covers several events: the members-only sales (2609, 2611), the President's Day 50% housing sale (2528), TCG booster weekend sales, and the 50% wiki rotators. None are counted here.",
  "Spanish article 2712 and 2716 were checked by fact lines in the articles index, which give the Aug 10-12, 2012 window. The previous lookup returned nothing for 2712 because of a plain-text query; the fact line is now the source.",
  "The members-only sale dates (May 25-28, 2012) are from article summaries and were not re-read.",
  "Locale 862 and 863 are verified by ids check (ui strings): 862 'Weekend Price Cuts' is the in-game title; 863 is the banner text."
 ],
 "confidence_note": "Live: yes, based on the 2012 official posts and the in-game banner. Recurrence not established."}
