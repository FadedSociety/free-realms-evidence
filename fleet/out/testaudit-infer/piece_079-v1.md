<!-- fleet job=testaudit-infer id=piece_079-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[9665, 14305, 6, 1520] model=claude-haiku-5-5 -->
# tests/piece_079.rs

{"file": "tests/piece_079.rs",
 "tests": [
  {"name": "classifies_the_preserved_header_shapes", "verdict": "keep", "covered_by": null, "reason": "Unit-level check of the Rust classify() header parser (GCNK version, placeholder, unknown magic, truncation). No similar test file exercises piece_079's classifier; the similar piece_0xx files cover other work items."},
  {"name": "survey_accumulates_versions_and_placeholders", "verdict": "keep", "covered_by": null, "reason": "Only test of TerrainSurvey accumulation and the out-of-window version (7) and unknown-magic refusal paths in this crate. Not covered by the similar files."},
  {"name": "declared_coverage_matches_the_pinned_reader", "verdict": "keep", "covered_by": null, "reason": "Canary asserting the declared coverage constants (collision and detail mask not decoded, version window 0..=6). Guards against silently overstating coverage; keep."},
  {"name": "preserved_world_matches_the_recovered_inventory", "verdict": "keep", "covered_by": null, "reason": "Re-derives the 2,344-chunk inventory from the preserved lab originals and checks the version histogram. Depends on ../lab evidence, which is the only check of that inventory here; it is a canary for asset drift."},
  {"name": "pinned_survey_matches_the_declared_gap_numbers", "verdict": "keep", "covered_by": null, "reason": "Checks the recorded pinned-reader survey JSON against declared OK/fail/abort/NotImplemented counts. Unique gap-number canary; not duplicated in the similar files."},
  {"name": "variant_survey_recovers_the_documented_share_and_keeps_the_v4_gap_open", "verdict": "keep", "covered_by": null, "reason": "Checks the variant-reader recovery share and that the v4 gap stays open. This is a refusal/canary-style guard on a documented gap; no equivalent elsewhere in the pack."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Nothing is clearly superseded. The closest overlap is the Python checker test tests/pieces/test_piece_079.py (it re-checks the same recorded survey JSON, variant survey, and placeholder/version counts via scripts/pieces/piece_079.py), and the inventory/gap-number tests here largely mirror it. It is a different language and binary, and the Python file is not in the similar-file pack, so I kept everything rather than name a cross-language duplicate. If the team consolidates, the pinned_survey and variant_survey tests are the likeliest candidates to be checked against the Python suite. Several tests depend on the out-of-Git ../lab tree and will fail or be skipped without it; that is a portability concern, not a redundancy one."}
