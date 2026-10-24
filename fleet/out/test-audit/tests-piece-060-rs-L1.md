<!-- fleet job=test-audit id=tests-piece-060-rs-L1 status=done turns=5 usd=0.0046 tokens(read,write,in,out)=[37755, 15660, 12, 4580] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_060.rs lines 1-475 of 475

Window: `prototype/osfr-tools/tests/piece_060.rs` lines 1-475. Read in full, plus `src/restoration/piece_060.rs` at lines 566-612 (`reconnect`/`reap`) and the state constants at lines 81-84. The captured-frame, byte-literal and error-variant assertions are real checks and are not listed. Four findings:

- **[medium] tests/piece_060.rs:241 start_walks_the_recovered_encounter_states - `assert!(STATE_READY < STATE_GO && STATE_GO < STATE_RUNNING);` compares constants with each other and checks nothing about behaviour.**
  Why it cannot catch a regression: `encode_zone_ready` (41/107) and `start` never put state 4 (`STATE_READY`) on the wire in this test. A change that drops, reorders or renames the READY step would still pass, because only the constant ordering is asserted and the constants are fixed at src lines 81-84. The comment "4 -> 5 -> 6" is therefore not exercised.
  Fix: assert the state-4 packet emitted by the ready transition (or the zone-ready path) bytes, e.g. `hex(&packets[0]) == "29006a009b01000041420f0004000000"`, or delete the constant-only line and rename the test to match what it checks.

- **[medium] tests/piece_060.rs:343 completion_requires_a_connected_member_and_emits_no_reward_bytes - the "no reward bytes" claim is checked only by `starts_with(&[0x27, 0x00])` and `len() == 2`.**
  Why it cannot catch a regression: every op39 frame starts with `0x27 0x00`, so a grant or loot packet on another op39 subcode would pass as long as the count stays at 2 (for example, replacing the 39/19 body with a currency grant). The packet bodies are not compared to the pinned bytes that line 322-329 uses for the same completion.
  Fix: assert the exact bytes of both packets, as line 322-329 does, e.g. `assert_eq!(hex(&completion.packets[0]), "270012...")` and `hex(&completion.packets[1]) == "2700139b010000ffffffff9b010000"`, and drop the name's "no reward bytes" claim unless that exact-match check is present.

- **[low] tests/piece_060.rs:429-433 expired_membership_is_reaped_and_reconnect_after_the_deadline_is_rejected - the comment "the grace window is inclusive of its deadline" is attached to `reap(1_000)`, which is the disconnect time, not the deadline (31_000).**
  Why it cannot catch a regression: the inclusive boundary at `now_ms >= deadline` (src line 587) is never tested here. A change to `now_ms > deadline` would still pass this block. The boundary is only exercised indirectly by `reap(30_010)` at line 445, which is in a different test and is not named for it.
  Fix: add `assert_eq!(life.reap(30_999).unwrap_err(), Reject::NothingExpired);` and `life.reap(31_000)` expecting expiry on the same instance, and point the comment at the exact deadline value.

- **[low] tests/piece_060.rs:318-331 completion_is_once_only_and_emits_the_recovered_terminal_packets - the packet bytes are pinned to the full encoder output, so a benign field change (for example the `Won` flag or the state field) breaks the test, but the test is about once-only completion.**
  Why it is churn, not a missed bug: the test name is about single completion and terminal packet emission, but the byte literals also pin the 39/18 layout. Any unrelated encoder tweak fails this test, and the check on lines 332-339 duplicates the same bytes through the encoder.
  Fix: keep the once-only assertion (line 332) and move the exact-byte check into the dedicated encoder test (`captured_op41_frames_re_encode_byte_for_byte` or a new op39 layout test), so this test only asserts the packet count and `AlreadyCompleted`.
