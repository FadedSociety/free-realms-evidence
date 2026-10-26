<!-- fleet job=testaudit-infer id=startup_messages-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[7488, 14188, 6, 1405] model=claude-haiku-5-5 -->
# tests/startup_messages.rs

{"file": "tests/startup_messages.rs",
 "tests": [
  {"name": "mapped_messages_reproduce_the_private_capture", "verdict": "keep", "covered_by": null, "reason": "Ignored private byte oracle that is the only test in the suite calling build_login_reply, build_initialization_parameters, build_zone_details, build_hit_points, build_mana, build_journal_set and build_done_sending_preload_characters against captured packets. Its per-message comparison is not reproduced by a named test. It is a canary and runs only with OSFR_GATEWAY_REFERENCE, so it is not removable on this evidence. Note: the gateway-level startup parity test (notes cite gateway::built_startup_sequence_matches_the_captured_character_byte_for_byte) may cover the same bytes end to end, but I did not confirm that it exercises each builder, so I keep it."},
  {"name": "synthetic_zone_name_and_id_change_their_fields", "verdict": "keep", "covered_by": null, "reason": "Only test of build_zone_details field sensitivity (name and zone_id changes). No other file in tests/ calls build_zone_details. Not clearly covered elsewhere."},
  {"name": "synthetic_journal_size_and_values_change_the_message", "verdict": "keep", "covered_by": null, "reason": "Only test of build_journal_set size and value sensitivity. No other file in tests/ calls build_journal_set. startup_world's journal test covers a different builder (journal rows) and does not replace this one."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Searched tests/ for every build_* function used here: they are called only from startup_messages.rs. Similar files (startup_catalogues, startup_world, startup_selfdata) test their own builders with analogous synthetic and oracle tests, so there is no duplicate in them. I did not inspect src/ or the gateway test bodies, so the superseded check against gateway-level parity is unverified; that is the main reason confidence is moderate."}
