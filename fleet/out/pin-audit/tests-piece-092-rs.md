<!-- fleet job=pin-audit id=tests-piece-092-rs status=nothing_found turns=4 usd=0.0024 tokens(read,write,in,out)=[15274, 10515, 10, 1950] model=claude-haiku-5-5 -->
# tests/piece_092.rs

No findings in `prototype/osfr-tools/tests/piece_092.rs`.

Screened line 288 (`GLIDE_FALL_TIME_STAT` == `0.75`) is not a finding:

- The `0.75` value does exist in `data/content/mounts.json` at `trained_glide.stats.glide_fall_time` (line 17). The `mounts.json` value is not what the test reads, though.
- The dragon's stats come from `mount_stats(dragon)` in `src/restoration/piece_092.rs`, lines 526-537 (`able_to_fly` branch). That function hard-codes `float_stat(GLIDE_FALL_TIME_STAT, 0.75)` and never reads `mounts.json`.
- Retuning `glide_fall_time` in the data file would not change this test's result, so the test does not pin a data value. It pins the value that the code under test writes. That is a separate concern: the same tunable (0.75) is duplicated as a literal in the restoration code and the data file, and that duplication should be reviewed. It is not a test-side finding under the stated rule.

Sibling lines 289-292 (fall speed 4.0, glide accel 4.0, glide enabled 1, and the 8.0/2.0/18.0 forward speeds) follow the same pattern: the code's literals match the data, but the test would not break on a data retune.
