<!-- fleet job=citem-infer id=ccallahan-s-cutter-384116-v1 status=done turns=5 usd=0.0039 tokens(read,write,in,out)=[38829, 16416, 12, 2987] model=claude-haiku-5-5 -->
# Callahan's Cutter

{"item": {"name": "Callahan's Cutter", "locale_id": 384116, "kind": "weapon"},
 "sources": [
  {"type": "quest_reward", "detail": "Medic: Paying Your Student Debts (given by Doctor Callahan; Medic level 20 weapon, the wiki's acquisition route)", "where": "Seaside (Seaside School of Combat Medicine)", "price": null, "currency": null, "source": "wiki page \"Callahan's Cutter\" (\"It is acquired by completion of the quest Medic: Paying Your Student Debts\"); repo:data/content/npcs/seaside.json (quest title 'Medic: Paying Your Student Debts', Doctor Callahan)"},
  {"type": "vendor", "detail": "Coin store listing for client item 48323 (vendor not named in our store data; category 207)", "where": null, "price": "2363 coins (member price 2126 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 48323 (line 13299); repo:prototype/osfr-tools/data/reference/weapons.json line 10315 (cost 2363)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client weapon definition 48323 is named Callahan's Cutter (name locale 384116), slot 7, class 28, model sword_ar_ag_weapon_megasaw.adr", "source": "client definition; locale:384116"},
  {"claim": "Callahan's Cutter is a level 20 Medic weapon, power 5, cannot trade, acquired by completing the quest Medic: Paying Your Student Debts", "source": "wiki page \"Callahan's Cutter\""},
  {"claim": "Abilities: Incision 2609 damage; Triage 8302 damage and 2372 heal", "source": "wiki page \"Callahan's Cutter\"; repo:prototype/osfr-tools/data/reference/weapons.json line 10277-10309"},
  {"claim": "Resell value 236 coins (matches store sell_price_coins 236)", "source": "item tooltip image (image:item_tooltip); repo:data/content/stores.json item 48323"},
  {"claim": "Coin store purchase price 2363 coins, member price 2126 coins", "source": "repo:data/content/stores.json item 48323 (line 13299)"},
  {"claim": "Quest title 'Medic: Paying Your Student Debts' is given by Doctor Callahan in Seaside", "source": "repo:data/content/npcs/seaside.json (quest title entry); locale:72972"},
  {"claim": "Client line 384117-384121 neighbours (Molten Dragon Blade, Bullseye's Blasting Bow, Brawl Club, The Rumbler, Archer & Brawler Weapons) show this is part of a weapon set group, not a promotion", "source": "client cluster locale:384117-384121"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin store listing (2363 coins) is in our store data but the vendor/NPC that sells it is not named there; confirm which Coin vendor stocks item 48323 and whether it is sold at all today.",
  "The quest reward is supported only by the wiki page text; repo quest data for Medic: Paying Your Student Debts has empty rewards, so the reward list is unverified in our own quest store.",
  "Retirement status not established: no source states the weapon was retired or made unobtainable. Live status is 'unsure' because the store listing exists but no current-era source confirms it.",
  "Wiki gives no separate coin price beyond the store figure; no sale price was found on the wiki.",
  "Client definition description is empty; the name locale is tagged quest_title, so the item name source is a quest title string shared with the quest."
 ]}
