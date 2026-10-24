<!-- fleet job=pin-audit id=tests-derby-route-rs status=nothing_found turns=5 usd=0.0022 tokens(read,write,in,out)=[20377, 8764, 12, 1858] model=claude-haiku-5-5 -->
# tests/derby_route.rs

No findings in `prototype/osfr-tools/tests/derby_route.rs`.

- The screened line 1489 is not an assertion. It is `run_to_running(...)`. The assertion the screen meant is `derby_route.rs:1455 - assert_eq!(farmed.inventory.coins, before_coins + 2 * COMPLETION_COINS);`.
- `COMPLETION_COINS` is the file's own constant (`derby_route.rs:38`, `25`, documented as "Synthetic package payout"). It is not read from data. The fixture writes its own `derby_entry.json` from `content()` (`derby_route.rs:86-91`), and that content sets `completion_reward_coins: COMPLETION_COINS` (`derby_route.rs:315`). So the expected value comes from the test's own fixture, not from `data/content/derby_entry.json`. The shipped value there is also 25 (`completion_reward_coins`, line 74), but retuning the shipped file would not change this test.

The test is not pinning a tunable shipped number, so no change is needed.
