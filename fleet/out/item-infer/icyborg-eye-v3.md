<!-- fleet job=item-infer id=icyborg-eye-v3 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[5420, 5850, 6, 1315] model=claude-haiku-5-5 -->
# Cyborg Eye

{"item": {"name": "Cyborg Eye", "locale_id": 42250, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, All Jobs head-slot clothing, open to everyone", "where": "Station Cash Marketplace", "price": "349 Station Cash (regular price); 314 Station Cash for Members (10% member discount, not a sale)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Cyborg_Eye (rev 36890, station_cash field 349 and 314; categories SC Marketplace / SC Marketplace Clothing). The price text is blank in the fetched page, so the figures rest on the station_cash field."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Cyborg Eye is an All Jobs, head slot clothing item sold through the Station Cash Marketplace, available to everyone; Members get a 10% discount price.", "source": "https://freerealms.fandom.com/wiki/Cyborg_Eye (page text confirmed by lookup; the price figures are blank in the text)"},
  {"claim": "Client name string for the item is Cyborg Eye.", "source": "locale:42250"},
  {"claim": "The wiki igd description is 'The future is here, and you got some in your eye!'", "source": "https://freerealms.fandom.com/wiki/Cyborg_Eye (igd field)"},
  {"claim": "The page is in Category:Mysterious Merchant, but no vendor is named on the page and no stock row, price or date ties this item to Cragara.", "source": "Category:Mysterious Merchant on https://freerealms.fandom.com/wiki/Cyborg_Eye"}
 ],
 "confidence": 0.6,
 "open": [
  "Mysterious Merchant: category membership only. The vendor (Cragara) is inferred from sibling pages (Chibi, Frog Face), not from this item's page, and no price or availability window is evidenced, so it is not listed as a source.",
  "The 349 and 314 Station Cash prices come from the station_cash field; the page text is blank, and 314 = 349 less 10%. Re-verify on the live wiki page.",
  "No retirement or end date is stated, so live status is unconfirmed; the Marketplace listing may have rotated out.",
  "locale:150504 ('This is a Cyborg Eye item.') is a flagged placeholder and is not used as evidence.",
  "No repo, coin-vendor, drop, or quest data was checked; none was in the pack."
 ]}
