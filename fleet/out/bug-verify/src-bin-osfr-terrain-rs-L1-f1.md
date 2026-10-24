<!-- fleet job=bug-verify id=src-bin-osfr-terrain-rs-L1-f1 status=done turns=6 usd=0.0060 tokens(read,write,in,out)=[63022, 20553, 14, 5542] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/bin/osfr-terrain.rs:74-79

**Verdict:** refuted (the infinite-vertex path in the claim is blocked upstream; only a narrower, low-severity finite-overflow edge case survives, and it needs corrupt trusted input)

**Severity if confirmed:** low (not medium). The defect is in an offline developer tool that reads the locally extracted client assets. No remote player input reaches it.

**Evidence:**

1. **Module tree (passes).** `src/bin/osfr-terrain.rs:8-10` includes `../restoration/piece_098.rs` via `#[path]`, and it is a real bin (under `src/bin/`). `terrain.rs` is in the lib (`src/lib.rs:96: pub mod terrain;`). So the code is in the real tool, not test-only.

2. **Upstream block on non-finite input (refutes the main claim).** The claim says `load_terrain` does no finiteness check on positions. That is wrong:
   - `piece_098.rs:432-433`: `read_terrain_vertex` reads `cursor.vec3("GCNK vertex position")`.
   - `piece_098.rs:167-169`: `vec3` calls `self.f32`.
   - `piece_098.rs:158-165`: `f32` does `if !value.is_finite() { return Err(LoadError::NonFinite(context)); }`.
   
   So a tile with `+inf`, `-inf` or NaN positions fails to load. In `osfr-terrain.rs:57-60` that is `let Ok(tile) = ... else { skipped += 1; continue; }`, so the tile never reaches the min/max loop at lines 74-78. The "stages disagree" premise does not hold. The suggested fix (`skip !is_finite` in the min/max loop) is redundant.

3. **Residual case (real but narrow).** Finite values are still allowed through `load_terrain`, so a finite extent with `(max-min)/cell >= 2^32` (e.g. coordinates around 1e10 at `--cell 2`, or f32 extents that overflow to inf when subtracted) saturates `as u32` in `terrain.rs:43-44`. The `+ 1` then panics in a debug build, and wraps to `cols = 0` in release. In release, `cols*rows > 64<<20` at `terrain.rs:45` passes with 0, `add_triangle` writes nothing, and `height_range()` returns `None` (`terrain.rs:124-127`). The check at `osfr-terrain.rs:85` uses `.filter` on `Some` only, so an empty `zone_N.hgt` is written (`to_bytes`, `terrain.rs:137-149`). The gateway's `from_bytes` accepts that grid (`terrain.rs:157-161`). I checked this arithmetic and it is correct, but it needs a client tile with a finite coordinate around 4e9 times the cell size. That is corrupt data, not a normal input.

**Corrected fix (for the residual case only):** in `HeightGrid::new` (`terrain.rs:43-44`), compute `let fc = ((max[0]-min[0])/cell).ceil();` and reject before casting if `!(fc < (1u64<<32) as f32)` or the sum with the row count exceeds the cap. Also make `to_bytes`/the tool reject `cols == 0 || rows == 0` instead of writing an empty grid. Drop the non-finite skip from the proposed fix, since `load_terrain` already rejects it.
