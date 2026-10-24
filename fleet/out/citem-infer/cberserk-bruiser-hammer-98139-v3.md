<!-- fleet job=citem-infer id=cberserk-bruiser-hammer-98139-v3 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[6665, 15314, 6, 2186] model=claude-haiku-5-5 -->
# Berserk Bruiser Hammer

{"item": {"name": "Berserk Bruiser Hammer", "locale_id": 98139, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store row for item 37578 (category 207, unresolved vendor). Generic category-207 row shared with about 40 other gear rows; no named vendor. Treat as an unresolved coin-store sale, not a confirmed vendor.", "where": null, "price": "2054 coins (member price 1848 coins, 10% member discount); sell price 205 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12281 (item_id 37578, purchase_price_coins 2054, member_price_coins 1848, sell_price_coins 205, no_sale false)"},
  {"type": "other", "detail": "Wiki claim: 'can only be acquired through trade' (player-to-player). Conflicts with the store row; recorded as a conflicting claim, not a second confirmed source.", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Berserk_Bruiser_Hammer"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Berserk Bruiser Hammer' is locale:98139; 10 definitions (37578, 37581, 37584, 37587, 37590, 37593, 37597, 37600, 37604, 37608), slot 7, class 5, model hammer_ar_ag_weapon_crystal.adr", "source": "locale:98139"},
  {"claim": "Store row for 37578 exists: purchase 2054, member 1848, sell 205, no_sale false, category 207. Verified by reading the row.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12281"},
  {"claim": "Tooltip 'Coin: 205' equals the store row's sell_price_coins, so 205 is a resell value, not a purchase price.", "source": "image:item_tooltip; repo:prototype/osfr-tools/data/content/stores.json:12281"},
  {"claim": "Wiki: level 16 Brawler weapon, Green Text, 'can only be acquired through trade'; Glancing Blow 2372 dmg, Leg Sweep 8302 dmg", "source": "https://freerealms.fandom.com/wiki/Berserk_Bruiser_Hammer"},
  {"claim": "Wiki page is in Category:Retired Weapons", "source": "https://freerealms.fandom.com/wiki/Berserk_Bruiser_Hammer"},
  {"claim": "Tooltip shows Required Level 20 while the wiki says level 16; the wiki's Brawler page lists the hammer under Level 16 and the Level 20 hammers are separate entries.", "source": "image:item_tooltip; wiki page Brawler"},
  {"claim": "Other definition ids (37581-37608) are listed in weapons.json at lines 4850-4906 but have no stores.json row found by search.", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:4850-4906; search of stores.json"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor for the 37578 store row is unresolved: category 207 is a generic gear category, and vendors.json has no entry for 37578. Do not name a vendor until one is mapped.",
  "Conflict: the wiki says trade-only, but a store row with no_sale false exists. Unresolved which is current.",
  "Live status unsure. Retired per wiki category; no retirement date found; store row not marked no-sale.",
  "Level conflict: wiki 16 vs tooltip 20. Unresolved.",
  "Variant 37584 'cost 1780 / rank 20' from weapons.json was not verified against any store row; no stores.json row found for the other nine definition ids. Per-variant prices remain unverified.",
  "No quest, drop, event, collection, or prize-wheel evidence found."
 ]}
