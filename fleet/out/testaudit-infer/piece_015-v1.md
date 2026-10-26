<!-- fleet job=testaudit-infer id=piece_015-v1 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[7505, 13410, 6, 1346] model=claude-haiku-5-5 -->
# tests/piece_015.rs

{"file": "tests/piece_015.rs",
 "tests": [
  {"name": "parses_rows_and_reports_launch_modes", "verdict": "keep", "covered_by": null, "reason": "Only Rust test of LaunchCatalogue.parse counts and the Flash/Native/None launch-mode mapping; no similar test in the other piece files drives this module."},
  {"name": "rows_with_an_undeclared_type_are_undeclared", "verdict": "keep", "covered_by": null, "reason": "Pins the undeclared-TYPE path (row references a type MiniGameTypeData does not declare). Distinct behaviour, no Rust equivalent elsewhere."},
  {"name": "malformed_row_reports_source_and_line", "verdict": "keep", "covered_by": null, "reason": "Error-reporting and hostile/short-input check (source, line, field count, expected width). Not removable without an equal test."},
  {"name": "duplicate_game_id_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Rejection check for duplicate ids; refusal-type test, keep by policy."},
  {"name": "group_links_resolve_to_game_rows", "verdict": "keep", "covered_by": null, "reason": "Only Rust check of games_in_group resolution and the empty-group case."},
  {"name": "real_tables_match_the_recovered_catalogue_counts", "verdict": "keep", "covered_by": null, "reason": "Canary against the shipped lab tables (783/22/20/610 counts and specific ids). Skips when lab absent, but it is the only real-data canary. Note: tests/test_minigame_coverage.py (Python, outside the cargo suite) checks overlapping counts and parsing, but it does not drive this Rust module, so it is not a counted equivalent."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Pack's similar files (piece_066, piece_059, piece_020, piece_010, piece_067) are about other quest/group/match modules; their shared score reflects shape, not the same code path, so none was judged superseding. Only overlapping test is the Python tests/test_minigame_coverage.py, which is not in the Rust suite; I did not read it in full and did not rely on it. The file is small, self-contained and the only Rust coverage of the piece-015 catalogue, so all six tests are kept. Lab-dependent test skips without the lab corpus, which is noted but not a reason to remove it."}
