<!-- fleet job=testaudit-infer id=housing_rating-v1 status=done turns=6 usd=0.0039 tokens(read,write,in,out)=[71674, 17218, 14, 2127] model=claude-haiku-5-5 -->
# tests/housing_rating.rs

{"file": "tests/housing_rating.rs",
 "tests": [
  {"name": "the_native_34_byte_request_decodes_field_by_field", "verdict": "keep", "covered_by": null, "reason": "Only test that pins the 174/16 candidate-info request layout (34 bytes, field order) against the client writer; no similar rating-request codec test exists in the repo."},
  {"name": "malformed_requests_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal/hostile-input check (truncated, trailing, wrong family/subtype, oversize, bad UTF-8, negative length). Security-type test; no equivalent elsewhere."},
  {"name": "an_empty_reply_is_the_header_the_correlation_and_a_zero_count", "verdict": "keep", "covered_by": null, "reason": "Sole check of the empty 174/17 reply encoding and round trip; not covered by another file."},
  {"name": "a_one_entry_reply_follows_the_client_reader_order", "verdict": "keep", "covered_by": null, "reason": "Sole byte-level check of the one-record reply field order against the client record reader."},
  {"name": "malformed_replies_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for reply decoding (oversize count, truncated record, trailing byte, wrong subtype); no equivalent elsewhere."},
  {"name": "an_oversize_string_is_not_encoded", "verdict": "keep", "covered_by": null, "reason": "Bound check on encoding; the similar housing_native.rs oversize tests cover a different packet family, not this encoder."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Every test is a unique codec or refusal check for the 174/16 and 174/17 rating candidate-info packets, and no other test file in the repo covers them, so all six are kept. The similar files (npc_interaction, coin_store_siblings, zone_transition, station_cash, piece_046) test other packet families and do not overlap. Caveat: the crate module osfr_tools::housing_rating is not present under prototype/osfr-tools/src in this snapshot (only src/housing_native.rs exists). The briefs T562 and T563 name src/housing_rating.rs as an owner to be extended, so this test may not compile or run against the current tree. I could not verify the assertions against the implementation. Confidence is moderate for that reason."}
