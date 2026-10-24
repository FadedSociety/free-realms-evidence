<!-- fleet job=bug-hunt id=src-zone-transition-rs-L1 status=nothing_found turns=4 usd=0.0039 tokens(read,write,in,out)=[25303, 16008, 10, 3354] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/zone_transition.rs lines 1-264 of 264

Reviewed `prototype/osfr-tools/src/zone_transition.rs` lines 1-264 in full, plus the callers (`gateway.rs:955-985`, `world.rs:1470-1493`, `soccer_service.rs:1014-1039`, `kart_gateway.rs:261`). I found no defect that meets the criteria. Checks performed:

- **Decode bounds:** `decode` requires `len >= 9` (line 191) before indexing `bytes[0..2]`, `bytes[2]` and `bytes[3..7]`, so those slices are safe. `declared != len - 7` (line 204) cannot underflow. `Cursor::take` (137-152) uses `checked_add` and a bounds filter. `text` (174-185) rejects negative and over-4096 lengths before `as usize`, and `from_utf8` is handled with `map_err`, not unwrap. The `try_into().unwrap()` calls at 159, 163 and 167 are on exact-size slices from `take`, so they cannot panic.
- **Trailing bytes and layout:** the fixed tail is 16 bytes (`TAIL_BYTES`, line 33), matching the fields read at 236-242 and written at 113-119. The final `cursor.offset != bytes.len()` check (243) rejects trailing data.
- **Encode:** string lengths are capped at 4096 before `as i32` (97-98, 105, 111), so there is no truncation. Non-finite position, rotation and update radius are rejected (99-101), consistent with the decoder. The `u32::try_from` check (121) is correct.
- **Atomicity:** `encode` and `decode` are pure. They build a local buffer and return it, so no state changes before a fallible step.
- **Trust:** `decode` is only reached from `gateway.rs:977`, which decodes a frame the server built itself as a self-check, and from tests. It is not a client-input path. The client-facing side goes through `encode`, which validates every field it writes.
- **Non-issues noted but not reported:** `tutorial` is normalised to a bool (any nonzero becomes `true`), and `decode` is stricter than the native reader on position floats. Neither is a defect.
