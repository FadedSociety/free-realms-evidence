<!-- fleet job=item-infer id=ibeanie-cap-v3 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[6217, 6689, 6, 1783] model=claude-haiku-5-5 -->
# Beanie Cap

{"item": {"name": "Beanie Cap", "locale_id": 9260, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Cragara, the roaming Mysterious Merchant (sells to everyone; Members get a 10% discount). Partly verified: the wiki names Cragara but the stock list is not shown.", "where": "Mysterious Merchant rotation", "price": "Regular price unverified (candidate 199 Station Cash from a bare unlabelled station_cash value; wiki text prints no figure). Members price unverified (candidate 179 Station Cash, which is about 10% off 199; wiki prints no figure).", "currency": "station_cash", "source": "wiki Beanie_Cap (rev 37256): 'available to everyone for purchase through Cragara at the regular price of , and to Members at the 10% discount price of .' Wiki categories: Mysterious Merchant, Clothing, Head, Freestyle Jobs."},
  {"type": "event", "detail": "Black Friday 2012 login reward: log in on any 2 days between November 23 and 26, 2012", "where": null, "price": null, "currency": null, "source": "wiki Beanie_Cap: 'introduced in-game as a part of Black Friday 2012... acquired by logging in daily for any 2 days within November 23 through 26, 2012'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Beanie Cap' is locale 9260; description 'It's sure to keep your noggin warm.' is locale 9261.", "source": "locale:9260, locale:9261"},
  {"claim": "Wiki says the Beanie Cap is a Freestyle Jobs head-slot clothing item sold through Cragara to everyone, with a Members discount. The wiki text prints no figure for either price.", "source": "wiki Beanie_Cap; lookup of wiki Beanie Cap confirms blank prices"},
  {"claim": "Wiki categories: Clothing, Freestyle Jobs, Head, Mysterious Merchant.", "source": "wiki Beanie_Cap"},
  {"claim": "Black Friday 2012 login event (2 logins between Nov 23 and 26, 2012) gave the Beanie Cap.", "source": "wiki Beanie_Cap"},
  {"claim": "Striped Beanie Cap (locale 436418) is a different item from Mystery Chests and is not this item.", "source": "locale:436418; wiki Mystery Chest"},
  {"claim": "Repo vendors_unresolved.json lists 'Beanie Cap' under Cragara with no price or stock row. It is not vendor-stock evidence.", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:824"}
 ],
 "confidence": 0.4,
 "open": [
  "Regular price 199 Station Cash is unverified. It appears only as a bare value in the station_cash list [199, 179]; the wiki text leaves the price blank. Confirm with a Cragara stock list or second source before wiring.",
  "Members price 179 Station Cash is unverified. The wiki does not print it; it is about 10% off 199, not a stated wiki figure.",
  "Cragara's current stock is unconfirmed. The wiki gives no date and the repo vendor entry has no stock row, so the vendor source is wiki-only.",
  "Black Friday 2012 login event ran Nov 23-26, 2012 and is closed. This closure is inferred from the date window, not from a wiki retirement note, so retired is left null.",
  "Live status is unsure: the Cragara listing may be current or may have rotated out, and the event is closed."
 ]}
