<!-- fleet job=guide-refresh id=Content-Dungeons-Howling-Hills status=done turns=17 usd=0.0201 tokens(read,write,in,out)=[580032, 64903, 36, 12394] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Howling Hills.md

**Verdict:** current, with one minor citation problem in the Entrance row. The note makes almost no claims about our code; nearly all of it is client-locale and wiki text. I checked the quoted strings, the item names, the coin figures and the code-side facts (difficulty, zone, level gate) against the client locale, `data/content/dungeons/howling_hills.json` and `Dungeons.md`. They match.

**Corrections:**

1. `old:` | Entrance | Click the **barrier** in **Snowhill**. It has an Atlas icon. The client calls it "the Howling Hills, north of Snowhill" (`loc 3394134736`), "the pass through Howling Hills" (`loc 797046977`) and says an NPC stands "near the entrance to Howling Hills, not far from here" (`loc 3882321755`). |
   `new:` | Entrance | Click the **barrier** in **Snowhill**. It has an Atlas icon. The client names the route "the pass through Howling Hills" (`loc 797046977`) and says an NPC stands "near the entrance to Howling Hills, not far from here" (`loc 3882321755`). A kill objective reads "Defeat Ice Trolls in the Howling Hills, north of Snowhill." (`loc 3394134736`); that places the area north of Snowhill but does not name the entrance. |
   `why:` The locale has no standalone "the Howling Hills, north of Snowhill" name. The phrase is a fragment of the objective "Defeat Ice Trolls in the Howling Hills, north of Snowhill." (locale row 389484), which the note itself cites as `3394134736` in the Related quests table. Zone is Snowhill, as the note says: `prototype/osfr-tools/data/content/dungeons/howling_hills.json:72` and `:184`, and `tests/pieces/test_piece_059.py:121`.

**Checked and holding (no change):**
- Overview: "Panel description" (locale 92500), "Journal description" (5056), "Find and defeat Snognosh!" (5055), "NOT LIVE - Howling Hills" (4828), the three-cub bonus text (139323) and "Bonus: 98 Coins!" (119968) all match.
- Requirements: "Requires a level 5 combat job" (4199). The dungeon JSON has `minimum_combat_job_level` = 5 and difficulty = 3 (`howling_hills.json:60-108`).
- Conflicts #1: the "343 Coins" string is absent from the locale ("no matches"). Bone Bog Cemetery is 112 and Briarheart Caverns (difficulty 5) is 117 (`notes/Build Guides/Content/Dungeons/Dungeons.md:29`, `:33`).
- Prize wheel: sampled item names exist in the locale, e.g. "Ninja's Scythe of 1000 Storms" (131981), "Cross Wind Archer Cap" (132767), "Wizard's Bone Wand of Glaciers" (132041), "Trauma Care Medic Cap" (133113), "Brawler's Anvil Hammer of Rumbling" (131921). Conflict #2's "Power Shard" spelling also holds.
- Quest rows: the quoted text for Patterwings (24960), Valinda (14904), Little Plecky (92220), Chaz (72993, 100494), Fastvi (71535), the Ice Wolf Trainers (103054), "Defeat opponents in the Howling Hills." (100763), the bear cub lines (139324, 140091, 140093) and "Howling Hills Bonus Objective" (140148) all match.
- Enemies: "Trained Ice Wolf" (14569), "Ice Troll Berserker/Warchief/Scout" (440737, 440740, 116741), "Lost Ice Bear Cub" and "Wild Mother Ice Bear" (139321, 139322), "Big Mean Ice Troll" (422751).
- Conflicts #3 and #5: "Defeat Snogosh, the Ice Troll King!" exists (92205). The "Bonus: " prefix is absent for the cub string.

**Unsure:**
- The `loc` numbers are hashes, so the `locale` tool could not resolve them by ID. I checked the strings by text only, and I did not check the hash IDs themselves.
- The video frame keys (`kXeF2h7Xsoo/00132`, `YxvolFOnaJM/00084`) and the "Howling Hills 62m" marker. No index in the repo confirmed them.
- The 343 Coins wheel figure is wiki-only; I could not settle whether it is real. The note already flags this.
