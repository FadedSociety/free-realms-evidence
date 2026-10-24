<!-- fleet job=test-audit id=tests-kart-racing-rs-L1 status=done turns=6 usd=0.0095 tokens(read,write,in,out)=[88399, 32315, 14, 9240] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_racing.rs lines 1-663 of 663

Reviewed `prototype/osfr-tools/tests/kart_racing.rs` lines 1-663 against `prototype/osfr-tools/src/kart_racing.rs` (decode_racing_frame, vehicle_body_asset, on_checkpoint, observe_racer_state, finish, abandon, snapshot/restore, claim_reward, TrackLayout::validate, and the constants). No `#[ignore]`, no early-return fixture skips, and no test whose expected value is computed from the code under test. The lap, checkpoint, clock, duplicate, restore-coherence and reward-once tests all exercise the real branches. Two low-severity findings:

- **[low] tests/kart_racing.rs:424 client_racer_state_is_opaque_and_never_advances_progress - the 73-byte `RACE_PROGRESS_BODY_LEN` observation is checked only for its `Recorded` return and the phase, never for the `observed_racer_states()` counter.**
  - Why it cannot catch a regression: `observe_racer_state` (src/kart_racing.rs:570-577) could stop incrementing `observed_racer_states` for the 73-byte branch (or for any branch after the first) and every assertion in this test would still pass, because the counter is only read at line 420, before the 73-byte call.
  - Fix: after line 428, add `assert_eq!(session.observed_racer_states(), 2);`. This pins the counter for both accepted lengths.

- **[low] tests/kart_racing.rs:129-131 and 143-145 captured_racing_frames_decode_with_their_recorded_flags_and_lengths - the SHA-256 assertions check the fixture bytes against a constant, not the decoder.**
  - Why it cannot catch a regression: these lines would pass for any change to `decode_racing_frame` or `vehicle_body_asset`, since they hash only the literal hex input. They do not touch what the test name claims. (The decode assertions that follow are real.) The same applies to the `digest(&encoded) == LOBBY_ORACLE_SHA256` check at line 120, which duplicates the byte comparison at line 121.
  - Fix: keep the hashes as fixture-integrity guards if desired, but move them into a separate fixture-integrity test, or add a comment stating that they guard the fixture rather than the decoder, so the decode test's name is not read as covering them.
