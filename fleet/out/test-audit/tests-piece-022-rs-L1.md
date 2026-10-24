<!-- fleet job=test-audit id=tests-piece-022-rs-L1 status=done turns=6 usd=0.0058 tokens(read,write,in,out)=[63884, 20540, 14, 5123] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_022.rs lines 1-343 of 343

Window: `prototype/osfr-tools/tests/piece_022.rs` lines 1-343. Read the full window plus `src/restoration/piece_022.rs` lines 1-200 and 256-305, and searched the module for fixture handling. Most tests check real encoder/decoder/router behaviour against inline captured bytes, so they can fail. Two findings:

- **[high] tests/piece_022.rs:333 fixture_updates_bind_to_the_entered_house_guid - the name claims a fixture update is bound to the entered house, but the body never calls any code under test; it only slices a hex constant and compares it with two test-local constants.**
  - Why it cannot catch a regression: `src/restoration/piece_022.rs` has no fixture-update encoder or decoder. The only fixture-related item is `HOUSING_FIXTURE_UPDATE: u16 = 40` (line 59), and the search for "fixture" in that file shows nothing that binds a fixture to a house guid. Any change to the router, the enter path, or the fixture code leaves this test green. Its assertions depend only on `VEC_FIXTURE_UPDATE_PREFIX`, `FIXTURE_GUID` and `HOUSE_GUID`, which are constants in the test file.
  - Fix: either rename the test to say it checks the captured fixture-prefix layout (for example `captured_fixture_update_prefix_layout`), or add a real check. The real check would decode the 127/40 message with a fixture-update decoder, or at least compare `FIXTURE_GUID` and the house guid against the record the router stores after `enter`. Until then, the header comment's claim that the house guid is "the same instance identity the enter request named" is not tested by this function.

- **[low] tests/piece_022.rs:314 malformed_requests_and_duplicate_houses_are_rejected - `decode_request_grant(&hex("7f001701")).unwrap_err();` discards the error variant, so it accepts any error.**
  - Why it cannot catch a regression: the input has a valid base opcode and a wrong sub-opcode (0x0117 instead of 23). The source returns `UnexpectedOpcode` (src lines 295-296), but a change that returned `ShortMessage` or `TrailingData` for this input would still pass. The four `decode_enter_request` checks above it do compare exact variants, so this one is the inconsistent case.
  - Fix: `assert_eq!(decode_request_grant(&hex("7f001701")), Err(EntranceError::UnexpectedOpcode));`

No `#[ignore]`, no early-return fixture skips, and no names that overclaim other than the one above. The other tests' assertions match their names: the leave/evict test checks the new instance id and that the house data survives, and the restart test checks routing and the zone-data bytes after reload.
