<!-- fleet job=note-refresh id=Pieces-025-Furniture-placement-client-wire status=done turns=13 usd=0.0147 tokens(read,write,in,out)=[364855, 49356, 28, 9853] model=claude-haiku-5-5 -->
# notes/Research/Pieces/025 Furniture placement client wire.md

**Verdict:** minor drift. The codec, opcode table, test counts, the `#[path]` include and the five-entry `UNRECOVERED_OPCODES` gate all still match the tip. Two statements are stale: the integration gate says routing into `housing.rs` is still to do, but the decoded opcodes are already routed through `housing_service.rs`, and one verification remark says `piece_027.rs` does not exist.

**Corrections:**

1. Next gate 2 (line 133, the start of the sentence that runs into line 134).
   - `old:` "2. Wire the decoded opcodes 1/3/5/6 into `housing.rs` (item 006) so a placement request is answered by the reconstructed state machine; inventory proposal/commit stays with item 026."
   - `new:` "2. Decoded opcodes 1/3/5/6/19/20 are already routed through `housing_service.rs`: `wire::decode` at line 485 and dispatch in `handle` at lines 1255-1297. Opcode 5 (`SaveFixture`) still returns `UnresolvedRequest`, and the placement reply and inventory proposal/commit stay with item 026."
   - `why:` repo:prototype/osfr-tools/src/housing_service.rs:58-60 (`#[path = "restoration/piece_025.rs"] mod wire;`), :485-510 (`wire::decode` then mapping to `Request` variants), :1255-1297 (dispatch; `SaveFixture` → `ServiceError::UnresolvedRequest`; `PlaceFixtureRequest` → `fixture_asset`). The codec itself is not in `housing.rs`; the note's "into `housing.rs`" is therefore also a citation drift.

2. Verification paragraph (line 126).
   - `old:` "`tests/piece_027.rs` includes `src/restoration/piece_027.rs`, which does not exist yet; that is not"
   - `new:` "`tests/piece_027.rs` included `src/restoration/piece_027.rs`, which did not exist when this was run (it is present at tip); that was not"
   - `why:` repo:prototype/osfr-tools/src/restoration/piece_027.rs exists (listed in `prototype/osfr-tools/src/restoration/`); repo:prototype/osfr-tools/tests/piece_027.rs:32 still has the `#[path]` include.

**Checked and still true (no change):**
- `prototype/osfr-tools/src/restoration/piece_025.rs` and `tests/piece_025.rs` exist. `tests/piece_025.rs:23-25` has the `#[path]` include, and `src/lib.rs` has no restoration module registration, so gate 1 is still open.
- `UNRECOVERED_OPCODES` lists 28, 39, 40, 41, 53 (`piece_025.rs:428-434`).
- Eight `#[test]` functions in `tests/piece_025.rs` (lines 38-154), matching "8 passed".
- Five Python tests in `tests/pieces/test_piece_025.py` (lines 37, 64, 72, 89, 110), matching "Ran 5 tests".
- The codec's opcode, body and reject rules (`piece_025.rs:130-282`) match the table: 1 = u32×3+u8, 3 = u64, 5 = u64+4×u32+4×u32+u32+tail+u32, 6 = u8, 19 = u64+u32+u8, 20 = u32.
- Client writers: `FUN_00aa4990` stamps 0x7f and the inner opcode, `FUN_00abcb90`, `FUN_00abcb30`, `FUN_00abca80`, `FUN_00abcd90`, `FUN_00abf620` and `FUN_00ac0510` match the body layouts (client_sql fn table).
- FreeRealms-Legacy has readers for exactly two housing requests (`SetEditMode`, `EnterRequest`). `EnterRequest.TryDeserialize` reads u64, int, bool and requires the body to be consumed (`refs:FreeRealms-Legacy/src/Sanctuary.Packet/BaseHousingPacket/ClientHousingPacketEnterRequest.cs:21-40`).

**Unsure:**
- Lines 49-50: "All six send wrappers are only reached when the client's connected flag at `*(*(process+0x10)+0x280)` is non-zero." I did not trace the callers, so I could not confirm it.
- Lines 45-48 (constructor/send pairings such as `FUN_00ac4200` → `FUN_00ac0400`): I checked only the writer side, not every call site.
