<!-- fleet job=item-infer id=ibrawler-s-hammer-of-rumbling-v3 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[7404, 8980, 6, 2851] model=claude-haiku-5-5 -->
# Brawler's Hammer of Rumbling

{"item": {"name": "Brawler's Hammer of Rumbling", "locale_id": 131917, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale of the level 4 Brawler weapon (Power 2). Wiki says it is acquired from the Coin Shop 'where it sells for 850 coins'. The rendered page blanks the price; the price is in the raw wikitext.", "where": "Coin Shop", "price": "850 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (wikitext rev 47110, line 3: 'acquired from the [[Coin Shop]] where it sells for {{Coin|850}}'; category Coin Shop Weapons)"},
  {"type": "vendor", "detail": "Lingan, Sells section (Brawler job vendor). Stock only: the wiki Lingan page lists the hammer for sale. The pack has no captured NPC price; the 850 coin figure is a stores.json reference price, not a quote.", "where": "Seaside (near the Seaside warpstone)", "price": "unconfirmed (stores.json reference 850 coins; not a live quote)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Lingan (Sells section, rev 2025-08-04); repo:prototype/osfr-tools/data/content/vendors.json:26654-26696 (stock_source; price_basis '(R) stores.json reference price; no captured retail NPC quote')"},
  {"type": "prize_wheel", "detail": "Prize wheel at Danger Peaks", "where": "Danger Peaks", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (wikitext rev 47110, line 3)"},
  {"type": "prize_wheel", "detail": "Prize wheel at Ice Troll Scout!", "where": "Ice Troll Scout!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (wikitext rev 47110, line 3)"},
  {"type": "prize_wheel", "detail": "Prize wheel at Pixie Hunters!", "where": "Pixie Hunters!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (wikitext rev 47110, line 3)"},
  {"type": "prize_wheel", "detail": "Prize wheel at Sweetwater Climb", "where": "Sweetwater Climb", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (wikitext rev 47110, line 3)"},
  {"type": "prize_wheel", "detail": "Prize wheel at Thugawug Sneak!", "where": "Thugawug Sneak!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (wikitext rev 47110, line 3)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Level 4 Brawler weapon, Power 2, requires Level 4 Brawler; effects Wallop (488 damage) and Ready to Rumble (1118 damage)", "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (item tooltip image; categories Level 4 Weapons, Power 2 Weapons)"},
  {"claim": "Wiki sells it in the Coin Shop for 850 coins and lists five prize-wheel locations", "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (wikitext rev 47110, line 3)"},
  {"claim": "Name text is locale 131917 'Brawler's Hammer of Rumbling'", "source": "locale:131917"},
  {"claim": "The Lingan Sells section lists this hammer (item_id 75033)", "source": "https://freerealms.fandom.com/wiki/Lingan (Sells, rev 2025-08-04); repo:prototype/osfr-tools/data/content/vendors.json:26654-26696"},
  {"claim": "The Lingan price 850 and member price 765 and sell price 425 are stores.json reference values, not captured NPC quotes", "source": "repo:prototype/osfr-tools/data/content/vendors.json:26664, 26693"},
  {"claim": "Wiki category 'Marketplace Items' exists, but no Station Cash price is shown on the page", "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Rumbling (categories)"}
 ],
 "confidence": 0.6,
 "open": [
  "The Coin Shop 850 and the Lingan 850 are probably the same price figure seen twice (the Lingan figure is a stores.json reference). Keep the Coin Shop entry as the wiki-stated price; treat the Lingan entry as stock only until a captured NPC price is found.",
  "The member price 765 has no wiki or NPC source in the pack. It is dropped from the sources, and the membership condition is undocumented.",
  "Resell value conflicts: wiki tooltip says 85; vendors.json (stores.json reference) says 425. Unresolved; neither should be used as a live sell price.",
  "Prize-wheel sources have no per-spin price, wheel tier, or drop rate in the pack.",
  "The enemies.json:20373 citation from the prior answer was not verified and is not used as evidence.",
  "No Station Cash or marketplace price is documented; 'Marketplace Items' is a category only.",
  "No retirement date or current-live check in the pack; live status is unsure.",
  "'Ready to Rumble' is a skill name, not a source."
 ]}
