<!-- fleet job=citem-infer id=cflying-dragon-sword-98790-v2 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[15190, 12452, 8, 2497] model=claude-haiku-5-5 -->
# Flying Dragon Sword

{"item": {"name": "Flying Dragon Sword", "locale_id": 98790, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin vendor, store category 207 (vendor name not verified in the pack): variant item 38229 (tint group 1) at 2054 coins, member price 1848 coins", "where": null, "price": "2054 coins (member 1848 coins, 10% discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12353 (item_id 38229, category_id 207, purchase_price_coins 2054, sell_price_coins 205)"},
  {"type": "vendor", "detail": "Coin vendor, store category 207: variant item 38232 (tint group 2) at 2054 coins, member price 1848 coins", "where": null, "price": "2054 coins (member 1848 coins, 10% discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12354 (item_id 38232)"},
  {"type": "vendor", "detail": "Coin vendor, store category 207: variant item 38235 (tint group 3) at 1780 coins, member price 1602 coins", "where": null, "price": "1780 coins (member 1602 coins, 10% discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12355 (item_id 38235)"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Flying Dragon Sword' is locale 98790; client cluster neighbour is Voidblade (98788)", "source": "locale:98790; locale:98788"},
  {"claim": "Level 16 Ninja weapon, power 5, Flame Flash (2372 dmg) and Dragonstrike (10674 dmg); Green Text; listed in Category:Retired Weapons; wiki says it can only be acquired through trade", "source": "https://freerealms.fandom.com/wiki/Flying_Dragon_Sword"},
  {"claim": "Wiki tooltip shows Resell Value 205, matching stores.json sell_price_coins 205 for item 38229/38232", "source": "wiki image File:Flying Dragon Sword item.jpg; repo:prototype/osfr-tools/data/content/stores.json lines 12353-12354"},
  {"claim": "Client definitions: 10 variant ids 38229-38259 under the name, power 5, slot 7, class 6; client cost 2054 on 38229/38232/38238/38241 and 1780 on 38235", "source": "repo:prototype/osfr-tools/data/reference/weapons.json lines 18038-18104"},
  {"claim": "Store rows exist for 38229, 38232 (2054 coins) and 38235 (1780 coins), all category 207 with source tags L1, L2, L4, R2, T633, R1; no store row for 38238-38259", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 12353-12355"},
  {"claim": "Prior answer's claim that no stores.json row exists for these ids was wrong; corrected here per critique", "source": "critique (evidence lens) of prior answer; verified against stores.json lines 12353-12355"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: wiki says 'acquired only through trade' and Retired Weapons, but stores.json lists coin purchase prices for 38229/38232/38235 with live-looking source tags. Retirement is undated in all sources, so live is left 'unsure'.",
  "Vendor name for store category 207 was not identified in the repo or client text; the vendor's location is unknown.",
  "Variant 38235 has min_profile_rank 20 in weapons.json, not 16 as the wiki and other variants state; verify before wiring it as a level 16 item.",
  "Variants 38238-38259 have client cost values (2054 / 1780) but no stores.json row, so they are not confirmed as coin vendor sales.",
  "No wiki price for the item; the coin prices come only from the store data. Sell price 205 coins is the sell-to-vendor value, not a purchase price.",
  "Only one model file (sword_ar_ag_weapon_shadowblade.adr) is listed across all variants; tint differences not verified."
 ]}
