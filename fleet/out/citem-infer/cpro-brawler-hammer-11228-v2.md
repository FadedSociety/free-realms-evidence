<!-- fleet job=citem-infer id=cpro-brawler-hammer-11228-v2 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[6315, 9818, 6, 2194] model=claude-haiku-5-5 -->
# Pro Brawler Hammer

{"item": {"name": "Pro Brawler Hammer", "locale_id": 11228, "kind": "weapon"},
 "sources": [
  {"type": "quest_reward", "detail": "Brawler: One Man's Junk... (title string 141010, giver Nurble, id 9000000415), wiki-only reward; the repo quest record has an empty rewards list", "where": "Robgoblin Camp (Wilds)", "price": null, "currency": null, "source": "Wiki page 'Pro Brawler Hammer' ('previously acquired by completion of the quest Brawler: One Man's Junk...'); repo:prototype/osfr-tools/data/content/quests/brawler.json:1624-1632 (quest title 141010, giver 9000000415, rewards []); repo:notes/Build Guides/Content/Jobs/Brawler.md:136. Numeric quest id 3030028 is a reconstructed batch key (brawler.json:1642-1644), not a server-confirmed id."},
  {"type": "coin_shop", "detail": "Coin store listing, category 207, tint group 1; vendor/NPC not named in store data. Historical: the wiki says the item is no longer obtainable, so this row is likely stale.", "where": null, "price": "715 coins (member price 643 coins, 10% member discount); sell value 71 coins", "currency": "coins", "source": "repo:data/content/stores.json item 8050 (line 2077: purchase 715, member 643, sell 71); client definition coin price 715 (repo:prototype/osfr-tools/data/reference/weapons.json line 34308); wiki tooltip Resell Value 71"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name 'Pro Brawler Hammer' is locale 11228; Brawler weapon, level 4, Power 2", "source": "locale:11228; repo:prototype/osfr-tools/data/reference/weapons.json line 34305 (client item 8050)"},
  {"claim": "Wiki: level 4 Brawler weapon, 'no longer able to be acquired', previously from completing Brawler: One Man's Junk..., cannot trade; in Retired Weapons and Unobtainable Weapons categories", "source": "Wiki page 'Pro Brawler Hammer' (ns0, confirmed by lookup)"},
  {"claim": "Coin store row: item 8050, category 207, tint 1, 715 buy / 643 member (10%) / 71 sell, no_sale false", "source": "repo:data/content/stores.json line 2077"},
  {"claim": "Quest 'Brawler: One Man's Junk...' given by Nurble (9000000415); quest record has no recorded rewards", "source": "repo:prototype/osfr-tools/data/content/quests/brawler.json:1624-1632"},
  {"claim": "Wiki tooltip image: Resell Value 71, Power 2, Required Level 4 Brawler, Cannot Trade", "source": "image:item_tooltip 'Pro Brawler Hammer item.jpg' (wiki)"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the wiki says the hammer is no longer obtainable and is in Retired/Unobtainable categories, but stores.json line 2077 is an active-looking coin row with the same live source_tags (L1, L2, L4, R2, T633, R1) as neighbouring rows. Either the row is stale (coin_shop source should be treated as historical) or the retirement claim is wrong. Not resolved from the repo.",
  "The coin store row names no vendor or NPC, and gives no start or stop date.",
  "The quest reward rests on the wiki sentence alone. brawler.json rewards are empty, and the quest id 3030028 is reconstructed, not server-confirmed.",
  "Wiki gives no retirement date; 'no longer able to be acquired' is the only retirement evidence.",
  "Client description is empty; effects (Glancing Blow 444 dmg, Leg Sweep 1554 dmg) come from the wiki and tooltip image only."
 ]}
