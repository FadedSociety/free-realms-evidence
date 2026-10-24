<!-- fleet job=event-infer id=vsummertime-marketplace-sale-v6 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[7295, 9160, 6, 2863] model=claude-haiku-5-5 -->
# Summertime Marketplace Sale

```json
{
 "event": {
  "name": "Summertime Marketplace Sale (working label)",
  "aliases": [
   "Summertime sale (SC Marketplace), article 142 wording 'fabulous deals'",
   "Possible Marketplace sub-promotion of Seaside Summer Splash (2009), unconfirmed"
  ]
 },
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [
  {
   "year": 2009,
   "when": "early July 2009 (exact day not stated in the article; the articles record shows 2009-07-03, inferred from a relative 'Posted 3 days, 23 hours ago' stamp, so do not schedule that day)",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"
  }
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Buying the Uncle Sam Outfit on sale in the SC Marketplace (opened from the SC icon on the in-game dock)"
 ],
 "items": [
  {
   "name": "Uncle Sam Outfit (locale:151336)",
   "price": null,
   "currency": "station_cash",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=142 (fact: 'An Uncle Sam suit was featured on sale in the SC Marketplace'); also articleId=137 ('The Uncle Sam Outfit was added to the Marketplace for the Seaside Summer Splash celebration'); wiki page 'Uncle Sam Outfit' (Station Cash Marketplace, Independence Day). No price in any source."
  },
  {
   "name": "Fireworks Crate (locale:394790)",
   "price": null,
   "currency": null,
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=142 (quote: 'You can place it on the ground and have it deliver exclusive fireworks on demand!'). Single source; not confirmed as this sale's item."
  }
 ],
 "rewards": [],
 "evidence": [
  {
   "claim": "Article 142 (articles record dated 2009-07-03, inferred) announces fabulous deals on the SC Marketplace; the quoted text is 'Some fabulous deals just hit the SC Marketplace!'. The words 'Summertime' and 'Marketplace Sale' appear only in the pack's fact statement and summary, not in the quoted article text.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"
  },
  {
   "claim": "Article 142: an Uncle Sam suit was featured on sale in the SC Marketplace, viewable via the SC icon on the in-game dock; quote 'see how your character would look in an Uncle Sam suit!'",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"
  },
  {
   "claim": "Article 137 says the Uncle Sam Outfit was added to the Marketplace for the Seaside Summer Splash celebration (Splash began 2 July 2009), tying the outfit to that event",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=137"
  },
  {
   "claim": "Summer 2011 return: article 2160 says the Uncle Sam Outfit was available again on the Marketplace for a limited time (jacket, top hat, pants, shoes pieces). Article 2171 says the Uncle-Sam summer items (SC) were removed after 10 August 2011. These are a separate 2011 sighting, not part of the 2009 sale.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160 ; http://www.freerealms.com/article/detail.action?articleId=2171"
  },
  {
   "claim": "Wiki 'Uncle Sam Outfit': an All Jobs clothing bundle in the Station Cash Marketplace during the time of Independence Day",
   "source": "wiki: Uncle Sam Outfit"
  }
 ],
 "confidence": 0.3,
 "open": [
  "Name: 'Summertime Marketplace Sale' is a working label from the pack summary. Article 142 says only 'fabulous deals'. Do not treat the name as an article title.",
  "Date: only 'early July 2009' is supported by article 142. 2009-07-03 comes from a relative timestamp. No exact day is scheduled.",
  "4th of July tie-in: the pack summary attributes it to article 142, but the quoted text does not mention it. The only source for the Independence Day link is the wiki page 'Uncle Sam Outfit'.",
  "Merge question, unresolved: article 137 ties the same outfit to Seaside Summer Splash (began 2 July 2009), and article 142 puts it on sale in the same window. The sale may be a Marketplace sub-promotion of Seaside Summer Splash rather than a separate event. If merged, cite 137 for the outfit and 142 for the sale, and use Seaside Summer Splash's own occurrence (2009, starting 2009-07-02).",
  "Recurrence: the Uncle Sam Outfit was sold in summer 2009 (137/142) and returned in summer 2011 (2160; removed after 10 August 2011, per 2171). Two dated sightings of the item exist, but no source says this sale recurs. Recurring is null. The 2011 return should be a separate occurrence if the item is tracked.",
  "Price: no source gives a price for the Uncle Sam Outfit or the Fireworks Crate in this sale. Store frame video:9NOkMosko1E/00024.jpg shows a Fireworks Crate at 315 station_cash, undated and not tied to this sale, so it is not listed.",
  "Fireworks Crate: single source (article 142), not confirmed as this sale's item. The Highroad Junction Crate of Fireworks ids (locale:115748, 115583, 115590, 115346, 431153, 399473) are a different item and excluded.",
  "Uncle Sam Jacket, Pants, Shoes and Top Hat: excluded from this sale. Article 142 names only the suit, and the piece list comes from the 2011 article 2160.",
  "Quest objective locale:400873 ('summertime reward') is not tied to this sale by any source; excluded. No quest answers mention this event.",
  "Live: unsure. Article 142 reads as a live announcement, but its date is inferred and it has no end date or duration. No end date for the 2009 sale is sourced.",
  "Currency: article 142 says 'SC'; the wiki says Station Cash. Read as station_cash."
 ]
}
```
