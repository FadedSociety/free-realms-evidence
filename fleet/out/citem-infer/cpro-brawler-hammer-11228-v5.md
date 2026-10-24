<!-- fleet job=citem-infer id=cpro-brawler-hammer-11228-v5 status=done turns=2 usd=0.0032 tokens(read,write,in,out)=[6845, 15196, 6, 2530] model=claude-haiku-5-5 -->
# Pro Brawler Hammer

{"item": {"name": "Pro Brawler Hammer", "locale_id": 11228, "kind": "weapon"},
 "sources": [
  {"type": "quest_reward", "detail": "Brawler: One Man's Junk... (title locale 141010, quest 3030028, giver Nurble, NPC 9000000415); wiki says the hammer was previously acquired by completing this quest. brawler.json lists no rewards, so the reward is wiki-only.", "where": "Robgoblin Camp (Nurble's location)", "price": null, "currency": null, "source": "Wiki page 'Pro Brawler Hammer' (ns0): 'previously acquired by completion of the quest Brawler: One Man's Junk...'; repo:prototype/osfr-tools/data/content/quests/brawler.json:1624-1632 (rewards empty); notes/Build Guides/Content/Jobs/Brawler.md:68 and :136 (M9 One Man's Junk, giver Nurble at Robgoblin Camp); repo:prototype/osfr-tools/data/content/npcs/wilds.json:30515-30541"},
  {"type": "coin_shop", "detail": "Coin store row for item 8050 (category 207, tint group 1). Stored price only: no vendor, NPC, or start/stop date is recorded, and the wiki says the item is no longer obtainable. Treat as a historical price, not a live sale.", "where": null, "price": "715 coins buy; 643 coins member price (10% member discount); 71 coins sell value", "currency": "coins", "source": "repo:data/content/stores.json item 8050 (stores.json:2077); client coin price 715 (repo:prototype/osfr-tools/data/reference/weapons.json:34308); wiki tooltip 'Pro Brawler Hammer item.jpg' Resell Value 71"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name 'Pro Brawler Hammer' is locale 11228; Brawler weapon, Power 2, slot 7, class 5, model hammer_ar_ag_weapon_drill.adr", "source": "locale:11228; repo:prototype/osfr-tools/data/reference/weapons.json:34270-34305 (client item 8050)"},
  {"claim": "Wiki: level 4 Brawler weapon, 'no longer able to be acquired', previously from completing Brawler: One Man's Junk..., cannot trade; categories Retired Weapons and Unobtainable Weapons", "source": "Wiki page 'Pro Brawler Hammer' (ns0)"},
  {"claim": "Tooltip: Resell Value 71, Power 2, Required Level 4 Brawler, Cannot Trade; effects Glancing Blow and Leg Sweep", "source": "image:item_tooltip 'Pro Brawler Hammer item.jpg' (wiki)"},
  {"claim": "Coin store row for item 8050: 715 buy / 643 member (10%) / 71 sell, no_sale false, sits in a block of category-207 rows with identical source tags (re-read this run)", "source": "repo:prototype/osfr-tools/data/content/stores.json:2077"},
  {"claim": "Quest 'Brawler: One Man's Junk...' given by Nurble (9000000415), quest 3030028; no rewards recorded", "source": "repo:prototype/osfr-tools/data/content/quests/brawler.json:1624-1632"},
  {"claim": "Nurble is at the Robgoblin Camp and gives One Man's Junk (M9)", "source": "notes/Build Guides/Content/Jobs/Brawler.md:68, :136; notes/Build Guides/Content/NPCs/NPCs - Wilds.md:91; repo:prototype/osfr-tools/data/content/npcs/wilds.json:30541"},
  {"claim": "Brawler notes place Pro Brawler Hammer at level 5 in the tier list, while the wiki and client say level 4", "source": "notes/Build Guides/Content/Jobs/Brawler.md:210"}
 ],
 "confidence": 0.55,
 "open": [
  "The coin row (stores.json:2077) is the only coin price evidence. It conflicts with the wiki's 'no longer able to be acquired'; no vendor, dated listing or stock row names it, and its neighbours share the same generic tags. Treat the 715/643/71 price as historical.",
  "The quest reward rests on one wiki sentence. brawler.json records no rewards and no reward item, so no server-side grant is confirmed.",
  "Level conflict: wiki and client say level 4; Brawler.md:210 says level 5. Not resolved.",
  "No retirement date appears in any source. 'No longer able to be acquired' is the only retirement evidence.",
  "Client description is empty; effect numbers (444 and 1554 damage) come from the wiki and tooltip only."
 ]}
