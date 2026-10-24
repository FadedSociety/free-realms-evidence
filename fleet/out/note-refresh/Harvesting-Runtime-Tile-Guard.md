<!-- fleet job=note-refresh id=Harvesting-Runtime-Tile-Guard status=done turns=9 usd=0.0090 tokens(read,write,in,out)=[128107, 32312, 20, 7325] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Runtime Tile Guard.md

**Verdict:** minor drift. The gate itself matches the tip; only the "Owner action" section is stale, because its fixture fix has already landed.

**Corrections:**

1. `old:`
```
`tests/type8_harvesting_gateway.rs` builds a synthetic Harvest fixture whose `spec()` registers only
the four collectables (`tiles: VALUES…category 600`). The new gate correctly refuses it, so that
target now reports 9 failures whose cause is exactly
`harvesting tile registration: content: value 401 has no registered tile kind` (captured in
`harvesting-family.log`). Its owner needs one line in that fixture: prepend the four regular kinds
`(401..404, category 400)` to `spec().tiles` — the same contract the writer emits. That file is
outside this task's ownership and was left untouched.
```
`new:` The owner action is done. `tests/type8_harvesting_gateway.rs` `spec()` now registers the four regular kinds `(401..404, category 400, icons 1..4)` ahead of the four collectables, so the gate no longer refuses that fixture. The change was the authorized fixture edit recorded in [[Harvesting Border Fix]] (item 4). No owner action remains for this guard.
`why:` repo:prototype/osfr-tools/tests/type8_harvesting_gateway.rs:95-110 (`selectable: vec![401, 402, 403, 404]`; `tiles` built from `[401, 402, 403, 404]` at category 400, chained with `VALUES` at category 600); repo:notes/Research/Harvesting Border Fix.md:89-91 (the authorized edit) and :73-74 (`type8_harvesting_gateway 11 -> 53 passed, 0 failed`).

**Checked and holding at the tip:**
- `prototype/osfr-tools/src/gameplay.rs:1000-1010`: the optional Harvest branch calls `harvesting::validate_tile_kinds_parts(&spec.selectable, &spec.collectable, &tiles)` after the profile and asset checks and before `Some(engine)` at :1023. A refusal is `invalid(...)`, which is `io::ErrorKind::InvalidData` (gameplay.rs:346-347).
- `prototype/osfr-tools/src/harvesting.rs:1242-1249`: `validate_tile_kinds(spec)` is now a thin wrapper over `validate_tile_kinds_parts`, which is `pub(crate)` at :1253.
- `prototype/osfr-tools/tests/harvesting_runtime_tiles.rs` exists with 3 tests: the malformed-config test (four cases, each asserting the tree is unchanged), `valid_four_kind_content_loads`, and `missing_content_legacy_and_mining_stay_permissive`. The count of 3 matches.
- The Mining engine stays permissive: the gate sits only in the Harvest branch, and the test pins the Mining and legacy cases.

**Unsure:**
- The receipt path `lab/reports/harvesting-runtime-tiles-20261009-1414Z/` and the logs (`green-tests.log`, `lib-tests.log`, `harvesting-family.log`) cannot be checked. `lab/` is not in the repo tree; the tests reference `lab/references/` outside it. The RED and GREEN counts therefore stand unverified.
- The RED log line `test valid_eight_kind_content_loads ... ok` quotes a test name that is now `valid_four_kind_content_loads` (harvesting_runtime_tiles.rs:184). I left it alone because it is a captured log, not a current claim.
- The note's "Change" section describes only the tile gate. The same branch now also calls `harvesting::validate_border` (gameplay.rs:1011-1014). The note's Limits section already mentions the border fix, so this is a scope note, not a false claim.
