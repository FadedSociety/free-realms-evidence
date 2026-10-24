<!-- fleet job=test-audit id=tests-field-kill-rewards-rs-L1 status=done turns=4 usd=0.0085 tokens(read,write,in,out)=[44126, 31329, 10, 8330] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/field_kill_rewards.rs lines 1-789 of 789

Window: `prototype/osfr-tools/tests/field_kill_rewards.rs` lines 1-789. I read the whole window, plus `tests/common/field_reward_fixture.rs`, `data/content/field_kill_rewards.json`, and the loader/credit constants in `src/encounter/field_rewards.rs` (`CREDIT_TTL_MS`, overlap and duplicate-override refusals). Most tests are sound: they compare concrete packets and banks against literal expected values, and the field helpers panic rather than skip. The findings below are the real gaps.

- **[medium] tests/field_kill_rewards.rs:299 `a_credit_expires_and_a_bad_row_changes_nothing` - the name claims a bad reward row leaves state unchanged, but the body only checks that `Gameplay::load` returns `Err`; no game, bank, or field state is compared after the bad write.**
  - Why it cannot catch a regression: a loader change that refuses the bad file but mutates the live session or field (for example by partially applying the bands before the error) still passes, because lines 325-349 never compare `bank`, `game.state()`, or `field_view` after the failed loads. The only bank checks (319-322) run before the bad rows are written.
  - Fix: capture `game.state()` and `field_view(&field, ENEMY)` before the bad writes, then assert both are equal after each refused load. Or rename the test to say it only checks the loader refusals.

- **[medium] tests/field_kill_rewards.rs:690-694 (inside `a_credit_survives_a_reconnect_and_expires_once`) - the "expires" check is made true by the prune at 681, not by the tick's TTL logic.**
  - Why it cannot catch a regression: `retain_casters` at 681 with `second_at + CREDIT_TTL_MS + 1` already removes the credit (asserted at 685-689). The later `tick_shared_effects` at 691 then pays nothing even if the tick ignored the TTL, so the assertion at 693 cannot fail for that reason.
  - Fix: run the expiry tick without the prune first (or on a second credit) and assert it pays nothing and the credit count goes to 0. Keep the prune assertion as a separate check. The tick-side TTL is only covered in the earlier test at 313-322, so this test's name should drop "expires" unless that path is isolated here.

- **[low] tests/field_kill_rewards.rs:325-349 `overlapping bands` / `duplicate overrides` - `Gameplay::load(...).is_err()` accepts any failure, not the specific overlap or duplicate refusal.**
  - Why it cannot catch a regression: if a later edit makes every non-empty `level_rewards` fail to parse, both tests still pass even though the overlap and duplicate rules were never exercised.
  - Fix: assert on the error text, e.g. `.unwrap_err().to_string().contains("overlapping field kill reward bands")` and `"duplicate field kill reward override"`, which are the messages in `src/encounter/field_rewards.rs:166` and `:180`.

- **[low] tests/field_kill_rewards.rs:435 `a_shared_kill_pays...` (overflow test, `assert_eq!(b_after.1.len(), 1)`) - pins the exact number of XP profile entries, which is incidental to the claim that job 43 gets 1 XP and the refused reward pays nothing.**
  - Why it is churn, not a missed bug: any unrelated change that adds a zero or default experience entry for another profile breaks this test without touching the refusal behaviour.
  - Fix: drop the length assertion and keep `b_after.1.get(&43) == Some(&1)` plus an explicit check that no XP is credited to the refused job (`get(&35)` is `None`).
</result>
