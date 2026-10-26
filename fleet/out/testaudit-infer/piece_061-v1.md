<!-- fleet job=testaudit-infer id=piece_061-v1 status=done turns=2 usd=0.0036 tokens(read,write,in,out)=[12199, 18371, 6, 2308] model=claude-haiku-5-5 -->
# tests/piece_061.rs

{"file": "tests/piece_061.rs",
 "tests": [
  {"name": "recovered_room_boxes_come_from_the_original_area_table", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the recovered tutorial room boxes, area ids and the spawn-sample containment against the src/restoration/piece_061.rs constants. No other test file includes this module."},
  {"name": "tutorial_rooms_are_ordered_by_both_name_and_axis", "verdict": "keep", "covered_by": null, "reason": "Only check of tutorial room order and wall-plane geometry. Its door_02 Z-bounds assertions overlap recovered_doors_sit_on_the_recovered_room_transitions, but the room-order and wall-plane assertions are unique, so it is kept conservatively."},
  {"name": "recovered_doors_sit_on_the_recovered_room_transitions", "verdict": "keep", "covered_by": null, "reason": "Only test pinning DOOR_01/DOOR_02 object ids, rotations and positions against the room transitions."},
  {"name": "recovered_gate_clips_and_verb_sounds_are_listed", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the door clip set, rock-barrier clips and verb sound names. Asset-list data check with no other coverage in the suite."},
  {"name": "chain_opens_each_gate_only_after_its_room_is_cleared", "verdict": "keep", "covered_by": null, "reason": "Core ordered-completion behaviour of DungeonChain; no equivalent elsewhere."},
  {"name": "gate_requests_are_refused_until_the_server_unlocks_them", "verdict": "keep", "covered_by": null, "reason": "Refusal check: client-initiated door requests are locked until the server unlocks them. Security-relevant, so kept."},
  {"name": "duplicate_and_out_of_order_clears_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check for duplicate clears, out-of-order rooms and invalid actor instance 0. Kept as hostile-input coverage."},
  {"name": "chain_refuses_wave_specs_that_do_not_match_the_recovered_rooms", "verdict": "keep", "covered_by": null, "reason": "Refusal check for malformed wave specs (missing room, duplicate room, zero count). Kept."},
  {"name": "position_reports_reject_bypass_into_a_locked_room", "verdict": "keep", "covered_by": null, "reason": "Security refusal check: walking into locked rooms yields BypassAttempt. Kept."},
  {"name": "extra_clears_after_a_completed_room_are_rejected_and_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check that an extra clear after completion changes nothing. Partly overlaps duplicate_and_out_of_order_clears_are_rejected (out-of-order rejection), but it uses a fresh instance on a completed room and asserts state is unchanged, so it is kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "The file is the only test driver for src/restoration/piece_061.rs (included via #[path]); no other test file in the pack covers this module, so no superseded or duplicate verdicts are supported. The five similar files (kart_service, piece_032, player_trade, kart_npc_entry, housing_service) test unrelated modules and share only generic gate/refusal vocabulary. Possible minor overlap: tutorial_rooms_are_ordered_by_both_name_and_axis and recovered_doors_sit_on_the_recovered_room_transitions both assert DOOR_02's Z bounds; and extra_clears vs duplicate_and_out_of_order_clears overlap on out-of-order rejection. Trimming those would be a cosmetic cleanup, not a redundancy removal. The lab notes list 10 tests, matching the file."}
