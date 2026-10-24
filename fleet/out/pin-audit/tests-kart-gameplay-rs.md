<!-- fleet job=pin-audit id=tests-kart-gameplay-rs status=done turns=5 usd=0.0033 tokens(read,write,in,out)=[27586, 13338, 12, 2696] model=claude-haiku-5-5 -->
# tests/kart_gameplay.rs

**prototype/osfr-tools/tests/kart_gameplay.rs:241 test_name (the race-completion test that asserts `progress == 94`; the function name is not in the screened excerpt) - pins `50` from `prototype/osfr-tools/data/content/kart_entry.json` `race.reward.coins` (line 7122).**
- **Fix:** read it through the reward row: `let reward = <loaded kart_entry race.reward>` (the same source the later test at ~line 1175 uses via `reward.coins`), then assert `before.inventory.coins + reward.coins`.

**prototype/osfr-tools/tests/kart_gameplay.rs:251 test_name (same test) - pins `25` from `prototype/osfr-tools/data/content/kart_entry.json` `race.reward.xp` (line 7123).**
- **Fix:** read it through the same reward row (`reward.xp`) and assert `xp(&before) + reward.xp`.

Not findings:
- 766 and 789: the `90_000` / `1600` values are fixture timestamps the test passes to `handle_at`, not values from any data file; `max_race_ms` (600000, kart_entry.json:7473) is not used here.
- 1222: `[48, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]` is a packet layout (profile/job id 48 and a fixed field of 2 that is not the reward XP of 25); it does not equal a data-file reward value, so it is not a tunable pin.
