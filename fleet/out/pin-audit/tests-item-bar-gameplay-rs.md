<!-- fleet job=pin-audit id=tests-item-bar-gameplay-rs status=nothing_found turns=6 usd=0.0040 tokens(read,write,in,out)=[49100, 18586, 14, 2354] model=claude-haiku-5-5 -->
# tests/item_bar_gameplay.rs

Checked `prototype/osfr-tools/tests/item_bar_gameplay.rs:118` (`a_bound_potion_heals_once_per_recast_and_the_bar_survives_a_reload`, `35` in `max as u32 * 35 / 100`).

Not a finding. The 35% does not come from any shipped data file:
- No `data/content/*.json` row holds a potion heal percent, heal amount or heal-over-time value. Ability 4696 (the potion's ability, shared by item rows 2173 and 11002) appears only in `stores.json` and `reference/weapons.json` as an id and price row, not as a heal amount.
- The heal value is not in code either. `src/restoration/piece_046.rs` (lines 34-48) says healing percent, duration and instant heal are "unresolved" and that the consumable model takes no healing amount.

So the 35 is the test's own expectation formula, not a copy of a data value, and retuning a data file cannot break it. The test does not read from data here, and there is no data value to read it from yet. If a heal percent is later added to a data file, this line should read it from that row. Nothing to change now.
