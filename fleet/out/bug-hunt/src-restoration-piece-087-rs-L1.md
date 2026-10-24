<!-- fleet job=bug-hunt id=src-restoration-piece-087-rs-L1 status=nothing_found turns=4 usd=0.0064 tokens(read,write,in,out)=[40601, 27144, 10, 5264] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_087.rs lines 1-800 of 1289

## piece_087.rs lines 1-800: no reachable defects found

I read the whole window (1-800, plus the `Reader` tail to 860) and checked the client-facing decode paths against their callers and bounds.

What I checked:
- **`Reader::take` (787-798):** uses `checked_add` and a `len()` bound before slicing, so a huge `count` cannot panic.
- **`Reader::i32` / `u64` / `f32` (820-840):** each reads a fixed width through `take`, so no out-of-range index. `f32` rejects non-finite values.
- **`Reader::string` (842-853):** rejects negative lengths and anything over `MAX_NAME_BYTES` (128) before `take`. `from_utf8` errors are mapped, not unwrapped.
- **`Reader::boolean` (812-818):** rejects any byte other than 0 or 1.
- **`decode_friend_list` (650-662):** `count` is bounded to `0..=MAX_ROSTER_ENTRIES` before `Vec::with_capacity`, so no unbounded allocation, and it calls `reader.end()`.
- **`decode_command` (665-694):** the sub-opcode is mapped through `from_code` first. Add/Remove/Confirm bodies go through the bounded reader, the empty-name check is present, and the two unrecovered commands return `UnrecoveredBody` instead of guessing. `reader.end()` rejects trailing bytes.
- **`decode_friend_entry` (743-774) vs `encode_friend_entry` (724-741):** the field order and the online/offline branches match, including `offline_unknown` and `is_in_static_zone`.
- **Sub-opcode and command tables (121-259):** `ALL` ascending, `from_code` consistent with `code()`, and `COMMAND_SUB_OPCODES` consistent with the match arms.
- **`encode_notification` (584-637) and `encode_string` (704-707):** encoders take server-built values only (`len() as i32` on server strings). No client-controlled length reaches them.

Observation, not a reported finding: the module doc at line 50 lists `MAX_POSITION_ENTRIES` among this module's "defensive decode bounds". The constant is not defined or used in piece_087.rs. It lives in `src/social_lists.rs:34`, and this module has no position-entry decoder, so no client input reaches an unbounded position list here. This is a stale doc reference with no behavioural impact.
