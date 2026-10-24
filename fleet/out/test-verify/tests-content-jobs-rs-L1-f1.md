<!-- fleet job=test-verify id=tests-content-jobs-rs-L1-f1 status=done turns=6 usd=0.0054 tokens(read,write,in,out)=[56734, 20217, 14, 4652] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/content_jobs.rs:163-186

**Verdict:** `refuted`

**Evidence:**

The claim says the test cannot catch "any change that drops real NPCs, breaks the `npcs/` files, or makes the loader stop validating NPC references." The first two are caught by the real-data set assertion the claim itself identifies, and the third is covered by a different test file.

1. **Dropping real NPCs or breaking `npcs/` files is caught.** `tests/content_jobs.rs` builds `referenced_npcs` from real job trainer IDs (lines 84-89), quest giver IDs (line 91) and talk-goal `npc_id`s (lines 92-97). It builds `resolved_ids` from the real `data/content/npcs/*.json` files (lines 99-116). Then line 117-122 asserts:
   `referenced_npcs.iter().all(|id| resolved_ids.contains(id) || unresolved_ids.contains(id))`.
   Walk-through: remove a `npcs/` record for an NPC that a quest gives from, and that NPC is not listed in `npcs_unresolved.json`. Then the ID is in `referenced_npcs`, not in `resolved_ids`, and not in `unresolved_ids`, so the assertion fails. A malformed `npcs/` file hits an `unwrap()` at lines 105-116 and panics. Both regressions fail the test. The only way to pass is if the NPC is also declared unresolved, which is the intended "resolve or are declared" behaviour.

2. **Loader NPC validation is covered elsewhere.** The claim says a loader that stops validating NPC references passes this test. That is true for this test, but the loader's NPC checks have their own tests in `tests/content.rs`. `dangling_references_fail_with_the_owner_field_and_target` (lines 83-101) sets `quests.json` `giver_npc_id` to 999999 and asserts `DanglingReference { owner: "quest 101", field: "giver_npc_id", target: "999999" }`. `missing_zone_references_fail...` (lines 124-143) covers an NPC `zone_id` dangling reference. Removing the `npcs.contains` check at `src/content.rs:749` would fail the first of these. The `trainer_npc_ids` (line 777) and `goal.npc_id` (line 908) checks are not directly exercised by `tests/content.rs`, so that is a partial gap. It is not the regression as claimed, and it is not this test's job.

3. **The synthetic NPC rows do not make the test vacuous.** The synthetic rows only supply the loader's cross-reference check. The real NPC coverage is the set assertion above, which uses real data. The claim's observation that lines 124-127 disable the loader's NPC check is accurate. It does not show that the test is blind to NPC data regressions.

The claim's fix (derive the synthetic NPCs from `resolved_ids` and assert the loader's error set) would be a reasonable hardening. It is not required for this test to catch the regressions it names.
