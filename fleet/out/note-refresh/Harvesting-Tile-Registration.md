<!-- fleet job=note-refresh id=Harvesting-Tile-Registration status=done turns=9 usd=0.0125 tokens(read,write,in,out)=[168899, 38065, 20, 12162] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Tile Registration.md

**Verdict:** badly stale in the Repair and Owner-action sections. The core defect (regular kinds unregistered) and the `validate_tile_kinds` guard are still current, but the tip no longer registers the 601..604 collectables at all, and the four-kind selectable set is per region, not `401..404`.

**Corrections:**

1. `old:`
```
- `board_spec` now registers the four regular kinds **first** (`category = 400`, `icon_id` 1..4,
  mirroring the mining spec's selectable entries) and then the four collectables in the recovered
  produce order; `selectable` is emitted from the same constant.
```
`new:`
```
- `board_spec` registers only the region's four selectable kinds (`category = 400`, one per recovered produce value, taken from `produce_value_for(slug)`, so region 109 gives 401/410/415/407). Each kind's `icon_id` is `value - 400` (1/10/15/7 for region 109), and `collectable` is `Vec::new()`. `selectable` is emitted from the same list.
```
`why:` repo:prototype/osfr-tools/src/harvesting.rs:933-972 (tiles pushed per produce, `icon_id: value - 400`), :999 (`collectable: Vec::new()`); tests/harvesting.rs:531 (`(401,400,1),(410,400,10),(415,400,15),(407,400,7)`). Also notes/Research/Type8 Native Repair Round.md:87-91 records the same removal.

2. `old:` `Preserved unchanged: collectable values/order, quotas,`
`new:` `Preserved unchanged: quotas,` and add after the list: `validate_content` now refuses any non-empty `collectable` ("harvesting must not use the 600-block collectables").
`why:` repo:prototype/osfr-tools/src/harvesting.rs:1208-1214 (refusal); :82-88 (600-block never used by harvesting).

3. `old:` `and `REGULAR_TILE_VALUES = [401, 402, 403, 404]`.`
`new:` `and no shared regular-value table. The regional produce values come from `produce_value_for(slug)` per region (region 109: 401/410/415/407).`
`why:` repo:prototype/osfr-tools/src/harvesting.rs:946 (`produce_value_for`); a repo-wide search finds `REGULAR_TILE_VALUES` only in notes (Type8 Native Repair Round.md:86 says it is gone). Also tests/harvesting_tile_registration.rs:87-102 (`selectable_values` / `expected_pairs`).

4. `old:` `exact eight-kind registration contract:`
`new:` `four-kind contract (`tiles.len() == 4`, category 400, icons 1/10/15/7 for region 109, `collectable.is_empty()`). The block now sits at lines 522-544, and the eight-kind snippet below is not in the file:`
`why:` repo:prototype/osfr-tools/tests/harvesting.rs:522-544 (line 524 `assert_eq!(c.spec.tiles.len(), 4);`, line 539 `assert!(c.spec.collectable.is_empty());`).

5. `old:` `The collectable subset order and the Gummyfruit icon pin are preserved, so the test keeps its`
`new:` `The Gummyfruit icon pin is kept as a goal icon (`goals[0].icon_id == 706`, line 540), and the collectable subset check is replaced by `collectable.is_empty()` (line 539), so the test keeps its`
`why:` repo:prototype/osfr-tools/tests/harvesting.rs:539-540. No tile entry carries icon 706; the 706 pin is on the goal.

6. `old:` `` `(401,1)(402,2)(403,3)(404,4)(601,1)(602,2)(603,3)(604,4)` for every one of the six regional ``
`new:` `` the four produce pairs `(value, value - 400)` of each regional spec, e.g. region 109 `(401,1)(410,10)(415,15)(407,7)`; no 601..604 pairs are asserted ``
`why:` repo:prototype/osfr-tools/tests/harvesting_tile_registration.rs:97-102 (`expected_pairs`), :171-210 (kind count 4, `collectable.is_empty()`, wire set `== expected_pairs(game_id)`).

**Unsure:**
- The 9-test count in `tests/harvesting_tile_registration.rs` is correct (9 `#[test]` functions), but the test bodies now assert the regional produce set, not the 601..604 set described in the wire-vector sentence above.
- The hash move `b01020e4…` → `9ac8a2f1…` for `tests/harvesting.rs` and all pass/fail counts in the Verification table could not be checked (no logs read). The current file no longer has the eight-kind block, so the hash claim is probably stale too.
- `lab/reports/harvesting-tile-registration-20261009-1351Z/` (logs, `fresh-content/`, `tile-registration.json`) was not inspected; the lab directory was outside the roots I could list.
- The "RED: 1 passed / 7 failed" baseline and the "fresh export" are historical and unverifiable from the tip.
- Verified as current: `TILE_SELECTABLE_CATEGORY = 400` / `TILE_COLLECTABLE_CATEGORY = 600` (harvesting.rs:81, 88); `validate_content` (harvesting.rs:1053) calls `validate_tile_kinds` (:1163, wrapper at :1242 over `validate_tile_kinds_parts` :1253); `mining.rs::initialize_board` (:1320) emits `OnTileInfoMsg/t{value}/t{index}` (:1377).
