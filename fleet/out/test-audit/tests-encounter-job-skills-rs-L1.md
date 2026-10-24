<!-- fleet job=test-audit id=tests-encounter-job-skills-rs-L1 status=done turns=4 usd=0.0046 tokens(read,write,in,out)=[24875, 16361, 10, 4705] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/encounter_job_skills.rs lines 1-426 of 426

Window: `prototype/osfr-tools/tests/encounter_job_skills.rs` lines 1-426. Four findings. I did not verify the wire constants (e.g. the `287` cooldown byte at line 104), so I did not report them.

- **[medium] prototype/osfr-tools/tests/encounter_job_skills.rs:107 area_damage_hits_each_in_radius_once_and_honours_target_limit - the name promises "each in radius once" but the body only counts hits and checks a lower damage bound.**
  - Why it cannot catch a regression: the fixture's three enemies (guids 100-102) all sit within radius 6 of the caster. A change that hits the same enemy twice, or that hits a non-target (e.g. the caster or an out-of-radius enemy), still yields two replies with damage `>= 337`, so the test passes.
  - Fix: collect the target guid of each hit (the attacker/target field in the reply, via the same offset logic as `hits_from`). Assert the guids are exactly two distinct values, each in `100..=102`. Optionally assert the damage equals the exact expected value rather than `>= 337`.

- **[medium] prototype/osfr-tools/tests/encounter_job_skills.rs:151 stun_stops_attacks_and_movement_until_exact_expiry - the name claims movement is stopped, but the body never checks movement.**
  - Why it cannot catch a regression: the test only checks that no hits happen at 1900 ms and that hits resume at 2000 ms. An implementation that stops attacks but still moves the stunned enemy (the stun check in `encounter/field.rs:896` is the movement path) passes unchanged.
  - Fix: snapshot the stunned enemy's position (or its motion state) before the stun window and assert it is unchanged at t=1900 ms. Alternatively, rename the test to drop "movement" if movement is out of scope.

- **[medium] prototype/osfr-tools/tests/encounter_job_skills.rs:268 invalid_range_cooldown_and_unavailable_summon_do_not_spend_or_damage - the name mentions a summon, but no summon is exercised; the "unavailable" branch only asserts that no damage was dealt.**
  - Why it cannot catch a regression: line 277 sets `a.unavailable = true` and asserts only `is_empty()` on the hit damages. Any silent no-op, including a bug that stops all skill use, passes. The test also never checks that the skill is still castable after the rejected range attempt, beyond the cooldown check at line 275.
  - Fix: for the unavailable case, assert the specific reply or feedback that the engine emits for an unavailable skill, and assert that the cooldown/state is unchanged (e.g. re-enable the skill and confirm it hits immediately). Rename or split the test so the summon claim is either tested or removed.

- **[low] prototype/osfr-tools/tests/encounter_job_skills.rs:94 self_heal_clamps_and_scales_with_the_existing_hp_curve - the name says it checks clamping and scaling, but the body only checks that health is full afterwards.**
  - Why it cannot catch a regression: the 250 heal fills the gap here, so `health == max` holds whether heal is clamped, unclamped, or scaled to the HP curve. A change that heals a wrong amount (for example, ignoring the level-based HP curve) still passes as long as the gap is under 250.
  - Fix: record `before.0` and `before.1`, then assert the healed amount equals `min(250, before.1 - before.0)` (or the exact curve-based value). Add a second case with a gap larger than 250 so the clamp is actually exercised.
