<!-- fleet job=test-audit id=tests-quest-save-tolerance-rs-L1 status=done turns=5 usd=0.0052 tokens(read,write,in,out)=[44748, 17199, 12, 5198] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/quest_save_tolerance.rs lines 1-486 of 486

Window reviewed: `prototype/osfr-tools/tests/quest_save_tolerance.rs` lines 1-486. I checked the code under test in `src/quest_engine.rs` (`from_content_db` min_level validation around line 2147) and confirmed the `tests/fixtures/content` directory exists. Most tests exercise real behaviour. The findings below are the ones that hold up.

- **[medium] tests/quest_save_tolerance.rs:420 invalid_authored_requirement_fields_fail_closed - every case asserts only `.load(...).is_err()`, with no valid control in the loop, so any load failure passes.**
  - Why it cannot catch a regression: if `SplitFixture::new` or `from_split_content` starts failing for every input (a broken fixture copy, a schema change, an unreadable jobs.json, or an empty catalogue such as the "split quest catalogue is empty" error at quest_engine.rs:880), all nine cases still return Err and the test stays green. It never shows that the rejection is specific to the bad field.
  - Fix: add `json!({"min_level":20})` (and a valid job such as `{"job":43}`) to the same loop and assert `is_ok()` for it. Also match the error text or kind for the bad-field cases, for example that it contains "min_level" or "job", so an unrelated error cannot satisfy them.

- **[low] tests/quest_save_tolerance.rs:188 completed_quests_stay_completed_and_unchanged_without_drift - the name promises no drift, but the body asserts that counts are rewritten.**
  - Lines 206-207 assert `counts == vec![2; goals]` (so counts are rebuilt to the authored goal count), and lines 213-215 assert that a Completed quest's counts change from `[2]` to `[3]` after the requirement is edited. The only real "unchanged" check is `engine.state() == &saved` at line 197.
  - Why it cannot catch a regression: a change in the requirement-repair logic that rewrites counts would be asserted as expected, and the name's claim of no drift is never tested in the cases that could drift.
  - Fix: rename the test to say that counts are re-derived from the authored goal count (for example `completed_quests_stay_completed_and_rederive_counts`), or split the drift-free case from the re-derive case, and assert the status and the absence of changes for the no-drift case.

- **[low] tests/quest_save_tolerance.rs:470 round70_saves_load_against_current_repository_content - the sidecar branch's "source bytes unchanged" check is a no-op.**
  - Line 461 reads `bytes`, lines 462-469 only write the scratch copy and parse the JSON, and line 470 re-reads the same file and compares it with `bytes`. Nothing that could modify the source runs in between, so the check cannot fail. The later check at line 479 is meaningful; this one is not. The sidecar branch also never loads anything.
  - Why it cannot catch a regression: a change that writes to the source file inside `game_store::load_or_create` or `Gameplay::load` is not on this path, so this assertion would still pass.
  - Fix: either drop line 470, or move the byte-equality check after the load for every input, including sidecars, so that it covers the operations that could touch the source.
  - Note: the test is `#[ignore]` with a stated reason, and the reason is acceptable, so I am not reporting the ignore itself.
