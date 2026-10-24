<!-- fleet job=pin-audit id=tests-piece-019-rs status=nothing_found turns=2 usd=0.0014 tokens(read,write,in,out)=[1797, 8373, 6, 616] model=claude-haiku-5-5 -->
# tests/piece_019.rs

No finding for `prototype/osfr-tools/tests/piece_019.rs:208` (`one_entry_per_character_keeps_the_better_value`, `assert_eq!(rows[0].value, 150)`).

The 150 is the test's own fixture. Line 199 calls `commit(&mut store, "A", "Ayla", ScoreKind::Points, 150)`, and the leaderboard keeps the better value, so `rows[0].value` must equal the value the test just committed. It is not read from any data file. A grep for `150` under `data/content` turns up only unrelated values (for example `max_health` in enemies.json, `respawn_seconds` in field_enemies.json), so retuning any shipped data value would not affect this assertion. No change is needed.
