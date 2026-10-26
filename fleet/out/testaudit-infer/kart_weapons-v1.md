<!-- fleet job=testaudit-infer id=kart_weapons-v1 status=done turns=3 usd=0.0043 tokens(read,write,in,out)=[28877, 22687, 8, 2396] model=claude-haiku-5-5 -->
# tests/kart_weapons.rs

{"file": "tests/kart_weapons.rs",
 "tests": [
  {"name": "codec_payload_lengths_match_the_reader_report", "verdict": "keep", "covered_by": null, "reason": "Pins the payload layout constants against the reader report; the only test asserting all eight lengths in one place. Not a duplicate of the round-trip test, which checks lengths only per encoder."},
  {"name": "codecs_round_trip_every_subtype_and_keep_the_offsets", "verdict": "keep", "covered_by": null, "reason": "Only unit-level check of field offsets for every codec. kart_service.rs tests drive the service layer and check reply length and subtype, not per-field byte offsets."},
  {"name": "inner_frames_wrap_opcode_and_subtype", "verdict": "keep", "covered_by": null, "reason": "Only check of the inner frame header (opcode and subtype bytes). Small, but not clearly covered elsewhere."},
  {"name": "decoders_refuse_wrong_lengths_and_non_finite_values", "verdict": "keep", "covered_by": null, "reason": "Refusal check on hostile input (wrong length, NaN, infinity). Must be kept under the refusal rule."},
  {"name": "pose_validation_requires_a_finite_orthonormal_right_handed_basis", "verdict": "keep", "covered_by": null, "reason": "Refusal check for non-finite, non-orthonormal and left-handed poses. kart_service::weapon_pose_rejects_nan_invalid_basis_and_clock_regression covers only NaN and a zero basis at service level, so this is not fully superseded."},
  {"name": "use_item_writes_owner_words_and_owner_local_create_matrices", "verdict": "keep", "covered_by": null, "reason": "Asserts the owner-local create matrix and owner words at unit level. kart_service::mine_use_emits_original_create checks only the subtype and length, so it is weaker."},
  {"name": "missile_update_is_a_world_matrix_and_expires_with_a_terminal_point", "verdict": "keep", "covered_by": null, "reason": "Pins the world-matrix missile update, the 10 Hz slot, the terminal point and the single destroy. Unique detail; no equivalent in the other similar files."},
  {"name": "mine_update_is_inverse_owner_local_and_expires_once", "verdict": "keep", "covered_by": null, "reason": "Pins the inverse-owner-local mine update and single expiry. Unique; kart_service mine test does not check matrix values."},
  {"name": "status_refuses_without_mutating_and_covers_every_guard", "verdict": "keep", "covered_by": null, "reason": "Refusal test covering each guard and checking that no state changes. Must be kept under the refusal rule."},
  {"name": "clear_keeps_the_id_counter_and_begin_resets_it", "verdict": "keep", "covered_by": null, "reason": "Checks that clear keeps the id counter and begin resets it. Persistence-style invariant with no equivalent elsewhere in the similar files."},
  {"name": "serde_defaults_round_trip_and_validate_for_refuses_forged_saves", "verdict": "keep", "covered_by": null, "reason": "Forged-save refusal and persistence round trip. Security-relevant; kart_service restore tests check snapshot equality but not each forged field."},
  {"name": "lifecycle_never_emits_an_explosion_or_a_hit_frame", "verdict": "keep", "covered_by": null, "reason": "Canary that 27/28 explosion subtypes are never emitted. Must be kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "All twelve tests are unit-level codec, pose, lifecycle or refusal checks on src/kart_weapons.rs. The similar kart_service.rs tests exercise the service layer and assert subtypes and lengths, not per-field offsets, matrix values or forged-save fields, so none is clearly superseded. Nothing was obviously obsolete: the file's header says explosions and hits are deferred, and the current assertions match that. I did not compare against every similar file in depth, so a light overlap with kart_service.rs (the mine-use and pose-refusal paths) may exist, but no test here is a clear duplicate."}
