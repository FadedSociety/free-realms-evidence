<!-- fleet job=test-audit id=tests-power-up-use-rs-L1 status=done turns=6 usd=0.0080 tokens(read,write,in,out)=[96521, 28316, 14, 6953] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/power_up_use.rs lines 1-987 of 987

Reviewed `prototype/osfr-tools/tests/power_up_use.rs` lines 1-987 in full, and checked the code under test in `src/encounter/skills.rs` (`apply_dot`, 379-400), `src/encounter.rs` (shield/dormant logic), and `data/content/power_ups.json` (flame_wave burn: 4000 ms, 1000 ms interval). No test is outright unable to fail. The three findings below are the real gaps.

- **[medium] prototype/osfr-tools/tests/power_up_use.rs:717-721 a_shielded_summoner_is_not_burned_by_flame_wave - `enemy_health(...).unwrap_or(shielded_health)` makes a missing health report count as "no burn", so the assertion passes whenever the tick emits no 35/5 for the summoner.**
  - Why it cannot catch a regression: if `apply_dot` loses its `!self.shielded(guid)` guard (encounter/skills.rs:389), the burn is still stored, but it only shows up as a 35/5 packet with lower health. If the tick path does not emit that packet for the summoner (for example, a burn that only changes internal state, or a tick that emits nothing for an enemy at 0 damage), the `unwrap_or` returns `shielded_health` and the test still passes. The burn would be applied and the test would still be green.
  - Fix: replace `.unwrap_or(shielded_health)` with `.expect("the summoner's health is reported after the tick")` and then assert `== shielded_health`. Optionally also assert `ticked` has a summoner health report at all, so a silent tick fails.

- **[low] prototype/osfr-tools/tests/power_up_use.rs:459 a_held_power_up_uses_its_own_key_once_and_restores_the_job_bar - the name says "once", but the body only presses the key once and never presses it again.**
  - Why it cannot catch a regression: a change that leaves the kind held after a successful use (so a second press would fire it again) still passes, because no second press occurs in this test. The repeat-refused case only lives in `the_flame_wave_burn_ticks_and_a_repeat_changes_nothing` (lines 569-576), which tests a different scenario.
  - Fix: either rename it to drop "once", or add a second `cast(2, 1)` after line 500 and assert it is `failed(...)` with `game.state()` unchanged. The same applies to `the_shared_field_route_uses_the_same_key_and_consumes_once` (line 874), which also never repeats the press.

- **[low] prototype/osfr-tools/tests/power_up_use.rs:315 definition_ids - the filter pins the wire length of a 36/0/13 definition packet to exactly 160 bytes, which is incidental to what the callers check.**
  - Why it cannot catch a regression: it is churn, not a missed bug. Any change to the definition packet's trailing fields (for example, adding a field) makes `definition_ids` return an empty list, so `definition_ids(&used).contains(&slot.definition_id)` at line 500 turns into a silent pass for "not re-sent" rather than a meaningful check.
  - Fix: filter on the header and the id only (`p.starts_with(&[36, 0, 13, 0]) && p.len() >= 8`), which keeps the definition-id lookup working when the packet grows.
