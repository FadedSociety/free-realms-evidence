<!-- fleet job=citem-infer id=ccourageous-defender-axe-98991-v1 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[13149, 14225, 8, 2275] model=claude-haiku-5-5 -->
# Courageous Defender Axe

{"item": {"name": "Courageous Defender Axe", "locale_id": 98991, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store weapon listing (category 207), tint variants: item 38430 (tint group 1) and 38433 (tint group 2) at 866 coins, item 38436 (tint group 3) at 760 coins; the vendor NPC is not named in the store data", "where": null, "price": "866 coins (tint groups 1-2); 760 coins (tint group 3); member price 779 / 684 coins with 10% member discount", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 38430, 38433, 38436 (lines 12360-12362); client definition coin_store_prices 760 and 866"},
  {"type": "other", "detail": "Player trade only, made by a Blacksmith; listed on the Green Text weapon page as trade-only, not sold by a vendor", "where": null, "price": null, "currency": null, "source": "wiki: Courageous Defender Axe ('can only be acquired through trade'); wiki: Green Text weapon ('Blacksmith made', 'Trade only')"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Client item name is locale 98991 'Courageous Defender Axe'; 10 definitions (38430 to 38461) share the name, one axe model axe_ar_ag_weapon_battleaxe.adr, slot 7, class 17", "source": "client definition; locale:98991"},
  {"claim": "Level 4 Warrior weapon, Green Text weapon, can only be acquired through trade; Sweeping Slash 853 damage, Spinning Attack 1548 damage; categorized Retired Weapons", "source": "wiki: Courageous Defender Axe"},
  {"claim": "Green Text weapon list includes Courageous Defender Axe as 'Blacksmith made, Trade only'", "source": "wiki: Green Text weapon"},
  {"claim": "Store data lists the 10 definitions in the coin store weapon category at 760 or 866 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json items 38430, 38433, 38436"}
 ],
 "confidence": 0.5,
 "open": ["Conflict: the wiki says the axe is trade-only and Blacksmith-made, and lists it as retired, but stores.json has it as a coin store item at 760/866 coins. Not resolved; I treated the store entry as a coin vendor sale per the rules, but the wiki gives no vendor name or date for it.",
  "The store data does not name the vendor or NPC or the store location for category 207; the 'where' field is unknown.",
  "Unknown whether the coin store listing was ever live on the original server or only exists in the data; the 'live' field is set to unsure.",
  "The wiki's 'trade' source is player-to-player and is not in the listed source types; it is recorded above as type 'other'. The Blacksmith crafting route is not documented with a recipe here.",
  "Wiki price lines are not given for this item, so no sale price comparison is possible.",
  "Only one wiki article and no images or video describe it; the wiki's image files were not read."]}</result>
