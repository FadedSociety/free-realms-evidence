<!-- fleet job=test-audit id=tests-soe-send-rs-L1 status=done turns=5 usd=0.0074 tokens(read,write,in,out)=[40200, 18252, 12, 9345] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soe_send.rs lines 1-357 of 357

Window reviewed: `prototype/osfr-tools/tests/soe_send.rs` 1-357 against `prototype/osfr-tools/src/soe_send.rs` (sender logic) and `src/soe.rs` constants. Most assertions are real. The sequence/window walk-through in `selective_ack_holes...`, the retry timing in `retries_are_identical...`, the queue-limit and rollover checks all match the code. Two findings:

- **[medium] prototype/osfr-tools/tests/soe_send.rs:135 loss_reordering_and_duplicates_reassemble_multiple_messages_once - the ACK assertions accept any `InvalidAcknowledgement`, so the ACK path is effectively unchecked (same pattern at line 141).**
  - Why it cannot catch a regression: if `ReliableSender::acknowledge` wrongly rejected every valid cumulative or selective ACK with `InvalidAcknowledgement`, line 135 and line 141 would still pass. The test would only fail indirectly, later, when `poll(...).unwrap()` hits `RetryLimit` after retransmissions. The name's "reassemble once" claim is covered by `delivered == messages` at line 150, but the ACK-handling claim is not.
  - Fix: for the first (non-duplicate) receive, assert `sender.acknowledge(&ack.packet()) == Ok(())` when `result.acknowledgement` is `Some`. For the duplicate receive (line 141), assert `Ok(())` or `Err(InvalidAcknowledgement)` explicitly, and add a `pending_packets()` or `is_idle()` check that proves the ACK changed state.

- **[medium] prototype/osfr-tools/tests/soe_send.rs:337-338 malformed_ack_clock_and_configuration_errors_do_not_mutate_sender - the clock-regression "does not mutate" claim is not tested.**
  - Why it cannot catch a regression: `poll(99)` is checked once (line 338). `src/soe_send.rs:216-217` returns before `self.last_poll = Some(now_ms)` at line 230, so a regression that records `last_poll = 99` before the check would still pass: the next `poll(199)` at line 354 succeeds either way. The test's name promises no mutation, but nothing observes `last_poll`.
  - Fix: after the ACK checks, repeat `assert_eq!(sender.poll(99), Err(SendError::ClockWentBackwards));`. That fails if the rejected clock value was stored. Optionally also assert `poll(100)` still returns the same retry state.

Minor and not reported as findings: the config-error asserts at lines 305-334 use fresh senders, so "do not mutate" there is trivially true. The `65_540` and `4` values at lines 275 and 300 are intentional wrap arithmetic, not incidental pinning.
