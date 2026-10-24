<!-- fleet job=note-refresh id=World-Enemies status=done turns=25 usd=0.0297 tokens(read,write,in,out)=[980407, 74458, 52, 21245] model=claude-haiku-5-5 -->
# notes/Research/World Enemies.md

**Verdict:** minor-to-moderate drift. The engine, policy constants, reader addresses and the W36 packet claims hold. The lib.rs registration claim is wrong, and the W58 section is partly out of date after the W58b and T015 additions.

**Corrections:**

1. `old:` It is not registered in `lib.rs`; `tests/enemies.rs` includes it with `#[path]` until lead integration.
   `new:` It is registered in `lib.rs` (`pub mod enemies;`); `tests/enemies.rs` imports it as `osfr_tools::enemies`, with no `#[path]`.
   `why:` repo:prototype/osfr-tools/src/lib.rs:20 (`pub mod enemies;`); repo:prototype/osfr-tools/tests/enemies.rs:1 (`use osfr_tools::enemies::{EnemyEngine, ...}`); no `#[path]` in the first 25 lines.

2. `old:` 1. Register `enemies` in the shared library and load `data/content/enemies.json` through the normal content validation path.
   `new:` 1. `enemies` is already registered in the shared library (`pub mod enemies;`); load `data/content/enemies.json` through the normal content validation path.
   `why:` repo:prototype/osfr-tools/src/lib.rs:20. `EnemyEngine::load` already reads `enemies.json` (src/enemies.rs:170-173).

3. `old:` All new levels are null.
   `new:` The W58 definitions 930000..930025 carry the levels in the table above (1, 3, 5, 9 or 13); the W58b and later additions (for example 930033, 930034 and 930079) have `level: null`.
   `why:` repo:prototype/osfr-tools/data/content/enemies.json:153 and :179 (`"level": 5`, `"level": 13`), :1011 and :1037 (`"level": null` on w58b_ghost_miner and w58b_shambler_miner), :2207 (`"level": null` on giant_bat). The note's own table at lines 76-101 already shows non-null levels, so this sentence contradicts it.

4. `old:` Those four remain listed in `definition_field_gaps` and are not represented as client-catalog-verified.
   `new:` The four gaps were closed by the client model table (Models.txt) in W58b. `definition_field_gaps` is now empty and the sidecar records `existing_model_id_gaps: 0`.
   `why:` repo:prototype/osfr-tools/data/content/enemies_unresolved.json:10162 (`"definition_field_gaps": []`) and :76 (`"existing_model_id_gaps": 0`). The note's own line 142 says the same thing, so line 113 is now inconsistent with it.

5. `old:` Exact field-level sources are recorded for all 31 definitions.
   `new:` Exact field-level sources are recorded for every definition in the sidecar (`coverage.total_definitions` is 85 at the tip, including the T015 additions).
   `why:` repo:prototype/osfr-tools/data/content/enemies_unresolved.json:118 (`"total_definitions": 85`), :116 (`"t015_definitions_added": 30`). enemies.json also reaches definition 930079 (giant_bat, line 2203).

6. `old:` contains 53 of the 55 selected files
   `new:` contained 53 of the 55 selected files at W58b; the sidecar now reports 83 of 85 present (`catalog_pairs_missing: 2`).
   `why:` repo:prototype/osfr-tools/data/content/enemies_unresolved.json:79-81 (`client_model_table_pairs_checked: 85`, `catalog_pairs_present: 83`, `catalog_pairs_missing: 2`).

**Checked and holding:**
- `src/enemies.rs` exists. Its `EnemyDefinition` uses `deny_unknown_fields` and has no `abilities` or `loot_table_refs` (enemies.rs:81-103).
- Constants: `MIN_TICK_MS` 100 and `MAX_STEP_MS` 250 (enemies.rs:18-19). Aggro, leash, speed 3.0, attack range 2.5, cooldown 1000 and respawn 30000 match the W36 values in enemies.json:26-31.
- The 1..13 level health and damage formula checks out against the table (for example level 5 normal = 180 HP and 15 damage; boss = 540 and 30).
- New definitions grant zero coins, XP and items (enemies.json reward blocks; only the W36 rows at :34-35 are non-zero).
- `QuestEvent::KillActorKind` and `rewards::apply_grant` are used (enemies.rs:628, :639). The movement writer uses `[1, 0]` (enemies.rs:803).
- The Client reader addresses in the note (00a2a910, 00a2ba40, 008d6f10, 009392c0, 0089d2b0, 00a2a8a0, 00921a10, 0092f460, 0089e670, 008d86e0, 008d8910, 0089d410, 00b8a640, 00b8a300, 008e7930, 00bf9430) all exist in client `fn`/`label`, with labels that match the stated roles.
- `tests/enemies.rs` has six `#[test]`s. `tests/content_enemies.rs` has two.
- Hooligan Wolf's model 3284 is wolf_generic.adr in Models.txt:2470 (cited in the sidecar).

**Unsure:**
- `notes/Design/Build Ledger.md:77` says `enemies.rs / enemies.json` has "55 definitions". The file and sidecar now show 85. That ledger line is outside this note, so I left it alone.
- The W58b coverage table (`Definitions | 31 | 55`) and the "24 definitions" line are accurate as a dated W58b snapshot, so I did not change them.
- The "28 evidence entries across seven definitions" count is confirmed for 28 (`known_ability_evidence_strings: 28`). I did not verify the "seven definitions" part.
- The Native-map disassembly claims (for example the 32/7 handler's argument order) were checked only at the label level, not byte by byte.
