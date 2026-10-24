<!-- fleet job=pin-audit id=tests-encounter-rs status=nothing_found turns=4 usd=0.0023 tokens(read,write,in,out)=[14958, 10493, 10, 1704] model=claude-haiku-5-5 -->
# tests/encounter.rs

No findings in `prototype/osfr-tools/tests/encounter.rs` for the screened lines. None of them pins a value from a shipped data file.

- **Reward lines 523-524** (`save_restart_win_and_exit_preserve_reward_exactly_once`): expected `50` coins and `(1195, 1)` come from the test's own fixture. `Fixture::new()` (lines 44-45) writes `"reward_coins":50,"reward_items":[[1195,1]]` into a synthetic `encounters.json` in a temp dir. The test loads that fixture, not `data/content`, so retuning shipped data cannot break it.
- **Timer lines 449, 452, 453, 456 and 693, 694** (`cave_waits_for_valid_start_or_attack_and_rejoining_disarms`, `malformed_requests_are_non_mutating_and_cooldown_cannot_burst`): the 600 ms attack cooldown is a hard-coded constant in `src/encounter.rs:1868` (`< 600`). The 100 ms tick gate is also hard-coded, in `src/encounter.rs:2343-2344`. Neither is read from a data file, so these are code constants, not tunables. The timestamps in the test (9000, 9099, 9100, 6100, 599, 600) are derived from those code constants and the test's own inputs.

Note for the team: the attack cooldown is a code constant rather than a data field. If it is ever moved into data, these assertions should read the value from that row instead of hard-coding 600.
