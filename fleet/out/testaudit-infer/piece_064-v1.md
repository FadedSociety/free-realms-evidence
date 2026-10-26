<!-- fleet job=testaudit-infer id=piece_064-v1 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[9694, 13247, 6, 1423] model=claude-haiku-5-5 -->
# tests/piece_064.rs

{"file": "tests/piece_064.rs",
 "tests": [
  {"name": "parses_the_recovered_prefix_and_keeps_the_tail_unparsed", "verdict": "keep", "covered_by": null, "reason": "Only Rust test of CdtaMesh::parse success path and tail_len handling; no other Rust file exercises src/restoration/piece_064.rs."},
  {"name": "rejects_a_bad_magic_truncation_and_out_of_range_index", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check (bad magic, truncated index block, out-of-range index); must be kept."},
  {"name": "rejects_an_unsupported_version", "verdict": "keep", "covered_by": null, "reason": "Refusal check for version gate; distinct error path not covered by the other rejection test."},
  {"name": "bounds_cover_every_vertex", "verdict": "keep", "covered_by": null, "reason": "Only check of mesh.bounds() on the Rust side."},
  {"name": "classifies_collision_bounds_against_render_bounds", "verdict": "keep", "covered_by": null, "reason": "Only Rust check of the three BoundsRelation outcomes. The Python mirror in tests/pieces/test_piece_064.py tests scripts/pieces/piece_064.py, a different implementation, so it does not supersede this."},
  {"name": "floor_query_returns_the_highest_walkable_surface_below_the_probe", "verdict": "keep", "covered_by": null, "reason": "Only Rust check of horizontal_floor hit, miss and below-probe cases."},
  {"name": "floor_query_ignores_vertical_surfaces", "verdict": "keep", "covered_by": null, "reason": "Negative/refusal check that wall-only geometry yields no floor; not covered elsewhere in Rust."},
  {"name": "horizontal_floor_ignores_the_unparsed_tail", "verdict": "keep", "covered_by": null, "reason": "Checks that a 4096-byte tail does not change the floor result; a canary for the unparsed-tail boundary."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The five similar files (kart_service, piece_088, piece_035, piece_032, piece_027) test unrelated modules and share only boilerplate, so none supersedes these tests. The file is the sole Rust suite coverage of piece_064.rs. The Python checker tests in tests/pieces/test_piece_064.py mirror the same floor/bounds cases in a different language and implementation; if the team decides cross-language duplicates count, that is a candidate for review, but I did not mark anything removable. Doc lines are empty for all tests, so verdicts rest on names and the excerpt. No task created or changed this file per the pack (null), so no obsolescence by a later task was found."}
