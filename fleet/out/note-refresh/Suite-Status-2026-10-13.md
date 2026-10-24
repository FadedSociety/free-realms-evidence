<!-- fleet job=note-refresh id=Suite-Status-2026-10-13 status=done turns=8 usd=0.0149 tokens(read,write,in,out)=[147362, 42984, 18, 16117] model=claude-haiku-5-5 -->
# notes/Research/Suite Status 2026-10-13.md

**Verdict:** minor drift. The run record, ignored total (87), target count (185) and the `stored_count`/checked `i32` fixture claims still hold at the tip. One claim about the code is now false, and two citations have moved.

**Corrections:**

1. `old:` `` `game_store::SCHEMA_VERSION` is private, so this integration test retains the current numeric assertion without widening the source API. ``
   `new:` `` `game_store::SCHEMA_VERSION` is public (`pub const`, currently 7). `BASE_SCHEMA_VERSION` (5) and `PET_SCHEMA_VERSION` (6) are public too, and `tests/game_store.rs` asserts against `BASE_SCHEMA_VERSION` rather than a numeric literal. ``
   `why:` repo:prototype/osfr-tools/src/game_store.rs:15-17 (`pub const BASE_SCHEMA_VERSION: u32 = 5`, `PET_SCHEMA_VERSION: u32 = 6`, `SCHEMA_VERSION: u32 = 7`); repo:prototype/osfr-tools/tests/game_store.rs:4 (imports them) and :42 (`assert_eq!(upgraded["schema_version"], BASE_SCHEMA_VERSION)`).

2. `old:` `The W14 snapshot also contains the old expectation at `tests/game_store.rs:38`.`
   `new:` `The W14 snapshot also contains the old expectation at `tests/game_store.rs:38`. At the tip the schema assertion is at line 42 and uses `BASE_SCHEMA_VERSION`; line 38 is now a byte-identity check.`
   `why:` repo:prototype/osfr-tools/tests/game_store.rs:38, :42.

3. `old:` `It reported `error[E0308]` at `tests/housing_service.rs:287`: expected `i32`, found `i64`.`
   `new:` `It reported `error[E0308]` at `tests/housing_service.rs:287` (that line is now a `retain` call; the checked `i32::try_from(item.last_cast_time)` the note describes is at line 366): expected `i32`, found `i64`.`
   `why:` repo:prototype/osfr-tools/tests/housing_service.rs:287 (`self.instances.retain(...)`) and :366 (`i32::try_from(item.last_cast_time).unwrap()`).

**Unsure:**

- **Per-target rows.** Several rows do not match the test attributes at the tip. These are probably later test additions, since this is a dated run record, so I did not rewrite them:
  - `tests/game_store.rs`: the table says 1 passed; the file now has 3 `#[test]` (lines 19, 54, 73).
  - `tests/startup_selfdata.rs`: the table says 3 passed / 1 ignored; the file has 12 `#[test]`, 2 of them ignored.
  - `tests/save_schema.rs`: the table says 3 passed; the file has 5 `#[test]`.
  - `tests/kart_gameplay.rs`: the table says 9 ignored; the file has 10 `#[ignore]`.
  - `tests/dev_teleport.rs`: the table says 0 passed / 7 ignored; the file has 8 `#[ignore]` and 2 unignored `#[test]`.
  - The ignored column sums to 87 and the table has 185 rows, matching the note. I did not re-sum the passed column (1781).
- **Schema 4.** The note's "schema 4" is superseded by the tip constants (base 5, pet 6, current 7). It is dated history, so I left it.
- **"`tests/startup_selfdata.rs` and `src/startup_selfdata.rs` were not edited" and "No `src/` file needed a literal fix."** These depend on git history, which a read-only tip check cannot see. `src/startup_selfdata.rs:637` and `:666` are consistent with the note's description of the i32 self-body time field.
- **Checked as accurate:** `stored_count: 0` in `economy_review.rs:166`, `piece_045.rs:59`, `piece_081.rs:47` and `type8_harvesting_gateway.rs:427`; `i64::from(i32::MAX)` in the same files; the checked `i32::try_from` self-body encoders in `piece_045.rs:75`, `piece_081.rs:67` and `housing_service.rs:366`; `InventoryItem.last_cast_time: i64` at `src/inventory.rs:62`; and the cited `Inventory Search Crash.md` line ranges 105–106, 110–112 and 120–121.
