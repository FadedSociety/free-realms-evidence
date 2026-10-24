<!-- fleet job=test-audit id=tests-housing-service-rs-L1 status=done turns=5 usd=0.0080 tokens(read,write,in,out)=[73157, 35552, 12, 5599] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/housing_service.rs lines 1-1200 of 1790

Window reviewed: `prototype/osfr-tools/tests/housing_service.rs` lines 1-1200. Findings below; I checked each against `src/housing_service.rs` and `tests/housing_service.rs`. No fixture is missing, and I found no `#[ignore]` or early-return skips in the window.

- **[medium] prototype/osfr-tools/tests/housing_service.rs:897 fixture_item_list_contains_only_configured_owned_items - the name promises an exclusion check, but the stock holds only one owned item, and that item is configured, so nothing is excluded.**
  - Why it cannot catch a regression: `fixture_item_list` (src/housing_service.rs:1840-1843) skips instances whose `row_for_item_definition` fails. If that `continue` were deleted, or the filter were inverted to include unknown items, this test would still see one item with `fixture_guid == INSTANCE` and pass.
  - Fix: add a second `owned(…, 4_242, 1)` instance to the stock, then assert `list.items.len() == 1` and that no item has `item_definition_id`/`fixture_guid` for the unconfigured instance.

- **[medium] prototype/osfr-tools/tests/housing_service.rs:823 recovered_entry_packets_encode_and_preview_without_selector_stays_unrecovered - the name claims the selector stays unrecovered, but the body never checks that.**
  - Why it cannot catch a regression: the body only checks entry opcodes, a preview reply, and `decode_request` of a save frame. Nothing asserts that a placement without a selector is refused. A change that bound the selector on preview would still pass. The refusal is only checked in a separate test (line 512).
  - Fix: either rename the test to match what it checks, or add `service.handle(OWNER, &place_frame(SELECTION, …))` with no prior `offer` and assert `ServiceError::UnresolvedSelection { selection_id: SELECTION }` with `service.lot(HOUSE).unwrap().count == 0`.

- **[medium] prototype/osfr-tools/tests/housing_service.rs:1172 the_housing_snapshot_seam_is_path_free - "path-free" is only checked as the absence of a top-level `"path"` key.**
  - Why it cannot catch a regression: a path stored under any other key, or nested inside a lot or fixture, would still pass, because `encoded.get("path")` only looks at the top level of the serialized state.
  - Fix: walk the whole `serde_json::Value` and assert that no string value contains a path separator or a `.json`/`.bin` suffix, or assert that the set of top-level keys equals exactly `{"schema_version","lots"}`.

- **[medium] prototype/osfr-tools/tests/housing_service.rs:934 a_denied_request_encodes_the_recovered_53_body - the expected denial text is taken from the code under test.**
  - Why it cannot catch a regression: line 949 compares the decoded message with `error.denial_message()`, which is the same function that produced it. Changing `denial_message()` to a different wrong string (for example, "" is excluded only by line 950) would still pass, so the wording is never pinned.
  - Fix: assert the literal text, e.g. `assert_eq!(message.message, "Only the lot owner can edit this lot.")` for the `NotPermitted` case, and keep the opcode check.

- **[low] prototype/osfr-tools/tests/housing_service.rs:563 a_native_placement_consumes_the_real_inventory_instance - an exact inner-packet length of 231 is pinned in a test about inventory consumption.**
  - Why it cannot catch a regression: any unrelated codec change to the fixture-update record (padding, a new trailing field) breaks this test without touching consumption. The test's own comment shows the number is a codec detail.
  - Fix: drop the exact `231` and keep the decoded-field asserts (lines 564-569), or move the length check to the `housing_native` codec tests.

- **[low] prototype/osfr-tools/tests/housing_service.rs:1189-1190 enabled_bundled_lots_have_scene_bounds_and_source_tags - exact content counts (31 lots, 22 enabled) are pinned.**
  - Why it cannot catch a regression: adding or enabling one bundled lot breaks this test even when every lot's scene and bounds are valid, which is the property the name claims.
  - Fix: keep the per-lot loop, and replace the exact counts with `assert!(enabled_count > 0)` plus a check that the enabled count equals the number of lots whose `enabled` flag is true in the bundled file, or move the count pins to a content-snapshot test.
