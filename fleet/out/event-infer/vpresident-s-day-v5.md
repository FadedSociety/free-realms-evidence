<!-- fleet job=event-infer id=vpresident-s-day-v5 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[16137, 9445, 8, 2883] model=claude-haiku-5-5 -->
# President's Day event

```json
{"event": {"name": "President's Day weekend sale", "aliases": ["Presidents' Day weekend sale", "Presidents' Day weekend promotion", "Shop the President's Day Sale (article 2528 title)"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Presidents' Day weekend: 18 Feb 2011 (21:00 CET = 12:00 PST) to 21 Feb 2011 23:59 PST (08:59 CET 22 Feb)", "source": "http://www.freerealms.com/article/detail.action?articleId=2043&request_locale=en_US (start/end times, 'ran from 21:00 CET on 18 February 2011 until 08:59 CET on 22 February 2011'); http://www.freerealms.com/article/detail.action?articleId=2039 and articleId=2040 (18-21 Feb window, 23:59 PST end, per pack)"},
  {"year": 2012, "when": "Presidents' Day weekend: 12:01am PST 17 Feb 2012 to 11:59pm PST 20 Feb 2012", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2528 (summary and fact: 'valid 12:01am PST 2/17/12 to 11:59pm PST 2/20/12'); locale:615 (in-game banner, flagged not_live, corroboration only)"}
 ],
 "recurring": "Two occurrences observed (2011, 2012), both on Presidents' Day weekend in February. Yearly is an inference from these two years only; no 2013+ or other-year evidence was found.",
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Buy Station Cash housing items and land lots at 50% off during the sale window (2011 and 2012)",
  "Buy TCG booster packs and starter decks (Sets 1-3) at sale prices from the Marketplace (2012)"
 ],
 "items": [
  {"name": "TCG booster packs, Sets 1, 2, 3", "price": "200 SC each (sale)", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2528; locale:615 (corroboration)"},
  {"name": "TCG starter decks, Sets 1, 2, 3", "price": "450 SC each (sale)", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2528; locale:615 (corroboration)"},
  {"name": "Station Cash housing items and land lots", "price": "50% off (individual SC prices not confirmed)", "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=2043&request_locale=en_US (2011: 'all housing and land items sold for Station Cash were discounted 50%'); http://www.freerealms.com:80/article/detail.action?articleId=2528 (2012: houses and lots 50% off on Marketplace)"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "2011 Free Realms President's Day weekend sale ran 21:00 CET 18 Feb to 08:59 CET 22 Feb 2011 (= noon PST 18 Feb to 23:59 PST 21 Feb).", "source": "http://www.freerealms.com/article/detail.action?articleId=2043&request_locale=en_US"},
  {"claim": "2011 sale: all housing and land items sold for Station Cash were 50% off.", "source": "http://www.freerealms.com/article/detail.action?articleId=2043&request_locale=en_US"},
  {"claim": "2011 window 18-21 Feb with 50% off Station Cash housing and lots (English and Spanish posts), used for the 2011 end time.", "source": "http://www.freerealms.com/article/detail.action?articleId=2039 ; http://www.freerealms.com/article/detail.action?articleId=2040"},
  {"claim": "2012 President's Day weekend sale valid 12:01am PST 2/17/12 to 11:59pm PST 2/20/12; houses and lots 50% off on the Marketplace; discounted TCG booster packs and starter decks from Sets 1-3.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2528"},
  {"claim": "TCG Sets 1-3 sale prices: booster packs 200 SC, starter decks 450 SC; same offer and window in in-game banner text.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2528 ; locale:615"}
 ],
 "confidence": 0.7,
 "open": [
  "Merge risk: the SOE-wide President's Day promotion (articles 2033, 2042; 2042 gives an 18-21 Feb 2011 window across several SOE games) is a different record and is not used as evidence here. 2033's heading does not match its body and it is pre-launch wording; not used for dates.",
  "Article dates are null in the pack. Years come from article text (2011 in 2043/2039/2040; 2012 in 2528 summary, captured 2012-02-19).",
  "2039 and 2040 were cited by the pack but their text was not re-read in this pass; the 2011 start/end times are confirmed from 2043 instead.",
  "locale:614 and locale:1417 ('President's Day Sale!') are name-only banners flagged not_live with no sale window or scope. Not used as evidence or as an alias.",
  "2011 item list not found: 2011 items beyond the Station Cash housing/lot discount are unknown. Individual housing and lot SC prices are not confirmed. Island land plots and Briarwood lots are not confirmed as sale scope (2043 says 'housing and land items', not itemised).",
  "Yearly recurrence is an inference from two years only.",
  "Time-zone conversions (CET to PST) are calculations.",
  "No wiki category members, NPCs, zones, quests or quest answers were found for this event; category 'President's Day' is empty."
 ],
 "confidence_note": "0.7",
 "id_check": ["locale:614, locale:1417 flagged not_live; not cited as evidence", "locale:615 flagged not_live; cited only as corroboration of article 2528"]
}
```
