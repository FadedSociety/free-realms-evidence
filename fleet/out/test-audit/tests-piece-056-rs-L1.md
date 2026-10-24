<!-- fleet job=test-audit id=tests-piece-056-rs-L1 status=done turns=5 usd=0.0054 tokens(read,write,in,out)=[50106, 20544, 12, 4638] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_056.rs lines 1-416 of 416

Window: `prototype/osfr-tools/tests/piece_056.rs` lines 1-416. I read the whole window, plus `src/restoration/piece_056.rs` (the constructor `captured_coin_boost` at 270-298 and `remaining_seconds` at 380-388), to check the tests against the code.

- **[high] prototype/osfr-tools/tests/piece_056.rs:395 reference_effects_keep_their_original_fields - the final assertion compares `encode_add_effect_tag(2, &effect.tag)` with `encode_add_effect_tag(2, &tag)`, where `effect.tag` was copied from `tag` and never changed, so it is a self-comparison.**
  - Why it cannot catch a regression: `remaining_seconds` takes `&self` and only reads the expiry (src 380-388), so `effect.tag` always equals `tag`. The encoder can be changed in any way (wrong field offset, dropped field, wrong opcode) and both sides change together, so the test still passes. The test name also promises that "original fields" are kept, but no field of `effect` or `tag` is checked against a fixed value.
  - Fix: assert the encoded bytes against a literal captured buffer (the 89-byte `PacketSendSelfToClient.json` row, or at least the header `[38,0,16,0]`, TagId 2 and the known fields 3600/7334/4270/495), and assert that `effect.tag` and `effect.kind`/`definition_id` are unchanged after calling `remaining_seconds`.

- **[medium] prototype/osfr-tools/tests/piece_056.rs:93 captured_retail_coin_boost_round_trips_byte_for_byte - the name promises a byte-for-byte check against the capture, but the body never compares to captured bytes.**
  - Why it cannot catch a regression: `EffectTagPayload::captured_coin_boost()` is a hand-written struct literal (src 272-298), not decoded from the captured JSON. The test only checks field values, then `decode(encode(tag)) == tag` (line 111). An encoder/decoder pair with a symmetric layout error (for example, swapping `unknown_10` and `unknown_11` on both sides, or a wrong width for `unknown_9`) still passes. Only the header bytes (lines 106-107) are pinned to fixed values.
  - Fix: add a fixed `[u8; ADD_EFFECT_TAG_LEN]` built from the captured `PacketSendSelfToClient.json` row (TagId 2, 495, 3600, 7334, 4270, 142556, 3978, composite 0, etc.), and assert `encode_add_effect_tag(2, &captured_coin_boost()) == CAPTURED_BYTES` and that decoding those bytes yields the expected tag. Rename the test if this is not done.

- **[medium] prototype/osfr-tools/tests/piece_056.rs:127 captured_profile_row_matches_the_recovered_self_payload_shape - the row body is compared with `encode_add_effect_tag(2, &row)[8..]`, which is the same encoder, so the self-payload shape is never checked against an independent source.**
  - Why it cannot catch a regression: if the shared `ClientEffectTag` layout changes, `encode_profile_rows` and `encode_add_effect_tag` change together and the comparison still holds. Only the count header (lines 125-126) and total length (line 124) are independent checks.
  - Fix: compare `&bytes[8..]` with a literal 85-byte captured ClientEffectTag, not with another encoder output.

No other findings in this window. The `#[ignore]`, early-return and `is_ok()`-only patterns do not appear in lines 1-416. The `ADD_*_LEN` checks at lines 84-89 use literal arithmetic and do pin the recovered sizes, so they are not tautologies.
