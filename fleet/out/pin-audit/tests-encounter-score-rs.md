<!-- fleet job=pin-audit id=tests-encounter-score-rs status=nothing_found turns=4 usd=0.0026 tokens(read,write,in,out)=[20896, 12882, 10, 1562] model=claude-haiku-5-5 -->
# tests/encounter_score.rs

Checked the one screened line, `prototype/osfr-tools/tests/encounter_score.rs:209` in `won_total_row_carries_the_local_objective_award`.

- The `5000` does not come from any data file. It is the code constant `OBJECTIVE_AWARD_SCORE: i32 = 5000` at `prototype/osfr-tools/src/encounter.rs:93`, used for the won total at line 2937 and the writer at line 2959. A search of `data/content` for a matching score field found only unrelated `5000` values (boomboxes, chess, derby durations), none of which feed this path.
- The `4` in the row is the protocol Order/Score-Type from the community writer (the file header and `WIN_GOLDEN` document it), and `-1` entries are protocol sentinels. Neither is a tunable.
- The `WIN_GOLDEN` bytes are a compiled-writer fixture the test builds itself, and the defeat count `4` comes from the fixture's four enemies, not from data.

Not a data-file finding, so nothing to report under the data-tunable rule. Optional note for the team, not a finding: `OBJECTIVE_AWARD_SCORE` is a code constant that the test pins; if it ever becomes live-tunable it should move to a data file, and the test would then read it from there.
