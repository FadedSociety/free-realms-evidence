<!-- fleet job=test-audit id=tests-soe-capture-rs-L1 status=done turns=7 usd=0.0051 tokens(read,write,in,out)=[48120, 15485, 16, 5269] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soe_capture.rs lines 1-135 of 135

Window `prototype/osfr-tools/tests/soe_capture.rs` 1-135. The main replay assertions are sound: opcode and expanded length per frame, a flipped-CRC frame must return `Error::BadCrc` (checked against `soe.rs:145-158`, where a flipped trailer byte does fail the CRC compare), per-message length and byte comparison against the captured files, and `buffered_bytes`/`fragment_bytes` drained to 0. The `#[ignore]` has a reason and the fixture is external, so it is not a silent skip. The findings below are all in the diagnostics and the unchecked ack branch. None of them can let a real codec or reassembly regression pass the message-level checks.

- **[low] tests/soe_capture.rs:121 replay_local_legacy_capture - The report hardcodes `"byte_comparisons_passed":true` as a literal, so the artifact reports a pass without any computed value behind it.**
  - Why it cannot catch a regression: the literal is written whatever happened. It only stays true because the earlier asserts panic first. If a verifier or the ps1 script reads this field, it can never observe a failure from it.
  - Fix: compute the flag from the comparison loop (for example, a `byte_mismatches` counter that is asserted zero and reported), or drop the field.

- **[low] tests/soe_capture.rs:74 replay_local_legacy_capture - `corruption_rejections += 1` runs unconditionally after the `assert_eq!`, so the reported `crc_corruption_rejections` is just the frame count.**
  - Why it cannot catch a regression: the counter cannot differ from `frames.len()`, so a decode that stopped rejecting corruption would still be reported as N rejections. The only real check is the assert at lines 69-73.
  - Fix: count only when `codec.decode(&corrupt)` returns `Err(Error::BadCrc)` and assert the count equals `frames.len()`, or have the report use the counter from a match instead of an unconditional increment.

- **[low] tests/soe_capture.rs:97-100 replay_local_legacy_capture - The `CUMULATIVE_ACK` branch checks only that the payload is 2 bytes and never checks the acknowledged sequence.**
  - Why it cannot catch a regression: the sequence value is never compared to anything, so an ack encoding or sequence-order change that keeps length 2 still passes. The `acknowledgement_frames` count in the report is also unchecked.
  - Fix: decode the ack sequence and assert it is at most `receiver.next_sequence()` and non-decreasing across ack frames. Otherwise, document that the check is length-only and rename the count so it is not presented as validated.

- **[low] tests/soe_capture.rs:66 replay_local_legacy_capture - `compressed` is counted from the raw wire byte `wire[2] == 1`, independent of the decoded result, and is never asserted or compared to the index.**
  - Why it cannot catch a regression: the codec could mis-handle the compression flag, or the header offset could change, and the report would still show a count. The raw-byte read also duplicates the header layout that `Codec::decode` (`soe.rs:159-166`) already interprets.
  - Fix: assert that the codec-visible flag matches a per-frame expectation from the index, or derive the count from a decode-side accessor rather than re-reading `wire[2]`.
