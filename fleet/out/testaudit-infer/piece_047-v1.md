<!-- fleet job=testaudit-infer id=piece_047-v1 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[8418, 12374, 6, 1601] model=claude-haiku-5-5 -->
# tests/piece_047.rs

{"file": "tests/piece_047.rs",
 "tests": [
  {"name": "stat_table_is_contiguous_and_matches_the_recovered_enum", "verdict": "keep", "covered_by": null, "reason": "Only test of the 69-id character stat table and its contiguity; no other test file includes src/restoration/piece_047.rs (searched repo: only tests/pieces/test_piece_047.py, a Python checker, and this file reference it)."},
  {"name": "parachute_and_fire_hawk_vectors_decode_to_the_recovered_values", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the decoded 18092 and 78397 stat vectors; no Rust duplicate elsewhere. The Python test checks the source file, not this decode path."},
  {"name": "glide_vectors_keep_the_recovered_min_default_max_ordering", "verdict": "keep", "covered_by": null, "reason": "Invariant check over the gear vectors (min<=default<=max, flag values); not repeated in another test file."},
  {"name": "int_kind_stats_must_decode_to_integral_values", "verdict": "keep", "covered_by": null, "reason": "Refusal check: non-integral int stat and unknown stat id must be rejected. Security/refusal test with no equivalent elsewhere."},
  {"name": "fire_hawk_item_binds_to_the_recovered_mount_row", "verdict": "keep", "covered_by": null, "reason": "Only check of the Fire Hawk item-to-mount binding and the unrecovered-slot assertion."},
  {"name": "recovered_classes_name_their_owning_profile_or_shared_scope", "verdict": "keep", "covered_by": null, "reason": "Class ownership rows for piece_047 only. Similar files (piece_033, piece_040) test other profiles' class ownership in their own modules, not this table."},
  {"name": "equip_gate_applies_the_recovered_profile_scope_rank_and_member_flags", "verdict": "keep", "covered_by": null, "reason": "Refusal/gate policy check (WrongProfile, UnknownClass, RankTooLow, MembersOnly). Refusal tests are kept; no equivalent gate test for piece_047 exists elsewhere."},
  {"name": "native_container_capacity_stays_above_the_recovered_id_space", "verdict": "keep", "covered_by": null, "reason": "Canary tying the native container capacity (71) to the 69-id space; the only check of this constant."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file is the sole Rust test of src/restoration/piece_047.rs and is included via #[path], so no other tests/*.rs drive the same module. Similar files (piece_032, piece_033, piece_040, piece_042, piece_092) exercise different modules and different job/packet tables; none supersedes these assertions. Nothing is removable. Minor note: the Python checker tests/pieces/test_piece_047.py overlaps in intent (it checks the same constants in source) but is not a Rust test and was out of scope. Work-item notes list 8 vectors, matching this file."}
