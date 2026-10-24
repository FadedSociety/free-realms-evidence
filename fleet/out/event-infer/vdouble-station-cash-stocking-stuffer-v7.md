<!-- fleet job=event-infer id=vdouble-station-cash-stocking-stuffer-v7 status=done turns=3 usd=0.0038 tokens(read,write,in,out)=[16502, 12875, 8, 4052] model=claude-haiku-5-5 -->
# Double Station Cash Stocking Stuffer

{
 "event": {
  "name": "Double Station Cash Stocking Stuffer",
  "aliases": ["Doppel Station Cash (German 2011 headline, per the articles.json summary of article-2474: 'Doppel Station Cash - Ab 24. Dezember'; the page title is 'Free Realms - Quoi de neuf ?'; this is a summary field, not a page read)"]
 },
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Fri 24 Dec 2010 12:00 PDT to Mon 27 Dec 2010 00:00 PDT (year inferred: article 1974 gives no year; the summary says it was captured Dec 2010, and 24 Dec 2010 was a Friday)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
  {"year": 2011, "when": "24 Dec 2011 09:01 CET to 28 Dec 2011 08:59 CET (self-redeemed SOE Pre-Paid Game Cards; body quotes at articles/facts.json 3742, 3758, 3774; not re-read on the live page)", "source": "http://www.freerealms.com/article/detail.action?articleId=2474"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Buy an SOE Pre-Paid Game Card (Station Cash retail card) at a participating retailer (article 1974)",
  "Redeem the card during the promotional window to receive double its value in Station Cash (articles 1974, 2474)"
 ],
 "items": [
  {"name": "SOE Pre-Paid Game Card (Station Cash retail game card)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974; http://www.freerealms.com/article/detail.action?articleId=2474 (sold in Europe, USA, Mexico, Australia, New Zealand per facts.json 3755-3758; the 2474 list is the only region list in the pack)"}
 ],
 "rewards": ["Double Station Cash on the redeemed card's value"],
 "evidence": [
  {"claim": "2010: players with accounts in good standing could redeem pre-paid Station Cash retail game cards bought at participating retailers for DOUBLE their value in Station Cash during the promotion.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
  {"claim": "2010: cards had to be redeemed between Friday, December 24 at 12 p.m. PDT and Monday, December 27 at 12 a.m. PDT. The article gives no year.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
  {"claim": "2011: a German promotion ('Löst eine SOE Pre-Paid Game Card ein und erhaltet doppeltes Station Cash!') gave double Station Cash for redeeming a card between 12/24/11 09:01 and 28.12.2011 08:59 CET.", "source": "http://www.freerealms.com/article/detail.action?articleId=2474 (articles/facts.json 3742, 3771-3774)"},
  {"claim": "The 2474 headline 'Doppel Station Cash - Ab 24. Dezember' is stated in the articles.json summary for article-2474; the page title is 'Free Realms - Quoi de neuf ?' (articles.json line 19733).", "source": "http://www.freerealms.com/article/detail.action?articleId=2474 (articles/articles.json 19733-19738, summary field)"},
  {"claim": "Article 2474 lists SOE Pre-Paid Game Cards sold through retailers in Europe, USA, Mexico, Australia and New Zealand.", "source": "http://www.freerealms.com/article/detail.action?articleId=2474 (articles/facts.json 3755-3758)"},
  {"claim": "The 2010 article (1974) and the 2011 article (2474) describe the same card and bonus mechanic. Neither the pack nor the sources tie them to one recurring event.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974; http://www.freerealms.com/article/detail.action?articleId=2474"}
 ],
 "confidence": 0.4,
 "open": [
  "Year of the 2010 window is inferred. Article 1974 has no year; the Dec 2010 capture and the Friday 24 Dec weekday agree.",
  "Article 2474 has no post date. The summary gives only a relative 'vor 10 Monaten, 1 Woche' at capture (2012-11-03), so the year 2011 rests on the window's dates and the 2474 body, not on a posted date. Body quotes were not re-read on the live page.",
  "Article 2462 ('Verschenkt Doppel Station Cash!') is a separate German gift-purchase promotion, not part of this event. Its summary says buying an SOE Pre-Paid Game Card as a gift gives the recipient double Station Cash on redemption. Its body quote (facts.json 16497, 16517) gives a 24-27 Dec 2011 window, which conflicts with the 2474 window (24 Dec 09:01 to 28 Dec 08:59 CET). Those are two articles, so the windows may not conflict, but the pack does not say. Read article 2462 before deciding whether it belongs in this event or a separate one.",
  "The 2010 article gives no region. The 2011 article lists several regions. Earlier drafts' 'US-only' claim for 2010 has no source and was dropped.",
  "The 'Stocking Stuffer' title comes only from article 1974. Whether the 2011 German promotion is the same event under another name is not proven. The name is kept for 2010 only.",
  "The alias 'Doppel Station Cash' is only a headline in a summary field, not a page title. Treat it as a candidate alias.",
  "The mechanic recurs across many other promotions (articles 1186, 1590, 346, 2790, 2806, 2807, 2893, 2294, 2717, 2144, 2943, 1970, 2455, 2457). None are merged here. A late-December pattern is not shown: 2010 and 2011 are two data points, and the pack has no schedule.",
  "No quests, NPCs, zones, item IDs, or card prices appear in the pack, quest answers, or lookup. Not wireable as a scheduled live event."
 ]
}
