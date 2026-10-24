<!-- fleet job=test-audit id=tests-content-jobs-rs-L1 status=done turns=4 usd=0.0046 tokens(read,write,in,out)=[21805, 16086, 10, 4646] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/content_jobs.rs lines 1-195 of 195

Window: `prototype/osfr-tools/tests/content_jobs.rs` lines 1-195. Read the window in full, plus `src/content.rs` 700-800 and 880-920 to confirm what `ContentDb::load` validates.

- **[high] prototype/osfr-tools/tests/content_jobs.rs:163-186 and 188 `job_batch_loads_and_npc_references_resolve_or_are_declared` - the `ContentDb::load` step cannot fail on NPC references because the test synthesizes an NPC row for every key it is about to check.**
  - Why it cannot catch a regression: `npc_rows` is built from `referenced_npcs`, the same set of giver, trainer and talk-goal NPC IDs that the loader checks. So `src/content.rs:749` (`giver_npc_id`), `:777` (`trainer_npc_ids`) and `:908` (`goal.npc_id`) always find their target. Any change that drops real NPCs, breaks the `npcs/` files, or makes the loader stop validating NPC references still passes the loader step. The only real NPC check is the set test at lines 117-122, and it is the only assertion in the test that can fail on NPC data. The loader portion adds the claimed "resolve" coverage in name only. Line 124-127 admits the synthetic rows exist "only so the unchanged loader can check every numeric relationship", which means the NPC part of that check was disabled.
  - Fix: build `npcs.json` from the real `npcs/` records (`resolved_ids`), not from `referenced_npcs`. Then assert that `ContentDb::load` fails with an NPC-reference error for exactly the unresolved IDs, or that the load succeeds only when the set of referenced-but-unresolved IDs equals `unresolved_ids`. Either form fails if a real NPC is removed or the loader stops checking.

- **[low] prototype/osfr-tools/tests/content_jobs.rs:191-194 `job_batch_loads_and_npc_references_resolve_or_are_declared` - the "declared" half is never checked in the reverse direction, and the only use of `unresolved_ids` is a `println!`.**
  - Why it cannot catch a regression: `npcs_unresolved.json` can list an ID that now resolves in `npcs/`, or list an ID that no job or quest references, and the test still passes. The count is printed, not asserted.
  - Fix: assert `unresolved_ids.is_subset(&referenced_npcs)` and `unresolved_ids.is_disjoint(&resolved_ids)`, so a stale declaration fails the test.

- **[low] prototype/osfr-tools/tests/content_jobs.rs:82 `job_batch_loads_and_npc_references_resolve_or_are_declared` - pins the raw directory entry count of `quests/` at 18, including non-JSON entries that the loop at lines 63-67 skips.**
  - Why it cannot catch a regression: it is not about the quest content. Adding a README or a `.bak` file breaks the test, while a quest file that fails to parse would not change the count at all.
  - Fix: assert the number of `*.json` files that were actually parsed (count inside the loop), or drop the count assertion.

- **[low] prototype/osfr-tools/tests/content_jobs.rs:60, 189 `job_batch_loads_and_npc_references_resolve_or_are_declared` - the exact job count of 17 is pinned twice, in the input file and in the loaded DB.**
  - Why it cannot catch a regression: a change to the job catalogue that is unrelated to NPC references (a job added or a job renamed) fails here as churn. The line-189 check repeats the line-60 check and adds no coverage, since both read the same `jobs` input.
  - Fix: compare `db.jobs.len()` with `jobs["records"].len()`, and keep only one fixed-count canary if the batch size is meant to be pinned.
