<!-- fleet job=note-refresh id=Pieces-026-Housing-inventory-transactions status=done turns=18 usd=0.0252 tokens(read,write,in,out)=[603251, 64475, 38, 22132] model=claude-haiku-5-5 -->
# notes/Research/Pieces/026 Housing inventory transactions.md

**Verdict:** minor drift. The core claims hold at the tip: the module, its 12 Rust vectors and 10 checker tests exist, the pool bounds (8192 rows / 256 KiB), the rollback error variants, the conservation rules, the `InstanceInUse` refusal and the `AmbiguousPlacedTint` refusal all match the code. Four statements are stale or overstated, mostly about integration status and the write set of a pick-up.

**Corrections:**

1. `old:` Register `pub mod housing;` and the restoration module in `src/lib.rs`
   `new:` Register the restoration module in `src/lib.rs` (`pub mod housing;` is already registered at `src/lib.rs:30`), then replace the `#[path] = "../housing.rs"` include in
   `why:` repo:prototype/osfr-tools/src/lib.rs:30 has `pub mod housing;`. `src/lib.rs` has no `restoration` module (no match for `restoration` in that file), and the `#[path]` include is still at repo:prototype/osfr-tools/src/restoration/piece_026.rs:54-56. The comment at piece_026.rs:58-60 still says to register `housing`, which is also stale.

2. `old:` **Placement and pick-up write one file.**
   `new:` **Placement and move write one file.**
   `why:` repo:prototype/osfr-tools/src/restoration/piece_026.rs:444-470 (`place_fixture`) and 521-546 (`move_fixture`) save only the housing snapshot. `pickup_fixture` (475-517) also writes the pool when the pick-up repaints the unit (486-511), so a pick-up is not always one file. The Tints bullet in the same note already says this.

3. `old:` after a placement, a pick-up and a move; the vectors assert that.
   `new:` after a placement, an unrepainted pick-up and a move; the vectors assert that.
   `why:` repo:prototype/osfr-tools/tests/piece_026.rs:240-258 asserts the pool is unchanged after placement and an unrepainted pick-up. Repainted pick-ups change the pool: tests/piece_026.rs:456-472 asserts the pool row's tint becomes 7 after a repainted pick-up.

4. `old:` undecoded, so nothing here answers the client.
   `new:` decoded at the wire by `housing_service.rs:457-500` (127/1 selection id, 127/3 pickup, 127/5 save/move), but that service never calls this module, so nothing here answers the client. Drop "still" from the preceding line ("bodies are still").
   `why:` repo:prototype/osfr-tools/src/housing_service.rs:457-500 decodes these bodies (`wire::HousingWireMessage::PickupFixture`, `PlaceFixtureRequest`, `SaveFixture`), and `gameplay/housing.rs` binds that service to the session. `piece_026` is referenced only from tests, scripts and notes (no `src` caller outside its own file). The note's gap 3 should say so, rather than say the bodies are undecoded. I did not check whether `HousingPacketFixturePlacementDenied` is encoded; the service imports `PlacementDenied`, so that part of the list may also be stale.

**Unsure:**
- The verification table (log files under `lab/reports/piece-026-20261009T025209Z/`, the `cargo` and `python` pass counts, `conserved: true`, owned 6 / placed 2 / available 4) and the `lab/decompiled/...` citations cannot be checked. `lab/` is gitignored (repo:.gitignore:28) and does not exist at the tip. The 12 Rust and 10 Python test counts do match the source.
- The checker CLI flags (`--housing`, `--stock`, `--consensus`) match repo:scripts/pieces/piece_026.py:246-249. I did not run it.
- "The community gateway implements only `ClientHousingPacketSetEditMode` and `ClientHousingPacketEnterRequest`" refers to an external reference gateway, so I could not check it. The repo's own `housing_service.rs` handles more opcodes.
- `scripts/cargo.ps1` exists at the repo root (the note's path is correct when run from the project root), so I did not flag it.
