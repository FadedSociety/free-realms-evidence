<!-- fleet job=test-verify id=tests-kart-entry-rs-L1-f1 status=done turns=7 usd=0.0061 tokens(read,write,in,out)=[69981, 21108, 16, 5603] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/kart_entry.rs:327

**Verdict:** `confirmed` (with one correction to the claim's examples)

**Evidence:**

- The test's only check on the echo is `tests/kart_entry.rs:327-330`: `decode_inner(&frames[3]).unwrap().1 == content.client_data.as_slice()`. `content` is `synthetic_content()`, whose `client_data` already has `[77..81] = 0x2a6ac44a LE` and `[81..85] = 1 LE` (lines 98-99).
- `register_payload` sends `word_8 = 0x2a6ac44a` and `word_12 = 1` (lines 125-126). So the handler's overwrite at `src/kart_entry.rs:676-677` writes the same bytes the fixture already holds.
- Deleting `src/kart_entry.rs:676-677`: frame 3 equals the fixture, so the assertion at 327-330 passes. The regression goes uncaught by this test.
- Echoing from any source that yields the same two words also passes. That covers the "echo is a no-op" case the claim describes.
- The claim's "writes them swapped" example is wrong. Swapping gives bytes `[1,0,0,0]` at 77..81 and `[0x4a,0xc4,0x6a,0x2a]` at 81..85. Those differ from the fixture, so the assertion at 327-330 fails. The swap is caught.
- Other tests do not close the gap within this test's scope. `typed_decoders_match_the_recovered_layouts` (lines 612-619) only decodes the register and never calls the handler. `kart_entry.rs:762-763` is also decode-only. Other `client_data` uses (`kart_gateway.rs:97`, `kart_npc_entry.rs:153`) use zeros and do not touch this handler's echo. The only path that could catch it is `private_capture_reencodes_the_full_entry_bundle` (line 676). That test is `#[ignore]` with a stated reason and needs `OSFR_KART_ENTRY_CAPTURE`. Whether it would catch the deletion depends on the captured sub5 bytes 77..85 differing from the 33/9 words. I could not verify those bytes from `repo`, so I am not counting it as coverage.

**Minimal fix:** Use distinct register words in this test. Send `word_8 = 0x1111_2222` and `word_12 = 3`, then assert `frames[3]` bytes `77..81 == 0x1111_2222u32.to_le_bytes()` and `81..85 == 3u32.to_le_bytes()`, plus `frames[3][..77] == content.client_data[..77]`. Add a comment tying this to the local-player registration rule.
