<!-- fleet job=test-audit id=tests-character-store-rs-L1 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[18849, 13448, 10, 4982] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/character_store.rs lines 1-234 of 234

Window reviewed: `prototype/osfr-tools/tests/character_store.rs` lines 1-234, against `src/character_store.rs` (validate, load_or_create, save, replace_bytes_with, create_temporary). Most tests in the window are sound: the expected values are literals, the corrupt/unsupported-file test compares raw bytes after the rejected load, and the successive-save and invalid-update tests check both content and directory entry count. Findings:

- **[medium] tests/character_store.rs:79-108 a_fresh_process_restores_saved_coordinates - the child run is selected by a hard-coded `--exact` name, so if the test is renamed the child matches zero tests and exits successfully.**
  - Why it cannot catch a regression: `cargo test --exact <missing name>` runs "0 tests" and reports success. The parent only checks `output.status.success()`, so the parent passes without the child ever asserting `moved`. Any later change that breaks restart restore would go unnoticed after a rename.
  - Fix: have the parent require that the child actually ran the test, for example by asserting that `stdout` contains `"1 passed"` (or `"running 1 test"`), or by deriving the name from the function (e.g. a `const NAME` shared with the `#[test]` attribute). The child should also write a sentinel that the parent checks.

- **[medium] tests/character_store.rs:214-234 failed_windows_replacement_preserves_the_previous_file - only `is_err()` is asserted, so any error (not the replacement denial the comment describes) passes.**
  - Why it cannot catch a regression: with `share_mode(0)`, a regression that calls `fs::remove_file(path)` before the rename also fails with a sharing violation and returns an error. The file is then still intact, so the test passes, even though the "never delete the destination before replacement" invariant (src/character_store.rs:5, 125-127) has been broken. It would also pass if `save` failed earlier for an unrelated reason.
  - Fix: assert the error's `raw_os_error()` is `Some(5 | 32)` (sharing violation), and optionally assert the rename path was attempted (e.g. the temporary file is absent after failure and the count of entries is 1). Note that this test is `#[cfg(windows)]`, so Linux CI never compiles or runs it; the behaviour is only gated on a Windows runner.

- **[low] tests/character_store.rs:147 oversized_existing_save_is_bounded_and_preserved - the test checks the human-readable message substring "16 KiB" rather than the bound itself.**
  - Why it cannot catch a regression: it is over-pinned to wording. Rewording the error (or changing the bound text to "16384 bytes") churns the test while the bound behaviour is unchanged. Conversely, a change to a different bound that still reports "16 KiB" would pass.
  - Fix: keep the `InvalidData` kind and the byte-equality check, and derive the expected text from `MAX_FILE_BYTES` (or drop the substring check and rely on the kind plus unchanged bytes).
