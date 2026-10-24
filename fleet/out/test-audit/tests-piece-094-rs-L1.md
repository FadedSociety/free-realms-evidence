<!-- fleet job=test-audit id=tests-piece-094-rs-L1 status=done turns=6 usd=0.0071 tokens(read,write,in,out)=[54199, 22984, 14, 7339] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_094.rs lines 1-319 of 319

Window reviewed: `prototype/osfr-tools/tests/piece_094.rs` lines 1-319, against `src/restoration/piece_094.rs` (harness: `deliver`, `retire_client`, `pump`, `tick`, `set_partitioned`, `apply_ack`). The first four tests (`several_clients...`, `session_replacement...`, `reused_key_or_zero_crc...`, and the `sequence_rollover...` assertions) hold up: stale frames are classified by session tag on decode failure, and the negative control does reach `stale_accepted`. The findings are concentrated in the last test.

- **[medium] tests/piece_094.rs:305-310 a_stalled_client_fails_at_its_retry_limit_without_disturbing_others - the "delivered(0) unchanged after retirement" check cannot fail.**
  - Why it cannot catch a regression: `retire_client` sets `retired`, clears the backlog and purges every in-flight datagram for client 0 (harness lines 335-344). `deliver` returns early for retired links (line 590) and `pump` returns early too (line 492). So `delivered(0).len()` is frozen by construction between line 305 and line 310, whatever the sender or receiver does. A change that let the stalled client deliver stale or duplicate messages after the retry failure would still pass, because the retire step has already removed those datagrams.
  - Fix: before `retire_client`, assert the stall is real (`stalled_prefix < 60`, and `stress.stats(0).failed` is true). Remove the retire step, or deliver a late datagram from the stalled session afterwards, then assert that `delivered(0)` does not grow past the prefix. The current form only tests the harness's own retire logic.

- **[low] tests/piece_094.rs:315 a_stalled_client_fails_at_its_retry_limit_without_disturbing_others - `stats.loss > 0 || stress.stats(0).loss > 0` is a disjunction that is satisfied by the partitioned client alone.**
  - Why it cannot catch a regression: `loss_percent` is 0 and client 0 is partitioned, so `stress.stats(0).loss > 0` is always true (harness line 542). The clause says nothing about client 1, the client the name says must be undisturbed. Dropping all loss accounting for client 1 would still pass.
  - Fix: assert `stress.stats(1).loss == 0` (no loss is configured for it) and `stress.stats(0).loss > 0` as two separate assertions. Also assert `stress.stats(1).stale_accepted == 0`, which the sibling test checks but this one does not.

- **[low] tests/piece_094.rs:159 session_replacement_rejects_stale_datagrams_and_restarts_exactly - the message contradicts the assertion.**
  - Why it cannot catch a regression: `assert!(stats.discarded > 0, "the replaced sender retained nothing")` asserts the opposite of its message. `discarded` counts `pending_packets()` at replacement (harness line 323). A regression that dropped the discard accounting would be read as "retained nothing" in the failure output, which misleads the reader about what broke.
  - Fix: change the message to "the replaced sender had no pending packets to discard", or assert the count against the expected pending value.

- **[low] tests/piece_094.rs:247-250 sequence_rollover_with_a_small_queue_delivers_exactly_once_and_stays_bounded - nothing in the body shows the sequence actually wrapped.**
  - Why it cannot catch a regression: `COUNT = 65_600` only implies a rollover if each message takes one sequence number. That holds for these short messages, but the test never checks it. A change that made the stress harness use fewer sequences per message (for example by batching) would silently stop covering rollover, and the test would still pass on exact delivery alone.
  - Fix: assert that the sequence space was crossed, for example that `stats.sent` (or the highest sequence seen in `pump`) is at least 65_536, or expose the max sequence from the harness and assert it wrapped.

No `#[ignore]`, no early-return skips, and no fixture-missing passes were found in the window.
