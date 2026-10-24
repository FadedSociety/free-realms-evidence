<!-- fleet job=event-infer id=vsummertime-marketplace-sale-v8 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6787, 8627, 6, 2127] model=claude-haiku-5-5 -->
# Summertime Marketplace Sale

```json
{
 "event": {
  "name": "Summertime Marketplace Sale (SC Marketplace sale, 2009)",
  "aliases": ["Summertime Marketplace Sale (pack label, not a source title)"]
 },
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [
  {"year": 2009, "when": "early July 2009; start and end days not stated in the article", "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buying the sale items on the SC Marketplace (opened from the SC icon on the in-game dock)"],
 "items": [
  {"name": "Uncle Sam suit (Uncle Sam Outfit, per the pack's summary; the article says only 'an Uncle Sam suit')", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Article 142 announces that 'Some fabulous deals just hit the SC Marketplace!' (a store sale; no prices, no end date)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"},
  {"claim": "The 2009-07-03 date is inferred from a relative 'Posted 3 days, 23 hours ago' stamp in the capture, not stated by the article; the year 2009 and 'early July' are the only sourced timing", "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"},
  {"claim": "The Uncle Sam Outfit was added to the Marketplace for the Seaside Summer Splash celebration. That is a separate event: Summer Splash began July 2, 2009", "source": "http://www.freerealms.com:80/article/detail.action?articleId=137"},
  {"claim": "The Uncle Sam Outfit is a Marketplace clothing bundle, listed as available in the Station Cash Marketplace during Independence Day (wiki only; not tied to article 142's text)", "source": "wiki: Uncle Sam Outfit"}
 ],
 "confidence": 0.3,
 "open": [
  "Name: 'Summertime Marketplace Sale' does not appear in article 142. The article's only text is 'Some fabulous deals just hit the SC Marketplace!'. The name is a pack label. Use the article title 'Free Realms - What is New?' as the source name.",
  "Not merged with Seaside Summer Splash. Article 137 ties the Uncle Sam Outfit to Summer Splash, and article 142 does not mention Summer Splash, Seaside, or a Summer Splash window. Summer Splash (began 2009-07-02, per articleId=137) is a separate event and is not given here. The shared item does not establish one event.",
  "Start and end dates: only 'early July 2009' is sourced. No end date. No day is scheduled.",
  "Uncle Sam Outfit currency: the wiki calls it a Station Cash Marketplace item, but article 142 says only 'SC' with no expansion, and the pack's gloss 'Subscriber Currency' is unsourced. Currency left null.",
  "Fireworks Crate: the pack's summary says article 142 offered one, but the article quote does not name it. Left out of items.",
  "Uncle Sam Jacket, Top Hat, Pants and Shoes come from 2011 articles (2160, 2146, 2171) and are not part of this 2009 sale.",
  "Live status is 'unsure': a single undated-day article shows the sale existed in early July 2009. No article confirms it ran as a live event beyond the announcement.",
  "No quests, NPCs, zones or prices are sourced for this sale."
 ]
}
```
