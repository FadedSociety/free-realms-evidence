<!-- fleet job=item-infer id=icyborg-eye-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[2919, 4371, 6, 2149] model=claude-haiku-5-5 -->
# Cyborg Eye

{"item": {"name": "Cyborg Eye", "locale_id": 42250, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, All Jobs head-slot clothing, open to everyone", "where": "Station Cash Marketplace", "price": "349 Station Cash (regular price); 314 Station Cash for Members (10% member discount)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Cyborg_Eye ; wiki category SC Marketplace / SC Marketplace Clothing"},
  {"type": "vendor", "detail": "Cragara, the Mysterious Merchant (category listing only; the page does not state a separate price for this vendor)", "where": "Mysterious Merchant (Cragara)", "price": null, "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Cyborg_Eye ; wiki category 'Mysterious Merchant' (Category:Mysterious Merchant: 'Items that are sold by the Mysterious Merchant, Cragara.', tagged Station Cash)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Cyborg Eye is an All Jobs, head slot clothing item sold through the Station Cash Marketplace at the regular price of 349 Station Cash, and 314 Station Cash for Members at a 10% discount (the second price is the member discount, not a sale).", "source": "https://freerealms.fandom.com/wiki/Cyborg_Eye (rev 36890; station_cash values 349, 314)"},
  {"claim": "Item is in the Mysterious Merchant category, whose members are items sold by Cragara, the Mysterious Merchant.", "source": "wiki Category:Mysterious Merchant (lookup result)"},
  {"claim": "Client name string for the item is Cyborg Eye.", "source": "locale:42250"},
  {"claim": "Client description locale:150504 ('This is a Cyborg Eye item.') is a placeholder generic text and is not used as evidence for the description.", "source": "locale:150504 (FLAG placeholder)"},
  {"claim": "The wiki igd description is 'The future is here, and you got some in your eye!'", "source": "https://freerealms.fandom.com/wiki/Cyborg_Eye (igd field)"}
 ],
 "confidence": 0.7,
 "open": [
  "The Mysterious Merchant (Cragara) source rests only on the category tag; the page gives no price or rotation dates for that vendor, so the price for it is unknown.",
  "No retirement or end date is given on the page, so live status is unconfirmed; the Marketplace listing may be current or may have rotated out.",
  "No repo or coin-vendor evidence was checked for this item; the pack had no vendor_stock or drop data.",
  "The wiki_page text in the pack had its price numbers blanked; prices were taken from the station_cash field (349 and 314). The 314 is consistent with 349 less 10%."
 ]}
