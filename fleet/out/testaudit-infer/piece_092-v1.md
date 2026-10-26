<!-- fleet job=testaudit-infer id=piece_092-v1 status=done turns=3 usd=0.0040 tokens(read,write,in,out)=[28302, 20246, 8, 2454] model=claude-haiku-5-5 -->
# tests/piece_092.rs

{"file": "tests/piece_092.rs",
 "tests": [
  {"name": "recovered_packet_family_constants", "verdict": "keep", "covered_by": null, "reason": "Pins the recovered opcode and sub-opcode values for family 168 and stat block 38/7; no other test file asserts these constants (mount coverage elsewhere is AddPc in mount_follow.rs and fuzz inputs in app_fuzz.rs, which do not check values)."},
  {"name": "decode_mount_spawn_request", "verdict": "keep", "covered_by": null, "reason": "Only test decoding the 168/6 mount-spawn body into mount_number 1034; no other file drives MountClientRequest."},
  {"name": "decode_dismount_request_has_no_payload", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a dismount with trailing bytes must be rejected with TrailingBytes. Unique in the suite."},
  {"name": "decode_spawn_by_item_definition_request", "verdict": "keep", "covered_by": null, "reason": "Only decode of 168/8 spawn-by-item body, including truncation refusal."},
  {"name": "decode_rejects_malformed_and_absent_requests", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal test (empty, truncated, zero mount number, unknown sub-opcode). Security-relevant; no equivalent elsewhere, and app_fuzz only feeds random bytes without asserting these errors."},
  {"name": "decode_reports_unrecovered_request_bodies", "verdict": "keep", "covered_by": null, "reason": "Pins that unrecovered sub-opcodes (set automount) are reported with their payload instead of guessed; unique."},
  {"name": "captured_character_carries_the_recovered_ownership_rows", "verdict": "keep", "covered_by": null, "reason": "Asserts the 34 captured ownership rows, validate(), and the Fire Hawk/member/unknown lookups. Unique data check; the len() assertion overlaps with round_trip_owns_the_request_surface but this test also covers row content."},
  {"name": "round_trip_owns_the_request_surface", "verdict": "keep", "covered_by": null, "reason": "Stateful session test covering refusal of unowned mounts, replacement, dismount, unknown item and unrecovered requests. Its first assertion (session_rows == CAPTURED_MOUNTS.len() == 34) is a weak restatement of the test above, but the session behaviour is unique; keep."},
  {"name": "mount_speed_profiles_follow_recovered_values", "verdict": "keep", "covered_by": null, "reason": "Pins per-mount stat values (speed, glide, zero-speed branch, dismount stats); unique to this module."},
  {"name": "stat_block_bytes_match_the_recovered_field_order", "verdict": "keep", "covered_by": null, "reason": "Byte-level wire canary for the 38/7 stat update (float and int kinds); unique."},
  {"name": "server_responses_match_the_recovered_field_order", "verdict": "keep", "covered_by": null, "reason": "Byte-level wire canary for the 168/2 mount response and 168/4 dismount response; unique."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "No other test file in tests/ drives the piece_092 module (MountSession, decode_client_request, encoders). The most similar files (coin_store_siblings, piece_091, piece_056, piece_048, housing_service) share generic vocabulary (owned, refused, round-trip, byte-for-byte) but not the mount packet family. Structural note only, not a removal reason: the file compiles src/restoration/piece_092.rs via #[path] because the module is not registered in src/lib.rs; once the lead integration lands, the file should be replaced by lib-level tests, which would not remove any assertion here. Minor within-file overlap: the 34-row length check appears in two tests."}
