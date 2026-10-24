<!-- fleet job=test-audit id=tests-piece-081-rs-L1 status=done turns=5 usd=0.0063 tokens(read,write,in,out)=[51356, 21738, 12, 6075] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_081.rs lines 1-465 of 465

Window reviewed: `prototype/osfr-tools/tests/piece_081.rs` lines 1-465, checked against `src/restoration/piece_081.rs` (counter logic) and `src/inventory.rs` 1012-1016 and 1062-1103 (production grant and consume). The core counter assertions (allocate, floor-on-open, exhaustion, corrupt documents, verify errors) check real behaviour and would fail on realistic regressions. The findings below are the ones that are not.

- **[medium] prototype/osfr-tools/tests/piece_081.rs:372 counter_supplied_ids_close_the_production_reuse_gap - the name says the counter closes the reuse gap, but the counter is never passed to the inventory.**
  - Why it cannot catch a regression: `inventory.grant` takes its id from `allocate_from_snapshot(staged.state.next_instance_id, ...)` (inventory.rs:1013-1016), not from the `InstanceCounter` in the test. The test passes if the counter is deleted or disconnected, because the inventory's own snapshot counter gives the same 3 then 4. The only check that could fail is `production_reused == 4`, and that is a restatement of production's own allocator.
  - Fix: pass the counter's `next_instance_id()` into the inventory's stored snapshot counter (or make the grant take the id from the counter), then assert that the granted row id equals `counter.allocate()` on every grant. Or rename the test to say what it checks, which is that the snapshot counter and the durable counter agree.

- **[medium] prototype/osfr-tools/tests/piece_081.rs:392 counter_stays_monotonic_across_a_simulated_restart_after_deleting_the_top_row - no row is deleted, and the reopen is not a restart with live rows.**
  - Why it cannot catch a regression: the body only calls `counter_over(&[2, 3])`, allocates 4, then reopens with `f.counter()` (no live ids) and expects 5. Nothing is removed from the inventory. The reopen check is the same as `counter_persists_across_reopen` (line 212). A change that broke the "top row removed" case, such as a floor that ignored live ids on reopen, would not fail here, because the test never supplies a shrunken live set on reopen.
  - Fix: after allocating 4, reopen with `counter_over(&[2])` (the row 3 is deleted) and assert the next allocation is 5. Keep the name only if that is what the body does.

- **[medium] prototype/osfr-tools/tests/piece_081.rs:280 counter_write_failure_leaves_memory_and_the_document_unchanged - the name promises the document is unchanged, but the body never reads it.**
  - Why it cannot catch a regression: once the path is a directory, `fs::read` cannot read the document. The test checks only `allocate().is_err()` and the in-memory `next_instance_id`. A change that wrote a partial document before failing would still pass.
  - Fix: before replacing the file with a directory, record the bytes. Or assert the failure is `CounterError::Io(_)`. Then compare the on-disk state through a fresh `InstanceCounter::open` on a restored path, and check the reopened next id equals the value before the failed allocation.

- **[low] prototype/osfr-tools/tests/piece_081.rs:353-354 production_reward_never_reuses_a_retired_top_instance_id - the doc comment describes behaviour that is no longer in the code.**
  - Why it matters: the comment says production still allocates `max(live id) + 1` and says to delete the test once `inventory.rs` takes its id from the counter. But `inventory.rs:1012-1016` already allocates from the stored high-water mark via `allocate_from_snapshot`. The test passes today for the right reason, and the comment would mislead whoever decides whether to keep it. It is also now the same check as line 372.
  - Fix: update the doc to say production uses the snapshot high-water mark, and keep the assertion as a regression guard. Remove the duplicate once one of the two tests remains.

- **[low] prototype/osfr-tools/tests/piece_081.rs:455-460 private_campaign_counter_leads_the_live_rows - the expected values (34 rows, highest 35, next 36, persisted 37) are exact counts from one save snapshot.**
  - Why it matters: the test is about the counter leading every live row, not about the size of this character's inventory. Any change to the snapshot, even one that keeps the invariant, breaks it.
  - Fix: assert `next_instance_id() == verify(&ids)? + 1` and that `allocate()` returns `highest + 1`, and keep the exact values only in the printed evidence.
