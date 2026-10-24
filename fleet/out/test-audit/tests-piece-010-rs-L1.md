<!-- fleet job=test-audit id=tests-piece-010-rs-L1 status=done turns=5 usd=0.0053 tokens(read,write,in,out)=[42809, 19318, 12, 4932] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_010.rs lines 1-383 of 383

Window reviewed: `prototype/osfr-tools/tests/piece_010.rs` lines 1-383, checked against `src/restoration/piece_010.rs` (all 596 lines). Most tests are sound: the opcode and constant pins compare against literals, the replay/out-of-order test changes state and checks it, the snapshot round-trip compares against an independently built match, and the rejected-event tests check the state afterwards. Three tests overclaim their names.

- **[medium] tests/piece_010.rs:265 the_winner_receives_the_reward_named_by_that_deck_row_only_once - the name says "only once", but `reward_card` is a stateless read and the body only checks that repeated reads return the same card.**
  - Why it cannot catch a regression: the module has no grant ledger (`reward_card(&self, ...)` takes `&self` and records nothing), so nothing in the test could detect a caller paying twice. A change that makes `reward_card` pay out only on the first call would not be caught, and neither would a change that makes it pay on every call. The test passes either way, because it only checks the value returned by a second read.
  - Fix: either rename the test to say it grants nothing after the match finishes (for example `reward_is_withheld_after_a_rejected_post_game_event`), or add a test that exercises a real once-only mechanism if the gateway owns one. Do not claim "once" for a function with no state.

- **[low] tests/piece_010.rs:254 a_match_target_must_be_reachable_in_whole_point_events - the name is about point events, but the body only checks that `TcgMatch::new` accepts targets 1..=WIN_SCORE and rejects 0 and 13.**
  - Why it cannot catch a regression: no point event is applied anywhere in the test, so a change that stops a target of 1 or 12 from being reachable with whole-point events (for example, `apply_points` rejecting a valid final event) would still pass.
  - Fix: rename the test to `a_match_target_must_be_in_the_recovered_range`, or add a check that a target of 1 is won by one `apply_points(side, id, 1)` and that a target of 12 is won by exactly 12 points in one event, with `Phase::Finished` and `winner` asserted.

- **[low] tests/piece_010.rs:355 an_out_of_range_snapshot_is_rejected - the second case is a structural rejection (finished with no winner), not an out-of-range value, so the name only covers half of what the body tests.**
  - Why it cannot catch a regression: the test name misleads a reader about what is covered, so a change that loosens the `(true, None)` arm to accept a finished match with no winner would be missed by anyone reading only the name. It also leaves `last_event_id < 0` (`from_snapshot` line 458) with no test at all, and the name does not signal that gap.
  - Fix: rename to something like `malformed_snapshots_are_rejected`, and add a case with `last_event_id: -1` and `InvalidSnapshot` expected.
