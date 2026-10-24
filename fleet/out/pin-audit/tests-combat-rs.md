<!-- fleet job=pin-audit id=tests-combat-rs status=nothing_found turns=3 usd=0.0025 tokens(read,write,in,out)=[11500, 12016, 8, 1792] model=claude-haiku-5-5 -->
# tests/combat.rs

No findings in `repo:prototype/osfr-tools/tests/combat.rs`. Every screened number comes from the test's own fixture (`Content::new()`, lines 24-38), not from a shipped data file under `data/content/`:

- Lines 84, 86: `model_id: 4` and the NPC/enemy position x `4.0` are set in the fixture config (line 37). The packet offsets are layout constants.
- Line 92: value `8` is the fixture's `range: 8.0` / layout field in the packet, not a data row.
- Line 94: `0x5a` is written by the fixture into the template at offset 250 (line 32).
- Lines 162, 225, 229: `75` = fixture `max_health 100` minus fixture `hit_damage 25` (line 38). Not a data value.
- Lines 163-165: `1599`/`999`/`1600` are `1000` ms (the test's own clock) plus the fixture `cooldown_ms: 600` (line 38), so the boundary is fixture-derived.

The test never loads `data/content/*.json`, so retuning shipped data cannot break these assertions. Lines 84-94 and 162-229 need no change to satisfy the live-tunable rule. Note the `#[ignore]` private-capture test (line 261) is the only one that reads real content, and it asserts only shape and defeat id 1294, not tunable values.
