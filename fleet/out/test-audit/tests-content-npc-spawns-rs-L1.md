<!-- fleet job=test-audit id=tests-content-npc-spawns-rs-L1 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[9073, 11353, 8, 3432] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/content_npc_spawns.rs lines 1-250 of 250

Window reviewed: `prototype/osfr-tools/tests/content_npc_spawns.rs` lines 1-250. Three findings, one of them a real coverage hole.

- **[medium] prototype/osfr-tools/tests/content_npc_spawns.rs:131-133 npc_spawn_models_names_positions_and_capture_matches_are_valid - every regional NPC that is not `legacy_data_spawn` is only counted; its model, name, position and heading are never checked.**
  - Why it cannot catch a regression: the `else` branch only does `regional_reconstructed += 1`. Any change that breaks reconstructed rows (a model file missing from the catalog, a `name_string_id` absent from the locale table, a NaN or 2-component position, a non-finite heading) still passes as long as the total row count stays at 1201. The data has many such rows (for example `data/content/npcs/blackspore_swamp.json` has several `reconstructed_zone_center` and `reconstructed_poi_name_match` entries), so most regional NPCs are unvalidated.
  - Fix: move the `model_file_name` catalog check, the `name_string_id` locale check, the heading check and `finite_xyz(row, &owner)` out of the `legacy_data_spawn` branch so they run on every regional row. Keep only the Legacy-specific provenance and `placement == "legacy_data"` assertions inside the branch. Then a reconstructed row with a bad model or position fails the test.

- **[low] prototype/osfr-tools/tests/content_npc_spawns.rs:243-244 npc_spawn_models_names_positions_and_capture_matches_are_valid - exact row counts (`extra_rows.len() == 3301`, `captured_actors.len() == 9`) are pinned to values that unrelated content appends change.**
  - Why it cannot catch a regression: these counts only fail when someone adds or removes a spawn row, not when a row's data is wrong. The comments on lines 240-242 show this churns with every content task. The assertion is about the validity of each row, which the loop at lines 141-223 already checks.
  - Fix: keep a floor (for example `extra_rows.len() >= 3301`) or derive the expected value from a single named constant that is updated in one place. Leave the per-row checks to do the real work.

- **[low] prototype/osfr-tools/tests/content_npc_spawns.rs:229-230 npc_spawn_models_names_positions_and_capture_matches_are_valid - `assert_eq!(broken_model_rows.len(), 3)` pins the number of `knocker_m_boss.adr` rows, and the following `!catalog_names.contains("knocker_m_boss.dme")` does not touch any extra row.**
  - Why it cannot catch a regression: the count fails on any unrelated change to those rows, and the `.dme` negative check tests the catalog file contents, not the spawn data. Neither proves the three rows are handled correctly, and the body never states the purpose of the "broken" label.
  - Fix: drop the exact count, or assert that each of those rows has a `model_id` whose `models` entry maps to `knocker_m_boss.adr` (which the loop at 151-156 already does). Add a comment that says what the `.dme` negative check guards, or remove it.

No `#[ignore]`, no early returns, and no fixture-missing passes were found in the window. The `models` lookup (lines 151-156) fails on an empty table, so it cannot pass silently.
