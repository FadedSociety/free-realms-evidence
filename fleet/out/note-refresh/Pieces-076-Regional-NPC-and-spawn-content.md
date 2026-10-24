<!-- fleet job=note-refresh id=Pieces-076-Regional-NPC-and-spawn-content status=done turns=10 usd=0.0095 tokens(read,write,in,out)=[180600, 33794, 22, 6929] model=claude-haiku-5-5 -->
# notes/Research/Pieces/076 Regional NPC and spawn content.md

**Verdict:** minor drift. The note's file paths, test counts and the zone record match the tip. One area-shape count is wrong (three rectangles and six circles, not four and five).

**Corrections:**

- `old:` (four rectangles, five circles)
  `new:` (three rectangles, six circles)
  `why:` `repo:prototype/osfr-tools/src/restoration/piece_076.rs:102-187` (`REGION_AREAS`) has Blackspore, Sanctuary and Seaside as `AreaShape::Rectangle` and Briarwood, Merryvale, Shrouded Glades, Snowhill, Wugachug and Sunstone Valley as `AreaShape::Circle`. The same shapes appear in `refs:Sanctuary/src/Resources/Zones/FabledRealms.json:23-98`.

**Checked and holding:**

- The four owned artifact paths exist: `src/restoration/piece_076.rs`, `tests/piece_076.rs`, `scripts/pieces/piece_076.py` and `tests/pieces/test_piece_076.py`.
- `tests/piece_076.rs` is a `#[path = "../src/restoration/piece_076.rs"]` include (lines 25-29), and no `pub mod piece_076;` is registered anywhere under `src/`. The note's "until the lead registers it" is accurate.
- The Rust acceptance file has 9 `#[test]` functions, matching "9 focused tests".
- The Python suite has 16 `def test_` cases, matching "16 stdlib unittest cases".
- The checker writes `placement-catalogue.json` and `validation-report.json` (`scripts/pieces/piece_076.py:443-446`).
- The wiki aliases `Merryvale`→`Merry Vale` and `Shrouded Glades`→`Shrouded Glade` are present (`scripts/pieces/piece_076.py:67-69`).
- The zone record matches the source: id 1, name FabledRealms, tile size 64, latitude -48..80, longitude -32..96, spawn `[-1904.883, -39.7098, 412.6024]`, nine area definitions (`refs:Sanctuary/src/Resources/Zones/FabledRealms.json`). The Rust constants also match (`piece_076.rs:28-73`).
- The 33081 guid is `100000033190` in the pinned Sanctuary revision (`refs:Sanctuary/src/Scripts/Zone/FabledRealms.lua:3409`).

**Unsure:**

- The placement total (3426), the capture-guid and model-asset counts (793 and 56), the 4253 legacy placements, and the 4 terrain-bound rows could not be recounted with the search tool. The Rust constants agree with the note, but I did not verify the source counts.
- The note pins Sanctuary revision `4f028dcc`, which I take to be the `refs:Sanctuary/` tree. Other snapshots in refs differ: `refs:Sanctuary-main-20261019/src/Scripts/Zone/FabledRealms.lua:3458` uses `100000033167` for npc 33167, where the pinned revision uses the CaptureGuid. This is a different revision, so I did not treat it as a correction.
- The test-run results (1298 passed, 130 targets) and the `lab/reports` paths are outside the repo and cannot be checked from here.
