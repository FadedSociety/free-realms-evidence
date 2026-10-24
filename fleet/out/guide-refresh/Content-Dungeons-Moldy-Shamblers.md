<!-- fleet job=guide-refresh id=Content-Dungeons-Moldy-Shamblers status=done turns=17 usd=0.0184 tokens(read,write,in,out)=[468633, 53212, 36, 14094] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Moldy Shamblers.md

**Verdict:** Current, with minor drift. The status and path claims hold; the note's content is client-locale evidence, which I checked against `locale/en_us_data.dat`. Two statements are misleading. Neither is a routing or build claim.

**Corrections:**

1. `old:` NPCs: [[Whigguma]] (seen on the video overworld, `CR7BfAesNLM/00000`), [[Chief Bilgragum]].
   `new:` NPCs: Whigguma (seen on the video overworld, `CR7BfAesNLM/00000`) and Chief Bilgragum, both listed on [[NPCs - Briarwood]] (no separate NPC pages exist).
   `why:` The links `[[Whigguma]]` and `[[Chief Bilgragum]]` point to pages that do not exist. `notes/Build Guides/Content/NPCs/` has only area pages (`NPCs - Briarwood.md` and the rest), and no file or `# Whigguma` / `# Chief Bilgragum` heading exists in the repo. Both NPCs appear in `repo:notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:152` and `:154`.

2. `old:` Members get "Members Only Bonus: 40 Coins" (client label `loc 1925651180`)
   `new:` Members get a "Members Only Bonus!" reward (client label `loc 1925651180`). The client gives no amount; "40 Coins" comes from the wiki only.
   `why:` `locale/en_us_data.dat:50746` reads `1925651180 ucdt Members Only Bonus!` with no amount. The "40 Coins" figure appears only in the wiki-cited rows, and `Bonus: 40 Coins!` (`loc 3342032968`, `en_us_data.dat:88373`) is a separate, generic string.

**Checked and holding:**
- Locale ids for the name, panel description, goal, quest objectives, enemies, Moldering Fungaloid, Safety First and the level-9 line all match the locale file (`en_us_data.dat` lines 112525, 62573, 61280, 70050, 8298, 74631, 86554, 36249, 19209, 75492, 34198, 49667, 85632, 70225, 85522, 77651, 31188, 49775, 46496, 38806, 47834, 101269, 4265826352 game data at 112577, and the enemy game-data ids 391771898 and 2031409020).
- Quest-text ids: "Tackle a group of Fungaloids in eastern Nettleseed..." (3829646810) exists; `repo:notes/Build Guides/Content/Jobs/Adventurer.md:135` lists it as the candidate for "There's Fungus Among Us!", as the note says.
- Prize wheel: every item name in the job table exists in the locale as written (for example Archer's Power Shard of Regeneration IV at line 86972, Archer's Recurve Bow of Booming at line 2005168045, Medic's Ring of Regeneration IV at line 98187). "Archer's Natural" and "Bow of Blessing" have no entries, which supports Conflict 3.
- "No 'Moldy Shamblers Bonus Objective' or 'Win Combat Encounter Moldy Shamblers' string": no hits in the locale.
- `repo:notes/Build Guides/Content/Dungeons/Dungeons.md:137` agrees with the note's difficulty 4 and level 9.

**Unsure:**
- Video-only claims (`liVAgboeCLg/00004`, `ATNDJ0I3sf0/00046`, `00054`, the "1/6" and "1/3" counters, the Archer wheel frame) and the wiki-only figures (153 stars, 68-coin slot, Safety First reward) cannot be checked from the repo or the locale.
- The repo has `prototype/osfr-tools/data/content/dungeons/moldy_shamblers.json`, which carries this note's claims. I did not check the JSON against the note, since the task was the note alone.
