<!-- fleet job=note-refresh id=Content-Batch-Dungeons status=done turns=18 usd=0.0265 tokens(read,write,in,out)=[706288, 81986, 38, 18345] model=claude-haiku-5-5 -->
# notes/Research/Content Batch Dungeons.md

**Verdict:** Badly stale in the W58 enemy-crosswalk section and in the scene-name claim. The file layout, the 75-file count, the reference totals (2,095 / 87 / 2,008 and the per-kind breakdown), the opening-cave parity, the `Dungeon` schema-gap description and the test counts (content_dungeons 3, content_enemies 2, enemies 6) still hold at the tip.

**Corrections:**

1. `old:` `| Resolved occurrences | 45 |`
   `new:` `| Resolved occurrences | 130 |`
   `why:` `repo:prototype/osfr-tools/data/content/enemies_unresolved.json:65` (`resolved_dungeon_occurrences: 130`); the same change is recorded in `repo:notes/Autopilot/T015.md:22`. The 45 figure was the pre-W58b value (`enemies_unresolved.json:87`).

2. `old:` `| Unresolved occurrences with reason | 322 |`
   `new:` `| Unresolved occurrences with reason | 237 |`
   `why:` `repo:prototype/osfr-tools/data/content/enemies_unresolved.json:66` (`unresolved_dungeon_occurrences: 237`); `repo:notes/Autopilot/T015.md:23`.

3. `old:` `| Unique names resolved | 32 |`
   `new:` `| Unique names resolved | 82 |`
   `why:` `repo:prototype/osfr-tools/data/content/enemies_unresolved.json:67` (`resolved_unique_dungeon_names: 82`); `repo:notes/Autopilot/T015.md:24`.

4. `old:` `| Unique names unresolved | 218 |`
   `new:` `| Unique names unresolved | 169 |`
   `why:` `repo:prototype/osfr-tools/data/content/enemies_unresolved.json:68` (`unresolved_unique_dungeon_names: 169`); `repo:notes/Autopilot/T015.md:25`.

5. `old:` `| Added definitions | 26 (`930000..930025`) |`
   `new:` `| Added definitions | 80: 26 at W58 (`930000..930025`), 24 at W58b (`930026..930049`), 30 at T015 (`930050..930079`) |`
   `why:` `repo:prototype/osfr-tools/data/content/enemies.json:148` and `:2202` (930079 present); `enemies_unresolved.json:78` (`w58b_definitions_added: 24`); `repo:notes/Autopilot/T015.md:12`.

6. `old:` `82 `enemy_kind` rows from 74 regional NPC files (70 unique description texts) remain unresolved because the regional content supplies descriptive prose rather than a hostile actor/model/stat record.`
   `new:` `43 of 82 `enemy_kind` rows from 74 regional NPC files (70 unique description texts) remain unresolved, 36 are fully resolved and 3 are partial (W58b). The unresolved rows are still descriptive prose rather than a hostile actor/model/stat record.`
   `why:` `repo:prototype/osfr-tools/data/content/enemies_unresolved.json:82-83` (`world_rows_resolved: 36`, `world_rows_partial: 3`), `:74` (`world_rows_unresolved: 43`); `repo:notes/Research/World Enemies.md:132-133`.

7. `old:` `Guide pages do not provide an exact instance scene-name field, so their scene values remain null.`
   `new:` `Guide pages do not provide an exact instance scene-name field. Twenty-four guide pages now carry a client scene stem in `dungeon_data.instance_scene_name` (an inferred `(R)` key-to-stem association, e.g. Bandit Hideout = `sg_bandit_hideout`); the other 50 files keep null scene values.`
   `why:` `repo:prototype/osfr-tools/data/content/dungeons/bandit_hideout.json:304-306` (value `sg_bandit_hideout`, reason null); `repo:notes/Autopilot/T015.md:5-9` and table at `:19-20` (24 guide pages plus the opening cave = 25 files with a scene name). The test at `tests/content_dungeons.rs:278` checks only that the field exists.

**Unsure:**

- The W58 `Commands and results` lines (`content_enemies` printing `45/367` and `0/82`) are historical command output. The current run prints 130/367 (T015) and 36/82 regional rows (W58b). I did not run the tests.
- The 2,095 / 2,008 / 5,281 / 19,470 totals and the 64 NPC / 23 zone resolutions are not recounted. I could not count the 28,505-line unresolved JSON with the tools. The arithmetic across the note's own tables is consistent.
- Out of scope for this note: `repo:notes/Design/Build Ledger.md:78` still says "293 of 367 enemy references are unresolved" and "Only 1 has a numeric zone id or scene name". The first is the pre-T015 figure. The second is true for numeric zone ids only, since 25 files now carry scene names.
