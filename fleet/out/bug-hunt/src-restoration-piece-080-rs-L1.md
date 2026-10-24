<!-- fleet job=bug-hunt id=src-restoration-piece-080-rs-L1 status=done turns=6 usd=0.0101 tokens(read,write,in,out)=[66660, 26833, 14, 12072] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_080.rs lines 1-422 of 422

Window: `prototype/osfr-tools/src/restoration/piece_080.rs` lines 1-422. No remote-player path exists for any finding below. The module is not registered in any module tree. Its only compiled use is `tests/piece_080.rs` via `#[path]`, and `CollisionSection::from_gcnk` / `parse` have no production caller (checked by search). Input is a `.gcnk` file read from disk, so every finding is capped at medium/low. Most are reachable only through a malformed local asset.

- **[medium] prototype/osfr-tools/src/restoration/piece_080.rs:400 - `root_node_index + subtree_size` is an unchecked u32 addition, so the range check wraps.**
  - Failure scenario: a subtree header with `root_node_index = 0xFFFFFFFF` and `subtree_size = 1` in a payload with `node_count = 2`. The sum wraps to 0, so `0 > node_count` is false and the header is accepted. The stored `SubtreeHeader { root_node_index: 0xFFFFFFFF, subtree_size: 1 }` points outside the node array. In a debug build the same addition panics instead (and line 403 repeats it in the error message).
  - Reach: `CollisionSection::from_gcnk(bytes)` (line 185) → `parse(&collision)` (line 217) → `parse_tile(&section[..], index)` (line 231) → lines 388-400, reading the u32s from file bytes. Nothing upstream bounds them; `node_count` is checked only at 351.
  - Fix: `if subtree_size == 0 || (root_node_index as u64) + (subtree_size as u64) > node_count as u64 {` and format the end with the same widened value.

- **[low] prototype/osfr-tools/src/restoration/piece_080.rs:378 - `size - boundary - PAYLOAD_TRAILER` underflows when the bytes after the node array are 12 to 15.**
  - Failure scenario: `boundary = 208 + 16*node_count` and `size = boundary + 12`. The `head` read at line 372 succeeds (it needs 12 bytes), then line 378 computes `12 - 16` on usize. This panics in a debug build. In release it wraps to a huge value, and line 379 rejects it, so release only errors by accident.
  - Reach: same as above, `from_gcnk` → `parse_tile`, on a file-controlled `size`.
  - Fix: `let subtree_bytes = size.checked_sub(boundary + PAYLOAD_TRAILER).ok_or_else(|| CollisionError(format!("tile {index}: no room for subtrees")))?;`

- **[low] prototype/osfr-tools/src/restoration/piece_080.rs:350 - `(-first_escape)` overflows when `first_escape == i32::MIN`.**
  - Failure scenario: the root escape field at payload offset 220 is `0x80000000`. Line 345 accepts it because it is negative. `-i32::MIN` panics in a debug build; in release it wraps and line 351 rejects it.
  - Reach: `parse_tile` line 344 reads `i32_at(payload, PAYLOAD_PREFIX + 12)` from file bytes with no prior check.
  - Fix: `let node_count = first_escape.unsigned_abs() as usize;` (or `checked_neg()` with an error).

- **[low] prototype/osfr-tools/src/restoration/piece_080.rs:329 and 336 - NaN passes both the span and scale validators.**
  - Failure scenario: a tile whose `aabb_max[0]` is NaN. `span` is NaN, so `*s <= 0.5` is false and the `any` check passes. `expected = QUANT_MAX / NaN` is NaN, so `(scale - NaN).abs() > 0.01 * NaN` is false and the scale check passes too. The `parse` span check at line 265 also passes, since `NaN > 0.05` is false. The tile is accepted, but `contains_xz` (line 155) is always false, so `column()` silently never reports that tile's collision leaves.
  - Reach: `parse_tile` reads the AABB and scale floats from file bytes at lines 316-323 with no `is_finite` check.
  - Fix: reject non-finite values first, e.g. `if !span.iter().all(|s| s.is_finite() && *s > 0.5) {` and `if !(scale[axis] - expected).abs().le(&(0.01 * expected)) || !expected.is_finite()` (or simply check `is_finite()` on `aabb_min`, `aabb_max`, `scale` after the f32_at reads).

- **[low] prototype/osfr-tools/src/restoration/piece_080.rs:204 - `decompress_to_vec_zlib` has no output limit, and the declared size is checked only after inflation.**
  - Failure scenario: a zlib section whose stream inflates far beyond its header's `uncompressed` value. Deflate reaches roughly 1000:1, so a ~435 KB chunk can expand to hundreds of MB before line 206 rejects it.
  - Reach: `from_gcnk` lines 198-206 on a `.gcnk` file. The sibling `restoration/piece_098.rs:222` uses `decompress_to_vec_zlib_with_limit` for the same job.
  - Fix: `miniz_oxide::inflate::decompress_to_vec_zlib_with_limit(data, uncompressed)` and map its error to the existing "is not zlib" message, keeping the length comparison at line 206.
