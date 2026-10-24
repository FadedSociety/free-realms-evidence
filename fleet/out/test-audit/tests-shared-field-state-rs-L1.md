<!-- fleet job=test-audit id=tests-shared-field-state-rs-L1 status=done turns=5 usd=0.0096 tokens(read,write,in,out)=[58538, 31936, 12, 9972] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/shared_field_state.rs lines 1-1176 of 1176

Window: `prototype/osfr-tools/tests/shared_field_state.rs` lines 1-1176. Read in full; also read `world.rs` (prepare_membership / field_for_player signatures) and the `encounter/shared.rs` and `gameplay.rs` entry points. Not every test has a finding; the ones below are the real holes.

- **[medium] prototype/osfr-tools/tests/shared_field_state.rs:228 two_players_do_not_accelerate_motion_or_enemy_attack_clock - `assert_ne!(field.position(M), Some([0.,0.,0.]))` passes when the marker is missing from the shared field.**
  - Why it cannot catch a regression: if the swap drops the marker's walk, `field.position(M)` becomes `None`, and `None != Some([0,0,0])` still passes. The message "the marker's walk is swapped into the shared field" is therefore not what is checked.
  - Fix: assert `field.position(super::M).is_some()` and that it differs from the origin (e.g. `assert!(matches!(field.position(M), Some(p) if p != [0.,0.,0.]))`). Keep the line-224 equality against `control`, which does catch a missed swap on its own.

- **[medium] prototype/osfr-tools/tests/shared_field_state.rs:462 refused_shared_ability_leaves_skill_effects_untouched (assertions at 496-503) - the refused casts re-apply the same debuff that A already holds, so the final "400" cannot show that a refusal mutated skill state.**
  - Why it cannot catch a regression: a refused `b` cast with the same `target_debuff(30000)` at 1300 or 1300-with-NaN could refresh the debuff's expiry, reset its timer, or re-stack it. A is still hit at 400 either way, and no expiry is checked after the refusals.
  - Fix: use a refused debuff with distinct values (different `damage_taken_multiplier` or duration), or assert the debuff's expiry by attacking A just past 700+30000 (expect 100 if the refusal had no effect, but a refresh would still hit 200). Also assert B's cooldown/attack clock is unchanged after the refused casts.

- **[medium] prototype/osfr-tools/tests/shared_field_state.rs:1146-1149 two_bot_socket_shared_hp_route - the "foreign-instance" refusal is not isolated; B was already unequipped at 1073 and never re-armed.**
  - Why it cannot catch a regression: the final cast by B at 1146 is refused because B is unarmed, which is the refusal at 1073-1077. If the instance-binding check at the field-access point were removed, B's cast would still be refused, so the test passes. The printed receipt at 1151 ("foreign-instance requests refused") is therefore not proven.
  - Fix: re-equip B (or use a player who still has a weapon) before the cross-instance cast, and assert the refusal while B is armed and A is in the other run. Add a positive control: the same cast from B's own instance must land (HP changes) to show the refusal is caused by the instance.

- **[medium] prototype/osfr-tools/tests/shared_field_state.rs:357 area_and_dot_damage_share_hp_and_never_deliver_personal_credit (assertion at 394) - the name says personal credit is never delivered, but the body asserts the caster's engine reports two defeats.**
  - Why it cannot catch a regression: the body's `out.defeated == [930108, 930108]` is the opposite of the name. The comment at 352-355 explains the split (reward vs. defeat credit), but a reader or a future change that drops personal defeat reporting would be judged against a name that says the opposite.
  - Fix: rename to reflect what is asserted (e.g. `..._share_hp_and_defer_reward_payout`), or assert the reward payout explicitly (`rewards.is_empty()` plus `completed.is_none()` at 395 already covers it) and keep the name to the reward half only.

- **[low] prototype/osfr-tools/tests/shared_field_state.rs:1014-1016 two_bot_socket_shared_hp_route - exact per-client counts (`actor_packets(...,2,E) == 1`, `hp_values == vec![300]`) pin the startup burst.**
  - Why it is churn, not a missed bug: any unrelated change to the startup packet set (an extra 35/2 spawn for another actor or an extra HP refresh) breaks the test even though the shared-HP behaviour is correct.
  - Fix: filter to the E guid and assert `>= 1` plus that every hp value is 300, keeping only the duplicate-delivery check that the later exact-count asserts rely on.
