<!-- fleet job=item-infer id=ismooth-dress-shoes-v3 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5473, 5798, 6, 1853] model=claude-haiku-5-5 -->
# Smooth Dress Shoes

{"item": {"name": "Smooth Dress Shoes", "locale_id": 151348, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace listing, regular price for everyone; Members get a 10% discount to 44 Station Cash", "where": "SC Marketplace", "price": "49", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Smooth_Dress_Shoes (rev 37167; categories SC Marketplace, SC Marketplace Clothing, Marketplace Items; wiki text 'available to everyone in the SC Marketplace ... to Members at the 10% discount price'). Prices 49 and 44 come from the page's station_cash field [49, 44]; the rendered price text in the export is blank, so the figures are not confirmed in visible text. 44 is the Member sale price (49 x 0.9 = 44.1, rounded)."},
  {"type": "vendor", "detail": "Cragara, the Mysterious Merchant. Stock implied by the item's Category:Mysterious Merchant tag only; the item page does not name Cragara, gives no price, and says nothing about occasional or rotating availability.", "where": "Cragara, the Mysterious Merchant", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Smooth_Dress_Shoes (Category:Mysterious Merchant); wiki ns14 Category:Mysterious Merchant ('Items that are sold by the [Mysterious] [Merchant], [Cragara]')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Smooth Dress Shoes is an All Jobs, feet-slot clothing item sold in the SC Marketplace at 49 Station Cash to everyone, with a Member 10% discount to 44.", "source": "https://freerealms.fandom.com/wiki/Smooth_Dress_Shoes"},
  {"claim": "Item name matches client text table entry 151348 'Smooth Dress Shoes'.", "source": "locale:151348"},
  {"claim": "The page carries Category:Mysterious Merchant, defined as items sold by Cragara, the Mysterious Merchant. This supports a Cragara sale but not a price or stock frequency.", "source": "https://freerealms.fandom.com/wiki/Smooth_Dress_Shoes ; wiki ns14 Category:Mysterious Merchant"},
  {"claim": "Page categories include SC Marketplace, SC Marketplace Clothing, Marketplace Items, Feet, Clothing, All Jobs.", "source": "https://freerealms.fandom.com/wiki/Smooth_Dress_Shoes"}
 ],
 "confidence": 0.6,
 "open": [
  "Cragara vendor source: no price and no stock frequency on the page. Sibling pages (Soccer Ball, Bowling Pin Outfit, Chibi, Frog Face, Scout, Marlin) describe occasional Cragara sales at 49/44, but that cannot be attributed to this item without its own text. Do not treat the Cragara entry as priced or as rotating. A re-check of the rendered page or a Cragara stock capture is needed to confirm the price and whether it is current.",
  "Price 49 / 44 rests on the station_cash field, not visible rendered text. Confirm against the rendered infobox.",
  "Whether the SC Marketplace listing or Cragara stock is still available today is not established. No retirement note was found, so live is unsure and retired is null.",
  "No coin vendor, quest reward, enemy drop, or event evidence in the pack. Lookups of 'Cragara Mysterious Merchant Smooth Dress Shoes' in wiki and client returned no matches, so no further corroboration was found."
 ]}
