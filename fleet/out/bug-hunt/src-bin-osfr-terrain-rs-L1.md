<!-- fleet job=bug-hunt id=src-bin-osfr-terrain-rs-L1 status=done turns=7 usd=0.0084 tokens(read,write,in,out)=[76030, 23263, 16, 9549] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-terrain.rs lines 1-141 of 141

Three findings in the window. All are local to this offline tool, which reads the operator's extracted client assets, so none is reachable by a remote player. Severities reflect that.

- **[medium] prototype/osfr-tools/src/bin/osfr-terrain.rs:74-79 - the bounding box is taken over every vertex, including non-finite and huge ones, and the grid is then sized from it, which overflows `cols`/`rows` in terrain.rs:43-44.**
  - Failure scenario: one GCNK tile has a vertex with x = +inf, or a finite x around 1e10 with `--cell 2`. Line 77 sets `max[0]` to that value. `HeightGrid::new` (terrain.rs:43) computes `((max-min)/cell).ceil() as u32 + 1`. The cast saturates to `u32::MAX`, so `+ 1` panics in a debug build. In a release build it wraps to `cols = 0`. Then `add_triangle` writes nothing, `height_range()` returns `None`, the flat-placeholder check at line 85 does not fire, and an empty `zone_N.hgt` is written.
  - Reach: `load_terrain` (piece_098.rs:464-573) does no finiteness or range check on positions. `read_terrain_vertex` (piece_098.rs:432-433) reads raw `vec3` floats. The tile reaches the loop at lines 62-69 and then lines 74-79. `add_triangle` (terrain.rs:62) skips non-finite triangles, but the min/max loop at lines 75-78 does not, so the two stages disagree.
  - Fix: in the min/max loop, skip vertices with `!v.is_finite()` (`if !v.iter().all(|c| c.is_finite()) { continue }`), and also reject extents where `(max-min)/cell` exceeds the 64M-node cap before the cast in terrain.rs:43-44 (e.g. `checked_add` or compare as f32 first).

- **[low] prototype/osfr-tools/src/restoration/piece_098.rs:548 (reached from osfr-terrain.rs:57) - the batch range check uses unchecked `i32` addition, so a crafted `index_offset` panics.**
  - Failure scenario: a GCNK tile has `index_offset = i32::MAX` and `index_count = 1`. In a debug build, `batch.index_offset + batch.index_count` panics with overflow. In a release build it wraps to a negative value, so the `> indices.len()` test passes. Then the slice at piece_098.rs:553 computes `(index_offset + index_count) as usize`, which wraps to a huge value, and the slice panics. Either way the whole tool aborts, instead of skipping the tile as `load_terrain` errors are meant to be skipped on line 57.
  - Reach: `i32` fields come straight from file bytes (piece_098.rs:502-503). `load_terrain` is called on each catalog tile at osfr-terrain.rs:57.
  - Fix: `batch.index_offset.checked_add(batch.index_count)` and return `LoadError::IndexOutOfRange` on `None` (or use `i64` for the sum).

- **[low] prototype/osfr-tools/src/bin/osfr-terrain.rs:121-124 and 130-138 - a spawn with a missing or non-numeric y becomes a NaN error that is counted in the statistics, while a spawn with a missing x or z is dropped.**
  - Failure scenario: a record in `npc_spawns_extra.json` has `"position": [x, z]` with no y, or with y as a string. `p.get(1)` yields NaN, so `(h - NaN).abs()` is NaN. That NaN is pushed into `errors` (line 124). It sorts last under `total_cmp`, so it can become the p90 value and print `NaN m`. It also inflates the denominator of `within(...)`, so the "% within" figures are understated. A missing x or z returns `None` from `height_at` (terrain.rs:103) and is filtered out instead, so the two cases are handled inconsistently.
  - Reach: the `--check` path, osfr-terrain.rs:105-106 and 112-124. The input is the operator-supplied spawn JSON.
  - Fix: in the `filter_map` closure, return `None` unless `x`, `y` and `z` are all finite, e.g. `if !(x.is_finite() && y.is_finite() && z.is_finite()) { return None; }` before the subtraction.

I checked the other lines in the window (argument parsing, `chunks_exact`, the index and vertex-offset lookups at 63-67, which `load_terrain` already validates at piece_098.rs:544-558, the flat-placeholder check, and the file write, which happens only after validation). I found no defects there.
