<!-- fleet job=event-infer id=vdouble-station-cash-stocking-stuffer-v4 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[15607, 8843, 8, 2285] model=claude-haiku-5-5 -->
# Double Station Cash Stocking Stuffer

{"event": {"name": "Double Station Cash Stocking Stuffer", "aliases": ["Double Station Cash pre-paid card redemption (holiday)", "SOE Pre-Paid Game Card double Station Cash (late December)"]},
"kind": "promotion",
"live": "yes",
"occurrences": [
 {"year": 2010, "when": "24 Dec 12:00 PDT to 27 Dec 00:00 PDT (year inferred, article gives no year; US-style PDT times)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
 {"year": 2011, "when": "from 24 Dec 2011 09:01 CET; end conflicting (27 Dec per body text, 28 Dec 08:59 CET per fine print)", "source": "http://www.freerealms.com/article/detail.action?articleId=2474"}
],
"recurring": null,
"zones": [],
"npcs": [],
"quests": [],
"activities": ["buy a pre-paid Station Cash retail game card at a participating retailer", "redeem the card during the promotion window for double its value in Station Cash"],
"items": [{"name": "Pre-paid Station Cash retail game card (SOE Pre-Paid Game Card)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"}],
"rewards": ["double Station Cash on redeemed card value"],
"evidence": [
 {"claim": "2010: players with accounts in good standing bought pre-paid Station Cash retail game cards at participating retailers and redeemed them in the promotional period for DOUBLE their value in Station Cash.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
 {"claim": "2010: cards had to be redeemed between Friday December 24 12p.m. PDT and Monday December 27 12a.m. PDT. The article gives no year; 2010 is inferred from the Dec 2010 capture and the weekday match.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1974"},
 {"claim": "2011: German news item headlined 'Doppel Station Cash - Ab 24. Dezember' announces double Station Cash for redeeming SOE Pre-Paid Game Cards in a late-December window starting 24 Dec 2011 (09:01 CET per the pack's reading of fine print; not independently re-read in full here).", "source": "http://www.freerealms.com/article/detail.action?articleId=2474"},
 {"claim": "Article 2462 ('Verschenkt Doppel Station Cash!') is a gift-purchase promotion (card bought as a gift, recipient gets double), so it is NOT attached to this event; it belongs to the separate gift-promotion event.", "source": "http://www.freerealms.com/article/detail.action?articleId=2462"},
 {"claim": "Article 2457 (day 8 of 'SOE 12 Days of Holidays', double Station Cash to 21 Dec 08:59 CET) is a different promotion and is not merged.", "source": "http://www.freerealms.com/article/detail.action?articleId=2457"}
],
"confidence": 0.4,
"open": [
 "Merge risk: the 2010 entry is a US promotion (PDT, participating retailers) and the 2011 entry is a German/European promotion (CET). Treat them as region-separate editions under one family name, not proven as one event.",
 "2011 end date is unresolved: article 2462 body says 27 Dec, its fine print says 28 Dec 08:59 CET. Article 2474's full window text was not confirmed here (only headline and summary were seen). Do not schedule an end date until 2474 is read in full.",
 "2010 year is inferred from the capture date and weekday match, not stated in article 1974.",
 "Recurrence not established: two occurrences, one with an inferred year, in different regions. The card-redemption mechanic also recurs in other promotions (articles 2294, 2806, 2807, 2717, 2144, 2943, 1970, 2455, 2457), which are not merged, so no 'annual' schedule is claimed.",
 "No quests, NPCs, zones or item ids tied to this event in the pack, quest answers or lookup. No card price in any source.",
 "Article 2893 (SMS exclusion) and article 1186 (Starter Card exclusion) are not tied to these windows and are not attached.",
 "Pack title 'Double Station Cash Stocking Stuffer' comes only from article 1974; no source confirms the 2011 posts use that name.",
 "wireable: false. Timing is only partly known and the content is a multiplier on a card with no quests or NPCs, so it is a dated record rather than a scheduled live event."
]}
