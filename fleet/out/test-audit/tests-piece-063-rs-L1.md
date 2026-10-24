<!-- fleet job=test-audit id=tests-piece-063-rs-L1 status=done turns=4 usd=0.0054 tokens(read,write,in,out)=[24107, 16584, 10, 6144] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_063.rs lines 1-319 of 319

Window: `prototype/osfr-tools/tests/piece_063.rs` lines 1-319 (read with `src/restoration/piece_063.rs` as the code under test). No `#[ignore]`, no early returns, and no fixture-missing passes. The capture-frame expectations are hand-typed and check out against the hex. The rest of the window is sound.

- **[medium] tests/piece_063.rs:130 `reward_sub_opcodes_match_the_client_constructors_and_the_pinned_enums` - the name and the module doc claim a cross-check against the pinned community enum and reader, but the body only compares the source enum with a literal table in the same test.**
  - Why it cannot catch a regression: nothing reads `PacketCodes.cs` or `PacketReaderExtensions.cs`, or the client constructors. If the source and the literal table were both changed to the same wrong sub-opcode (for example 45 becoming 46 in both), the test would still pass, and so would a drift from the pinned references.
  - Fix: either rename the test to say it pins the table, or add a fixture that asserts the four (sub, class name) pairs against a checked-in copy of the pinned enum lines, with the sha256 recorded in the test, so a mismatch fails.

- **[medium] tests/piece_063.rs:190-221 `duplicate_and_replayed_finish_are_rejected_without_extra_grants` - the test never claims a parcel before the replayed finish, so it cannot show that a replay leaves existing grants intact.**
  - Why it cannot catch a regression: `finish` on a finished run returns early at `src/restoration/piece_063.rs:287`. A change that clears or resets `run.claimed` on that path (or re-inserts a claim) would still pass, because OWNER has not claimed yet at line 192. The later `claim(OWNER)` at lines 212-216 succeeds on both the correct and the broken code.
  - Fix: after `finish(INSTANCE, OWNER)` at line 192, call `claim(INSTANCE, MEMBER)` and assert it returns `bundle()`. Then do the replayed `finish` calls, then assert `pending(INSTANCE, MEMBER) == Ok(false)` and that `claim(INSTANCE, MEMBER)` is still `Err(AlreadyClaimed)`. That makes the "no extra grants" claim observable.

- **[low] tests/piece_063.rs:127 `parse_minigame_header_truncation` section (inside `original_capture_frames_decode_with_the_recovered_minigame_header`) - the comment says the header is "exactly 13 bytes", but the only acceptance check is an 18-byte `is_ok()` with no field comparison, and no 13-byte input is tested.**
  - Why it cannot catch a regression: a change to `if bytes.len() <= MINIGAME_HEADER_LEN` (rejecting exactly 13 bytes, which is the boundary) would still pass, because the 12-byte case at line 124 is rejected either way and the 18-byte case at line 127 is still accepted. The `is_ok()` also does not check that the fields come out right.
  - Fix: assert `parse_minigame_header(&bytes("0700 ..."))` on exactly 13 bytes returns `Ok` with `sub`, `state_id`, `group_id`, `game_id` and an empty `extra`, and keep the 12-byte `Err(MalformedHeader)` check.
