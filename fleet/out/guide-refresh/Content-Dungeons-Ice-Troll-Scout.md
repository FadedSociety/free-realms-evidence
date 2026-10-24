<!-- fleet job=guide-refresh id=Content-Dungeons-Ice-Troll-Scout status=nothing_found turns=12 usd=0.0116 tokens(read,write,in,out)=[244574, 35858, 26, 9409] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Ice Troll Scout.md

**Verdict:** current. The note makes almost no claims about our code. Its checkable claims are client strings and prize-wheel item names, and those hold at the tip.

**Corrections:** none.

What I checked and found consistent:
- **Client strings.** The quoted texts exist in the locale: "Ice Troll Scout!" (93277), "Ice Troll Scout" (116741), "Defeat the Ice Troll Scout!" (116830), "Find and defeat the Ice Troll Scout! Careful... He may try to ambush you!" (116831), "Ice Troll Scouts can be found near Snowhill." (388539), "Chase off some Ice Troll Scouts" (388538), "Keep Snowhill safe from the wandering Ice Troll Scout!" (389477), "Defeat the Ice Troll Scout" (389478), "Defeat an Ice Troll Scout" (417480), "Find the Ice Troll Scout in Snowhill and defeat him." (417491), the Ice Clap dev note (116820), the quest texts at 417474 and 417476, and the 389444 follow-up. The panel text "An ice troll is stealing from tourists! Find him and knock him out!" is 116829.
- **Medic wheel.** "Urgent Care Medic Fatigues" has no locale match. The Urgent Care Medic Pants, Gloves, Boots, Shirt, Cap and Backpack all exist (133092–133097). "Energy Transfer Medic Fatigues" exists (133132). The note's conflict entry is accurate.
- **Other wheel items.** All the item names I checked exist as written: the Power Shard and Ring of Energy II items for all six jobs, Medic's Scalpel of Vitals (131947), the Archer, Brawler, Ninja, Warrior and Wizard weapons, Point Blank Archer Leggings, Peek-a-Boo Brawler Pants, Nokizaru Ninja Hakama, Basic Attack Warrior Breeches, Hedge Wizard Slacks and Skirt, and Battle Item Mystery Pack (6666).
- **Repo consistency.** `notes/Build Guides/Content/Dungeons/Dungeons.md:123` lists this battle as difficulty 2, "none (3+ recommended)", **written**, which matches the note. The `[[Howling Hills]]`, `[[NPCs - Snowhill]]`, `[[Frostfang Snarlers]]` and `[[Petty Yetis]]` link targets exist. `[[Jonathon Forkpath]]` has no page of its own, but he is covered in `NPCs - Snowhill.md:84`.
- **Build status.** The note claims no build status for our server, so there is nothing to contradict. For reference, `prototype/osfr-tools/data/content/npc_spawns_extra.json:37150` places an "Ice Troll Scout" NPC with name id 116741, and `field_battles.json` holds only the Troll Summoner (Troll Scoutling) battle.

**Unsure:**
- The `loc <number>` ids in the note (for example `loc 2863547858`, `loc 1647936596`, `loc 3590488412`) do not resolve in the `locale` tool, which uses row ids (for example 93277, 116830, 388539). They look like a different hash scheme, so I could not match each id. I matched the text instead, and every quoted text was found.
- The wiki-sourced rows (infobox level, Stars 25, the 24 Coins members bonus, the Members tag) and the entrance marker distances from video cannot be checked in the repo or the client.
