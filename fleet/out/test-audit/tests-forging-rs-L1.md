<!-- fleet job=test-audit id=tests-forging-rs-L1 status=done turns=4 usd=0.0066 tokens(read,write,in,out)=[42082, 24636, 10, 6220] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/forging.rs lines 1-756 of 756

Window reviewed: `prototype/osfr-tools/tests/forging.rs` lines 1-756 (read in full), with `src/forging.rs` consulted for the code under test. Most tests check real state and reply bytes; the findings below are the holes I could confirm.

- **[medium] prototype/osfr-tools/tests/forging.rs:700 content_and_persisted_bounds_fail_closed_with_explicit_reconstruction_labels - the oversize-file check is vacuous: the body writes 32769 spaces and asserts `load` errors, but that input is not valid JSON either.**
  - Why it cannot catch a regression: `forging.rs:151` rejects oversize files via `fs::metadata(...).len() > MAX_CONTENT` (`MAX_CONTENT = 32 * 1024`, line 22). Delete or weaken that cap and the same file still fails at the JSON parse (EOF), so the assertion still passes.
  - Fix: write a *valid* `forging.json` (for example the fixture JSON plus a padding string field) whose length is just over 32 KiB, and assert the load error is the size error (or that a same-shape file just under the cap loads). Alternatively, assert on the error message text.

- **[medium] prototype/osfr-tools/tests/forging.rs:660 content_and_persisted_bounds_fail_closed_with_explicit_reconstruction_labels - the name promises checks on "explicit reconstruction labels", but the mutation list touches only `reconstructed_rules` (line 664) and `reconstructed_consumption` (line 671); `reconstructed_tint_selection` is never mutated.**
  - Why it cannot catch a regression: `forging.rs:1036` checks `!r.reconstructed_tint_selection`. Removing or inverting that check still leaves every case in the loop erroring out, so the test passes. The loop also uses bare `is_err()` without checking the error reason, so an error from an unrelated field also satisfies it.
  - Fix: add `(vec!["recipe", "reconstructed_tint_selection"], json!(false))` to the case list, and assert on the error message (or on a distinct error) so each label is shown to be the reason for rejection.

- **[low] prototype/osfr-tools/tests/forging.rs:626 pause_server_deadline_cancel_and_pending_queue_reconnect_never_award - the name claims a "pending queue reconnect" is covered, but the body never builds a pending tile queue or reconnect state. It only cancels a restored game and begins a new one.**
  - Why it cannot catch a regression: a change that mishandles a pending/queued tile state across reload would still pass, because no queued state is set up before the save/restore at lines 645-651.
  - Fix: before the save at line 645, set a non-empty pending `tile_queue` (or the equivalent pending state), then assert after `load` that the queue is preserved or cleared as intended and that `completed` stays 0. Otherwise rename the test to drop "pending queue reconnect".
