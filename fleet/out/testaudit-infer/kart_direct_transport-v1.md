<!-- fleet job=testaudit-infer id=kart_direct_transport-v1 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[7522, 8885, 6, 1135] model=claude-haiku-5-5 -->
# tests/kart_direct_transport.rs

{"file": "tests/kart_direct_transport.rs",
 "tests": [
  {"name": "direct_pose_roundtrips_both_encodings_and_negotiated_crc_widths", "verdict": "keep", "covered_by": null, "reason": "Only test in the tests/ directory that calls decode_kart_pose_datagram on a valid datagram. A grep of prototype/osfr-tools/tests finds no other caller, so no other file covers the direct-pose path for both encodings and CRC widths 0-4."},
  {"name": "direct_pose_rejects_forged_use_headers_lengths_and_crc", "verdict": "keep", "covered_by": null, "reason": "Hostile-input and refusal check: bit flips in header bytes, a forged item-use opcode (19), out-of-range lengths, a corrupted CRC and every truncation. No other test drives this decoder, so nothing equivalent exists elsewhere."},
  {"name": "direct_pose_requires_single_complete_zlib_stream_and_supported_flag", "verdict": "keep", "covered_by": null, "reason": "Refusal check for unsupported flag values, trailing bytes or concatenated zlib streams, and an output cap that is too small. Security-relevant and unique to this decoder."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "All three tests are the only checks of decode_kart_pose_datagram (src/soe.rs:176) in the repo's tests directory. The similar files (kart_service.rs, transport_fuzz.rs, kart_weapons.rs) test the kart service, the generic SOE transport parser and the weapon codecs; they do not call this decoder, so none supersedes these tests. transport_fuzz.rs covers zlib bombs and trailing bytes for the general transport, not this datagram format, so it is not a true equivalent. I did not read the decoder body, so the verdicts rest on the test code and the grep, not on a line-by-line comparison of assertions."}
