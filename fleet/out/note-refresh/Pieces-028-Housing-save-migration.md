<!-- fleet job=note-refresh id=Pieces-028-Housing-save-migration status=done turns=20 usd=0.0273 tokens(read,write,in,out)=[844285, 72665, 42, 19555] model=claude-haiku-5-5 -->
# notes/Research/Pieces/028 Housing save migration.md

**Verdict:** minor drift. The module, file paths, test counts (14 Rust vectors, 11 Python tests), the version dispatch, the `load_state` refusal, the Houses.json row-1 values and the community-server claims all hold at the tip. Four statements are stale because `housing` was registered and item 045 added a field to `SavedFixture`. A fifth citation (tests/piece_028.rs) is wrong.

**Corrections:**

1. `old:` the item 006 housing module is still awaiting lead registration.
   `new:` the item 006 housing module is registered in `src/lib.rs` (`pub mod housing;`); this module (028) is not yet.
   `why:` repo:prototype/osfr-tools/src/lib.rs:30 (`pub mod housing;`). `src/lib.rs` has no `restoration` module, so 028 is still unregistered (repo:prototype/osfr-tools/src/lib.rs:1-102).

2. `old:` Register `housing` and this module in `src/lib.rs`, then replace the
   `new:` `housing` is already registered (`pub mod housing;`, `src/lib.rs:30`); register only this module in `src/lib.rs`, then replace the
   `why:` repo:prototype/osfr-tools/src/lib.rs:30; repo:prototype/osfr-tools/src/restoration/piece_028.rs:69-73 still includes housing by `#[path]`.

3. `old:` `#[path]` include here and in `tests/piece_028.rs` with `use crate::housing;`.
   `new:` `#[path]` include here (`src/restoration/piece_028.rs:69-71`) with `use crate::housing;`. `tests/piece_028.rs` does not include `housing.rs`; it includes this module by `#[path = "../src/restoration/piece_028.rs"]` (line 27), so that include is what switches to the registered module once 028 is registered.
   `why:` repo:prototype/osfr-tools/tests/piece_028.rs:27-29 (the only `#[path]` in that file names piece_028.rs, not housing.rs); repo:prototype/osfr-tools/src/restoration/piece_028.rs:69-75.

4. `old:** **cannot complete**: `tests/piece_035.rs` and `tests/piece_038.rs` include `src/restoration/piece_035.rs`/`piece_038.rs`, which do not exist yet. Not this item's failure`
   Note: the old text is the table cell in the `cargo.ps1 test` (whole crate) row, at line 131. Copy it exactly.
   `new:` **could not complete when logged**: `tests/piece_035.rs` and `tests/piece_038.rs` include `src/restoration/piece_035.rs`/`piece_038.rs`, which were missing at that run. Both files now exist at the tip, so this row needs a re-run. Not this item's failure.
   `why:` repo:prototype/osfr-tools/src/restoration/ (`piece_035.rs` and `piece_038.rs` are listed); repo:prototype/osfr-tools/tests/piece_035.rs:27 and tests/piece_038.rs:27 both include them.

5. `old:` `minus the two fields the item 006 review added` (line 84)
   `new:` `minus the two fields the item 006 review added`, and a legacy fixture row carries no `placed_by` (added by item 045, `#[serde(default)]` = 0). The loader attributes a 0 to the lot owner when it restores. The migration copies that 0 through unchanged.
   `why:` repo:prototype/osfr-tools/src/housing.rs:128-134 (`placed_by`, `#[serde(default)]`) and :137-140 (`attributed_to`, applied in `rebuild` at :1314); repo:prototype/osfr-tools/src/restoration/piece_028.rs:269 (fixtures copied as-is); repo:notes/Autopilot/L045.md:56-61 (the item that added the field and touched `tests/piece_028.rs`).

**Unsure:**
- `lab/reports/piece-028-20261009-0345Z/` (red/green logs, checker summary) and the Houses.json sha256 cannot be checked: `lab/` is not in the repo tree, and I have no hash tool. The 14-vector and 11-test counts do match the code.
- `src/game_store.rs` "loads version 1 … and version 2 … upgrades in memory" (note line 75-77): the version dispatch exists at `game_store.rs:32`, `:88`, `:165`, but I did not read the upgrade path to confirm the wording.
- Houses.json has 31 rows (Ids 1–10 and 14–34), as the note says. Row 1 (Id 1, ZoneId 1, NameId 6514, Min 322.0/-100/392.1, Max 443.3/60.0/477.8) matches `piece_028.rs:17-19`.
- Verified as true: `DatabaseContext` has the 11 listed DbSets; the MySql migrations are the 8 listed; `housing not implemented` appears at `BaseHousingPacketHandler.cs:35`; `load_state` refuses any version other than 1 with `CorruptSnapshot` (`housing.rs:1296-1297`).
