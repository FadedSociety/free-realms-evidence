<!-- fleet job=pin-audit id=tests-piece-065-rs status=nothing_found turns=3 usd=0.0015 tokens(read,write,in,out)=[8998, 7802, 8, 936] model=claude-haiku-5-5 -->
# tests/piece_065.rs

No findings for `prototype/osfr-tools/tests/piece_065.rs:302` (`boss_gate_requires_the_tallest_enemy_dead_and_displayed`).

The `100` is set by the test's own fixture: lines 289-296 push `ReplayEvent::EnemyHealth { guid: 5, hp: 100, max: 500 }`. The gate's detail string is built from that row's `hp` (`src/restoration/piece_065.rs:735`, `format!("the tallest enemy still had {hp} hp ...")`). The assertion therefore checks that the gate reports the replay's own hp, and no data file value is involved. The boss data in `data/content` (for example `bandit_hideout_dungeon` `BOSS_BASE_HEALTH` 320) is not read by this test, so retuning it cannot break this line.
