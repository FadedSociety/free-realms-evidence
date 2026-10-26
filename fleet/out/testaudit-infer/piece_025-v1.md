<!-- fleet job=testaudit-infer id=piece_025-v1 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[9801, 13554, 6, 1846] model=claude-haiku-5-5 -->
# tests/piece_025.rs

{"file": "tests/piece_025.rs",
 "tests": [
  {"name": "place_fixture_request_matches_recovered_writer_order", "verdict": "keep", "covered_by": null, "reason": "Pins the exact byte layout of PlaceFixtureRequest against the recovered client writer FUN_00abcb90 and round-trips it. No other test in the pack drives this #[path]-included restoration::piece_025 codec; housing_service.rs and housing.rs exercise the crate's own housing module, not this encoder."},
  {"name": "set_edit_mode_is_one_byte_after_the_header", "verdict": "keep", "covered_by": null, "reason": "Only byte-level check of SetEditMode (opcode 6) in this codec; the crate-level edit-mode tests in housing_service.rs assert service behaviour, not these wire bytes."},
  {"name": "enter_request_matches_the_community_reader", "verdict": "keep", "covered_by": null, "reason": "Byte-exact EnterRequest (opcode 19) layout cross-checked against the community reader; unique to this codec module. Not a duplicate of the housing_service enter-sequence tests, which assert zoning/reply bytes for a different path."},
  {"name": "preview_request_carries_one_definition_id", "verdict": "keep", "covered_by": null, "reason": "Only check of the PreviewByItemDefinitionIdRequest (opcode 20) body layout in this codec; distinct from the crate-level preview tests."},
  {"name": "pickup_fixture_carries_the_fixture_guid", "verdict": "keep", "covered_by": null, "reason": "Only byte-level check of PickupFixture (opcode 3) u64 body in this codec."},
  {"name": "save_fixture_keeps_the_undecoded_tail", "verdict": "keep", "covered_by": null, "reason": "Pins the opaque nested tail and trailing u32 of SaveFixture (opcode 5) so the undecoded block is preserved on round trip; the tail-preservation property is not asserted anywhere else in the pack."},
  {"name": "decode_rejects_wrong_base_opcode_truncation_and_unknown_opcodes", "verdict": "keep", "covered_by": null, "reason": "Refusal/hostile-input check (wrong base opcode, truncation, unknown opcode, trailing bytes). Security-style refusal test; no equally strong equivalent found for this codec."},
  {"name": "schema_table_matches_the_encoder", "verdict": "keep", "covered_by": null, "reason": "Canary tying the schema table (BASE_OPCODE=127, six entries, sizes, opcodes) to the encoder; guards drift used by the piece_030 gate work. Not duplicated elsewhere in the pack."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file is a standalone #[path] include of src/restoration/piece_025.rs, so its tests exercise a codec that no other test file in the pack imports. The similar files (housing_service.rs, housing.rs, piece_030.rs) use the crate's housing module and share only the BASE_OPCODE=127 header concept and some opcode names; they test service behaviour and gate evidence rather than these encoder bytes. Overlap is conceptual only, so every test is kept per the conservative rule. Possible future consolidation: once the lead registers the module (as the file's own header requests) and drops the include, these vectors could be checked against housing_service's decoder, but that is not a redundancy today."}
