<!-- fleet job=test-audit id=tests-mining-rs-L1 status=done turns=5 usd=0.0087 tokens(read,write,in,out)=[83215, 32015, 12, 7815] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mining.rs lines 1-1138 of 1138

Window: `prototype/osfr-tools/tests/mining.rs` lines 1-1138. Checked against `src/mining.rs` (`collect_fall` at 1554-1586, load game-id check at 318, `write_content` at 1052-1055, `COPPER_MINING_GAME_ID`/`SIDE` at 50/60).

- **[high] prototype/osfr-tools/tests/mining.rs:569 a_fall_that_is_not_the_bottom_row_or_not_a_collectable_is_rejected - the "not the bottom row" branch is never exercised; both rejected falls are on non-collectable cells.**
  - Why it cannot catch a regression: the first call targets `(LEFT, TOP)` (row 0, a plain value-1 cell, not a goal). The second targets `(LEFT+1, TOP+7)` (bottom row, value 1, also not a goal). Both fail on the goal lookup at `mining.rs:1586`, so deleting the `y != bottom` / `!in_board` guard at `mining.rs:1565-1566` still passes. The only collectable (`rows[7][0] = ORE`) is never reported off-row.
  - Fix: add a call that reports a real collectable from a non-bottom row, e.g. put `-ORE` at `rows[6][1]` and send `OnLevelEventMsg\t50\t{LEFT+1}\t{TOP+6}`, asserting `is_err()` and that `engine.state()` is unchanged. Keep the bottom-row, non-goal case as a separate check.

- **[medium] prototype/osfr-tools/tests/mining.rs:782 copper_mining_gets_its_own_instance_namespace - the name claims an instance-namespace check, but the load fails only because the file's game id is 18, not 91.**
  - Why it cannot catch a regression: `mining.rs:318` rejects `content.game_id != game_id` before any instance logic runs. The `91_000_001` instance id is never checked, so a change that drops or breaks the instance-namespace handling still passes. Lines 792-793 are constant-versus-constant assertions (`MINING_GAME_ID != COPPER_MINING_GAME_ID`, `TILE_COLLECTABLE_START == 600`) and cannot fail on their own.
  - Fix: write a fixture with `game_id: COPPER_MINING_GAME_ID` (or make the load accept it deliberately, matching `write_content`'s refusal). Assert the exact error kind/message from the game-id check, and for the namespace claim assert that `begin` on a copper engine emits instance ids in the `91_000_xxx` range, not `18_000_xxx`. Otherwise rename the test to "copper game id refused at load".

- **[medium] prototype/osfr-tools/tests/mining.rs:319 chain_must_be_orthogonal_distinct_matching_and_on_the_board - the "different selectable value" case is rejected for non-adjacency, so the value-match rule is never isolated.**
  - Why it cannot catch a regression: the case `x,y, x+1,y, x+3,y` (line 347) has a gap between `x+1` and `x+3`. It fails the adjacency check first, whatever the values are. Removing the "chain tiles must share a value" check would leave this test green.
  - Fix: use an adjacent third tile with a different selectable value, e.g. `x,y, x+1,y, x+2,y` with `rows[5][2] = -402` (the chain is then `401,401,402`), and assert the rejection is about the value. Keep the gap case as its own assertion.

- **[medium] prototype/osfr-tools/tests/mining.rs:643 loss_on_timer_expiry_is_authoritative_and_quit_only_cancels_before_a_win - the name promises a quit-versus-win check, but the body never quits after a win.**
  - Why it cannot catch a regression: the only quit (line 654) happens after a timer loss, and the window contains no quit after `OnNextLevelMsg`/completion. A change that lets a post-win quit cancel or refund the run passes. `ordinary_quit_cancels_only_a_pre_win_active_run` (line 671) has the same gap: its name says "pre-win" but no win occurs there.
  - Fix: in a win-path test, after the `completed` outcome at line 616, send `header(6, id, -1)` and assert the run is still complete (`completed == 1`, `transaction.is_none()`, and no `39,0,19` cancel reply). Otherwise shorten the name to "quit after loss is a no-op".

- **[low] prototype/osfr-tools/tests/mining.rs:812 default_mining_spec_is_consistent_and_marks_reconstructed_rules - pins content tuning values (`collectable_percent == 40`, quotas `[6, 6]`, `outputs.len() == 2`) that are unrelated to the test's consistency and reconstructed-rules claim.**
  - Why it matters: any balance change to the default mining board breaks this test even though no consistency rule is violated, which causes churn.
  - Fix: keep the structural invariants (goal values in `collectable`, `per_reward >= 1`, `quota >= per_reward`, which the loop at 807-811 already covers) and move the exact tuning numbers into a separate test named for the content values, or assert them only against a constant from `mining.rs`.
