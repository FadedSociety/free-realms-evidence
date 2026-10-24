<!-- fleet job=pin-audit id=tests-field-battle-roster-rs status=nothing_found turns=5 usd=0.0030 tokens(read,write,in,out)=[31847, 13698, 12, 1939] model=claude-haiku-5-5 -->
# tests/field_battle_roster.rs

No findings in `prototype/osfr-tools/tests/field_battle_roster.rs` for the two screened lines.

- **Line 856 (`assert_payout`, `before.experience + 50`):** The 50 is the code constant `BATTLE_JOB_XP: u32 = 50` at `prototype/osfr-tools/src/encounter.rs:76`, applied at `encounter.rs:2003` when the battle has no guide. It is not read from any file under `data/content/`, so it is not a shipped data value. The test is pinning a code constant, not a tunable. Not a finding under the stated rule. (If Bryce wants it live-tunable, that is a code-side move to data, not a test fix.)
- **Line 908 (`assert_eq!(level(&gateway, BRAWLER), 3)`):** The level is set by the test's own chat command `"realm level 3"` (line 902), which the gameplay code handles at `src/gameplay.rs:2767-2771` by setting experience to `(level - 1) * 100`. The `level()` helper (line 395) uses the code formula `1 + xp / 100`. The 3 comes from the test's own fixture input, and the 100-per-level divisor is code, not a `data/content` field. Not a finding.
