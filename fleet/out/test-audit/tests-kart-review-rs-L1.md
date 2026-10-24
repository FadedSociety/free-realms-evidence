<!-- fleet job=test-audit id=tests-kart-review-rs-L1 status=done turns=8 usd=0.0086 tokens(read,write,in,out)=[126719, 27835, 18, 7767] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_review.rs lines 1-691 of 691

Window reviewed: `prototype/osfr-tools/tests/kart_review.rs` lines 1-691 (read in full, plus `src/kart_racing.rs` 196-260, 565-600, 636-724 to check the code under test). Three findings.

- **[medium] prototype/osfr-tools/tests/kart_review.rs:219 `checkpoint_skips_stale_replays_and_unknowns_never_advance_progress`... (actually in test `captured_lobby_payload_has_a_length_prefix_and_six_rows`) - `assert_eq!(2393 - 11, 2382)` compares a literal arithmetic expression with a literal and touches no code under test.**
  - Why it cannot catch a regression: it can never fail, whatever the decoder, the capture, or the module does. It only looks like a check that the 2,393-byte frame yields a 2,382-byte payload.
  - Fix: delete the line, or make it real: `decode_racing_frame` on the full captured frame must report `payload.len() == 2382`. The full frame is not in this file, so either load the archived capture from the `lab/reports/...` path with a hash check, or assert the payload length from the 48-byte prefix via the declared length (`declared + 7 - 11 == 2382`) using the parsed `declared` variable.

- **[medium] prototype/osfr-tools/tests/kart_review.rs:378-388 `session_claims_are_local_and_the_id_is_exposed_for_provenance` (the "impostor" block) - the impostor never finishes, so the test does not exercise the claim "a different session with the same id has no claim authority".**
  - Why it cannot catch a regression: `claim_reward` (src/kart_racing.rs:706-708) returns `NotFinished` on the phase check before reading any other state. The impostor is abandoned, so the assertion passes for any implementation that keeps that early phase check, including one that keys a shared reward record by `session_id`, which the test is supposed to rule out. The block only repeats the abandoned-run case already covered in `reward_authority_is_derived_from_the_priced_run_only`.
  - Fix: drive the impostor to `Finished` with the same id 9 and an unpriced layout (`on_checkpoint` 11 and 12 with `finish` ready). Then assert `claim_reward() == Ok(RewardProposal::Unpriced)` and that the `finisher` still returns `RewardAlreadyClaimed` on a second call. A shared-by-id grant would then return `Granted` or `RewardAlreadyClaimed` and fail.

- **[low] prototype/osfr-tools/tests/kart_review.rs:365-366 `session_claims_are_local_and_the_id_is_exposed_for_provenance` - the two `on_checkpoint` results for the finisher are discarded, with no assertion.**
  - Why it cannot catch a regression: if either gate were refused (for example, `OutOfOrder` or `NotRacing` after a change in gate handling), the test would still reach `finish(20)`. That call only fails if the phase is not `Finished`, so the test reports the failure only indirectly and with a less clear message.
  - Fix: `assert_eq!(finisher.on_checkpoint(10, 11), CheckpointOutcome::CheckpointAccepted { lap: 1, index: 0 });` and the matching `LapCompleted { lap: 1, lap_ms: 20 }` for gate 12.

Checked and not reported: the restore case table (each case reaches `CorruptSnapshot` through its named check, e.g. `laps_completed > laps` at src/kart_racing.rs:650); the flag-0 and lobby oracle tests (expected bytes come from the pinned hex and SHA, not the code under test); there are no `#[ignore]` attributes and no early returns in the window.
