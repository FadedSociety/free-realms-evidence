<!-- fleet job=pin-audit id=tests-medic-level-five-chapter-rs status=done turns=8 usd=0.0034 tokens(read,write,in,out)=[40197, 12292, 18, 2947] model=claude-haiku-5-5 -->
# tests/medic_level_five_chapter.rs

**prototype/osfr-tools/tests/medic_level_five_chapter.rs:1084 test (the test containing this line, the one that finishes the Level 5 chapter for both Medics) - pins `425` from `data/content/quests/medic.json` `quests[Achieve Level 5].rewards[0].job_xp["11"]` (value 25), plus a fixture-set base of 400.**

Where 425 comes from: line 1013-1014 sets Medic XP to 400 through `set_medic_xp` (the test's own fixture, not a finding). The finish step then adds the level-five reward, which is `LEVEL_XP = 25` (`tests/support/medic_entry.rs:39`). That constant mirrors `medic.json` line 498 (`"11": 25`), and `medic_entry.rs:353-354` already asserts the data matches it. So 425 = 400 + 25, and retuning the level-five `job_xp` in `medic.json` would break the assertion even though the code is right.

- **Fix:** Read the base and the reward instead of the literal. Keep `let second_xp = medic_xp(&second);` (line 1016) as the baseline for the second Medic and assert `medic_xp(&first) == 400 + LEVEL_XP` and `medic_xp(&second) == second_xp + LEVEL_XP`, which matches the pattern used at line 1218. Better still, read the reward from the row with `reward["job_xp"]["11"]` from `quests/medic.json` (via the helper in `tests/support/medic_entry.rs` that already loads it) rather than using the `LEVEL_XP` constant, so the test follows the data. Use `400` only as the fixture's own set value.
