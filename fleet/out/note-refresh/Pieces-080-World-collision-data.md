<!-- fleet job=note-refresh id=Pieces-080-World-collision-data status=done turns=19 usd=0.0208 tokens(read,write,in,out)=[693191, 60394, 40, 12609] model=claude-haiku-5-5 -->
# notes/Research/Pieces/080 World collision data.md

**Verdict:** current, with minor drift. The repo-side claims hold: the files, the test counts, the reader's recovered schema and the pinned-reader quote all match the tip. Two citations about client strings are slightly off. The 281-sample numbers sit in private lab reports I could not open, so I left them unchecked.

**Corrections:**

1. `old:` `` `"Chunk %s:  Unknown chunk type (Expected \"GCNK\" or \"GCK2\")"` (`00d4e6b0`). ``
   `new:` `` `"Chunk %s:  Unknown chunk type("%s").  (Expected "GCNK" or "GCK2".)"` (`00d4e6b0`). ``
   `why:` The `00d4e6b0` strings column reads `0183ff68=Chunk %s:  Unknown chunk type("%s").  (Expected "GCNK" or "GCK2".)` (client_sql, fn `00d4e6b0`). The note's wording is a paraphrase presented as a quote.

2. `old:` `(`00775e20` → `00fdfab0`)`
   `new:` `(string held in `00786890`'s string table; `00775e20` builds the `AppPhysics::CollisionData` object and calls the loader `00fdfab0`)`
   `why:` The string `017ec798=Collision data %s fo…` is listed under fn `00786890` (client_sql strings). `00775e20` has no logging strings. Its callees are `00d833a6` and `00fdfab0` (client_sql, fn `00775e20`). The note's arrow implies `00775e20` is the logging site.

**Checked and holding:**
- `prototype/osfr-tools/src/restoration/piece_080.rs` exists. The constants match the note: 16 tiles, 66.0 cell, 208 prefix, 16-byte node, 32-byte subtree, 16-byte trailer, 65535 scale. Version range 1..=6 (lines 30–49, 190). Scale checked against `65535/span` within 1% (lines 334–341). Node count is `-first_escape` (lines 344–350). Subtree area is `size - boundary - 16` (lines 378–383).
- `world = aabbMin + q / scale` is at lines 146–153.
- `prototype/osfr-tools/tests/piece_080.rs` has 4 `#[test]`s (lines 128, 145, 164, 192). The note says 4.
- `tests/pieces/test_piece_080.py` has 10 `def test_` methods (lines 70–160). The note says 10.
- `scripts/pieces/piece_080.py` exists. It has four preserved chunk inputs and four sample inputs, matching the note's list of four sample files (lines 58–71).
- The ForgeLightToolkit quote is accurate: `refs:ForgeLightToolkit/Editor/FileTypes/GcnkFile.cs:179-184`.
- Bullet type names are present in the client (fn `01130050` strings).
- `00d4e6b0` version-check string and `00fd4290`/filter `0x143` call in `010ba6e0` match the note.

**Unsure:**
- "`010ba6e0` casts vertically from `Y+2` down to `Y-2000`": the offsets come from `DAT_017ea718` and `DAT_018867c0`. The decompile shows the subtraction, but the constant values are not in the client_sql `data` column, so I could not confirm +2 and −2000.
- The `281/281`, `171/281`, `24.813`, and `0.567` figures, and the `../lab/reports/piece-080-20261009T044143Z/` bundle, live outside the repo. I could not verify them.
- `rust` `preserved_original_chunk_parses_with_the_same_schema` (tests/piece_080.rs:193–198) returns early and passes when the chunk is absent. The note does not say otherwise, but the "includes the preserved original chunk" claim holds only where that lab file exists.
