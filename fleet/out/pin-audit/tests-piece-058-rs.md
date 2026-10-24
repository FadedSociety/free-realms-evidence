<!-- fleet job=pin-audit id=tests-piece-058-rs status=nothing_found turns=3 usd=0.0018 tokens(read,write,in,out)=[8839, 9835, 8, 965] model=claude-haiku-5-5 -->
# tests/piece_058.rs

No findings in `prototype/osfr-tools/tests/piece_058.rs`. Every screened number comes from the test's own fixture, not from a shipped data file:

- `ReviveArbiter::new(max_health, coins, revive_cost)` is called with literals in each test (1000 health, 2500 / 1500 / 999 / 5000 / 0 coins, 1000 cost). Those are the test's inputs, so 158, 215, 226, 227, 262, 265, 266, 267, 278, 290, 299, 307, 325, 326, 366 and 374 are fixture-set.
- The 400 at line 158 is 1000 minus the 600 hit the test applies itself.
- The 1000 in `outcome.charged_coins` (265) is the cost the test passed in, and `RespawnWindow.revive_cost: 1000` (line 178) is fixture input.
- The file loads no data file, and the 38-byte relocation length and the byte positions at 36/37 are packet layout, not tunables.
- `RECOVER_DELAY_MS` is only ever used as a symbol, never as a literal in an assertion.

No change is needed for these lines.
