<!-- fleet job=citem-infer id=csunlit-axe-139956-v1 status=done turns=4 usd=0.0024 tokens(read,write,in,out)=[17049, 9020, 10, 2290] model=claude-haiku-5-5 -->
# Sunlit Axe

{"item": {"name": "Sunlit Axe", "locale_id": 139956, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store listing (store item 48206, category 207); vendor NPC not identified in the store data", "where": null, "price": "811 coins (member price 729 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48206 (line 13255); definition 48206 at prototype/osfr-tools/data/reference/weapons.json:44025"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki; the wiki says it cannot be bought or earned otherwise. Conflicts with the coin store listing above", "where": null, "price": null, "currency": null, "source": "wiki page Sunlit Axe; wiki page Blue Text weapon (Blue Text weapons were members-only dungeon drops before retirement)"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client name 'Sunlit Axe' is locale 139956, item definition 48206, slot 7, class 17, model axe_ar_ag_weapon_battleaxe.adr", "source": "locale:139956; client definition"},
  {"claim": "Sunlit Axe is a level 5 Warrior weapon, Blue Text, 'can only be acquired through trade'; Sweeping Slash 853 damage, Spinning Attack 1548 damage", "source": "wiki page Sunlit Axe"},
  {"claim": "Sunlit Axe is in Category:Retired Weapons", "source": "wiki page Sunlit Axe (categories)"},
  {"claim": "Blue Text weapons were members-only weapons dropped in dungeons, before being retired", "source": "wiki page Blue Text weapon"},
  {"claim": "Store listing for item 48206: purchase 811 coins, member 729 coins, sell-back 81 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48206"},
  {"claim": "Sunlit family siblings (Sunlit Bow, Blade, Wand, Scalpel, Kendama Hammer) are all described the same way on the wiki: Blue Text, level 5, acquired through trade", "source": "wiki pages Sunlit Bow, Sunlit Blade, Sunlit Wand, Sunlit Scalpel, Sunlit Kendama Hammer"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the wiki says trade-only and retired, but the store data lists item 48206 at 811 coins. Unclear whether this is a live coin vendor sale or a stale or non-sale record. Not confirmed by any vendor page or screenshot.",
  "Vendor, NPC, and zone for the coin listing are unknown. Store category 207 was not resolved to a shop name.",
  "Retirement date and the date the coin listing stopped are not in the pack.",
  "Wiki price for the sale is not given; only the store-data coin price is known.",
  "No video frames or articles name this item."
 ]}
