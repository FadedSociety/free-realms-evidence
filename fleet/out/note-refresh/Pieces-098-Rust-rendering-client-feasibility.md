<!-- fleet job=note-refresh id=Pieces-098-Rust-rendering-client-feasibility status=done turns=16 usd=0.0180 tokens(read,write,in,out)=[445580, 56821, 34, 12935] model=claude-haiku-5-5 -->
# notes/Research/Pieces/098 Rust rendering/client feasibility.md

**Verdict:** minor drift. The file layout, test counts, Granny magics, version gates, limits and the terrain batch check all match the tip. One integration sentence is incomplete because a second in-tree consumer now uses the module by `#[path]`.

**Corrections:**

- `old:`
  ```
  5. Lead registration of `pub mod piece_098;` if this slice is adopted; the owned test uses
     `#[path]` until then.
  ```
  `new:`
  ```
  5. Lead registration of `pub mod piece_098;` if this slice is adopted; the owned test (`tests/piece_098.rs:21`) and the `osfr-terrain` bin (`src/bin/osfr-terrain.rs:8-10`, which calls `piece_098::load_terrain` at line 57 to build zone height grids) use `#[path]` until then.
  ```
  `why:` `prototype/osfr-tools/tests/piece_098.rs:21` and `prototype/osfr-tools/src/bin/osfr-terrain.rs:8-10,57`. `lib.rs` still has no `piece_098` module, so the registration gap itself is accurate; only the list of `#[path]` consumers is stale.

**Checked and holding (no change):**

- Paths exist: `src/restoration/piece_098.rs`, `tests/piece_098.rs`, `scripts/pieces/piece_098.py` (with `--verify`, `piece_098.py:485`), `tests/pieces/test_piece_098.py`.
- Rust test split: 11 `#[test]` in `tests/piece_098.rs`, one of them `#[ignore]` (line 646), so 10 ordinary plus 1 ignored.
- Python: 8 `def test_` in `tests/pieces/test_piece_098.py`.
- Granny magics (`piece_098.rs:35-42`) match the note's hex values.
- `GCNK` version gate 0..=6 (`piece_098.rs:470`). v2-v4 runtime objects are refused (`piece_098.rs:321-323`), as the note says.
- `DMOD` version 2..=3 (`piece_098.rs:717`). `DSKE` 48-byte tail (`piece_098.rs:855`). 52/36-byte model vertex layouts (`piece_098.rs:667,689`). 44-byte Granny section entry (`piece_098.rs:1070`).
- Terrain indices are checked per render batch with `vertex_offset` added (`piece_098.rs:544-558`).
- Non-finite floats are refused (`piece_098.rs:161`).

**Unsure:**

- The note says "Only piece 098's four assigned code/test paths … were written." `src/bin/osfr-terrain.rs` (a height-grid tool that consumes `load_terrain`) exists in the tree, and the note never mentions it. I could not establish who wrote it, so I did not correct the sentence. It may be the "existing artifact-floor work" the note refers to.
- "The whole ordinary suite does not compile right now" (lines 92-93) is a point-in-time build claim. I could not compile, so I could not confirm or refute it.
- The `--lib` count of 24 passing tests could not be verified by grep (the crate has many `#[test]` sites across bins and modules).
- The private-bundle numbers (76 derived checks, 16 tiles, the clip counts, the 6,559/1,224 magic split) live under `lab/` and were not checked.</result>
