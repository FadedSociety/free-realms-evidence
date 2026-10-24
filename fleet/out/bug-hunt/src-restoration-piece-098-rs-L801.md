<!-- fleet job=bug-hunt id=src-restoration-piece-098-rs-L801 status=done turns=9 usd=0.0137 tokens(read,write,in,out)=[172437, 43183, 20, 13196] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_098.rs lines 801-1158 of 1158

Window 801-1158 of `prototype/osfr-tools/src/restoration/piece_098.rs` reviewed in full (with `Cursor` at 109-212 and the constants at 53-58). No panic path was found. Every slice and index in the window is guarded: `u32_at`, `probe_granny`'s table and payload math (1113-1145), the 48-byte bind-pose tail (856-877), and the `get(..)` lookups in `scan_animation_slots` all hold. Nothing in the window mutates persistent state, so there is no atomicity issue. The loader has no caller in `src/` (only `tests/piece_098.rs`) and reads preserved asset files, not network packets, so all three findings below are low severity.

- **[low] piece_098.rs:849-854 - `load_skeleton` parses bone names with a cursor over the whole file, so a name can run past the declared name block (`names_end`).** 
  - **Failure scenario:** A `DSKE` with `names_size = 3` and bytes `ABC` at offset 12 has no NUL inside the block. `cursor.string` at 853 scans up to `MAX_STRING_BYTES` through the file and stops at the next NUL, which lies in the hierarchy or bind-pose bytes. The loader returns `Ok` with a bone name that spans into the hierarchy blob. Nothing rechecks `cursor.offset` against `names_end` after the loop, and `hierarchy_bytes` (863) is still computed as if the names ended at `names_end`.
  - **Reach:** Only `load_skeleton(bytes)`, which takes a file. `Cursor::string` (181-198) bounds reads by the whole buffer, not by the name block. No upstream check stops it.
  - **Fix:** Give the names loop its own cursor over `&bytes[..names_end]`, or return `Inconsistent` if `cursor.offset > names_end` after each `string` call.

- **[low] piece_098.rs:945-949 and 963-969 (`scan_animation_slots`) - the `0x01` and `0x02` length prefixes are only range-checked and never compared with the name or file length.** The doc comment at 931-932 says "length-prefixed", but the names are taken as the printable run up to a `0x00`.
  - **Failure scenario:** Section bytes `01 03 'a' 'b' 'c' 'd' 'e' 'f' 00 02 05 'x' '.' 'g' 'r' '2' 00` pass the scan and produce slot `"abcdef"`, even though the prefix says 3. A misaligned or stray `0x01` in a real bank yields a phantom animation slot with no length check to reject it.
  - **Reach:** `load_actor` (1059-1061) passes section 9 payloads straight to this scan. No check exists upstream.
  - **Fix:** Require `name_end - name_start == length_byte as usize` and `file_end - file_start == file_length as usize` (the 0x7f cap stays), or correct the doc comment if the pinned toolkit ignores the prefix.

- **[low] piece_098.rs:1059-1061 - `load_actor` extends `animation_slots` once per section 9 with no aggregate cap, so the per-section `MAX_ANIMATION_SLOTS` (1004) does not bound the actor total.** Dedup (1000-1012) is also per section, so identical slots repeat across sections.
  - **Failure scenario:** An `ADR` with 4096 section-9 blocks (the `MAX_ACTOR_SECTIONS` limit at 1023), each holding 4096 unique slots, yields about 16.7M `AnimationSlot`s, each with two heap strings. The input is roughly 180 MB, and the memory cost is over 1 GB, while the constant's name suggests a 4096 bound per actor.
  - **Reach:** `load_actor(bytes)` with a file of that size. Nothing checks the running total.
  - **Fix:** Check `actor.animation_slots.len() + new.len() <= MAX_ANIMATION_SLOTS` before `extend` (return `Limit`), and optionally dedup across sections.
