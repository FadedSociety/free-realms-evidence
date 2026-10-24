<!-- fleet job=test-audit id=tests-field-camps-elite-band-rs-L1 status=done turns=5 usd=0.0088 tokens(read,write,in,out)=[63931, 28769, 12, 9071] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/field_camps_elite_band.rs lines 1-1080 of 1080

Window reviewed: `prototype/osfr-tools/tests/field_camps_elite_band.rs` lines 1-1080. No `#[ignore]` and no early-return skips. The fixtures it uses (`tests/common/field_enemy_fixture.rs`, `tests/common/field_reward_fixture.rs`) exist. The respawn logic is in `src/encounter/field.rs:836` (`now_ms >= at`, with `at = kill + respawn_ms` from `field.rs`/`encounter.rs:1988`).

- **[medium] prototype/osfr-tools/tests/field_camps_elite_band.rs:806 a_level_twenty_kill_pays_the_14_20_band_once (respawn block, ~lines 806-827) - the comment says the respawn is "not one millisecond early", but the test only probes 100 ms before and 100 ms after the 180 s due time.**
  - Why it cannot catch a regression: a change such as `now_ms + 200 >= at`, or a due time shifted by up to about 99 ms, still passes, because the tests at `killed_at + 179_900` (still dead) and `+180_100` (alive) both hold. The boundary the name and comment promise is never exercised.
  - Fix: assert `field.health(guid) == Some(0)` at `killed_at + ELITE_RESPAWN_MS - 1`, and assert full health at exactly `killed_at + ELITE_RESPAWN_MS`. Use a tick timestamp that lands on those exact values (or call the tick at them directly) so the boundary is pinned.

- **[medium] prototype/osfr-tools/tests/field_camps_elite_band.rs:1027 the_uncovered_reward_level_or_definition_override_does_not_pay - the name says the definition override does not pay, but the second half asserts the 3156 override pays 2 coins and 5 XP.**
  - Why it cannot catch a regression: the test name and the body disagree, so a reader (or a later edit) relying on the name would believe the override path is refused. Only the uncovered-level half actually tests "does not pay"; the override half tests the opposite.
  - Fix: split into two tests named for what they check (e.g. `uncovered_reward_level_does_not_pay` and `definition_3156_override_pays_two_at_level_twenty`), or rename this one to match the body.

- **[medium] prototype/osfr-tools/tests/field_camps_elite_band.rs:831 a_malformed_or_duplicate_elite_camp_is_refused_atomically (reward half, lines 886-896) - the name and the comment claim "refused atomically" and "the previous table is restored before the field is used", but the reward half only checks `EncounterEngine::load(...)` is_err and then is_ok, and never uses the field or any payout after restore.**
  - Why it cannot catch a regression: a loader that partially mutates state before rejecting the malformed table, or a restore that leaves the field or payouts stale, would still pass. Also the malformed table is a reward table, not an elite camp, so the name overclaims for that half.
  - Fix: after the failed refusal, assert a live-state snapshot is unchanged (teleport targets, behaviour, and a kill payout on the previous table), then after restoring the shipped table, run a kill and assert the 14-20 band payout (18 coins, 35 XP). Or rename the test to cover only the field-camp refusals.

- **[medium] prototype/osfr-tools/tests/field_camps_elite_band.rs:565-578 the_elite_camps_spawn_in_on_zone_ready - the "scale ... once" claim is checked only as `hp > authored HP` and strictly increasing HP across actors.**
  - Why it cannot catch a regression: a loader that applies the level scaling twice (or applies a different multiplier) still yields a value above the authored base and still keeps the ordering, so it passes. The test never compares to an expected scaled value, so "once" is not checked.
  - Fix: pin the exact scaled HP per elite (for example from the loader's scale formula applied once to `elite.health` at `elite.level`), or compare against the value the loader produces for the same actor at level 1 with a known multiplier, and assert equality.

- **[low] prototype/osfr-tools/tests/field_camps_elite_band.rs:434 six_elite_camps_load_with_levels_fifteen_to_twenty - `assert!(camp.band[0] >= 1 && camp.band[1] <= 20)` checks a test-authored constant against a constant, so it can never fail for the code under test.**
  - Why it cannot catch a regression: `camp.band` comes from the `CAMPS` table in this file, not from the field data. The data's band is already checked against it at line 427, so this line adds nothing and would not notice a bad shipped band.
  - Fix: check the shipped row's band instead, e.g. `let [lo, hi] = row["level_band"]...; assert!(lo >= 1 && hi <= 20)`, and assert that each member's authored `level` falls inside that band.

- **[low] prototype/osfr-tools/tests/field_camps_elite_band.rs:556 the_elite_camps_spawn_in_on_zone_ready - the exact count 30 ("24 pre-T332 always-on + 6 elite") pins the total live spawn count to incidental roster size.**
  - Why it is churn, not a missed bug: any unrelated always-on spawn added or removed anywhere changes this count, even though the test is about the six elite spawns going through 35/2.
  - Fix: assert that the set of spawned GUIDs contains all six elite GUIDs (already done at 559-564) and drop the exact-total assertion, or compare against `EXISTING_ACTORS` filtered for always-on rows.
