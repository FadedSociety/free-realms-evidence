<!-- fleet job=testaudit-infer id=mystery_chest_codec-v1 status=done turns=3 usd=0.0038 tokens(read,write,in,out)=[30684, 18647, 8, 2412] model=claude-haiku-5-5 -->
# tests/mystery_chest_codec.rs

{"file": "tests/mystery_chest_codec.rs",
 "tests": [
  {"name": "check_and_use_requests_parse_with_their_native_subtypes", "verdict": "keep", "covered_by": null, "reason": "Only direct unit check that 42/16 parses to Check and 42/15 to Use with the native subtype values; tests/app_fuzz.rs exercises the Use/Check pairing at gameplay level but not the codec mapping."},
  {"name": "subtype14_is_not_a_check_request", "verdict": "keep", "covered_by": null, "reason": "Regression pin for a reproduced defect (legacy subtype 14 producing no dialog); a refusal-style check with no equivalent elsewhere."},
  {"name": "unrelated_packets_are_ignored", "verdict": "keep", "covered_by": null, "reason": "Refusal/ignore check for unrelated roots 50/1, 38/30, unknown subtype 17 and truncated owned roots; no equivalent in other files."},
  {"name": "every_truncation_of_an_owned_request_is_an_error", "verdict": "keep", "covered_by": null, "reason": "Hostile-input truncation sweep on the owned request; the error-kind assertion is only made for len<2 and then a second loop repeats the same error check for 2..len, so the test is partly redundant internally but not covered by another file."},
  {"name": "trailing_bytes_on_an_owned_request_are_an_error", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal (trailing bytes must fail with InvalidData); security-style check, keep."},
  {"name": "non_positive_instance_ids_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check for hostile instance ids (0, -1, i32::MIN) across both subtypes; keep."},
  {"name": "check_reply_matches_the_client_reader_bytes", "verdict": "keep", "covered_by": null, "reason": "Byte-exact pin of the 0x26/0x1e check reply against the client reader layout; no other test in the suite asserts these bytes."},
  {"name": "check_reply_carries_the_requested_instance_id", "verdict": "keep", "covered_by": null, "reason": "Endianness check of the instance id field at offset 4; partly overlapping with the byte-exact test above but tests negative and multi-byte values the other does not."},
  {"name": "item_reward_matches_the_independent_byte_layout", "verdict": "keep", "covered_by": null, "reason": "Full 114-byte hand-laid reward bundle comparison; the only whole-packet independent layout check for 50/1 kind 16."},
  {"name": "item_reward_field_offsets_match_the_note_and_native_reader", "verdict": "keep", "covered_by": null, "reason": "Field-by-field offset assertions with distinct values; overlaps the whole-packet test above but localises offset regressions; borderline, could be folded into the byte-layout test."},
  {"name": "item_reward_rejects_non_positive_ids_but_keeps_unknown_fields", "verdict": "keep", "covered_by": null, "reason": "Refusal check for non-positive item/definition ids plus -1 sentinel preservation; keep."},
  {"name": "item_reward_preserves_maximal_and_minimal_values", "verdict": "keep", "covered_by": null, "reason": "Boundary-value canary (u64::MAX guid, i32 extremes) compared against the hand layout; no equivalent boundary test elsewhere."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "The file is the only focused codec test for src/mystery_chest.rs (parse_request, check_reply, item_reward); tests/app_fuzz.rs and src/mystery_chest_loot.rs exercise the flow but not the byte layouts. tests/kart_rewards.rs only cites mystery_chest.rs in a comment and does not call item_reward. Two possible internal redundancies (item_reward_field_offsets vs item_reward_matches_the_independent_byte_layout; the two check_reply tests) are noted but kept per the conservative rule. I did not read the full src/mystery_chest.rs or the gameplay-level tests, so confidence is moderate."}
