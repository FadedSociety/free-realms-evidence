<!-- fleet job=test-audit id=tests-kart-lobby-native-rs-L1 status=done turns=7 usd=0.0058 tokens(read,write,in,out)=[72357, 19635, 16, 5243] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_lobby_native.rs lines 1-483 of 483

Window: `prototype/osfr-tools/tests/kart_lobby_native.rs` lines 1-483. Most of the file is sound. Sizes, offsets and counts (113/121/128, 40/48/55, the 2386/2378 split, the 1000-count `available: 16`, the 0x2000_0000 text length) were checked by hand against the layout and the decoder in `src/kart_lobby_native.rs`. The `#[ignore]` on the private-capture test has a reason, and the test panics on a missing env var rather than returning early. Two findings:

- **[medium] tests/kart_lobby_native.rs:474-478 private_capture_roundtrips_the_full_2378_byte_body - the assertion labelled "settings row name id" asserts a semantic the module says is not recovered.**
  - Why it cannot catch a regression: the check is `settings[0].fields[2] == 3031`. The source (`src/kart_lobby_native.rs:138-139`) says the settings fields "stay positional" and only the wire order is recovered. The name id is said to sit in the fourth word, not the third. A change that reorders or re-labels the fields, or a decoder that swaps word 2 and word 3, would still pass as long as the value stays at index 2 and the test keeps the label. The label is also wrong against the source: the test claims a field meaning the module does not claim.
  - Fix: rename the message to "settings row word 2 (unrecovered, positional)", or assert the field the source actually calls the name id (fourth word) and make the test name and message match that. Either way, the message should not claim a semantic the source disclaims.

- **[low] tests/kart_lobby_native.rs:340-363 tunnel_framing_roundtrips_and_refuses_bad_headers - the name says it refuses bad headers, but the flag byte is never checked.**
  - Why it cannot catch a regression: the test covers only the outer opcode (byte 0-1) and the inner length (bytes 3-6). `decode_tunnel` (`src/kart_lobby_native.rs:487-504`) never reads or validates the `u8 flag` at byte 2. A change that rejects or mis-handles a bad flag, or that starts reading it as part of the length, would not be caught here, and the test name suggests the header is covered.
  - Fix: either add a case that mutates `tunnel[2]` and asserts the intended result (an error variant if the flag is meant to be validated, or a decode that is unchanged if it is only carried), or rename the test to say it covers the outer opcode and inner length only.

Lower-value note (not counted as a finding): line 474 repeats `assert_eq!(body_decoded.settings.len(), 17)` already asserted at line 410. This is harmless.
