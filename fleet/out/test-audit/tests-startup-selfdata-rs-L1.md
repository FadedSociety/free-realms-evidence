<!-- fleet job=test-audit id=tests-startup-selfdata-rs-L1 status=done turns=7 usd=0.0078 tokens(read,write,in,out)=[99057, 25669, 16, 7122] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/startup_selfdata.rs lines 1-616 of 616

Window: `prototype/osfr-tools/tests/startup_selfdata.rs` lines 1-616. Confirmed against `prototype/osfr-tools/src/startup_selfdata.rs` (`parse_self_with_quest_bindings` ~L1024, `build_self` L1161, `write_inventory_item` L665).

- **[medium] prototype/osfr-tools/tests/startup_selfdata.rs:603 captured_opcode12_tutorial_keys_are_not_the_npx_mode_flag - the name says the tutorial keys are proven not to be the NPX mode flag, but the body only checks that `tutorial_keys` survive a parse→build→parse round trip.**
  - Why it cannot catch a regression: the only other output is a `println!` that prints the count and says "no IsInNPXTutorial field". A change that makes `tutorial_keys` carry the NPX flag, or that drops the flag from the wire, still passes as long as build and parse agree. The test never compares against a value from the capture or checks the field's semantics.
  - Fix: assert against a known captured value (for example, an expected key list or count from the reference that the NPX flag cannot produce), or rename the test to something like `captured_opcode12_tutorial_keys_round_trip` and drop the overclaim.

- **[medium] prototype/osfr-tools/tests/startup_selfdata.rs:340 synthetic_typed_sections_round_trip - `assert_eq!(body(&packet).len(), packet.len() - 13)` cannot fail.**
  - Why: `body()` (L209-218) returns `inner[6..]`, where `inner = packet[7..]`. Its length is therefore always `packet.len() - 13` by construction. The check restates the helper's own slicing arithmetic and does not test the code under test.
  - Fix: delete it, or replace it with a pinned length for the known sample, such as the expected total packet length computed from the wire spec, not from `packet.len()`.

- **[medium] prototype/osfr-tools/tests/startup_selfdata.rs:453 synthetic_collection_reward_and_keyed_rows_round_trip (also 335, 491, 530, 558) - these tests check only `parse(build(x)) == x`, so a layout error that is symmetric in build and parse passes.**
  - Why: for example, swapping the order of `common_fields` and `display_fields` in both `write_reward_bundle` and its parser, or changing a keyed-row key width on both sides, would still round-trip. The only byte-level check in the file is the `#[ignore]`d oracle at L310, which needs a private capture. Nothing in the default gate pins the wire offsets of these sections; the `*_wire_len` helpers at L224-308 are re-derived by hand in the test and do not check field order.
  - Fix: add a non-ignored golden-byte test for at least one section, for example a packed `CollectionRecord` with distinctive fields, asserting exact bytes at known offsets (such as `packet[13 + k..]` for the key u32 and the first display byte). A field-order swap then fails.

- **[low] prototype/osfr-tools/tests/startup_selfdata.rs:368 synthetic_inventory_zero_one_many_items_uses_server_item_type - the name claims a check on the item type, but the body checks only item round-trip equality and total packet lengths.**
  - Why: the item type is never inspected beyond equality after decode, so a change that makes the item wire type differ from the server type but still round-trips would pass. The length checks at L387-388 (30 and 46 bytes) match `write_inventory_item`, so they are correct but do not test "server item type".
  - Fix: rename to `..._zero_one_many_items_round_trip`, or add an assertion on a field that depends on the item type (for example, that the rental flag byte at the expected offset is 0 or 1).
