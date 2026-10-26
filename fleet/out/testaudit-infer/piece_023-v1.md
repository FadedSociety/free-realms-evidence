<!-- fleet job=testaudit-infer id=piece_023-v1 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[26374, 16822, 8, 2498] model=claude-haiku-5-5 -->
# tests/piece_023.rs

{"file": "tests/piece_023.rs",
 "tests": [
  {"name": "opcode_table_matches_supplied_server_enum", "verdict": "keep", "covered_by": null, "reason": "Only check of the piece_023 opcode constants against the supplied enum; the similar files test their own module's opcodes, not this one. Pins published numbers, so it is a canary for the module."},
  {"name": "permission_list_round_trips_exact_wire_bytes", "verdict": "keep", "covered_by": null, "reason": "Only exact-byte check of the piece_023 permission list layout (count, key, guid, level). No other test drives encode_permissions in this module."},
  {"name": "permission_list_preserves_multiple_entries_and_levels", "verdict": "keep", "covered_by": null, "reason": "Round-trip with two entries and the can_edit boundary; not covered elsewhere. Weak on its own, but nothing equivalent exists, so keep."},
  {"name": "permission_list_rejects_malformed_bodies", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check (truncated, trailing byte, impossible count). Must be kept."},
  {"name": "owner_may_enter_and_edit_own_house", "verdict": "keep", "covered_by": null, "reason": "Access-role policy for the piece_023 module. Service-level tests in housing_service.rs check a different code path (service state), not these pure role functions."},
  {"name": "editor_level_three_may_enter_and_edit", "verdict": "keep", "covered_by": null, "reason": "Level-3 editor grant policy; only test of this rule in the module. Keep."},
  {"name": "listed_guest_enters_but_unauthorized_edit_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a listed guest with level below 3 cannot edit. Security-relevant; keep."},
  {"name": "locked_house_denies_a_stranger_with_the_recovered_code", "verdict": "keep", "covered_by": null, "reason": "Refusal check tying the denial to the recovered error code. Keep."},
  {"name": "unlocked_house_admits_an_unlisted_visitor_as_guest", "verdict": "keep", "covered_by": null, "reason": "Policy for unlocked houses; the opposite side of the locked test. Keep."},
  {"name": "visitor_cap_denies_guests_but_never_the_owner", "verdict": "keep", "covered_by": null, "reason": "Visitor cap refusal plus owner exemption; security-relevant. Keep."},
  {"name": "housing_error_reply_is_one_little_endian_i32", "verdict": "keep", "covered_by": null, "reason": "Exact wire check of the error reply plus trailing and truncated refusals. Piece_030 only pins one constant (HOUSING_ERROR_PERMISSION_DENIED = 2) in another module, so it does not cover this layout."},
  {"name": "recovered_error_codes_keep_their_client_messages", "verdict": "keep", "covered_by": null, "reason": "Pins the client-facing message strings for each recovered code. Not covered by the housing_service or housing_session tests as far as the pack shows."},
  {"name": "client_edit_flag_follows_recovered_level_three", "verdict": "keep", "covered_by": null, "reason": "Checks that a guest list entry does not grant the client edit flag. Security-relevant and not a duplicate of the can_edit tests, since it asserts the client-level value."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "tests/piece_023.rs is a #[path] include of src/restoration/piece_023.rs, a standalone module not yet registered in src/lib.rs. No other Rust test file includes that module, so no test here has a named equivalent. The similar files (housing_service, housing_session, piece_087, piece_050, npc_interaction) exercise service- or session-level housing paths and different modules. Their names overlap in theme (guest edit refusal, cap, lock) but they drive other code. piece_030 pins HOUSING_ERROR_PERMISSION_DENIED = 2 in another module. Once the lead registers the module and drops the include, the file's tests may fold into the lib test suite, but that is a layout change, not redundancy. Nothing is marked removable. Verdicts were not checked line by line against housing_service.rs and housing_session.rs, so confidence is moderate."}
