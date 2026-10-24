<!-- fleet job=test-audit id=tests-piece-019-rs-L1 status=done turns=4 usd=0.0055 tokens(read,write,in,out)=[21065, 15603, 10, 6707] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_019.rs lines 1-312 of 312

Window: `prototype/osfr-tools/tests/piece_019.rs` lines 1-312, checked against `src/restoration/piece_019.rs` (commit, rows, page_payload, load/save, constants).

- **[high] prototype/osfr-tools/tests/piece_019.rs:153 a_score_is_only_written_from_a_finished_server_session - the test never looks at the board, so a write that happens before the "not finished" refusal goes unnoticed.**
  - Why it cannot catch a regression: at line 176, `commit(session, 10)` on an unfinished session is expected to return `SessionNotFinished`, but nothing checks that the board is still empty. If `commit` were changed to insert the record before the finished-check, line 176 would still return the error. The later `commit(session, 10)` at line 186 would then return `Ok(Recorded)` and insert the same value, so every assertion still passes. The same gap applies to the `InvalidValue` refusals at lines 181 and 183. The test name says scores are only *written* from a finished session, but no assertion checks a written score (`rows(BOARD)` is never called).
  - Fix: after each refused commit (lines 170, 176, 181, 183), assert `store.rows(BOARD).is_empty()`. Or assert `rows(BOARD)` is empty right after line 176 and only has one row of value 10 after line 186.

- **[medium] prototype/osfr-tools/tests/piece_019.rs:149 elapsed_seconds_rank_low_to_high_with_the_time_type_code - the expected `Type` code is taken from the constant the code under test uses.**
  - Why it cannot catch a regression: `format!("Type^{SCORE_TYPE_ELAPSED_SECONDS}")` expects whatever `SCORE_TYPE_ELAPSED_SECONDS` is, and `encode_rows` writes `kind.type_code()`, which returns that same constant (piece_019.rs:59). Changing the constant to 3 (or any other value) keeps the test green, even though the header says the client contract is `Type` 2 for elapsed seconds. The points case is pinned by the literal `Type^1` at line 109, so only the elapsed code is affected.
  - Fix: assert the literal `"Type^2"` (for example `assert!(payload.contains("Type^2"))`), and do the same with a literal in the `rows[0][5]` check at line 118.

- **[medium] prototype/osfr-tools/tests/piece_019.rs:183 a_score_is_only_written_from_a_finished_server_session - the ceiling is only tested relative to the constant, and the accepted boundary is never tested.**
  - Why it cannot catch a regression: `MAX_DISPLAYED_VALUE` (piece_019.rs:41, documented as the ten-digit client ceiling) is only probed as `MAX + 1`, which is rejected. No test commits `MAX_DISPLAYED_VALUE` and expects `Ok`, and no test pins the constant to `9_999_999_999`. Raising the ceiling to `i64::MAX` (or lowering it to 999) would keep every assertion in this file green, while the doc says the ceiling is recovered from the client's ten-digit fields.
  - Fix: add `assert_eq!(commit(session, 9_999_999_999), Ok(Recorded))` in a fresh session at the boundary, and assert the literal `9_999_999_999` (not the constant) is the ceiling, e.g. `assert_eq!(MAX_DISPLAYED_VALUE, 9_999_999_999)`.

- **[medium] prototype/osfr-tools/tests/piece_019.rs:261 pages_are_sliced_by_row_offset_and_report_the_total_count - the "ten rows per page" contract is not pinned, only compared with the constant.**
  - Why it cannot catch a regression: the header (line 12) and the module doc (piece_019.rs:38-39) say the high-score list renders ten rows per page, but `HIGH_SCORES_PAGE_ROWS` is used on both sides of every check here (lines 255, 261, and the `count` bounds at piece_019.rs:303). Changing the constant to 5 keeps the file green, and it would also make the "page too large" check reject 6 rows, which is not the client contract.
  - Fix: add `assert_eq!(HIGH_SCORES_PAGE_ROWS, 10)` (a literal, not the constant on both sides), and check that `page_payload(BOARD, 0, 10)` succeeds while `page_payload(BOARD, 0, 11)` returns `InvalidPage`.

- **[low] prototype/osfr-tools/tests/piece_019.rs:219-240 one_entry_per_character_keeps_the_better_value - the elapsed-seconds half checks only the outcomes, not the stored value.**
  - Why it cannot catch a regression: the points half checks `rows[0].value == 150` (line 208), but the `TIME_BOARD` half never inspects the stored row. A change that records the `KeptBest` value 250 in storage while still returning `KeptBest`, or a change that stores 300 instead of 200, would pass.
  - Fix: after line 229, assert `store.rows(TIME_BOARD)[0].value == 200`, and after line 240 assert it is still 200.

Nothing in the window uses `#[ignore]` or an early return, so there are no silently skipped tests. The payload-format test at lines 99-121 pins a literal string and is not circular.
