<!-- fleet job=testaudit-infer id=piece_080-v1 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[9042, 13532, 6, 1132] model=claude-haiku-5-5 -->
# tests/piece_080.rs

{"file": "tests/piece_080.rs",
 "tests": [
  {"name": "synthetic_section_matches_the_recovered_schema", "verdict": "keep", "covered_by": null, "reason": "Only Rust check of the recovered GCNK collision-section schema (tile count, node/leaf/subtree layout, span, escape and triangle index) against src/restoration/piece_080.rs. The similar Rust files (piece_068, piece_056, mining, kart_racing, harvesting) cover unrelated subsystems. The Python test tests/pieces/test_piece_080.py checks a different implementation (scripts/pieces/piece_080.py), so it does not drive this Rust path."},
  {"name": "synthetic_column_query_reports_leaf_bands_only", "verdict": "keep", "covered_by": null, "reason": "Unique check of the Rust column() query: leaf-band hits, empty outside cells, and the gap between leaves returning nothing. No equivalent Rust test in the similar files."},
  {"name": "malformed_sections_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal test (truncated input, bad size, bad scale, bad trailer). Security/refusal check; no equally strong Rust test elsewhere."},
  {"name": "preserved_original_chunk_parses_with_the_same_schema", "verdict": "keep", "covered_by": null, "reason": "Only test against the preserved original GCNK chunk (version, terrain count, 931 nodes, 9 subtrees, native start position in a leaf band). It skips when the chunk is absent, so it is conditional but is the only real-data canary for this file."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "No Rust test in the similar-file set duplicates these assertions. tests/pieces/test_piece_080.py (Python, unittest) covers the Python reader for the same work item. It is a different implementation and is not a duplicate of these Rust tests, so nothing is marked removable. The preserved-chunk test skips silently when lab/extracted is missing, so its coverage depends on the lab checkout being present. Its assertions are not superseded by anything found."}
