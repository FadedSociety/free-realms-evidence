<!-- fleet job=test-audit id=tests-soccer-service-rs-L1 status=done turns=5 usd=0.0073 tokens(read,write,in,out)=[61582, 25417, 12, 7094] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soccer_service.rs lines 1-1003 of 1003

Window reviewed: `prototype/osfr-tools/tests/soccer_service.rs` lines 1-1003. Most tests check real behaviour (wire round-trips, snapshot equality after refused steps, verified-target pass direction, stale-revision refusal). The findings below are the weak spots.

- **[medium] prototype/osfr-tools/tests/soccer_service.rs:742 `disconnect_mid_match_cancels_run_and_never_pays` - the "never pays" check reads a fixture the service never touches (`initial.inventory.state().coins == 0`, and `initial.applied_grant_keys.is_empty()` at line 743), so it cannot fail for a payout bug.**
  - Why it cannot catch a regression: `initial` is built by `reward_state()` and only passed by reference to `finish_minigame`. Nothing the service does can change it, so these asserts pass whatever the service does. The only real payment check is `result.reward_state.is_none()` at line 749, and `finish_minigame` returns early with `RunOutcome::default()` whenever the phase is not `Finished` (`src/soccer_service.rs:760-761`). A cancelled run that was wrongly settled would therefore still be caught only by that line, and the test never checks that the cancelled run's own state stayed `Cancelled` after the finish call.
  - Fix: delete lines 742-743. After line 746, assert `service.run_state(KICKER) == Some(RunState::Cancelled)` so settlement cannot flip the run to `Won`/`Lost`, and assert `result.replies` contains no reward-kind packet.

- **[medium] prototype/osfr-tools/tests/soccer_service.rs:530 `client_owned_score_goal_and_reward_authority_is_refused` - the name claims reward authority is refused, but the body never touches rewards, inventory or `RewardState`.**
  - Why it cannot catch a regression: the test only checks the goal refusal (lines 533-538), the impulse refusal, and that `score()` and `outcome()` are unchanged. A change that let a client-side action grant a reward would pass, because no reward path is called.
  - Fix: either rename the test to cover only goal/score authority, or add a reward assertion: after the client attempts, run `finish_minigame(KICKER, &reward_state())` once the match is driven to `Finished` (or assert `finish_minigame` returns `accepted == false` with no `reward_packets`) and check that the reward state is unchanged.

- **[low] prototype/osfr-tools/tests/soccer_service.rs:554-558 `client_owned_score_goal_and_reward_authority_is_refused` - the sub-13 impulse refusal is checked only with `.is_err()`, so any error passes, including a sender or length error that has nothing to do with the impulse.**
  - Why it cannot catch a regression: a change that refuses this frame for an unrelated reason (for example, a bad outer id) still returns `Err` and still satisfies the state checks that follow. The comment on lines 540-541 says the refusal is about the inbound sub-13 frame, but the test does not check that.
  - Fix: `expect_err` and assert the error text names the impulse or read-only refusal, the same way the neighbouring tests check `"read-only"` and `"target"`.

- **[low] prototype/osfr-tools/tests/soccer_service.rs:617-618 `solo_bots_match_runs_through_shared_lifecycle_to_one_win_payment` - exact roster counts (`bot_count() == 7`, `bots.len() == 14`) are asserted in a test about the match lifecycle and payment.**
  - Why it cannot catch a regression that matters: any change to the bot fill policy, such as a different team size, breaks this test even though the payout and lifecycle are unchanged. This is churn rather than a missed bug.
  - Fix: keep one check that the roster is non-empty and that the human is on the team with the bots, or move the exact count into a dedicated roster test.

No `#[ignore]` attributes or missing-fixture early returns appear in this window.
