<!-- fleet job=pin-audit id=tests-encounter-job-skills-rs status=nothing_found turns=5 usd=0.0031 tokens(read,write,in,out)=[29036, 13555, 12, 2211] model=claude-haiku-5-5 -->
# tests/encounter_job_skills.rs

No findings in `prototype/osfr-tools/tests/encounter_job_skills.rs`. None of the six screened lines pins a number from a shipped data file.

- **Line 27 (`unbuffed_critical_damage_keeps_existing_integer_rounding`)**: the x1.5 comes from the code constants `CRIT_NUMERATOR = 3` / `CRIT_DENOMINATOR = 2` in `src/encounter.rs:59-60`. No data file holds it, so it is not tunable data.
- **Line 111 (`self_heal_clamps_and_scales_with_the_existing_hp_curve`)**: `287` is the protocol locale id for the cooldown message, `Self::Cooldown => 287` in `src/abilities.rs:433`. It is a protocol constant.
- **Lines 173 and 175 (`stun_stops_attacks_and_movement_until_exact_expiry`)**: the 2000 ms stun comes from the `{"kind":"stun","duration_ms":2000}` literal the test builds itself. The 1900 and 2000 ticks are the test's own timeline.
- **Line 288 (`invalid_range_cooldown_and_unavailable_summon_do_not_spend_or_damage`)**: the 600 ms probe sits under the 5000 ms `cooldown_ms` that the `skill()` helper sets in the test. That value is a fixture value, not from `data/content`.
- **Line 290**: the 10000 ms time is past the fixture's cooldown, and the assertion depends on `a.unavailable = true`, not on any data value.

Lines 27, 173, 175, 288 and 290 are test-set or code-set values, not data-set ones. Line 111 is a protocol constant. The file's other numbers that come from the data are read through `common/combat_scale.rs`, which is the right pattern.
