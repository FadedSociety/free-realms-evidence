<!-- fleet job=pin-audit id=tests-combat-scale-rs status=no_submit turns=3 usd=0.0021 tokens(read,write,in,out)=[8012, 9266, 8, 1760] model=claude-haiku-5-5 -->
# tests/combat_scale.rs

**Findings**

- **prototype/osfr-tools/tests/combat_scale.rs:172 a_level_one_player_has_the_base_health - pins `500` from `data/content/combat_scale.json` `player_base_health`.**
  **Fix:** read it through `combat_scale::base_health()` from `tests/common/combat_scale.rs`, e.g. `assert_eq!(e.player_health(), (base, base))` with `let base = combat_scale::base_health();`.

- **prototype/osfr-tools/tests/combat_scale.rs:176 a_level_one_player_has_the_base_health - pins `500` from `data/content/combat_scale.json` `player_base_health`.** (Same assertion, the Warrior arm of the same test. The screen listed only 172, but the same literal sits in this assertion's second argument.)
  **Fix:** use `combat_scale::base_health()` as above.

- **prototype/osfr-tools/tests/combat_scale.rs:179 a_level_one_player_has_the_base_health - pins `500` from `data/content/combat_scale.json` `player_base_health`.**
  **Fix:** the helper is already in use on this line in the file (line 150 does the same). Compare `combat_scale::base_health()` to `combat_scale::base_health()`, or drop the line since 172 already covers it. Better: keep it as a sanity bound such as `assert!(combat_scale::base_health() >= 100)`, which matches the loader's accepted range.

- **prototype/osfr-tools/tests/combat_scale.rs:189 a_saved_player_above_the_new_maximum_is_clamped - pins `500` from `data/content/combat_scale.json` `player_base_health`.**
  **Fix:** read it through `combat_scale::base_health()`. The test's saved value of 1_000 is its own fixture and stays as is, but it should also stay above the base so the clamp still triggers. If retuning could drop the base to 1_000 or more, bound the fixture from the helper, e.g. `state.player_health = combat_scale::base_health() * 2`.

- **prototype/osfr-tools/tests/combat_scale.rs:240 enemy_rows_are_scaled_once_where_they_load - pins `670` from `data/content/combat_scale.json` `enemy_health_scale` (3.72 x the fixture's authored 180, rounded).**
  **Fix:** read it through `combat_scale::enemy_health(180)` from `tests/common/combat_scale.rs`, which applies the same scale and rounding. The 180 is the test's own authored fixture (`Fixture::new(180, 25)`) and stays.
