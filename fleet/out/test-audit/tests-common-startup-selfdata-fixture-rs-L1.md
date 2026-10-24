<!-- fleet job=test-audit id=tests-common-startup-selfdata-fixture-rs-L1 status=nothing_found turns=6 usd=0.0041 tokens(read,write,in,out)=[33339, 14217, 14, 3892] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/startup_selfdata_fixture.rs lines 1-108 of 108

Reviewed `prototype/osfr-tools/tests/common/startup_selfdata_fixture.rs` lines 1-108. It is a fixture (`self_data_packet`), not a test, so the test-level categories mostly don't apply. I checked its returned offsets against the encoder and found no defect.

- **Offset arithmetic (lines 22-34, 105-106):** `body_position_offset` matches `build_self` field order in `src/startup_selfdata.rs:1161-1230`: u64 + u64 + u32 (20), head/hair strings with their u32 prefixes, two u32 colours (8), skin/paint/customization strings, and five u32 customization ids (20). The position block starts at that body offset, and rotation sits +16 later because position is four u32s (x, y, z, w). The fixed header of 13 bytes is correct: `TUNNEL_PREFIX` is 3 bytes (`src/startup_selfdata.rs:10`), then u32 length, u16 opcode 12, and u32 body length, giving 3+4+2+4 = 13.
- **Consumers:** `tests/gateway.rs:277-280` reads the bytes at the manifest `position_offset` and compares them to the position, so a layout change would fail there. The offsets are not self-referential: they are hand-derived from the layout, not read back from `build_self`.
- **Fixture data:** the `SelfData` literal is a plain input (zeroed/empty collections, `post_effect_tail`), and `empty_quest_state()` is a normal constructor. No expected value is derived from the function under test.

The fixture has no `#[ignore]`, no early return, and no assertions of its own. Nothing in this window meets the five categories.
