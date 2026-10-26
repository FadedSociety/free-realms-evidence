<!-- fleet job=testaudit-infer id=fishing_review-v1 status=done turns=3 usd=0.0052 tokens(read,write,in,out)=[28334, 25546, 8, 3480] model=claude-haiku-5-5 -->
# tests/fishing_review.rs

{"file": "tests/fishing_review.rs",
 "tests": [
  {"name": "native_envelope_and_register_field_order", "verdict": "keep", "covered_by": null, "reason": "Builds bytes by hand from the native writers (opcode 138, u16 sub, handle, flag) and checks encode and decode. tests/fishing.rs::header_is_two_u16_fields and every_recovered_request_round_trips use the module's own encoder, so this independent byte-level check is not redundant."},
  {"name": "native_cast_anim_and_cast_field_order", "verdict": "keep", "covered_by": null, "reason": "Hand-built field order for CastAnim, Cast, ReelIn and Special, plus a bit-exact NaN payload round-trip. The NaN losslessness check is not in tests/fishing.rs."},
  {"name": "native_result_body_read_order_is_preserved", "verdict": "keep", "covered_by": null, "reason": "Distinct-value Result body pins read order field by field. Only partly overlaps tests/fishing.rs::fishing_result_rejects_nan_fields, which asserts validity, not field placement."},
  {"name": "result_prefixes_are_rejected_without_panicking", "verdict": "keep", "covered_by": null, "reason": "Every prefix of a minimal Result body must fail to decode. Refusal and truncation check, not found elsewhere in this form."},
  {"name": "result_blob_lengths_are_bounded", "verdict": "keep", "covered_by": null, "reason": "Security bound: oversized and u32::MAX blob lengths must be refused as Oversize before allocation. Keep."},
  {"name": "decode_known_enforces_the_decoder_body_bound", "verdict": "keep", "covered_by": null, "reason": "Refusal of bodies over MAX_BODY, plus byte-lossless opaque passthrough. Keep."},
  {"name": "deterministic_byte_scan_never_panics_and_round_trips", "verdict": "keep", "covered_by": null, "reason": "Fuzz-style canary over all lengths and all recovered sub-opcodes. Keep."},
  {"name": "request_bodies_are_exact_length", "verdict": "keep", "covered_by": null, "reason": "Exact-length refusal for each request sub (empty, short, trailing). tests/fishing.rs::request_lengths_match_native_writers checks encoded lengths only, so this is not a duplicate."},
  {"name": "request_decode_rejects_non_request_sub_opcodes", "verdict": "keep", "covered_by": null, "reason": "Rejects server-only sub-opcodes as client requests. tests/fishing.rs::decode_rejects_bad_envelopes checks only UnknownSub(9), so this covers a wider set."},
  {"name": "actor_accessor_matches_every_request_variant", "verdict": "keep", "covered_by": null, "reason": "Small accessor check across all five variants. Not found elsewhere in this form; low value but cheap and unique."},
  {"name": "session_binding_lifecycle", "verdict": "keep", "covered_by": null, "reason": "Binding, duplicate registration, foreign refusal and reset lifecycle. Overlaps tests/fishing.rs::re_registration_and_reset_policy and session_rejects_requests_from_a_foreign_actor in part; both are not fully equivalent, so keep conservatively."},
  {"name": "refused_requests_leave_the_session_untouched", "verdict": "keep", "covered_by": null, "reason": "Refusal test: non-finite inputs must not mutate the session. Related to tests/fishing.rs::session_rejects_nonfinite_and_negative_values_without_mutating; keep as a refusal check."},
  {"name": "invalid_results_do_not_mutate_the_session", "verdict": "keep", "covered_by": null, "reason": "Refusal and persistence-of-state check. Keep."},
  {"name": "replayed_result_is_refused_once_landed", "verdict": "keep", "covered_by": null, "reason": "Replay refusal. Security check, keep."},
  {"name": "result_is_refused_while_idle_after_registration", "verdict": "keep", "covered_by": null, "reason": "Ordering refusal. Keep."},
  {"name": "only_an_owned_cast_hook_reel_sequence_lands_a_result", "verdict": "keep", "covered_by": null, "reason": "Sequence-ownership refusal and landing. Keep."},
  {"name": "foreign_and_unbound_results_are_refused", "verdict": "keep", "covered_by": null, "reason": "Foreign-actor refusal for results. tests/fishing.rs::session_rejects_a_result_for_a_foreign_actor covers similar ground; keep as a security check."},
  {"name": "echo_and_result_value_strictness", "verdict": "keep", "covered_by": null, "reason": "Strictness refusal for echo and result values. Keep."},
  {"name": "catch_authority_surface_is_bounded_at_compile_time", "verdict": "keep", "covered_by": null, "reason": "Compile-time surface bound, a canary. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Partial read: I read tests/fishing.rs lines 100-399 and tests/fishing_review.rs lines 300-599 only. Lines 600-881 (refusal, replay, foreign-result and surface tests) were not read, so their verdicts are defaults under the conservative rule. The file's value is its independent byte-level oracle (hand-built bytes from the native readers, not the module's encoder), which tests/fishing.rs does not replicate. Possible overlaps to revisit: session_binding_lifecycle vs fishing.rs re_registration_and_reset_policy, and foreign_and_unbound_results_are_refused vs fishing.rs session_rejects_a_result_for_a_foreign_actor. Consolidation there would need a full read of both files."}
