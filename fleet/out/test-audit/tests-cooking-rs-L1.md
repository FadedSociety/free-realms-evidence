<!-- fleet job=test-audit id=tests-cooking-rs-L1 status=done turns=5 usd=0.0095 tokens(read,write,in,out)=[57756, 28916, 12, 10540] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/cooking.rs lines 1-598 of 598

Reviewed `prototype/osfr-tools/tests/cooking.rs` lines 1-598 against `src/cooking.rs` (`load` 144-174, `validate_state` 191-254, `begin_recipe` 277-320, `handle` 355-576, `cancel` 338-353). Most assertions are real: the sentinel gating, stat-suffix and round-ordering checks, and the replay/restore checks all exercise live validation. The findings below are the weak spots.

- **[medium] tests/cooking.rs:469 content_and_saved_state_reject_unlabelled_or_inconsistent_recipe - the name promises rejection of inconsistent saved recipe state, but no saved state with a bad recipe key is ever loaded.**
  - Why it cannot catch a regression: `load` rejects `state.active_recipe_key` that is not in `recipes` (cooking.rs:161-167), and `validate_state` rejects an empty key (cooking.rs:195-198). Neither is exercised here. Removing either check still passes, because the only saved-state rejections in this test come from stat mutations (lines 487-491). The only recipe-key rejection in the test is the content-level `chef.unknown` at line 476-478, which is not saved state.
  - Fix: after a `begin_recipe` run, clone the state, set `active_recipe_key = Some("chef.unknown")`, and assert `Cooking::load(&f.path, Some(state)).is_err()`. Add a second case with `Some(String::new())` and assert that it errors too.

- **[medium] tests/cooking.rs:419 native_results_wait_for_actual_close_ack_and_replays_preserve_recipe - the test never checks that the GameWon transaction is granted, so dropping the reward from the native path passes.**
  - Why it cannot catch a regression: line 430 binds `won` but only checks its replies. Nothing asserts `won.transaction` is `Some` with the expected `consumes`/`grants`/`experience_points`. The later `close.transaction.is_none()` (line 463) only proves close is not the grant point. If `GameWon` stopped producing a transaction (cooking.rs:526-531 removed, or the `out.transaction` assignment dropped), `completed` would still advance, and the test would still pass unless close also emits something.
  - Fix: assert `let t = won.transaction.as_ref().unwrap()` with `t.consumes == g-recipe requirements` and `t.grants == vec![(35, 1)]` before the close step. Keep the existing `close.transaction.is_none()` check.

- **[low] tests/cooking.rs:575 every_cooking_catalog_recipe_uses_exact_transaction_once - `assert_eq!(tested, 26)` pins the catalog row count, which churns with unrelated content edits.**
  - Why it cannot catch a regression: the count only changes when recipes are added or removed in `recipes.json`. It does not test the cooking transaction logic, so it adds churn and no protection beyond the non-empty guard.
  - Fix: replace it with `assert!(tested > 0)`, or assert that every `chef` row in the file was visited by counting them in a separate pass over the same JSON.

- **[low] tests/cooking.rs:129 captured_native_go_sentinel_starts_only_the_matching_offered_instance - `replies.len() == 8` pins the ready-data reply count, which is unrelated to the sentinel-gating claim.**
  - Why it cannot catch a regression: the assertion would only change if the phase-data message count changes (cooking.rs:446-453), and that is not what this test is about. It also means that a real gating regression that happened to keep 8 replies would still pass, so the count does not prove the sentinel was accepted.
  - Fix: assert `replies[0]` is the `OnGameDataMsg` packet and that `replies.last()` is the `OnDataComplete` packet, and drop the exact-length check.
