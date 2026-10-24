<!-- fleet job=test-audit id=tests-soccer-native-wire-rs-L1 status=nothing_found turns=6 usd=0.0052 tokens(read,write,in,out)=[50358, 17521, 14, 5088] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soccer_native_wire.rs lines 1-276 of 276

Reviewed `prototype/osfr-tools/tests/soccer_native_wire.rs` lines 1-276 (all 276 lines) against the code under test: `soccer.rs` `decode` (length-mismatch and trailing-byte checks at ~460-475, sub-13 refusal path), and `soccer_match.rs` `classify_state` (273-279), `client_packet` (299-348) and `client_intent` (352-365).

No findings in the five categories:

- **Cannot fail:** the round-trip, offset, and field assertions compare against hand-built byte vectors and hard-coded expected values (`sub14_payload`, `sub16_payload`, `sub13_payload`, `envelope`), not against output of the code under test. The 0..=255 classification loop uses a hand-typed table rather than calling `classify_state` to derive its expectation, so it does detect changes to the match arms.
- **Asserts nothing that matters:** every test has concrete assertions on decoded fields, re-encoded bytes, or the `ClientPacket`/`Intent` variant. The refusal tests check error substrings that name the refusal reason, and the read-only paths check the variant. The `is_err()` checks for malformed input (lines 238-258) are backed by the length and trailing-byte checks in `decode`.
- **Name overclaims:** each test name is backed by its body. `sub14_kick_state_refuses_context_free_intent_conversion` checks the refusal from `client_intent` and that the error is not "Move". The control-bits test checks that raw bit patterns come back as `Intent::Controls` and are preserved through encode. The NaN test checks `is_nan()` and byte-exact re-encode.
- **Silently skipped:** no `#[ignore]` and no early returns in this window.
- **Over-pinned:** the exact offsets in `exact_offsets_match_the_revision_3_readers` are the stated purpose of that test (the revision-3 layout), so they are not incidental.

Minor observations I did not count as findings: the sequence value passed to `client_intent` (5) is not asserted in the controls test, and the NaN test's byte-equality check depends on `f32` bit preservation through decode, which holds on this code path.
