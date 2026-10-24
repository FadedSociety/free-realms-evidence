<!-- fleet job=test-audit id=tests-mining-review-rs-L1 status=done turns=7 usd=0.0071 tokens(read,write,in,out)=[107589, 24819, 16, 5806] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mining_review.rs lines 1-806 of 806

Window reviewed: `prototype/osfr-tools/tests/mining_review.rs` lines 1-806. I read the window in full and checked the code under test in `src/mining.rs`. Most of the file is sound: the handshake, trailing-comma, verify, cap, and malformed-frame tests all compare against independent constants and check state for unchanged-on-refusal. Three findings:

- **[medium] tests/mining_review.rs:664 queue_and_board_stay_bounded_across_a_scripted_chain_run - the batch bound is `<= 196`, but the reply it guards is a 20-entry refill.**
  - Why it cannot catch a regression: `src/mining.rs:1538` refills with `QUEUE_BATCH` (20) tiles and `:1546` sends them as one `OnTileQueueMsg\t-1\t` reply. The test's own message says "a <=20 batch", yet it only enforces 196. A change that sends 100-tile or 196-tile refill batches on every chain would still pass, because each list stays under 196.
  - Fix: count the replies. Assert that any `OnTileQueueMsg\t-1\t` reply after the first (the initial board reply) has exactly `QUEUE_BATCH` (20) values, or `<= 20` at least. Also assert that at least one refill reply was observed across the loop, so the check cannot pass vacuously.

- **[low] tests/mining_review.rs:614 reconnect_cancel_drops_the_run_and_stale_instance_messages_are_ignored - `replay.replies.len() == 1` pins an exact reply count that the test's claim does not need.**
  - Why it is churn, not a gap: the test is about instance-id freshness and the dropped board. Any new begin-time packet (for example an extra quota init) breaks it without touching what the name claims.
  - Fix: check for the specific begin-reply header (the one carrying `instance_id` 18_000_002 and the profile) instead of the total count.

- **[low] tests/mining_review.rs:435-437 unusable_specs_are_rejected_at_load - the doc still reads "Counterexample: `validate_spec` accepts durations and shape codes ... so `load()` succeeds". The test is now a passing regression that asserts the opposite.**
  - Why it matters: a reader who trusts the doc will believe the load gap is still open. The body is correct, so this is documentation drift, not a hole in the gate.
  - Fix: reword the doc to say it is a regression that rejects over-cap durations, unexecutable shape codes, and oversized boards, and accepts the cap boundaries (600 s, 448 cells, codes 400/499/600/699/-200/-401/-601).
