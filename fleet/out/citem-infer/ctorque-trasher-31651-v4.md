<!-- fleet job=citem-infer id=ctorque-trasher-31651-v4 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[6754, 12645, 6, 1995] model=claude-haiku-5-5 -->
# Torque Trasher

{"item": {"name": "Torque Trasher", "locale_id": 31651, "kind": "weapon"},
 "sources": [
  {"type": "marketplace", "detail": "New School Torque Trasher (Brawler, Level 1, Power 5). Sold in the Station Cash Marketplace; members get a 10% discount. Regular price stripped from the wiki text, so unknown.", "where": "Station Cash Marketplace (SC Marketplace)", "price": "unknown (regular price stripped from wiki text; 10% Members discount stated)", "currency": "station_cash", "source": "wiki page 'Torque Trasher' (New School section; categories SC Marketplace, Marketplace Items)"},
  {"type": "marketplace", "detail": "Old School Torque Trasher (Brawler, Level 1). Previously sold in the Station Cash Marketplace; no longer obtainable. Listed here for history only.", "where": "Station Cash Marketplace (retired listing)", "price": "unknown (not in wiki text)", "currency": "station_cash", "source": "wiki page 'Torque Trasher' (Old School section; categories Retired Weapons, Unobtainable Weapons)"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Torque Trasher is two Brawler weapons: a New School version sold through the SC shop, and an Old School version previously sold through the SC Marketplace that can no longer be acquired.", "source": "wiki page 'Torque Trasher'"},
  {"claim": "The Old School version is categorised Retired Weapons and Unobtainable Weapons, so it is retired.", "source": "wiki page 'Torque Trasher' categories"},
  {"claim": "The New School version is acquired from the Station Cash Marketplace; regular price is stripped from the wiki text; Members get a 10% discount.", "source": "wiki page 'Torque Trasher' New School section"},
  {"claim": "Store row item 13659 (category 207, tint group 1) carries a legacy coin cost of 3522 (member 3169) with no price_provenance and no_sale true. Sibling rows in category 207 were reconstructed as Station Cash items (199 or 349 SC) and had the 3522 coin cost cleared. Row 13659 was not reconstructed, so the 3522 is not a live coin vendor price and gives no coin source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:3646 (compared with :3643-3652)"},
  {"claim": "No coin vendor stocks this item in the pack, so no coin_shop or vendor source is listed.", "source": "pack vendor_stock (empty); repo:prototype/osfr-tools/data/content/stores.json:3646"},
  {"claim": "Name locale text: 31651 and 386740 both read 'Torque Trasher'.", "source": "locale:31651; locale:386740"},
  {"claim": "Item tooltip shows resell value 352 and Power 5, Level 1 Brawler.", "source": "image:item_tooltip Torque Trasher"}
 ],
 "confidence": 0.45,
 "open": [
  "New School Station Cash regular price is not in the wiki text (stripped to 'sells at the regular price of , and'). Price is unknown; sibling 199/349 SC values are reconstructions, not evidence for this item, so no price is assigned.",
  "The 3522 coin figure on stores.json row 13659 is a legacy coin cost and is not treated as a coin vendor price.",
  "Retirement date of the New School SC listing is unknown; the wiki does not say whether it is still sold. Live status left 'unsure'.",
  "Mapping of the 12 listed definition ids (of 37 definitions) to the New School and Old School versions and their tints is not verified.",
  "No quest reward, enemy drop, event, prize wheel, or crafting source found in the pack or the wiki search.",
  "Old School Station Cash price is not in the pack; its retired listing is recorded without a price."
 ]}
