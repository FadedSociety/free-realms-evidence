<!-- fleet job=item-infer id=isplit-saw-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5989, 7363, 6, 2118] model=claude-haiku-5-5 -->
# Split Saw

{"item": {"name": "Split Saw (New School, Medic, Level 1, Power 5)", "locale_id": null, "kind": "weapon"},
 "sources": [
  {"type": "marketplace", "detail": "New School Split Saw, sold on the Station Cash Marketplace at the regular price; the wiki's price sentence is blank in the text, so the 199 figure comes from the station_cash array only", "where": "Station Cash Marketplace (SC Marketplace)", "price": "199 Station Cash (regular, inferred from station_cash array [199,179])", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Split_Saw (rev 47374: text 'The New School version of Split Saw is acquired from the Station Cash Marketplace'; station_cash [199,179]; categories SC Marketplace, SC Marketplace Weapons)"},
  {"type": "membership", "detail": "Members discount price on the New School Split Saw on the SC Marketplace (pairing of 179 to the member price is inferred from the array and the 10% arithmetic, not stated by text)", "where": "Station Cash Marketplace", "price": "179 Station Cash for Members (inferred)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Split_Saw (station_cash [199,179]; text 'to Members at the 10% discount price')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Page covers two Medic weapons named Split Saw: a New School version sold via the SC shop and an Old School version previously sold via the SC shop and no longer obtainable. This answer covers the New School version only.", "source": "https://freerealms.fandom.com/wiki/Split_Saw (wiki_page text)"},
  {"claim": "New School Split Saw tooltip: Power 5, Required Medic, Cannot Sell, Cannot Trade, Precise Strikes and Vital Strike effects match the New School version.", "source": "image:item_tooltip, New School Split Saw item.jpg (wiki)"},
  {"claim": "Wiki 'Items' page lists 'New School Split Saw' with its price blank.", "source": "wiki page:ns0 Items (lookup excerpt)"},
  {"claim": "A video frame shows an advertisement 'Pets Item Of The Day! New School Split Saw Membership $34.99', so the item was also promoted in a membership-priced advertisement; the frame's exact sale mechanics are not confirmed.", "source": "video:BhquFTn5CKo/00020.jpg"},
  {"claim": "Page categories include Retired Weapons and Unobtainable Weapons, but these are page-level tags covering both versions and do not show which one is retired.", "source": "https://freerealms.fandom.com/wiki/Split_Saw (categories)"},
  {"claim": "Tooltip Resell Value 352 is a resale figure, not an acquisition price.", "source": "image:item_tooltip (wiki)"},
  {"claim": "Client name 'Split Saw' appears under locale 31654 and locale 386331; locale 150415 is the description 'This is a Split Saw item.'", "source": "locale:31654, locale:386331, locale:150415"}
 ],
 "confidence": 0.5,
 "open": [
  "Retirement is unresolved: the body says the New School version is currently sold on the SC Marketplace, while page categories say Retired/Unobtainable. No dated source in the pack settles it, so retired is null and live is unsure.",
  "Prices: the wiki price sentence is blank. 199 (regular) and 179 (Members) come from the station_cash array [199,179] with the pairing inferred, and must be checked against a dated SC Marketplace listing.",
  "locale_id is ambiguous: 31654 and 386331 both read 'Split Saw'. No item template id links either to the New School tooltip, so it is left null.",
  "The Old School Split Saw (previously SC Marketplace; Incision 3391 damage, Triage) is not covered. It needs its own evidence if it is the target.",
  "No coin vendor, quest reward, enemy drop, crafting, collection, or prize wheel source is evidenced in the pack for this item. The repo search found no Split Saw references."
 ]}
