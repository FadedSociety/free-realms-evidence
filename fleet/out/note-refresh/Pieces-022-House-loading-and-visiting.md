<!-- fleet job=note-refresh id=Pieces-022-House-loading-and-visiting status=done turns=17 usd=0.0201 tokens(read,write,in,out)=[567033, 58262, 36, 14235] model=claude-haiku-5-5 -->
# notes/Research/Pieces/022 House loading and visiting.md

**Verdict:** minor drift. The status, module, router and test claims hold at the tip. One verification-status sentence cites a compile blocker that no longer exists. Several evidence claims could not be checked because `lab/` is absent from this checkout.

**Corrections:**

- `old:` (`tests/piece_030.rs` and its missing module) are present; that is outside this item.
  `new:` (`tests/piece_030.rs`) is present. The module it includes, `src/restoration/piece_030.rs`, now exists, so that cause is gone. The full suite was not re-run at the tip; `notes/Reviews/MMO Dispatch Status.md:94` still names sibling in-flight targets as the blockers, which is outside this item.
  `why:` `prototype/osfr-tools/tests/piece_030.rs:26-28` includes `src/restoration/piece_030.rs`, and that file exists (`src/restoration/` listing). The `piece_022` module gap named in `MMO Dispatch Status.md:94` is also gone: `src/restoration/piece_022.rs` exists and `tests/piece_022.rs:25-27` includes it.

**Checked and holding (no change):**
- `src/restoration/piece_022.rs` and `tests/piece_022.rs`, `scripts/pieces/piece_022.py` and `tests/pieces/test_piece_022.py` all exist at the owned paths.
- 12 `#[test]` functions in `tests/piece_022.rs` (lines 126–332), matching "12 Rust tests".
- 10 Python test methods (8 in `RecoveredEntrancePacketTests`, 2 in `CheckerShapeTests`), matching "10 Python checks".
- The five SHA-256 vectors in the note appear verbatim in `tests/piece_022.rs:55-61`.
- `HousingEntranceRouter` exists (`piece_022.rs:379`). Monotonic ids start at 1 (`:395-397`). `Unused` is set on the first response per instance via the `greeted` set and cleared on eviction (`:489`, `:518`). `request.unknown != 0` maps to the preview flag (`:499`). One `(zone definition, owner)` pair maps to one house, and a second registration is refused (`:420-427`). Runtime instances are not restored (`:530-531`).
- Not wired: `lib.rs` has no `piece_022` registration, and `gateway.rs` has no housing branch. So the "lead integration" and "wire integration" gates are still open, as the note says.
- Client facts: `FUN_00aa83c0` calls `FUN_00aa4990(0x13)` with the guid at +0x10, the int at +0x18 and the bool at +0x1c. `FUN_00ab07a0` calls `FUN_00aa4990(0x2d)` and sets `HeadSize` (`param_1[4]`) to 10 (client_sql `fn` rows).
- `refs/Sanctuary/src/Sanctuary.Game/ZoneManager.cs:160` keys zones by `(zoneDefinitionId, ownerId)`, and `:154`/`:239` require a non-null owner. `EvictIfEmpty` is at `:208-225`.
- The commented test vector in `refs/Sanctuary/src/Sanctuary.Gateway/Handlers/BaseHousingPacket/ClientHousingPacketEnterRequestHandler.cs:36-48` quotes the captured BeginZoning values.
- `encounter::zone_begin_packet` exists at `prototype/osfr-tools/src/encounter.rs:3111`.

**Unsure:**
- `lab/` does not exist in this checkout, so the capture hashes, the `lab/reports/piece-022-20261009T025254Z/` directory, the "26,657 of 26,662" frame count, the 68 terrain entries and the `Houses.json` row check could not be verified here.
- `tests/pieces/test_piece_022.py` skips when the capture is missing (`skipUnless(CAPTURE.exists())`, line 44). A "Ran 10 tests ... OK" result without the lab would therefore not prove the byte checks; the note does not mention this.
- `housing_service.rs:504` already answers `EnterRequest` and `:1383` builds `ZoneData`, so the note's "Wire integration" gate concerns only the new `piece_022` router, not housing as a whole. The note is not wrong, but it does not say that a separate housing service exists.
