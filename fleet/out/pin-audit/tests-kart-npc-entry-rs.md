<!-- fleet job=pin-audit id=tests-kart-npc-entry-rs status=nothing_found turns=12 usd=0.0088 tokens(read,write,in,out)=[237018, 33304, 26, 4436] model=claude-haiku-5-5 -->
# tests/kart_npc_entry.rs

No findings in `prototype/osfr-tools/tests/kart_npc_entry.rs`. None of the seven screened lines pins a value from a shipped data file.

- **Reward 40 coins / 60 xp (lines 704, 726, 746, 1281):** the test's own `race_content()` (line 178, `reward: Some(RewardSchedule { coins: 40, xp: 60 })`, line 183) sets this. `Fixture::write_content` (line 63) and `GameplayFixture` (line 1005) write that content to a temp `kart_entry.json`, so the value is fixture-set. The shipped `data/content/kart_entry.json` has no reward field that feeds it.
- **Cooldown `paid + 600` (line 654):** the 600 comes from the test's own `write_gates_raw` call (line 618, `"reward_cooldown_s": 600`). The shipped data has no kart gates file, so this is fixture-set.
- **Race clock `green + 100` / `green + 150` (lines 1220, 1261):** these are tick timestamps the test passes to `tick()`, and `green` is itself built in the test (`T0 + 500 + 6_000`, `start_to_green`). They are not data values.

The `86_401` bound at line 662 is a sanity bound, not a pinned value, and was not screened.
