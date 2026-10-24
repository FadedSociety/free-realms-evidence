<!-- fleet job=test-audit id=tests-npc-greetings-job-hubs-rs-L1 status=done turns=9 usd=0.0086 tokens(read,write,in,out)=[160312, 29088, 20, 6808] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/npc_greetings_job_hubs.rs lines 1-655 of 655

Reviewed `prototype/osfr-tools/tests/npc_greetings_job_hubs.rs` lines 1-655 (with `tests/common/npc_greetings.rs`, `src/npc_interaction.rs` constants, and `src/world.rs` `content_key` / legacy spawn path). The main assertions are real: the service and 26/3 body checks compare against pinned locale ids, the blank-greeting test verifies the refused select does not consume the menu, `content_key` is populated by the loader for legacy rows, and the locale line check reads the physical locale file. No high-severity holes found.

- **[medium] tests/npc_greetings_job_hubs.rs:559 the_existing_greetings_and_other_regions_are_unchanged - the name claims other regions are unchanged, but only the 22 hand-listed `EXISTING_GREETINGS` rows are checked.**
  - Why it cannot catch a regression: a change to any other region's file (e.g. `seaside.json`, `sanctuary.json`, `cobblestone_village.json`) that alters a greeting not in that list, or adds/removes a greeting binding, still passes. The other-row sweep at lines 535-555 covers only `snowhill.json` and `greenwood_forest.json`.
  - Fix: either rename it to `the_listed_existing_greetings_are_unchanged`, or sweep every `content_dir().join("npcs")` file and assert that each `greeting_string_id` equals the `EXISTING_GREETINGS` entry for that `(file, npc_id)` (or absent).

- **[low] tests/npc_greetings_job_hubs.rs:596 the_content_stays_within_the_loader_bounds - the bounds are duplicated as literals (8 MiB, 32 MiB, 20_000) instead of being read from the loader's constants.**
  - Why it cannot catch a regression: `src/npc_interaction.rs:53-55` defines `MAX_NPC_FILE_BYTES`, `MAX_NPC_TOTAL_BYTES` and `MAX_NPCS`. If the loader's bounds are changed, this test keeps enforcing the stale copies, so it can disagree with the real gate. The `let _ = service();` line does not check the bounds itself; it only confirms the load succeeds.
  - Fix: expose the loader's limits as `pub const` and assert against them, or assert directly that `NpcInteraction::load` rejects a synthetic file one byte over `MAX_NPC_FILE_BYTES`.

- **[low] tests/npc_greetings_job_hubs.rs:475 the_target_rows_are_spawned_and_non_target_rows_are_unchanged - `sources.len() == 2` pins the exact provenance-source count.**
  - Why it cannot catch a regression: this is incidental to the greeting binding. Adding a third legitimate source (for example a second verification note) breaks the test without any greeting change. The `kind == client` and `kind == reconstructed` lookups already check what matters.
  - Fix: drop the exact count and keep the two `find` checks plus the `(R)` label check, or assert `len() >= 2`.
