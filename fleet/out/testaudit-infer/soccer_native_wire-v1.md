<!-- fleet job=testaudit-infer id=soccer_native_wire-v1 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[23459, 16838, 8, 2679] model=claude-haiku-5-5 -->
# tests/soccer_native_wire.rs

{"file": "tests/soccer_native_wire.rs",
 "tests": [
  {"name": "sub14_exact_vector_round_trips_with_u8_state_aux_and_three_vectors", "verdict": "keep", "covered_by": null, "reason": "Pins every decoded field of the revision-3 sub-14 layout and a byte-exact re-encode. soccer.rs::synthetic_envelopes_round_trip_byte_exact only checks round-trip bytes, not field values, so it does not cover this."},
  {"name": "sub14_kick_state_refuses_context_free_intent_conversion", "verdict": "keep", "covered_by": null, "reason": "Refusal check: kick/pass states must not become a Move intent without charge policy and verified target, and read-only states must stay read-only. No equally strong test was found in the similar files."},
  {"name": "sub16_exact_vector_keeps_control_bits_as_a_u32", "verdict": "keep", "covered_by": null, "reason": "Exact-vector decode of sub 16 with field values and byte-exact re-encode. soccer.rs::ball_transform_controls_and_player_packets_decode decodes a different controls vector and checks only some fields, so this is not a duplicate."},
  {"name": "control_bits_and_unknown_states_never_classify_as_kick_or_pass", "verdict": "keep", "covered_by": null, "reason": "Exhaustive 0..=255 classification table plus control-bit canary. Nothing similar found elsewhere."},
  {"name": "sub13_impulse_round_trips_but_is_refused_as_a_client_request", "verdict": "keep", "covered_by": null, "reason": "Pins the sub-13 layout and the refusal of a client-authored impulse. soccer_match.rs (around line 214) refuses ImpulseBall through client_intent, but this test is the only one asserting the 'server-authored' reason and the exact decode."},
  {"name": "exact_offsets_match_the_revision_3_readers", "verdict": "keep", "covered_by": null, "reason": "Independent byte-offset check against raw payload slices, not through the decoder. It overlaps the field-level exact-vector tests in this file, but it guards the offset table itself, so it is kept conservatively."},
  {"name": "malformed_native_vectors_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for short, trailing and length-mismatched frames on sub 14, 16 and 13. Hostile-input coverage; no equal test named."},
  {"name": "nan_direction_bits_are_preserved_not_silently_normalized", "verdict": "keep", "covered_by": null, "reason": "Canary that NaN wire bits survive decode and re-encode. Not found elsewhere."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Every test here is a native-wire, refusal or canary check, so none is clearly removable. The strongest overlap is with tests/soccer.rs (synthetic_envelopes_round_trip_byte_exact, ball_transform_controls_and_player_packets_decode) and tests/soccer_match.rs (client_intent refusals for ImpulseBall and controls). Those overlaps are partial, since the other files do not assert these exact field values, so all verdicts stay keep. I did not read soccer_match.rs or soccer_service.rs in full, so a stronger duplicate could exist there; sub14_kick_state_refuses and sub13_impulse_round_trips are the best candidates to recheck against those files."}
