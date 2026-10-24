<!-- fleet job=event-infer id=vdouble-station-cash-stocking-stuffer-v5 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[7159, 10382, 6, 2467] model=claude-haiku-5-5 -->
# Double Station Cash Stocking Stuffer

{
 "event": {
  "name": "Double Station Cash Stocking Stuffer",
  "aliases": ["Double Station Cash pre-paid card redemption (holiday)", "Doppel Station Cash (late-December SOE Pre-Paid Game Card promotion, 2011)"]
 },
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "24 Dec 2010 12:00 PDT to 27 Dec 2010 00:00 PDT (year inferred: article gives no year; capture date Dec 2010 and weekday match, Friday 24 Dec)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
  {"year": 2011, "when": "24 Dec 2011 09:01 CET to 28 Dec 2011 08:59 CET (German fine print: cards redeemed between 12/24/11 09:01 Uhr and 28.12.2011 um 8:59 Uhr CET)", "source": "http://www.freerealms.com/article/detail.action?articleId=2474 (window as recorded in articles/facts.json, lines ~3771-3774; not re-read on the live page)"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "buy a pre-paid Station Cash retail game card (SOE Pre-Paid Game Card) at a participating retailer",
  "redeem the card during the promotion window to receive double its value in Station Cash"
 ],
 "items": [
  {"name": "Pre-paid Station Cash retail game card (SOE Pre-Paid Game Card)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974; http://www.freerealms.com/article/detail.action?articleId=2474"}
 ],
 "rewards": ["double Station Cash on the redeemed card's value"],
 "evidence": [
  {"claim": "2010: players with accounts in good standing bought pre-paid Station Cash retail game cards at participating retailers and, during the promotional period, redeemed them for DOUBLE their value in Station Cash.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
  {"claim": "2010: cards had to be redeemed between Friday, December 24 at 12p.m. PDT and Monday, December 27 at 12a.m. PDT. No year in the article; 2010 is inferred.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
  {"claim": "2011: double Station Cash for redeeming SOE Pre-Paid Game Cards, window 24 Dec 2011 09:01 CET to 28 Dec 2011 08:59 CET (headline 'Doppel Station Cash - Ab 24. Dezember').", "source": "http://www.freerealms.com/article/detail.action?articleId=2474"},
  {"claim": "Article 2462 ('Verschenkt Doppel Station Cash!') is a gift-purchase promotion and is NOT part of this event; it belongs to the separate gift-promotion event (vdouble-station-cash-holiday-gift-promotion). Its 27 Dec body date is not used here.", "source": "http://www.freerealms.com/article/detail.action?articleId=2462"},
  {"claim": "Article 2457 (day 8 of 'SOE 12 Days of Holidays') is a different promotion and is not merged.", "source": "http://www.freerealms.com/article/detail.action?articleId=2457"}
 ],
 "confidence": 0.5,
 "open": [
  "Year of the 2010 occurrence is inferred from the capture date and weekday match (article 1974 gives no year).",
  "2011 end date: resolved to 28 Dec 2011 08:59 CET from article 2474's fine print in articles/facts.json. An earlier draft said 27 Dec from article 2462; that was wrong for this event and is dropped. I did not re-read the live 2474 page; the window comes from the extracted facts file.",
  "Merge/alias risk: 2010 is a US (PDT, participating retailers) edition and 2011 a German-language (CET) edition. They share the mechanic and the late-December window, but whether they are one edition is not proven. A critique reports that 2474 names several regions (Europe, USA, Mexico, Australia, New Zealand); I did not verify that list.",
  "The title 'Double Station Cash Stocking Stuffer' comes only from article 1974. No source confirms the 2011 post uses that name.",
  "The card-redemption mechanic recurs in other promotions (articles 2294, 2806, 2807, 2717, 2144, 2943, 1970, 2455, 2457). They are not merged here, so no annual or recurring schedule is claimed.",
  "No quests, NPCs, zones or item ids tied to this event in the pack, quest answers or lookup. No card price in any source.",
  "Article 2893 (SMS exclusion) and article 1186 (Starter Card exclusion) are not tied to these windows and are not attached.",
  "Not wireable as a scheduled live event: it is a dated multiplier promotion on a card with no quests or NPCs, and only two past windows are known (one with an inferred year)."
 ]
}
