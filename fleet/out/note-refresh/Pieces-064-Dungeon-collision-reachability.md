<!-- fleet job=note-refresh id=Pieces-064-Dungeon-collision-reachability status=nothing_found turns=13 usd=0.0156 tokens(read,write,in,out)=[358571, 51504, 28, 11171] model=claude-haiku-5-5 -->
# notes/Research/Pieces/064 Dungeon collision/reachability.md

**Verdict:** current. Every code-checkable claim in `reachability.md` matches the tip. I found no false statements and no moved citations, so there are no corrections.

**Checked and holding:**
- **Rust reader:** `prototype/osfr-tools/src/restoration/piece_064.rs` exists. It defines `CdtaMesh::parse`, `classify_bounds`, `horizontal_floor` and `MAX_SLOPE_DEGREES = 50.0` (lines 47, 92, 214, 234). The note's description of the module matches.
- **Not registered:** no `mod piece_064` appears under `prototype/osfr-tools/src`. The test includes the file via `#[path = "../src/restoration/piece_064.rs"]` at `tests/piece_064.rs:33-35`, which matches the note's "until the lead registers it".
- **Rust tests:** `tests/piece_064.rs` has 8 `#[test]` functions (lines 78-207), matching "8 tests".
- **Python checker and tests:** `scripts/pieces/piece_064.py` exists, with `FLOOR_CELL = 0.5`, `MAX_STEP = 0.6`, `MAX_SLOPE_DEGREES = 50.0`, `CAVE_ZONE_ID = 411`, an `--out` option and a `--native-log` option (lines 48-62, 638-645). `tests/pieces/test_piece_064.py` has 15 `def test_` methods, matching "15 tests".
- **Room mapping:** `local_from_world` returns `(wz - 370, wy - 5, 380 - wx)` (`scripts/pieces/piece_064.py:367-370`), which matches `local = (worldZ - 370, worldY - 5, 380 - worldX)`.
- **Asset table:** all 11 pack paths and SHA-256 prefixes match `CAVE_COLLISION_ASSETS` (lines 70-137).
- **Test-backed figures:** room_01 has 1016 triangles and 361022 tail bytes (`test_piece_064.py:172-173`). The water header is `[8, 1, 0]` with 4 vertices (lines 178-179). The GCNK count is 16 chunks, each inflating to 5632 bytes (lines 183-184). The native replay expects 456 samples in zone 411, 456 render-supported, 0 collision-supported and max render delta under 0.1 (lines 192-196).
- **Decoder gap:** `ForgeLightToolkit/Editor/FileTypes/GcnkFile.cs` has `LoadCollision` at line 179 with `// TODO: Bullet Physics` at line 181, as the note says (`refs`).
- **Route probes:** `ROUTE_PROBES` has 8 entries and `route_probes()` returns one row per probe (lines 140-149, 560-580).

**Unsure (could not be checked from the repo):**
- The lab-only numbers: 2280 prefix vertices, 2108 shared vertices, 994/1007 triangle matches, the 456-sample trace bounds, `enemy3` 27.9622 and `boss_inward` 27.9912, the 0.046 and 0.040 deltas, and the render-AABB comparisons for room_02 and room_02_02. They depend on `lab/` artifacts that are not in the repo. The checker logic that produces them is consistent with the note.
- `room_01_02`, `room_03`, `room_03_02` and the water asset are marked "identical". The repo test only asserts identity for room_01, and the water relation is not tested.
- `probe-collision.py` is cited under `../lab/reports/piece-064-20261009T0438Z/`. It is not in `scripts/pieces/`, so I could not confirm it exists.
- The `visible_cube.adr`/`.cdt` pairing and the manifest `.z` pairs are client-asset claims that I did not check.
