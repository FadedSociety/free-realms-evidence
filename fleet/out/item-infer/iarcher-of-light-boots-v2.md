<!-- fleet job=item-infer id=iarcher-of-light-boots-v2 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[5107, 11640, 6, 2465] model=claude-haiku-5-5 -->
# Archer of Light Boots

{"item": {"name": "Archer of Light Boots", "locale_id": 442510, "kind": "clothing"},
 "sources": [
  {"type": "drop", "detail": "Defeating Necronomicus (Gloam Lord of Necromancy). Wiki wording only; the wiki does not say whether this is the Battle Boss in 'Necronomicus Unleashed' (beneath Merry Vale, Encounter 432 Necronomicus' Lair) or the Overworld Enemy Necronomicus. The battle is the more likely source by analogy with the sibling Brawler's Necronomicus Unleashed weapon, but this is unconfirmed.", "where": "Merry Vale caverns (battle version) or unspecified (overworld version)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Archer_of_Light_Boots (rev 31109: 'It is acquired from defeating Necronomicus'); https://freerealms.fandom.com/wiki/Necronomicus (lists Battle Boss NPC and Overworld Enemy NPC); locale:441903 'Defeat Necronomicus'; locale:442596 'Necronomicus Unleashed'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Archer of Light Boots is a Members-only, level 2 Archer feet clothing, acquired from defeating Necronomicus", "source": "https://freerealms.fandom.com/wiki/Archer_of_Light_Boots"},
  {"claim": "Sibling Warrior, Brawler, Medic, Wizard and Ninja of Light Boots use the same 'acquired from defeating Necronomicus' wording, so this looks like a set drop from the same boss", "source": "https://freerealms.fandom.com/wiki/Warrior_of_Light_Boots ; .../Brawler_of_Light_Boots ; .../Medic_of_Light_Boots ; .../Wizard_of_Light_Boots ; .../Ninja_of_Light_Boots"},
  {"claim": "Necronomicus has a Battle Boss NPC version (battle 'Necronomicus Unleashed', unlocked by the Fighter's Guild Message Board quest in Sanctuary) and an Overworld Enemy NPC version", "source": "https://freerealms.fandom.com/wiki/Necronomicus"},
  {"claim": "Client strings for the boss and battle exist: Necronomicus NPC name, 'Necronomicus Unleashed' quest and place, 'Defeat Necronomicus', 'Defeat Necronomicus!' (Rumbledome Encounter 432 - Necronomicus' Lair)", "source": "locale:440729 ; locale:442316 ; locale:442596 ; locale:441903 ; locale:5100664"},
  {"claim": "Archer's Wild Bow of Forbidden Magic is explicitly from the Overworld Boss Necronomicus, showing the overworld version also exists as a loot source for Archer gear", "source": "https://freerealms.fandom.com/wiki/Archer's_Wild_Bow_of_Forbidden_Magic"},
  {"claim": "Name locale matches the item name", "source": "locale:442510 [item] 'Archer of Light Boots'"},
  {"claim": "Repo has no drop table or item entry for Archer of Light Boots; the repo's Necronomicus notes (NPCs - Merry Vale.md) list no drops", "source": "repo: prototype/osfr-tools/data/content/enemies.json:510 ; notes/Build Guides/Content/NPCs/NPCs - Merry Vale.md:104"}
 ],
 "confidence": 0.4,
 "open": [
  "No price: the wiki page gives no coin, Station Cash or Coin Shop price, and no vendor stock lists the item.",
  "Battle vs overworld: the wiki says only 'defeating Necronomicus'. Which Necronomicus version drops the boots is unverified; the battle is the likely one by analogy, not proven.",
  "Drop rate and whether the boots drop every kill or only from a reward chest are not stated in any source.",
  "No repo drop table lists these boots, so the drop rests on the wiki wording alone.",
  "Live status is unknown: the battle exists in the client and in the video, but no source says whether it runs on the live server.",
  "Retired status is unknown: no source states retirement.",
  "Video frame video:G2tF5uF5cBE/01200.jpg was removed as evidence: it shows a different item (Bobtailed Archer Hoodie), not these boots.",
  "The critique's invalid ids locale:2004825146 and locale:2156346441 were removed. They are client hash keys (ucdt), not locale ids. The text they stand for ('Defeat the Awakened version of Necronomicus beneath Merry Vale' and the level 20 group warning) is in the notes but was not used as item evidence."
 ]}
