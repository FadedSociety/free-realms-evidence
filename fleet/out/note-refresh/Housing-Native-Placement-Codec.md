<!-- fleet job=note-refresh id=Housing-Native-Placement-Codec status=done turns=14 usd=0.0169 tokens(read,write,in,out)=[376227, 52672, 30, 13136] model=claude-haiku-5-5 -->
# notes/Research/Housing Native Placement Codec.md

**Verdict:** minor drift. The codec layouts, sizes and policies (sections "Scope and units", "Layouts and provenance", "Policies") still match the code. The status and integration text is stale in four places: the write hold, the "unregistered" module, the test count, and one "Only" claim about prefix framing.

**Corrections:**

1. `old:` The production write hold is active: **no `prototype/osfr-tools/src/` or `tests/` file was created
`new:` The production write hold was active when this was written (lifted by the lead integration below): **no `prototype/osfr-tools/src/` or `tests/` file was created
`why:` repo:prototype/osfr-tools/src/housing_native.rs:1 and repo:prototype/osfr-tools/tests/housing_native.rs:1 now exist; repo:notes/Autopilot/L045.md:131-132 runs `--test housing_native` (15 passed, 1 ignored).

2. `old:` ## Candidate files (to be copied by the lead after the hold)
`new:` ## Candidate files (copied by the lead into the tree at integration; see below)
`why:` repo:prototype/osfr-tools/src/housing_native.rs:1-2 and repo:prototype/osfr-tools/tests/housing_native.rs:1-3 (the copies are in place).

3. `old:` The test uses `#[path = "../housing_native.rs"] mod housing_native;` while the module is
`new:` The candidate test used `#[path = "../housing_native.rs"] mod housing_native;`; the registered test now uses `use osfr_tools::housing_native::*;` (`tests/housing_native.rs:3`), and the module is
`why:` repo:prototype/osfr-tools/tests/housing_native.rs:3 (no `#[path]` include in the tracked test).

4. `old:` unregistered; the lead owns `lib.rs` registration.
`new:` registered at `lib.rs:31` (`pub mod housing_native;`) by the lead.
`why:` repo:prototype/osfr-tools/src/lib.rs:31.

5. `old:` The registered module now passes14 ordinary tests and one explicit private gate
`new:` The registered module now passes15 ordinary tests and one explicit private gate
`why:` repo:prototype/osfr-tools/tests/housing_native.rs has 15 `#[test]` functions (lines 97, 109, 129, 143, 151, 174, 193, 205, 221, 244, 299, 319, 328, 347, 367) plus one `#[ignore]` private gate at line 483; repo:notes/Autopilot/L045.md:132 and repo:notes/Autopilot/L031.md:84 both record "housing_native 15 passed, 1 ignored". (The "14" also appears in repo:notes/Research/Module Registration 2026-10-13.md:85, which may need the same fix.)

6. `old:` Only `HousingPacket::encode_inner/decode_inner` include one127 prefix; the gateway transport wrapper remains outside the codec.
`new:` Inside `housing_native`, only `HousingPacket::encode_inner/decode_inner` include the one127 prefix; the service's `HousingReply::encode_inner` (in `housing_service.rs`) also adds it, and the gateway transport wrapper remains outside the codec.
`why:` repo:prototype/osfr-tools/src/housing_native.rs:1191-1208 (HousingPacket) and repo:prototype/osfr-tools/src/housing_service.rs:770-777 (HousingReply::encode_inner, which writes `BASE_OPCODE` then the body).

**Unsure:**
- The "Typed encode/decode methods still exclude family127" claim holds: `PlaceFixture`, `FixtureRemove`, `HouseInfo`, `PlacementDenied` and `HousingPacket::encode/decode` start at the subtype (housing_native.rs:223-245, 586-602, 620-637, 1163-1172, 1225-1257).
- Sizes check out: 127/2 = 42 (`place_round_trip_length_and_subtype` asserts 42), 127/40 = 2 + 133 + `TAIL_BYTES_EMPTY` 94 = 229 (housing_native.rs:528; test asserts that formula at tests/housing_native.rs:134), 127/41 = 10, 127/44 = 22 (20-byte body, housing_native.rs:619-631), 127/53 = 2 + 4 + message.
- The policies in lines 52-55 match housing_native.rs:16-24 and 116-144 (finite floats, `0..=4096` strings and counts, booleans only 0/1, exact consumption).
- The test name `update_empty_round_trip_is_227_bytes` (tests/housing_native.rs:130) disagrees with its 229-byte formula. It is not a claim in this note, so I did not correct it.
- Hashes (`9091118f`, `21233dc7`), the 1536-test root gate and the 44-vector private gate were not checked. The `Only` claim in item 6 is about the codec module, not the service.
