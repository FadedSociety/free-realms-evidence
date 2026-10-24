<!-- fleet job=test-audit id=tests-farnum-starting-quests-rs-L1 status=done turns=6 usd=0.0079 tokens(read,write,in,out)=[90129, 26976, 14, 7336] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/farnum_starting_quests.rs lines 1-830 of 830

Window reviewed: `prototype/osfr-tools/tests/farnum_starting_quests.rs` lines 1-830 (helpers read at `tests/support/npc_quest_chain.rs:529-720`). No `#[ignore]`, no early-return skips, and no test whose expected value is computed from the code under test. The main assertions (saved-state equality, counts, profile XP, reward bytes) do exercise production state. The findings below are the gaps I could confirm.

- **[medium] prototype/osfr-tools/tests/farnum_starting_quests.rs:619-665 the_two_new_records_load_and_their_targets_exist - the name says the targets exist, but the loop only checks that every objective has a non-empty `source`, never that the objective points at the intended definition.**
  - Why it cannot catch a regression: the kill goal could be changed from model 3156 (`quests/adventurer.json:690`) to any other model, or the copper goal from resource 2739 (`quests/adventurer.json:1223`) to the opening-stage key 1003 that the record's own evidence rules out. The loop would still pass, because it only checks `sources(goal)`. The 2739 check at lines 711-719 reads the mining board, not the quest record, so it does not cover the record's objective.
  - Fix: for the two records, assert that the kill objective's `model_id` equals `WOLF_DEFINITION` (3156) and that the copper objective's `resource_id` equals `COPPER_ORE` (2739), and that each objective's count matches the goal the tests use (5).

- **[low] prototype/osfr-tools/tests/farnum_starting_quests.rs:600-606 wrong_job_wrong_target_and_replay_change_nothing - the 49/14 "clean refusal" is checked only with `handle_in_world(...).is_ok()` and a saved-state comparison, and the replies are never inspected.**
  - Why it cannot catch a regression: a change that answers with a 49/3 or 49/4 reply and still leaves the saved state unchanged (for example, a reply-only quest-add that is not persisted) would pass. The `is_ok()` also passes for any `Ok` return, including one that releases a quest-completed packet.
  - Fix: use `assert_packet_changes_nothing(...)`, which already checks `changed == false` and rejects 49/3 and 49/4 replies, in place of the bare `is_ok()` and `saved` comparison.

- **[low] prototype/osfr-tools/tests/farnum_starting_quests.rs:491-496 wrong_job_wrong_target_and_replay_change_nothing / copper_collection_counts_five_gathers_from_the_node_path - the stale-win replay discards its result with `let _ =`.**
  - Why it cannot catch a regression: the replay's error and its reply packets are never inspected, so a change that starts returning an error for a stale win, or that emits a 49/x reply without changing the saved bytes, still passes. Only the serialized-state equality is checked.
  - Fix: assert the result is `Ok` (or assert the exact error) and assert that no 49/1, 49/4 or 49/13 reply appears in its outcome, alongside the existing `saved` equality.

- **[low] prototype/osfr-tools/tests/farnum_starting_quests.rs:279-283, 688-692 and 751-755 - the exact live-wolf population of 7 is pinned in three tests, and the test's claims depend on it.**
  - Why it cannot catch a regression: it is not a logic hole. Any unrelated field-enemy addition or move (for example, another 3156 spawn from a different camp) fails all three tests, even though the counting behaviour under test is unchanged. This is churn rather than a missed bug.
  - Fix: keep one population pin in `the_two_new_records_load_and_their_targets_exist`. In the other two tests, assert that the first five wolves are the starter group and that a kill of any remaining wolf does not advance the count past 5, instead of asserting the total of 7.

- **[low] prototype/osfr-tools/tests/farnum_starting_quests.rs:732-741 the_two_new_records_load_and_their_targets_exist - "Cleetus Farnum is drawn at his spawn" only checks that some 8-byte window of some packet equals the GUID.**
  - Why it cannot catch a regression: the position is the same `cleetus_position()` the test passes in, and the check never inspects the drawn placement. A change that draws the NPC at another location, or in a packet that does not carry the placement, would still pass whenever the GUID bytes appear anywhere in the output.
  - Fix: decode the drawn NPC's position from its spawn packet and compare it with the record's position, or drop the "at his spawn" wording and keep the presence claim.
