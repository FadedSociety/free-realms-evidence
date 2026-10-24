<!-- fleet job=pin-audit id=tests-thugamug-battle-rs status=done turns=17 usd=0.0113 tokens(read,write,in,out)=[283307, 30393, 36, 9245] model=claude-haiku-5-5 -->
# tests/thugamug_battle.rs

Line numbers below are the real ones in `thugamug_battle.rs`. Several screened numbers are a few lines off (e.g. screened 1438 is actually 1420), so the same assertions are listed at their real lines.

- **prototype/osfr-tools/tests/thugamug_battle.rs:141 test (battle roster test, the one that calls `battle(&file, THUGAMUG)`) - pins `220` from `data/content/field_battles.json` battle 12340 enemy `max_health` (boss row, line ~437).**
  Fix: read it through the row the test already loaded: `u32_field(&enemies[0], "max_health")` should be compared to a value read from `row["enemies"][0]["max_health"]` (or bound it as `> 0`, and `< 1000` if a sanity cap is wanted). The test already reads the row, so the literal only duplicates the data.

- **prototype/osfr-tools/tests/thugamug_battle.rs:142 test (same roster test) - pins `12` from `data/content/field_battles.json` battle 12340 enemy `damage` (boss row, line ~438).**
  Fix: read it through `row["enemies"][0]["damage"]` (or bound it).

- **prototype/osfr-tools/tests/thugamug_battle.rs:150 test (same roster test, Hands loop) - pins `140` from `data/content/field_battles.json` battle 12340 Hand enemy `max_health` (lines ~453, 469).**
  Fix: read it per hand through `hand["max_health"]` from the row, or bound it.

- **prototype/osfr-tools/tests/thugamug_battle.rs:151 test (same roster test, Hands loop) - pins `9` from `data/content/field_battles.json` battle 12340 Hand enemy `damage` (lines ~454, 470).**
  Fix: read it per hand through `hand["damage"]` from the row, or bound it.

- **prototype/osfr-tools/tests/thugamug_battle.rs:1187 and 1188 (MISSING_SISTERS end-screen test, via `open_end_screen`) - pins `MISSING_SISTERS_COINS = 5` and `MISSING_SISTERS_XP = 25` (consts at lines 822-823) from `data/content/quests/adventurer.json` quest id 3000029 `rewards[0].coins` (5) and `rewards[0].job_xp["1"]` (25), around lines 2427-2433.**
  Fix: read the expected values from that quest's reward row in `data/content/quests/adventurer.json` (the quest with `"id": 3000029`, `rewards[0].coins` and `rewards[0].job_xp["1"]`), and drop the two consts. The packet is built from that same data, so the test should not repeat it.

- **prototype/osfr-tools/tests/thugamug_battle.rs:1420 and 1421 (THIEVERY 49/13 end-screen test, "49/13 coin bundle") - pins `QUEST_COINS = 13` and `QUEST_XP = 25` (const lines 819-820) from `data/content/quests/adventurer.json` quest id 3000032 `rewards[0].coins` (13) and `rewards[0].job_xp["1"]` (25), around lines 2670-2676.**
  Fix: read the expected values from the quest 3000032 reward row in `data/content/quests/adventurer.json` instead of the consts.

- **prototype/osfr-tools/tests/thugamug_battle.rs:1465 and 1466 (THIEVERY end-screen test) - same pin as above: `QUEST_COINS = 13` and `QUEST_XP = 25` from `data/content/quests/adventurer.json` quest 3000032 `rewards[0]`.**
  Fix: same as 1420/1421. Read `rewards[0].coins` and `rewards[0].job_xp["1"]` for id 3000032.

- **prototype/osfr-tools/tests/thugamug_battle.rs:1612 and 1613 (THIEVERY end-screen test after relog/replay) - same pin: `QUEST_COINS = 13` and `QUEST_XP = 25` from `data/content/quests/adventurer.json` quest 3000032 `rewards[0]`.**
  Fix: same as 1420/1421.

- **prototype/osfr-tools/tests/thugamug_battle.rs:1807 and 1808 (THIEVERY `engine.quest_end_packet` test) - same pin: `QUEST_COINS = 13` and `QUEST_XP = 25` from `data/content/quests/adventurer.json` quest 3000032 `rewards[0]`.**
  Fix: same as 1420/1421. The engine test can read the reward row from the content directory (`content_dir()` is already imported) and compare against it.

Not findings: the `finish_quest` calls and the `session.coins()` / `session.xp()` deltas in these tests use the same QUEST_COINS / QUEST_XP consts, so they inherit the same fix. The `u32_at` offsets (27, 31) are packet layout, not tunables. `spawner.max_health == 1` (line 132) was not in the screened list and was not checked.
