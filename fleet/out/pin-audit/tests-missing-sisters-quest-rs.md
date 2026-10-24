<!-- fleet job=pin-audit id=tests-missing-sisters-quest-rs status=done turns=6 usd=0.0027 tokens(read,write,in,out)=[28873, 11873, 14, 1852] model=claude-haiku-5-5 -->
# tests/missing_sisters_quest.rs

Two of the three screened lines are tunable-value pins. All three read live data that the test loads itself. None of them is a code constant or a fixture-owned number.

- **prototype/osfr-tools/tests/missing_sisters_quest.rs:118 starting_farnum_wolves - pins `45` from `data/content/field_enemies.json` `spawn_groups[id=starting_farnum_wolves].respawn_seconds`.**
  Fix: read it through the group row, `json!(group["respawn_seconds"])`, or bound it as `respawn_seconds > 0`.

- **prototype/osfr-tools/tests/missing_sisters_quest.rs:147 starter wolf HP - pins `100` from `data/content/field_enemies.json` `enemies[guid in group].max_health`.** The three member rows (GUIDs 131000102001–003) carry `max_health: 100`.
  Fix: compare against the member row's own value, for example `assert_eq!(enemy["max_health"], wolf_row["max_health"])`, or assert it is a positive integer. The shared helper `shipped_row(guid)` in `tests/common/field_enemy_fixture.rs` already loads these rows.

- **prototype/osfr-tools/tests/missing_sisters_quest.rs:148 starter wolf damage - pins `7` from `data/content/field_enemies.json` `enemies[guid in group].damage`.** The same three member rows carry `damage: 7`.
  Fix: same as line 147. Read it from the member row via `shipped_row(guid)`, or bound it as `damage > 0`.

Lines 131–132 and the group-size assertion stay as they are; they check a definition id, a level and a count, not a tunable value.
