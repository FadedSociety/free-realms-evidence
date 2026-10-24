<!-- fleet job=pin-audit id=src-bin-osfr-gateway-f120-fishing-hour-reconnect-rs status=done turns=8 usd=0.0060 tokens(read,write,in,out)=[117500, 26606, 18, 2996] model=claude-haiku-5-5 -->
# src/bin/osfr_gateway/f120_fishing_hour_reconnect.rs

Coins (379, 546, 572) are not findings: the test's own fixture (f120_fishing_hour_reconnect.rs:244-246) overwrites every `payout.by_grade[].coins` with 25, so 25 and 50 (2×25) come from the fixture, not the shipped data (which ships coins 0). Fisherman XP is different: the fixture only overrides `coins` and the `catch_cap`/`items` fields, so `fisherman_xp` stays at the shipped value in `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp` (10 for all four grades, lines 10/15/20/25). The XP expectations therefore pin that data value.

- **src/bin/osfr_gateway/f120_fishing_hour_reconnect.rs:380 one-catch payout test (`fishing_hour_reconnect` test that reaches `assert_eq!(fisherman_xp(&paid), 10)`) - pins `10` from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp`.**
  - **Fix:** read it through the `by_grade` row for the caught grade (load `fishing_spots.json` as the fixture does at line 240, or use the `read_json(&content_dir().join("fishing_spots.json"))` pattern from `tests/fisherman_entry_chain.rs`), or bound it as `> 0` and `<= MAX_CATCH_XP`.

- **src/bin/osfr_gateway/f120_fishing_hour_reconnect.rs:547 same test, after the capped refusal - pins `10` from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp`.**
  - **Fix:** compare against the value read from the same `by_grade` row (or against the XP captured from the first payout, e.g. `let first_xp = fisherman_xp(&paid);` then assert equality with `first_xp`), so a refusal leaves XP unchanged without pinning 10.

- **src/bin/osfr_gateway/f120_fishing_hour_reconnect.rs:573 same test, after the second paid catch - pins `20` from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp` (two catches × 10).**
  - **Fix:** express it as `2 * row_xp` where `row_xp` is read from the `by_grade` row for the caught grade (or as `first_xp + row_xp` using the value captured after the first payout).
