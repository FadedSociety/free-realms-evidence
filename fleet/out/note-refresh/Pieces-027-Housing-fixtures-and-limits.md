<!-- fleet job=note-refresh id=Pieces-027-Housing-fixtures-and-limits status=done turns=14 usd=0.0204 tokens(read,write,in,out)=[513338, 65416, 30, 14261] model=claude-haiku-5-5 -->
# notes/Research/Pieces/027 Housing fixtures and limits.md

**Verdict:** minor drift. The note's paths, test counts, Lua line citations, client decompile facts and the 31-row community table check out. One dimension is wrong.

**Corrections:**

1. `old:` row 7 is a 1024 x 1024 x 1024 catch-all box spanning zones, unlike the ~120-200 unit lot boxes.
   `new:` row 7 is a 1024 x 200 x 1024 catch-all box (Y from -100 to 100) spanning zones, unlike the ~120-200 unit lot boxes.
   `why:` `repo` is not the source here; the table is `refs:Sanctuary/src/Resources/Houses.json:93-97`, where row 7 `BuildAreas` is Min `[0, -100, 0]` and Max `[1024, 100.0, 1024]`. The Y span is 200, not 1024. The note's own description of the table is otherwise confirmed.

**Verified, no change needed:**
- Owned files exist: `prototype/osfr-tools/src/restoration/piece_027.rs` (226 lines), `prototype/osfr-tools/tests/piece_027.rs`, `scripts/pieces/piece_027.py`, `tests/pieces/test_piece_027.py`.
- Test counts: 12 `#[test]` functions in `tests/piece_027.rs` (matches "12 passed"). 7 `unittest` methods in `tests/pieces/test_piece_027.py` (matches "7 passed").
- The module is not registered: no `pub mod piece_027` exists, and `tests/piece_027.rs` uses `#[path = "../src/restoration/piece_027.rs"]`, as the note says.
- `Housing.GRID_SIZE_ON = 25` / `GRID_SIZE_OFF = 5` at `ui:ScriptsBase.lua:33266-33267`, and `gridSpacing = 25` at `:33277`. `ToggleGrid` at `:33640`, `SetGrid` at `:33649`, `RotateFixtureClockwise` at `:33736`, `HousingInstance_DS.MaxFixtureCount` at `:2594`, auto-orientation at `:56830`/`:56870-56877`. `SetData` starts at `:33624`, and its `SetCounts` invoke is at `:33631`.
- Decompile facts: `FUN_00c0ba80` computes `DAT_017ec67c / local_8` and stores it at `+0x4188`. `FUN_00c0c0f0` (clockwise) passes id 7 and `FUN_00c0c0a0` (counter-clockwise) passes id 6 (`client_sql` fn table).
- Inverted axes: rows 30 (y), 31 (y), 32 (y and z), 33 (z), 34 (z) are the only inverted boxes in `Houses.json`. Ids 11, 12 and 13 are absent. Row 1 spawn x 444.3 against max 443.3 is confirmed. The 19-row spawn-outside list is consistent with spot checks.
- `PlayerHousingInstanceData.cs` has `MaxFixtureCount`, `MaxLandmarkCount` and `BuildAreas` (`refs:Sanctuary/src/Sanctuary.Packet.Common/Housing/PlayerHousingInstanceData.cs:24,25,57`).
- Test expectations use `HousingMaxFixtures` (`client:Resources/CodeStringMappings.txt:1666`). `test.adr` appears in `client:Resources/HousingPlacementData.txt:2`.

**Unsure:**
- `FixturePlacementDenied` and the `rg -a` confirmation against `FreeRealms.exe`: the exe is not in any readable root. The client `Resources` shows only `HousingMaxFixtures`; `FixturePlacementDenied` has no hits there.
- "so rows 30-34 cannot be loaded silently": the Rust `BuildBounds::validate` does reject inverted boxes (`piece_027.rs:163-175`). But nothing in the module loads `Houses.json`; only the Python checker reads it, and it reports inverted axes rather than calling the Rust validator. The phrase describes a contract, not a loader guard. It may mislead, but I did not find a false fact.
- The `Houses.json` sha256 and "identical in the pinned Sanctuary and FreeRealms-Legacy copies": both copies exist (`refs:FreeRealms-Legacy/...` and `refs:Sanctuary/...`, with `"Id": 7` at line 87 in each), but I did not hash them.
- The `+0x128` flag, `DAT_017ea5a4 = -0.0`, and the snap formula inside `FUN_00aab720` were not re-derived from the decompile beyond the function header.
