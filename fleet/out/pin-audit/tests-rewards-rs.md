<!-- fleet job=pin-audit id=tests-rewards-rs status=nothing_found turns=3 usd=0.0022 tokens(read,write,in,out)=[11377, 11061, 8, 1307] model=claude-haiku-5-5 -->
# tests/rewards.rs

No findings in `prototype/osfr-tools/tests/rewards.rs`. Every screened number comes from a fixture the test builds itself, not from a shipped data file:

- **157 (`signed(bundle, 8) == 15`):** the wallet is `state(10)` (`InventoryFixture::new(10)`, line 141), plus the grant's `coins: 5` from `grant()` (line 115). 15 = 10 + 5. Computed from fixtures.
- **160 / 161 (`700`, `800`):** `grant().display.source_guid` (line 122) and `player_guid` (line 123). Fixture values.
- **163 (`3`):** `grant().display.rows[0].type_id` (line 128). Fixture value.
- **167 (`coins == 15`):** same 10 + 5 computation as line 157.
- **170 (`items[0].count == 2`):** `grant().items[0].count` (line 118). Fixture value.
- **175 (`experience.get(&1) == 105`):** the test sets `experience.insert(1, 90)` (line 142), plus `job_xp {1: 15}` from `grant()` (line 120). 105 = 90 + 15. Fixture values.
- **291 (`signed(bundle, 16) == 16`):** the empty-bundle test sets `reward_kind: 16` (line 275) directly. Fixture value.

The only other numbers in the test are the wire-layout bytes and offsets, which are protocol constants and not tunables. Nothing needs changing.
