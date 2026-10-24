<!-- fleet job=pin-audit id=tests-mining-dead-board-rs status=nothing_found turns=7 usd=0.0037 tokens(read,write,in,out)=[68969, 16272, 16, 1939] model=claude-haiku-5-5 -->
# tests/mining_dead_board.rs

No findings for `prototype/osfr-tools/tests/mining_dead_board.rs`.

Screened line 281 `assert_eq!(run.score, 3500);` (test `chainless_board_with_bottom_ore_rebuilds_after_collect`) is not a data-file pin:

- The starting score of 3000 is set by the test's own fixture (`dead_state`, line 184: `score: 3000`).
- The +500 comes from the code constant `COLLECTABLE_SCORE: u32 = 500` in `src/mining.rs:117`, added on collect at `mining.rs:1594`.
- `data/content/mining.json` has no score or 500 value. Its only reward fields are `per_reward` 1 and 2 (lines 22, 29), which the test does not use.

So the expected value is fixture plus a code constant, not a shipped data value, and it does not fall under the rule. It is still a hard-coded number, though. If `COLLECTABLE_SCORE` moves into a data file later, this line should read the value from that file rather than pin 500. Nothing needs changing now.
