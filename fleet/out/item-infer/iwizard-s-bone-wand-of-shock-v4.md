<!-- fleet job=item-infer id=iwizard-s-bone-wand-of-shock-v4 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[15475, 9037, 8, 2681] model=claude-haiku-5-5 -->
# Wizard's Bone Wand of Shock

{"item": {"name": "Wizard's Bone Wand of Shock", "locale_id": 132040, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Glenda (human NPC merchant), listed in the wiki Glenda page's wand list (the page names this wand among Glenda's stock). Price is a stores.json reference, not a captured NPC quote", "where": "Stillwater Crossing (near the warpstone)", "price": "reference 1055 coins purchase (stores.json item 75156); reference member 949; reference sell 527. Not confirmed as Glenda's live price", "currency": "coins", "source": "wiki page Glenda (rev 2025-03-21, 'Sells' section, per repo:prototype/osfr-tools/data/content/vendors.json:37561-37586); location from quest-lines/npc-packs.json:70936; price from repo:prototype/osfr-tools/data/content/stores.json:15167"},
  {"type": "coin_shop", "detail": "Coin Shop, Wizard level 8 weapon. Wiki category 'Coin Shop' and 'Coin Shop Weapons' only; the captured sentence reads 'sells for' with the price blank. No shop name or NPC is given. The 1055 figure is the same stores.json reference as the Glenda row, not a separate shop quote", "where": "Coin Shop", "price": null, "currency": "coins", "source": "wiki page Wizard's Bone Wand of Shock (categories 'Coin Shop', 'Coin Shop Weapons'; text 'acquired from the Coin Shop where it sells for  and')"},
  {"type": "prize_wheel", "detail": "Wizard Prize Wheel at Forgotten Caves, Mushroom Cavern and Return to Sender!. Wiki dungeon pages list the wand in the wheel reward list. Wiki dungeon pages also list it in the Battle Item Mystery Pack reward list at the same dungeons, so the container or wheel path is unresolved. Odds unknown", "where": "Forgotten Caves; Mushroom Cavern; Return to Sender!", "price": null, "currency": null, "source": "wiki page Wizard's Bone Wand of Shock ('acquired from the prize wheels at Forgotten Caves, Mushroom Cavern, and Return to Sender!', category 'Prize Wheel Weapons'); wiki pages Forgotten Caves, Mushroom Cavern, Return to Sender! (reward lists 'Wizard Prize Wheel' and 'Battle Item Mystery Pack' both include Wizard's Bone Wand of Shock); repo dungeon target_name rows forgotten_caves.json:2875, mushroom_cavern.json:2437, return_to_sender.json:2261"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name is client text locale 132040 'Wizard's Bone Wand of Shock'", "source": "locale:132040"},
  {"claim": "Level 8 Wizard weapon, Power 3, Zap 853 damage, Lightning Blast 3841 damage; Resell Value 105 is not a purchase price", "source": "wiki page Wizard's Bone Wand of Shock; image:item_tooltip"},
  {"claim": "Wiki says the wand is acquired from the Coin Shop, with the price blank in the captured sentence; categories Coin Shop and Coin Shop Weapons", "source": "wiki page Wizard's Bone Wand of Shock"},
  {"claim": "Wiki says the wand is acquired from prize wheels at Forgotten Caves, Mushroom Cavern and Return to Sender!", "source": "wiki page Wizard's Bone Wand of Shock"},
  {"claim": "Wiki dungeon reward lists for Forgotten Caves, Mushroom Cavern and Return to Sender! include the wand under both Wizard Prize Wheel and Battle Item Mystery Pack", "source": "wiki pages Forgotten Caves, Mushroom Cavern, Return to Sender!"},
  {"claim": "Wiki Glenda page lists the wand in her stock list", "source": "wiki page Glenda; repo:prototype/osfr-tools/data/content/vendors.json:37561-37586"},
  {"claim": "1055 purchase, 949 member, 527 sell are stores.json reference prices, not captured NPC quotes", "source": "repo:prototype/osfr-tools/data/content/stores.json:15167; vendors.json:37571 and 37597-37600"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin Shop price is unknown. The wiki sentence price is blank in the captured text. The 1055 figure is a stores.json reference and may be the Glenda price, not a shop price. No sale price is known.",
  "Glenda price 1055 coins is reference-only (stores.json item 75156), not a captured NPC quote. Glenda's live price and stock status are unconfirmed.",
  "Prize wheel vs Battle Item Mystery Pack: wiki dungeon pages list the wand under both. Which one actually grants it, and the wheel odds, are unknown.",
  "Station Cash, IGD and Marketplace: the page has a 'Marketplace Items' category, but no Station Cash or IGD price is evidenced.",
  "Retirement is not stated in any source, and no current vendor table confirms availability. Live status is unsure."
 ]
}
