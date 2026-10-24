<!-- fleet job=bug-hunt id=src-restoration-piece-096-rs-L1 status=nothing_found turns=7 usd=0.0112 tokens(read,write,in,out)=[129601, 40842, 16, 9558] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_096.rs lines 1-800 of 1169

Reviewed `prototype/osfr-tools/src/restoration/piece_096.rs` lines 1-800 in full, and read 800-1169 to trace how the window's helpers are reached. I found no defect that meets the criteria, so I am not reporting any findings.

What I checked:

- **Reader helpers (347-449).** `take` uses `checked_add` and `slice.get`, so it cannot panic. `u8`, `u16`, `u32`, `i32`, `i64` and `f32` only ever pass `take` a fixed-size slice, so the `try_into().unwrap()` calls cannot fail. `text` caps the length at `MAX_TEXT` before reading. `null_terminated` takes the whole remainder (`offset <= len` is invariant), and `rest[end + 1..]` is in bounds because `end < rest.len()`. `remaining` cannot underflow. The reader's offset is advanced before an error is returned, but every error aborts the decode, so this is not a partial-state defect.
- **`split_frame` (842-860).** Length 7 is checked before `frame[..2]`, `frame[2]` and `frame[3..7]`, and `frame.len() - 7` is safe after that check.
- **Typed decode (1002-1140).** Counts are bounded before `Vec::with_capacity`: `MAX_ITEMS`, `MAX_ITEM_CHILDREN`, `MAX_ANNOUNCEMENTS`, and `MAX_MESSAGE` for lengths. Trailing bytes are rejected both in `decode_items` (`inner.end()`) and in `decode_payload`.
- **Slot and opcode tables (72-258).** `ALL` has 12 entries, matching the enum. The typed slot numbers 0-7 and 42-45 line up with the `INIT_SLOTS` array positions, and the array length is compile-checked against `INIT_SLOT_COUNT`. `for_opcode` excludes the ambiguous opcodes 35 and 38, and the other opcodes are unique.
- **Encode/decode field order.** The field order in `ZoneDetails`, `ClientGameSettings`, `ItemDefinition` (including the stat and ability children), `AnnouncementRow`, `UpdateStat` and `Motd` is the same in the encode branch (680-833) and the decode branch (862-1000, 1002-1140).

Two things I noticed but do not count as defects:

- The encoders (`encode_text`, `encode_null_terminated`, `frame`) do not check their inputs. An oversized or non-ASCII value would produce bytes the decoder then rejects. These run only on server-built values, and nothing in this file takes them from a client packet.
- The module is not registered in `restoration/mod.rs` and is not wired into the gateway (its own doc comment says so). Its only callers are its tests, so no client packet reaches it today. Any finding in the window would therefore be latent rather than remotely exploitable.
