<!-- fleet job=testaudit-infer id=bundle_activity_content-v1 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[24859, 16621, 8, 1686] model=claude-haiku-5-5 -->
# tests/bundle_activity_content.rs

{"file": "tests/bundle_activity_content.rs",
 "tests": [
  {"name": "frozen_activity_bytes_are_the_reviewed_snapshot", "verdict": "keep", "covered_by": null, "reason": "Canary: pins SHA-256 of the shipped activity bytes. The encounters.json hash is also embedded in saved state and in fixtures/save_schema/current-v2.json and scripts/pieces/piece_051.py, so this is the only guard on the exact bytes."},
  {"name": "bundled_activity_content_loads_without_lab", "verdict": "keep", "covered_by": null, "reason": "Broad bundle-load check over a scratch copy of data/content with no lab fallback. Individual loaders are exercised elsewhere (kart_gateway.rs, kart_npc_entry.rs, mining.rs, harvesting_review.rs), but none of those prove the whole bundle loads from a directory copy, and T313 cites it as a bundle guard. Not clearly covered, so kept."},
  {"name": "activity_refusals_leave_the_content_directory_unchanged", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a wrong game_id board and duplicate kart gates must be refused and must leave the directory byte-identical. Similar refusals exist (mining.rs load refusals, kart_npc_entry.rs:398 and :406 for kart load errors), but none asserts the no-mutation property on a copied bundle. Refusal tests are not removable without an equally strong named test."},
  {"name": "python_activity_gate_refuses_loader_invalid_bindings", "verdict": "keep", "covered_by": null, "reason": "Runs a separate Python regression (tests/test_bundle_activity_content.py) that is a different language path; notes F165.md and T313.md cite it as a gate. Cannot be superseded by a Rust test. Kept conservatively; I did not open the Python file to confirm its assertions."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "No test is a clear duplicate. The file is a bundle-level canary and refusal suite, and its tests overlap only partially with per-loader tests in kart_gateway.rs, kart_npc_entry.rs, mining.rs and harvesting_review.rs. The pack's excerpt was cut off before the last test, so I read the file tail directly. I did not check the Python file's contents or run the suite."}
