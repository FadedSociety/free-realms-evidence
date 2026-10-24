<!-- fleet job=pin-audit id=tests-zone-quests-seaside-rs status=done turns=9 usd=0.0033 tokens(read,write,in,out)=[42725, 11597, 20, 2743] model=claude-haiku-5-5 -->
# tests/zone_quests_seaside.rs

Both screened lines pin values that come from `prototype/osfr-tools/data/content/quests/zone_seaside.json`, not from the test's own fixture. The test's `Quest` structs (lines 70-119) hold only ids, text ids and XP, and the test uses `COINS: u32 = 30` (line 45) with the comment "the fork's RewardCoins on every quest here". That value is the same as the shipped data.

- **zone_seaside.json:57-59 `rewards[].coins` = 30** on 3000320, 3000321, 3000322 and 3000323 (the four TOUR quests). Four quests at 30 give 120.
- **zone_seaside.json `rewards[].job_xp` "1"** = 20 (3000320), 20 (3000321), 30 (3000322), 30 (3000323). The sum is 100.

Both sums match the data, so retuning the data would break these asserts while the code stays correct.

- **prototype/osfr-tools/tests/zone_quests_seaside.rs:239 seaside_tour_runs_in_order_and_pays_once - pins `120` (4 × 30) from `data/content/quests/zone_seaside.json` `rewards[].coins`.**
  **Fix:** read it through the data. Load `quests/zone_seaside.json` with the `read_json` helper in `tests/common/` (e.g. `field_battle_fixture.rs` or `npc_greetings.rs`), then sum `rewards[0].coins` over each TOUR quest id. Or bound it as `>= 4` coins gained, with the exact amount read from the row. Also remove the `COINS` constant if it is no longer needed.

- **prototype/osfr-tools/tests/zone_quests_seaside.rs:240 seaside_tour_runs_in_order_and_pays_once - pins `100` (20+20+30+30) from `data/content/quests/zone_seaside.json` `rewards[].job_xp["1"]`.**
  **Fix:** the same as line 239. Sum `rewards[0].job_xp["1"]` over the TOUR quest rows, read from the JSON with `read_json`, instead of hard-coding 100. The per-quest `quest.xp` values at lines 77-108 should also be read from the rows rather than kept as literals.
