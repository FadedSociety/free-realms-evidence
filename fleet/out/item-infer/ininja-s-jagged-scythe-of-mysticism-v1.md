<!-- fleet job=item-infer id=ininja-s-jagged-scythe-of-mysticism-v1 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[12829, 13537, 8, 3220] model=claude-haiku-5-5 -->
# Ninja's Jagged Scythe of Mysticism

{"item": {"name": "Ninja's Jagged Scythe of Mysticism", "locale_id": 131993, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop (wiki category 'Coin Shop' and 'Coin Shop Weapons'; page says it is acquired from the Coin Shop)", "where": "Coin Shop", "price": "1504 coins (wiki coins field; the page's sell text has the price blanked, so treat as single wiki-listed price; no sale price given)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Ninja's_Jagged_Scythe_of_Mysticism (rev 34397)"},
  {"type": "vendor", "detail": "Shivering Shark, Ninja Job merchant (Sells list, wiki rev 2013-11-03; repo vendor npc_id 9500000063, item_id 75109)", "where": "Blackspore Swamp, behind the Blackspore Pet Adoption Center", "price": "1504 coins purchase (member price 1353 coins; sell-back 752 coins)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Shivering_Shark ; repo:prototype/osfr-tools/data/content/vendors.json:6452-6490"},
  {"type": "prize_wheel", "detail": "Prize wheels at Moldy Shamblers! and Vale of the Ancients (wiki category 'Prize Wheel Weapons')", "where": "Moldy Shamblers!; Vale of the Ancients", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Ninja's_Jagged_Scythe_of_Mysticism (page text and category 'Prize Wheel Weapons')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Level 12 Ninja weapon, Power 4, Mystic Rush and Mystical Blade effects", "source": "https://freerealms.fandom.com/wiki/Ninja's_Jagged_Scythe_of_Mysticism; image:item_tooltip"},
  {"claim": "Name matches client locale text id 131993", "source": "locale:131993"},
  {"claim": "Coin Shop listing at 1504 coins", "source": "https://freerealms.fandom.com/wiki/Ninja's_Jagged_Scythe_of_Mysticism (coins field 1504; categories Coin Shop, Coin Shop Weapons, Marketplace Items)"},
  {"claim": "Shivering Shark (Blackspore Swamp, Ninja Job merchant dated 27 August 2013) sells Jagged Scythe of Mysticism; reference price 1504 coins, member 1353, sell-back 752", "source": "https://freerealms.fandom.com/wiki/Shivering_Shark ; repo:prototype/osfr-tools/data/content/vendors.json:6452-6490 ; repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:96"},
  {"claim": "Mysticism listed in Ninja mystery/battle-item tables for Moldy Shamblers and Vale of the Ancients dungeon notes; these are consistent with the prize-wheel source but are not separate drop evidence", "source": "repo:notes/Build Guides/Content/Dungeons/Moldy Shamblers.md:67 ; repo:notes/Build Guides/Content/Dungeons/Vale of the Ancients.md:72"},
  {"claim": "Tooltip Resell Value 150 (this is a resell value, not a purchase price)", "source": "image:item_tooltip"}
 ],
 "confidence": 0.6,
 "open": [
  "Wiki page text blanks the Coin Shop price; 1504 comes from the wiki coins field and matches the repo stores.json reference price, which the repo itself says is not a captured NPC quote.",
  "Mechanism conflict: wiki says Coin Shop, while the repo vendor data places it at the Shivering Shark NPC vendor. Both are kept as separate sources; neither has a dated in-game capture.",
  "The pack's 'Moldy Shambler' enemy answer is not a drop. It cites moldy_shamblers.json:1366 for a prize-wheel source; I did not open that file, so the enemy-drop claim is rejected and the prize-wheel source rests on the wiki page only.",
  "No dated evidence of retirement or of current availability. The Shivering Shark listing is from the 2013-11-03 wiki revision, so live status is unsure.",
  "Prize wheel source has no odds or wheel name; the Vale of the Ancients wheel is wiki-only.",
  "Marketplace (Station Cash) listing: wiki category 'Marketplace Items' is present, but no Station Cash price is given. Not recorded as a source."
 ]}
