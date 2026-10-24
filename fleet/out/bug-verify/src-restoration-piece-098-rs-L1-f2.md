<!-- fleet job=bug-verify id=src-restoration-piece-098-rs-L1-f2 status=done turns=5 usd=0.0051 tokens(read,write,in,out)=[44839, 22592, 12, 3591] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_098.rs:517

**Verdict:** `refuted` (the arithmetic is real, but the defect has no reachable server or player-input path)

**Severity if confirmed:** n/a. At most low, as a hardening note for an offline tool.

**Evidence:**

1. **Module tree (passes, but only to the offline tool).** `piece_098.rs` is not in `src/lib.rs` or any `mod.rs`. Its only non-test includer is `src/bin/osfr-terrain.rs:8-10` (`#[path = "../restoration/piece_098.rs"] mod piece_098;`). The `tests/piece_098.rs` harness also includes it. `search` for `piece_098|load_terrain|GCNK` over `src/` finds no other caller: `osfr-gateway.rs` only loads `osfr_tools::terrain::Terrain` (`.hgt` grids), and `gameplay.rs`, `gateway.rs` and `encounter.rs` never touch `load_terrain`.

2. **Input source (blocks the reach).** `osfr-terrain.rs:46-57` reads a local catalog TSV (`--catalog lab/manifests/rust-asset-catalog.tsv`) and `fs::read(assets.join(fields[6]))`. These are the extracted client `.gcnk` files, not player packets. The file header says the output is "derived from client data… keep it under `lab/`". The only "error" path is `let Ok(tile) = ... else { skipped += 1; continue; }`, so a bad tile is skipped rather than fatal. No remote player controls these bytes.

3. **Code facts (true, but moot for the server).** `piece_098.rs:511-519`: `if size < 0 || height_bits > 64 { Err }` and then `chunk.skip(size as usize * size as usize * height_bits as usize / 2, …)`. On 64-bit, `2^29 * 2^29 * 64 = 2^64` does wrap to 0 in release, so the claim's arithmetic is correct. `Cursor::skip` (lines 136-138) goes through `take`, which uses `checked_add` and a bounds check (123-134). So there is no memory-safety issue: the wrap gives a misparse of one local tile, not an out-of-bounds read.

4. **Consequence (overstated).** `osfr-terrain` uses only `render_batches`, `indices` and `vertices` from the tile (lines 62-69). It never reads `height_map`. So even a wrapped skip just yields a malformed local tile that `load_terrain` may accept, which can only put bad triangles into one zone's `.hgt` grid during a manual offline build. It does not corrupt a save, grant items or coins, or crash the running gateway.

**Corrected fix:** Not required for the server. If you want hygiene, use `checked_mul` (`(size as usize).checked_mul(size as usize)?.checked_mul(height_bits as usize)? / 2`, returning `LoadError::Limit`) at `piece_098.rs:517`. Keep the finding as a low-severity, offline-tool note, not a medium server defect.
