<!-- fleet job=test-audit id=tests-soccer-match-rs-L1 status=done turns=5 usd=0.0070 tokens(read,write,in,out)=[62770, 28444, 12, 5723] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soccer_match.rs lines 1-1027 of 1027

Window: `prototype/osfr-tools/tests/soccer_match.rs` lines 1-1027. Read in full, with `src/soccer_match.rs` (client_packet 299-365, build_outcome 960-976) checked for the tests that depend on it. No `#[ignore]` or early-return skips in the window.

- **[medium] prototype/osfr-tools/tests/soccer_match.rs:813 fallback_half_length_is_labelled_reconstructed - the "labelled reconstructed" assertions cannot tell the fallback apart from a caller-supplied half.**
  - Why it cannot catch a regression: `build_outcome` (src/soccer_match.rs:972) sets `half_seconds_evidence: Evidence::Reconstructed` unconditionally. Lines 823 and 838 therefore pass for any config value. Only line 822 (`half_seconds == HALF_SECONDS`) tests the fallback, and it checks the value, not the label. If the code later labels the caller-supplied case differently (for example, by carrying the config source), this test still passes on the first half and would not notice.
  - Fix: either assert the label is derived from the configured source (add a `MatchConfig` source field and assert distinct evidence for default vs supplied), or rename the test to "half length is always labelled reconstructed" and drop the fallback claim.

- **[medium] prototype/osfr-tools/tests/soccer_match.rs:410 client_packets_never_supply_time - the body does not test that client packets carry no timing.**
  - Why it cannot catch a regression: lines 411-413 call `client_packet(&vec_player_pos(), 5)` twice on identical bytes and compare the results. Any deterministic mapping passes. The `sequence` argument is the only other input, and it is fixed at 5. A change that derived a time value from the packet bytes, or from a field such as `state_counter`, would still pass. Lines 416-420 pass `1234.5` to `apply` with `let _ =`, so the result is ignored. They only check that `server_time` is unchanged, which is already covered by `intent_clock_is_trusted_and_clamped` (line 399).
  - Fix: assert the mapping's output for a packet whose payload would carry a time if one were read, for example a `vec_player_state` with altered `state_counter`/vectors, and assert `client_intent` output is identical for two different `sequence` values, plus `assert!(game.apply(...).is_err())` or a check that the position is unchanged, instead of discarding the result with `let _`.

- **[low] prototype/osfr-tools/tests/soccer_match.rs:336 sender_identity_is_checked_before_any_victim_mutation - "victim untouched" checks only the sequence, not the victim's state.**
  - Why it cannot catch a regression: a spoofed `apply` that changed the victim's `position` or `direction` without changing `sequence` would still pass line 336, since the sequence is the only field compared. The name claims that no victim mutation happens.
  - Fix: snapshot `game.player(victim)` before the spoofed calls and assert the whole player record is equal afterwards (or assert `position` and `possession()` as well as `sequence`).

Items checked and not reported: the `is_ok()` at line 1024 (it does test a zero-distance apply after restore, so it is not vacuous), the `restore(&late).unwrap()` at line 872 (a weak but real round-trip), and the goal-once assertions at 587-592 (score and phase are compared, not only `advance`).
