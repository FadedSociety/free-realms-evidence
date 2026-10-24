<!-- fleet job=pin-audit id=tests-shared-field-interest-rs status=nothing_found turns=10 usd=0.0053 tokens(read,write,in,out)=[98659, 18242, 22, 4161] model=claude-haiku-5-5 -->
# tests/shared_field_interest.rs

No findings in `prototype/osfr-tools/tests/shared_field_interest.rs` for the three screened lines.

- **275 `assert_eq!(hp_values(packets), vec![hp_after(2)])`**: not a finding. `hp_after` (line 17) is `hp_full() - hits * unit::n()`. `hp_full()` goes through `combat_scale::enemy_health(authored_three())`, and `unit::n()` is `combat_scale::basic(2)`. Both read `data/content/combat_scale.json` (`enemy_health_scale`, `basic_damage`) through `tests/common/combat_scale.rs`. The test follows the data, and the three-hit enemy health is set by the test's own fixture (`set_three_hit_health`, line 22).
- **538 and 546 `assert_eq!(field.respawn_at(E), Some(2600))`**: not a finding. The death is at `now=600` (line 518). The 2600 is 600 + 2000 ms, and the 2000 comes from the synthetic enemy fixture's `"respawn_seconds": 2` (`shared_field_state.rs` line 77). `create_content` copies that synthetic `field_enemies.json` into the test's content dir (`shared_field_state.rs` ~line 926). The value is set by the test's fixture, not by a shipped data file such as `field_enemies.json` (which has 45/60/90 s groups). Nothing here pins a shipped tunable.</result>
