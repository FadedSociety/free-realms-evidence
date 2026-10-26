<!-- fleet job=testaudit-infer id=world_notice-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[11120, 14527, 6, 1392] model=claude-haiku-5-5 -->
# tests/world_notice.rs

{"file": "tests/world_notice.rs",
 "tests": [
  {"name": "admin_broadcast_sets_one_system_line_without_character_change", "verdict": "keep", "covered_by": null, "reason": "Only test in tests/ that drives a successful `realm broadcast` through handle_in_world and asserts the notice text, no state change, and the 15/3 encoding. The bin rig t199_world_notice.rs covers fanout, not this per-session gameplay path."},
  {"name": "player_and_builder_broadcasts_are_refused_without_a_notice", "verdict": "keep", "covered_by": null, "reason": "Role refusal check for the broadcast command. role_enforcement.rs checks \"Cannot do that\" for other commands, not realm broadcast. Refusal tests are kept by policy."},
  {"name": "empty_overlong_multibyte_or_control_text_is_refused", "verdict": "keep", "covered_by": null, "reason": "Hostile-input and bound pins (200 chars / 2048 bytes, control characters, NUL). Not covered by another test file. The bin rig repeats some of these cases but through the gateway, not gameplay, so it is not an equal check."},
  {"name": "announcement_text_is_trimmed_escaped_and_never_echoes_the_command", "verdict": "keep", "covered_by": null, "reason": "Unique check of trimming, XML-style escaping of the encoded packet, and no echo of the command. Nothing else in the suite asserts this."},
  {"name": "an_active_cooking_movie_refuses_the_broadcast_before_staging_it", "verdict": "keep", "covered_by": null, "reason": "Ordering refusal during a cooking movie. developer_teleport.rs checks the same \"Close the cooking game\" text on a different path (teleport), so it is not equivalent. Kept as a unique ordering check."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "The similar-file pack (kart_npc_entry, player_trade, npc_interaction, kart_service, coin_authoring) shares no broadcast tests, so the overlap comes from the shared handle_in_world path, not from matching assertions. I grepped the repo for 'realm broadcast' and found only scavenger_hunt_two_players.rs (uses broadcast as an event probe, not these assertions) and the bin rig t199_world_notice.rs (gateway fanout). Neither makes a test here redundant. The file is small and each test checks a distinct property, so I kept all five. I did not read the full bodies of the similar files, so the claim of no duplicates rests on the test names and the grep."}
