<!-- fleet job=testaudit-infer id=piece_035-v1 status=done turns=3 usd=0.0045 tokens(read,write,in,out)=[29127, 19747, 8, 3516] model=claude-haiku-5-5 -->
# tests/piece_035.rs

{"file": "tests/piece_035.rs",
 "tests": [
  {"name": "recovered_family_and_sub_opcodes_match_the_client_and_the_pinned_readers", "verdict": "keep", "covered_by": null, "reason": "Pins the family and sub-opcode constants. Partly overlaps tests/piece_036.rs::ability_packet_ids_are_the_recovered_original_values and tests/piece_055.rs::recovered_packet_vocabulary_is_pinned, but it also pins SET_DEFINITION, CLIENT_REQUEST_START_ABILITY, ABILITY_DEFINITION and the toolbar slot constants, which those do not. Cheap, so kept."},
  {"name": "archer_kit_is_the_recovered_ranged_kit_and_outreaches_the_melee_kits", "verdict": "keep", "covered_by": null, "reason": "Archer-specific kit constants with a reach ordering check. Only Archer data lives here; the wizard kit is pinned in piece_036 and is a different profile."},
  {"name": "start_ability_request_decodes_a_position_target", "verdict": "keep", "covered_by": null, "reason": "Only decode check of the Archer StartAbilityRequest position form. piece_036 covers a different module's ground-target path."},
  {"name": "start_ability_request_decodes_a_guid_target", "verdict": "keep", "covered_by": null, "reason": "Only decode check of the GUID target form for this request type."},
  {"name": "start_ability_request_rejects_wrong_family_truncation_and_trailing_bytes", "verdict": "keep", "covered_by": null, "reason": "Hostile-input and refusal check (wrong family/sub, truncation, trailing bytes). Must be kept."},
  {"name": "toolbar_decodes_eight_positional_slots_and_surfaces_the_range_float", "verdict": "keep", "covered_by": null, "reason": "Only check that the Type-3 slot range float is surfaced. Unique to this file."},
  {"name": "toolbar_rejects_a_wrong_slot_count_a_bad_profile_and_short_frames", "verdict": "keep", "covered_by": null, "reason": "Refusal check for bad slot count, profile and truncation. Must be kept."},
  {"name": "ability_failure_uses_the_recovered_no_cast_vocabulary", "verdict": "keep", "covered_by": null, "reason": "Pins the NoCast string-id mapping and the AbilityPacketFailed encoding. Not confirmed elsewhere, so kept."},
  {"name": "start_casting_frame_matches_the_client_constructor_defaults", "verdict": "keep", "covered_by": null, "reason": "Byte-level layout check of the StartCasting frame against the client constructor defaults. Not confirmed duplicated; kept."},
  {"name": "reach_gate_admits_the_documented_ranged_reach_and_refuses_beyond_it", "verdict": "keep", "covered_by": null, "reason": "Boundary check of this file's Archer reach gate. piece_036's out-of-reach test uses the wizard gate and 20u, a different path."},
  {"name": "line_of_sight_is_opt_in_and_never_fabricates_a_retail_rule", "verdict": "keep", "covered_by": null, "reason": "Reconstructed predicate. Checks that no refusal is invented without supplied geometry. Canary-like; kept."},
  {"name": "composed_gate_checks_reach_then_geometry_and_refuses_non_finite_positions", "verdict": "keep", "covered_by": null, "reason": "Tests the composed reach-then-geometry admit path and NaN/inf refusal. Unique to this module."},
  {"name": "no_ammo_is_consumed_because_no_ammo_economy_was_recovered", "verdict": "keep", "covered_by": null, "reason": "Pins the AmmoPolicy::NotRecovered stance. Shallow, but it is a deliberate canary against inventing an ammo economy; kept."},
  {"name": "non_finite_input_is_refused_before_any_policy_runs", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal across decode, gate constructor, admit and toolbar paths. Overlaps tests/piece_055.rs::out_of_range_target_never_enters_the_cast (NaN) and piece_036 non-finite caster, but covers more entry points. Must be kept."},
  {"name": "projectile_subs_are_known_but_their_payloads_stay_unrecovered", "verdict": "keep", "covered_by": null, "reason": "Pins that projectile payloads stay Unrecovered. Only piece_055 pins the sub-codes, not this payload stance. Canary; kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "No test is clearly redundant. The closest overlaps are the opcode pins with tests/piece_036.rs::ability_packet_ids_are_the_recovered_original_values and tests/piece_055.rs::recovered_packet_vocabulary_is_pinned, and the NaN refusal with piece_055::out_of_range_target_never_enters_the_cast. Each has a distinguishing part, so none is marked superseded. Verdicts are based on the names and the file body; I did not open the bodies of piece_036 or piece_055 beyond the pinning tests, nor the similar files' full assertions, so some keeps may be too conservative. The file is an Archer-specific sibling of piece_036 (wizard) and piece_055 (enemy cast), so the file as a whole is not removable."}
]}
