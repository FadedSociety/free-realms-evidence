<!-- fleet job=test-audit id=tests-mining-move-detection-rs-L1 status=done turns=12 usd=0.0127 tokens(read,write,in,out)=[241492, 39449, 26, 10790] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mining_move_detection.rs lines 1-248 of 248

Two findings in lines 1-248. The two wildcard regression tests (198-221) are sound: the old flood would report a move, so `reshuffles` would stay 1 and the `assert_eq!(..., 2)` would fail. The fixture board is consistent with `mining_spec()` (playable 3..11, bottom row y=10, goals 601/602), and `has_move` (mining.rs:2087) plus `settle_after_collect` (mining.rs:1677) match what the tests assume.

- **[medium] tests/mining_move_detection.rs:223 valid_three_tile_paths_keep_the_board_and_ignore_idle - the name says the board is kept, but the only assertion is the reshuffle counter.**
  - Why it cannot catch a regression: a change that alters the board without reshuffling still passes. Examples: gravity or collection clearing or shifting the path tiles, a changed `idle` vector, or a stray `OnQuotaUpdateMsg`/score change. `reshuffles` stays 1 in every such case, because `has_move` still finds the path.
  - Fix: after `fall_and_reshuffles`, assert `engine.state().active` `board` equals the expected board (path cells still present at their values, column 7 shifted by the one fall), and that `idle` and `collected` are unchanged except for the fall. Alternatively, rename the test to drop "keep the board". The name currently overclaims.

- **[low] tests/mining_move_detection.rs:167 chain21_snapshot_with_no_legal_path_must_reshuffle - the name says the snapshot has no legal path, but nothing checks that before the fall.**
  - The sha256 pin (line 170) fixes the file, and the reshuffle outcome (line 191) would fail if a legal path appeared after the trigger. The precondition itself is never asserted. The lib's `has_future_move()` is `#[cfg(test)]`, so integration tests cannot reach it. Also, lines 183-186 mutate the frozen board (setting 601 at (7,10) and a 401 tile queue), and the claim that column 7 has no path after refill is commented but not checked.
  - Why it cannot catch a regression: a change to `has_move` that wrongly reports a move on the snapshot is still caught by the reshuffle assertion. A snapshot that had a legal path before the fall, and whose path is not created by the fall, would not be detected as a fixture problem; the test would simply fail with a misleading message.
  - Fix: before the fall, assert the snapshot's pre-fall state directly, e.g. compare against a local three-tile scan over `run.board` with the same bounds, or assert the test's documented precondition in a helper. Otherwise soften the name to "no_move_snapshot_reshuffles_after_trigger".

Not reported: the `#[ignore]` on the snapshot test carries a reason, so it is not a silent skip. The `reshuffles == 2` exact count is the behaviour under test, not incidental.
