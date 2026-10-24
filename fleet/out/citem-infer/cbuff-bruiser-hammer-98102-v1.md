<!-- fleet job=citem-infer id=cbuff-bruiser-hammer-98102-v1 status=done turns=3 usd=0.0035 tokens(read,write,in,out)=[11158, 15362, 8, 3000] model=claude-haiku-5-5 -->
# Buff Bruiser Hammer

{"item": {"name": "Buff Bruiser Hammer", "locale_id": 98102, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, tint variants item 37541 and 37544 (tint groups 1 and 2)", "where": "Coin store category 207 (repo data; vendor/NPC not identified)", "price": "1656 coins (member price 1490 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12277 (item 37541), line 12278 (item 37544)"},
  {"type": "vendor", "detail": "Coin store sale, tint variant item 37547 (tint group 3)", "where": "Coin store category 207 (repo data; vendor/NPC not identified)", "price": "1431 coins (member price 1287 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12279 (item 37547)"},
  {"type": "other", "detail": "Player-to-player trade only (per the wiki; 'Green Text' weapon class)", "where": null, "price": null, "currency": null, "source": "wiki page Buff Bruiser Hammer; wiki page Green Text weapon (lists it as 'Trade only')"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Buff Bruiser Hammer' is locale 98102, item class 5, slot 7, model hammer_ar_ag_weapon_drill.adr, 10 definitions (variants)", "source": "locale:98102; client definition in pack"},
  {"claim": "Wiki: level 16 Brawler weapon, Green Text weapon, 'can only be acquired through trade'; Glancing Blow 2372 dmg, Leg Sweep 8302 dmg", "source": "wiki page: Buff Bruiser Hammer"},
  {"claim": "Wiki categories list it under Retired Weapons and Green Text Weapons", "source": "wiki page: Buff Bruiser Hammer (Category:Retired Weapons)"},
  {"claim": "Green Text weapon list marks Buff Bruiser Hammer as trade only", "source": "wiki page: Green Text weapon"},
  {"claim": "Coin store entries exist for the hammer's definition IDs 37541, 37544 (1656 coins) and 37547 (1431 coins), category 207, with member discount 10%", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12277-12279"},
  {"claim": "Pack's coin_store_prices [1431, 1656] are prices, not item IDs; matched by item ID to the hammer's definitions above", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12277-12279"},
  {"claim": "Other Buff Bruiser pieces (Pauldrons, Shirt, Boots, Gloves, Helmet, Pants) share the set name, but no link to this hammer's sale was found", "source": "locale:68943, 121008-121012"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: wiki says trade-only and Retired, but stores.json has three coin store entries for this item's definition IDs. Store data may be stale, or the listing may have been a limited-time sale. Need a dated store snapshot or a wiki/forum source for the coin sale period.",
  "Coin vendor location/NPC not identified; stores.json category 207 gives no vendor name. Need the store-to-vendor mapping.",
  "Only 3 of the 10 definition IDs (37541, 37544, 37547) appear in stores.json; 37550-37572 have no coin store entry (37562 in stores.json is not in this item's definition list, so it was not counted).",
  "Pack's critique items were not provided; none to fix.",
  "No wiki image, video, or article source confirms the coin sale or trade-only status beyond the wiki text."
 ]}
