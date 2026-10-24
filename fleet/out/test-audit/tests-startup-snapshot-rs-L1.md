<!-- fleet job=test-audit id=tests-startup-snapshot-rs-L1 status=done turns=6 usd=0.0043 tokens(read,write,in,out)=[34388, 14070, 14, 4385] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/startup_snapshot.rs lines 1-41 of 41

Window: `prototype/osfr-tools/tests/startup_snapshot.rs` lines 1-41. Two tests read: `empty_snapshot_serializes_as_typed_json_and_loads` (4-15) and the ignored `exports_typed_snapshot_to_lab_and_matches_all_45_builders` (17-41). Checked against `src/startup_snapshot.rs` (`empty` 139-206, `load` 208-221, `export_from_reference` 223-252, `validate` 254+, `verify_capture` 543-555).

- **[medium] prototype/osfr-tools/tests/startup_snapshot.rs:35 exports_typed_snapshot_to_lab_and_matches_all_45_builders - `assert!(output.starts_with(lab_root))` is tautological.**
  Why it cannot catch a regression: `output` is defined at line 27 as `lab_root.join("content/startup-snapshot/startup.json")`, so it always starts with `lab_root`. Any change to the export path or to `export_from_reference`'s own destination check (src 237-242) still passes this line.
  Fix: assert the exact path, e.g. `assert_eq!(output, lab_root.join("content/startup-snapshot/startup.json"))` on the path returned or written by the export, or drop the line and rely on a test that calls `export_from_reference` with a wrong output path and expects `Err`.

- **[medium] prototype/osfr-tools/tests/startup_snapshot.rs:19 exports_typed_snapshot_to_lab_and_matches_all_45_builders - the name claims a 45-builder match, but the body never checks builders.**
  Why it cannot catch a regression: the only builder check is the implicit `verify_capture` call inside `export_from_reference` (src 231, loop over `0..46` skipping 7 at src 544-552). If that call were removed or its loop narrowed, this test would still pass, since it only checks three row counts and a reloaded `schema_version`. The `Gateway::reference_state(...).expect(...)` on line 28 discards its value and checks nothing about the builders.
  Fix: assert the builder result directly, e.g. make `verify_capture` pub(crate) or add a public `verify_builders(reference)` and assert it returns Ok, and/or assert the number of compared indices equals 45 so a dropped index fails.

- **[medium] prototype/osfr-tools/tests/startup_snapshot.rs:9-13 empty_snapshot_serializes_as_typed_json_and_loads - the round trip is never compared to the original.**
  Why it cannot catch a regression: the test checks only `schema_version == 1` and two lengths. A serde change that drops or renames another field (for example `#[serde(skip)]` on `login.zone`, `character.stats`, or a `journal_definitions` vector) would still serialize and load, and the test would pass. The name's "typed JSON" claim is also unchecked.
  Fix: compare the reloaded snapshot with the original, e.g. `assert_eq!(serde_json::to_value(&loaded).unwrap(), serde_json::to_value(&snapshot).unwrap())`, so any dropped or renamed field fails.

- **[low] prototype/osfr-tools/tests/startup_snapshot.rs:30-31 exports_typed_snapshot_to_lab_and_matches_all_45_builders - exact counts 2470 quick-chat rows and 149 points of interest are pinned to reference content.**
  Why it is churn, not a missed bug: these counts change whenever the private reference content is re-captured, and they are not what the test is about (export and builder matching). Unrelated content updates would break it.
  Fix: assert `!snapshot.world.quick_chat.is_empty()` and compare against the capture's row count read from the reference, or move the exact counts to a content-specific check.

- **[low] prototype/osfr-tools/tests/startup_snapshot.rs:14 empty_snapshot_serializes_as_typed_json_and_loads - the temp file is removed only on success.**
  Why it matters: `fs::remove_file(path)` runs at the end, so any earlier assertion failure leaves `osfr-startup-snapshot-<pid>.json` in the temp dir. The leftover is harmless for pass/fail but it can make later runs with a reused PID read stale content, and the test is not self-cleaning.
  Fix: use a RAII guard (or `tempfile::NamedTempFile`) so cleanup runs on panic.

The ignored test has a reason string, so it is not a silent skip, and the `expect` on `OSFR_GATEWAY_REFERENCE` fails loudly when it is run without the reference.
