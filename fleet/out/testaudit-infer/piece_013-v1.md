<!-- fleet job=testaudit-infer id=piece_013-v1 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[21295, 14194, 8, 1671] model=claude-haiku-5-5 -->
# tests/piece_013.rs

{"file": "tests/piece_013.rs",
 "tests": [
  {"name": "recovered_movie_tables_are_present", "verdict": "keep", "covered_by": null, "reason": "Pins recovered Smelting77 constants (ores, furnace, heat, game-id, STAT_GAME_QUANTITY). No other test in the suite asserts these piece_013 tables; the smelting.rs tests drive runtime behaviour, not these tables."},
  {"name": "prepared_content_classifies_recovered_and_reconstructed_cells", "verdict": "keep", "covered_by": null, "reason": "Unique check of check_content's Origin classification (Original/Reconstructed/Unused) for the prepared content. Nothing else in tests/ exercises check_content in this module."},
  {"name": "contradictory_rows_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Hostile-input/refusal check on contradictory prepared rows (unknown ore, out-of-range measure, precision, non-positive heat/spill) plus the clamp-warning case. Refusal tests are kept; no equal test found elsewhere."},
  {"name": "wrong_phase_count_or_order_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check for phase count, stage_type order and data length. Unique to this module's check_content."},
  {"name": "payload_surface_rejects_messages_the_movie_never_sends", "verdict": "keep", "covered_by": null, "reason": "Refusal check for check_payload_surface, which is defined only in src/restoration/piece_013.rs. Smelting runtime tests (smelting.rs, smelting_gameplay.rs) send messages but do not test this surface checker."},
  {"name": "private_prepared_content_is_conformant", "verdict": "keep", "covered_by": null, "reason": "Ignored opt-in test over private lab content; it is the only check of the real prepared corpus. Removing it would lose that coverage."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "The file is a standalone focused proof: it #[path]-includes src/restoration/piece_013.rs and uses no crate modules or shared helpers. Its checks target functions (check_content, check_payload_surface, Origin) that appear nowhere else in tests/. The similar files (kart_service, harvesting, forging, piece_096, piece_092) cover other subsystems. tests/smelting.rs and smelting_gameplay.rs exercise Smelting runtime behaviour (StatUpdate and GameWon handling), which overlaps only loosely in topic, not in assertions. No test is removable. The module is not yet registered in lib.rs, so the file is the only consumer. Related Python test tests/pieces/test_piece_013.py is outside this audit."}
