<!-- fleet job=testaudit-infer id=zone_transition-v1 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[23158, 13399, 8, 1720] model=claude-haiku-5-5 -->
# tests/zone_transition.rs

{"file": "tests/zone_transition.rs",
 "tests": [
  {"name": "encode_lays_out_the_native_reader_field_order", "verdict": "keep", "covered_by": null, "reason": "Only byte-level layout check of opcode 31 in this crate; the reader order is the wire contract. Other files (housing_service.rs ~L1485, world.rs) compare encoded output only against their own fixtures, not the field offsets."},
  {"name": "decode_round_trips_the_documented_fields", "verdict": "keep", "covered_by": null, "reason": "Only decode-side check of the documented field set against the captured field map. Partially overlaps the encode test, but it is the sole decode-to-struct assertion for this codec."},
  {"name": "utf8_names_use_byte_length_and_round_trip", "verdict": "keep", "covered_by": null, "reason": "Pins that the length prefix is a byte count for non-ASCII names; no other test in the pack checks this."},
  {"name": "decode_refuses_wrong_envelope_opcode_and_length", "verdict": "keep", "covered_by": null, "reason": "Refusal check (wrong family, opcode, short/long length, empty and truncated input). Must be kept."},
  {"name": "bounded_string_reads_refuse_oversize_overrun_and_negative_lengths", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check on string length prefixes. Must be kept."},
  {"name": "non_finite_floats_are_refused_on_both_paths", "verdict": "keep", "covered_by": null, "reason": "Refusal check for NaN/inf on encode and decode. Must be kept."},
  {"name": "booleans_decode_as_nonzero_and_encode_canonically", "verdict": "keep", "covered_by": null, "reason": "Pins the non-canonical boolean decode policy and canonical re-encode; unique to this codec."},
  {"name": "short_tails_trailing_bytes_and_oversize_strings_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for short tail, trailing bytes and oversize encode input. Must be kept."},
  {"name": "defaults_do_not_invent_flags_or_geometry", "verdict": "keep", "covered_by": null, "reason": "Checks defaults produce no flags or geometry; cheap and not clearly covered elsewhere. Conservative keep."},
  {"name": "captured_op31_frame_round_trips_byte_exact", "verdict": "keep", "covered_by": null, "reason": "Ignored, env-gated byte-exact canary against the preserved capture (SHA-256 pinned). Not run by default; keep as a canary."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file tests the codec directly and no other file in the pack or the src/zone_transition.rs module (no inline tests found) asserts the same field offsets, refusals, or boolean policy. Housing and world tests only compare encoded output against their own fixtures, which is not the same assertion, so nothing was marked superseded or duplicate. Similar-file scores (housing_native, npc_interaction, kart_lobby_native) are for different codecs. Confidence is moderate because I did not read the similar files' assertions in full; the housing_service.rs encode-equality check at ~L1485 is the closest overlap and is weaker than this file's field-level checks."}
