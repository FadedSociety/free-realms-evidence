<!-- fleet job=pin-audit id=tests-chess-rs status=nothing_found turns=4 usd=0.0016 tokens(read,write,in,out)=[10860, 6135, 10, 1494] model=claude-haiku-5-5 -->
# tests/chess.rs

No findings in `prototype/osfr-tools/tests/chess.rs`. I checked all five screened lines.

- **450 / 1049 (`coins == 7`):** The 7 comes from the test's own fixture. `grant()` at `tests/chess.rs:125-127` builds `RewardGrant { coins: 7, .. }`, and line 1047 calls `live.inventory.grant_coins(7)` itself. Neither value is read from `data/content`, so retuning chess reward data would not change them.
- **640 / 641 / 642 (`skill_for_row` 20→20, 66→60, 67→100):** These come from the code constant table in `src/chess.rs:240-257` (`Mode::for_row`). They are not in a data file, and the test's own assertions match that code table, so they are not a data-tunable pin. Row 65 → `None` (line 642) is a row-id/mode check, also not a finding.

The one data-backed value in this area is `success_coins: 10` and `daily_reward_coins` in `service_content()` (`tests/chess.rs:745-750`). The test sets those itself, so they are not findings either.
