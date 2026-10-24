<!-- fleet job=pin-audit id=tests-enemies-rs status=nothing_found turns=3 usd=0.0019 tokens(read,write,in,out)=[8749, 9658, 8, 1113] model=claude-haiku-5-5 -->
# tests/enemies.rs

No findings in `prototype/osfr-tools/tests/enemies.rs`. All six screened assertions take their numbers from the test's own synthetic fixtures, not from shipped data files:

- **252 `ability…`/`nearby_player_aggroes…`: `players[0].health == 75`** - 100 start health minus the wolf's `damage: 25` in `test_engine()` (lines 28-72, built inline). Fixture, not data.
- **285 `coins == 5`** and **286 `experience[&43] == 7`** - from the `reward` block of the same inline `test_engine()` definition (`coins: 5`, `xp: 7`). Fixture.
- **292 `respawn_at_ms == Some(600)`** - `test_engine(500)` passes `respawn_ms: 500` into the inline definition; 600 = kill time 100 + 500. Fixture.
- **434 `public` health == 30** and **435 `private` health == 40** - `max_health: 40` from the inline definition, minus `damage_ability(10)` (lines 94-115, amount set by the test). Fixture.

No shipped data file (`data/content/*.json`) is read by these assertions, so retuning data would not break them. The file's only data-backed test (`opening_wolf_messages_match_encounter_engine_byte_for_byte`) compares message bytes, not pinned numbers.
