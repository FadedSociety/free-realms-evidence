<!-- fleet job=note-refresh id=NPC-Placement status=done turns=19 usd=0.0195 tokens(read,write,in,out)=[582225, 55880, 40, 13306] model=claude-haiku-5-5 -->
# notes/Research/NPC Placement.md

**Verdict:** Badly stale on the source-tag and runtime-loader points, and the counts have drifted since W56. The W56 join results and capture comparison were not checked row by row. The startup reader and crosswalk citations still hold.

**Corrections:**

1. `old:` Open limits, last bullet: "NPC placements and the extra file are data artifacts; the strict runtime loader does not yet consume them."
   `new:` "NPC placements and the extra file are data artifacts; the runtime consumes them. `world::NpcVisibility::load` reads `npc_spawns_extra.json` and the regional `legacy_data` rows, and `gameplay.rs` wires it in at startup."
   `why:` repo:prototype/osfr-tools/src/world.rs:323 (`read_rows(&content_dir.join("npc_spawns_extra.json"))`), world.rs:284 (`legacy_data` rows spawn), gameplay.rs:885-888 (`NpcVisibility::load(npc_content)`). Autopilot T331.md:46 describes the same loader.

2. `old:` "The strict v1 SourceTag at src/content.rs:21-34 has only client/video/wiki/reconstructed."
   `new:` "The strict v1 SourceTag at src/content.rs:21-28 has client/video/wiki/reconstructed and `#[serde(rename = "legacy-data")] LegacyData(String)` at lines 26-27; `evidence()` at lines 30-39 covers the variant."
   `why:` repo:prototype/osfr-tools/src/content.rs:21-39. Design/Integration Queue.md:8 records the `legacy-data` source tag as registered in W59.

3. `old:` "The temporary content_npcs test adapter maps legacy-data to reconstructed only for its scratch ContentDb package."
   `new:` "tests/content_npcs.rs accepts `legacy-data` directly as a source kind; no adapter maps it to `reconstructed`."
   `why:` repo:prototype/osfr-tools/tests/content_npcs.rs:68 (`"client" | "video" | "wiki" | "reconstructed" | "legacy-data"`).

4. `old:` "No production loader changed. Direct deserialization needs an explicit variant such as #[serde(rename = "legacy-data")] LegacyData(String) in SourceTag and that variant added to evidence(); lead integration must decide whether to add it."
   `new:` "The production `SourceTag` already has the `legacy-data` variant and its `evidence()` arm, so direct deserialization of `legacy-data` tags needs no further change."
   `why:` repo:prototype/osfr-tools/src/content.rs:26-27 and content.rs:37.

5. `old:` "data/content/npc_spawns_extra.json: 3,265 unlisted Legacy spawns with catalog-backed model, name/NameId when present, position and heading."
   `new:` "data/content/npc_spawns_extra.json: 3,301 rows at the tip (3,265 at W56, plus later appends, including the T372 and T385 rows), with catalog-backed model, name/NameId when present, position and heading."
   `why:` repo:prototype/osfr-tools/tests/content_npc_spawns.rs:243 (`assert_eq!(extra_rows.len(), 3301)`); notes/Autopilot/T385.md:12 (3,297 -> 3,301).

6. `old:` "| Total regional rows | 1,199 | 1,199 |"
   `new:` "| Total regional rows | 1,199 | 1,199 (1,201 at the tip) |"
   `why:` repo:prototype/osfr-tools/tests/content_npc_spawns.rs:234-235 (T379 appended two unanchored rows, `regional_legacy + regional_reconstructed == 1201`).

**Unsure:**
- The Legacy source paths (`FreeRealms-Legacy/src/Scripts/Zone/FabledRealms.lua`, `src/Resources/Npcs.json`) are not in the refs checkout. `refs/FreeRealms-Legacy` has `src/Resources`-level content only as far as SOURCE.json, so the line citations and the 4,253-row counts could not be checked.
- `lab/content/startup-snapshot/startup.json` (23 `npc_spawns` rows) and `lab/reports/locale-id-to-text.json` are absent from this checkout, so the 23-row count and the locale match figures (1,655/1,659, 3,956/4,253) could not be verified.
- The 621 reconstructed rows and the 9 capture-copied rows are consistent with the tests (`captured_actors.len() == 9`, content_npc_spawns.rs:244), but the 621 count itself was not recomputed.
- `notes/Design/Build Ledger.md:59` still says "3,265 extra spawns". That is outside this note, but it is the same stale count.
- `repo:prototype/osfr-tools/src/startup_world.rs` `parse_add_npc` (line 868) reads the rotation at line 881 and the animation at 882; the note's "868-881" range is accurate to the rotation read.
