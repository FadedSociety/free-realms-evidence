<!-- fleet job=item-infer id=ihearts-parachute-v2 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[5233, 5965, 6, 1549] model=claude-haiku-5-5 -->
# Hearts Parachute

{"item": {"name": "Hearts Parachute", "locale_id": 9931, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace listing, sold to all players at 1249 Station Cash; Members got a 10% discount price of 1124 Station Cash (the wiki text gives the Members discount in words; the numbers are from the wiki station_cash field, and the mapping of 1249 to standard and 1124 to Members is inferred from field order, not stated in the text)", "where": "SC Marketplace", "price": "1249 standard; 1124 Members (10% off)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Hearts_Parachute (rev 45707; categories SC Marketplace, SC Marketplace Clothing; page text 'available to everyone at the price of ... and to Members at the 10% discount price of ...')"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Hearts Parachute is a parachute that was no longer available for purchase; while in the SC Marketplace it was sold to everyone and to Members at a 10% discount.", "source": "https://freerealms.fandom.com/wiki/Hearts_Parachute"},
  {"claim": "Wiki categories: SC Marketplace, SC Marketplace Clothing, Marketplace Items, Clothing, Parachutes, All Jobs, Misc.", "source": "https://freerealms.fandom.com/wiki/Hearts_Parachute"},
  {"claim": "Client item name 'Hearts Parachute' is locale 9931; locale 9932 is its description ('Perfect for parachute lovers.').", "source": "locale:9931"},
  {"claim": "Locales 9939 and 9940 are not_live 'COMING SOON' / 'not yet available for purchase' strings for the same item, so the item existed in the client before release.", "source": "locale:9939"},
  {"claim": "Station Cash prices 1249 and 1124 appear only in the wiki station_cash field; the page text strips the currency amounts. Ratio 1124/1249 is about 0.9, consistent with a 10% Members discount.", "source": "https://freerealms.fandom.com/wiki/Hearts_Parachute"}
 ],
 "confidence": 0.7,
 "open": [
  "Price figures are unconfirmed: the wiki text strips them and no second source (article, forum, or other page) gives 1249 or 1124. Confirm before loading.",
  "Retirement date unknown; the wiki gives no date for when the parachute left the SC Marketplace.",
  "Possible Festival of Hearts link: wiki Template:News (Game Update 128, 02/04/2014) mentions Station Cash content and a Festival of Hearts event, but does not name Hearts Parachute. Not used as a source; check the full update text for the item.",
  "No vendor, quest, drop, crafting, collection, prize wheel, or promotion source found in the pack. Only the SC Marketplace listing is sourced.",
  "No images or article facts were in the pack, so the item was not cross-checked against the official site or forum."
 ]}
