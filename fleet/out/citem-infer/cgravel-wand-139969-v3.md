<!-- fleet job=citem-infer id=cgravel-wand-139969-v3 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[21548, 15365, 8, 2305] model=claude-haiku-5-5 -->
# Gravel Wand

{"item": {"name": "Gravel Wand", "locale_id": 139969, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, category 207, NPC and zone not identified (store tags L1, L2, L4, R2, T633, R1 not decoded)", "where": null, "price": "811 coins (member price 729 coins, 10% member discount; sell value 81 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item_id 48219 (line 13268); also FreeRealms-Legacy/src/Resources/CoinStoreItems.json Id 48219, CategoryId 207"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Gravel Wand is a level 5 Wizard Blue Text weapon, power 3, skills Zap (488 dmg) and Lightning Blast (1998 dmg), in Category:Retired Weapons.", "source": "wiki page: Gravel Wand"},
  {"claim": "Wiki says the item 'can only be acquired through trade'. This is player-to-player trade, not a game source.", "source": "wiki page: Gravel Wand"},
  {"claim": "Client name locale:139969 'Gravel Wand'; definition 48219; slot 7; class 10; model wand_ar_ag_weapon_bolt.adr. Gravel siblings are locale 139964-139968.", "source": "locale:139969 and client definition in pack"},
  {"claim": "Store row for item 48219 is in category 207 with purchase 811 coins, member 729 coins (10%), sell 81, no_sale false. Rows 48206-48219 share this 811/729/81 block.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13255-13268"},
  {"claim": "Rows 48220-48241 (and onward) carry 1431/1287/143, not 811. The earlier claim that 48220+ shared the 811 price was wrong.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13269-13290"},
  {"claim": "Wiki tooltip shows Resell Value 81, Power 3, Required Level 5 Wizard.", "source": "wiki image:item_tooltip Gravel Wand item.jpg"},
  {"claim": "The Blue Text weapon wiki page lists Gravel [Wand] with the other Gravel weapons. The retrieved excerpt names no dungeon, enemy or vendor for it.", "source": "wiki page: Blue Text weapon"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor NPC and zone for the 811-coin store row are unidentified. The store tags are not decoded in the repo, so the vendor source is price-only.",
  "Retired vs live conflict: the wiki says retired (Category:Retired Weapons), but the repo store row has no_sale false. The repo data may be a snapshot from before retirement. No retirement date was found, so live status is unsure.",
  "The wiki's only acquisition statement is player trade, which is not a game source.",
  "An earlier draft said Blue Text weapons dropped in dungeons. The retrieved excerpt does not confirm that for Gravel Wand, so no drop source is listed. The full Blue Text weapon page is needed to check it.",
  "No quest reward, enemy drop, event, prize wheel or crafting source for Gravel Wand was found in the pack."
 ]}
