<!-- fleet job=pin-audit id=tests-gathering-payout-rs status=nothing_found turns=3 usd=0.0016 tokens(read,write,in,out)=[6137, 7131, 8, 1347] model=claude-haiku-5-5 -->
# tests/gathering_payout.rs

No findings in `prototype/osfr-tools/tests/gathering_payout.rs` for the three screened lines.

- **512 `ordinary_win_pays_once_then_close_returns_to_the_world`: `vec![18, 47, 19]` is not a tunable.** These are the family-39 minigame sub-opcodes of the results sequence (`subs()` at line 342 reads the third byte of each reply). They are protocol values, not payout amounts.
- **539 and 547: `vec![2; game.goals]` is not a tunable.** The count comes from the test's own fixture. `board()` (lines 79-125) builds the synthetic board in the test and sets `per_reward: 1` on each `Type8Goal`. One win therefore pays 1 per output, and two wins pay 2. `ore()` (line 404) reads the inventory counts for `OUTPUTS[..game.goals]`, and `game.goals` (1 or 4) is a fixture value, not a data value. No shipped data file feeds this number, so retuning a data file does not break the test. The fixture's own `per_reward` is what sets it.

Nothing needs to change for these lines.
