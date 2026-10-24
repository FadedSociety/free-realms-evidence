<!-- fleet job=bug-hunt id=src-restoration-piece-064-rs-L1 status=nothing_found turns=4 usd=0.0039 tokens(read,write,in,out)=[23205, 16153, 10, 3216] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_064.rs lines 1-268 of 268

Reviewed `prototype/osfr-tools/src/restoration/piece_064.rs` lines 1-268 in full. No defect I can tie to a line and show reachable from client input.

Checked and cleared:
- `CdtaMesh::parse` (92-176): the 24-byte length check precedes every header read. `vertex_count * 12` uses `checked_mul`. The `index_count_offset + 4` length check runs before the vertex loop and before `Vec::with_capacity(vertex_count)`, so the allocation is bounded by the input length. The same holds for `index_count`: `checked_mul(2)` and the `bytes.len()` check both come before `with_capacity` and the index loop. All reads are in bounds. Every index is validated `< vertex_count` before it is stored, so `triangles()` (184-192) cannot index out of range. `tail_len` subtraction cannot underflow because the length check already passed.
- `bounds`, `classify_bounds`: no panics, and the logic matches the doc comments (Identical / subset / exceeds).
- `horizontal_floor` (234-268): the slope test (`|ny/len| < cos(max)` skips), the barycentric formulas, and the `y <= probe_y` highest-surface selection all match their doc comments. Degenerate triangles are guarded by `length` and `denom` thresholds.

Reach: this module is not reachable from any server or packet path. Its only consumers are the offline checker test `tests/piece_064.rs` (which `#[path]`-includes it) and the Python evidence script. No `src/` module includes `restoration/piece_064.rs` (grep of `src/` for `piece_0` and `restoration` finds no reference to it). Even if it were wired in, `parse` would accept the bytes safely, and the only defect-shaped behaviour (a NaN or infinite coordinate in `horizontal_floor`) only changes which triangles are picked and does not panic.
