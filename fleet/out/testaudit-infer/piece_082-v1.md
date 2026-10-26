<!-- fleet job=testaudit-infer id=piece_082-v1 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[9276, 13557, 6, 1474] model=claude-haiku-5-5 -->
# tests/piece_082.rs

{"file": "tests/piece_082.rs",
 "tests": [
  {"name": "fully_resolved_rows_report_no_gaps", "verdict": "keep", "covered_by": null, "reason": "Only test of the preflight's resolved-row report; no other file uses the piece_082 module (the similar files cover unrelated systems: piece_084 sell/buyback, piece_029 housing, mining, players)."},
  {"name": "instance_without_a_definition_is_reported_with_both_ids", "verdict": "keep", "covered_by": null, "reason": "Only check that a missing definition is reported with both instance and definition ids; unique to this module."},
  {"name": "dangling_definition_category_and_name_are_reported", "verdict": "keep", "covered_by": null, "reason": "Only check of dangling category and localized-name reporting; unique to this module."},
  {"name": "duplicate_instance_and_conflicting_definition_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check (duplicate instance id and conflicting definition rejected); no equivalent elsewhere."},
  {"name": "zero_and_negative_identifiers_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check for zero and negative ids; no equivalent elsewhere."},
  {"name": "fingerprint_is_deterministic_and_sensitive_to_the_input_set", "verdict": "keep", "covered_by": null, "reason": "Determinism and sensitivity of the fingerprint, which the Python checker cross-validates; not covered elsewhere."},
  {"name": "recovered_native_constants_stay_pinned", "verdict": "keep", "covered_by": null, "reason": "Pins recovered native offsets and data-source names; a canary against silent drift, not replaced by any later task."},
  {"name": "private_crash_run_preflight_matches_the_python_checker", "verdict": "keep", "covered_by": null, "reason": "Cross-implementation oracle against the Python checker on preserved crash-run inputs. It is #[ignore]d and needs a private file, so it is not run in the normal suite, but it is the only Rust/Python agreement check and must not be removed."}
 ],
 "whole_file_removable": false,
 "confidence": 0.9,
 "notes": "The file is the sole Rust test for src/restoration/piece_082.rs, which is the only implementation of this work item (piece_082 is referenced from notes and scripts/pieces/piece_082.py, with tests/pieces/test_piece_082.py as its Python counterpart). None of the five similar files exercise inventory search, the content index, or the fingerprint. No redundancy was found. The ignored private oracle does not run in the default suite, so it adds no per-merge cost, and it should stay. The research note records 7 passing and 1 ignored test for this file, which matches the test list."}
