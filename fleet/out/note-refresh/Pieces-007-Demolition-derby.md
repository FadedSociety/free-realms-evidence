<!-- fleet job=note-refresh id=Pieces-007-Demolition-derby status=done turns=15 usd=0.0162 tokens(read,write,in,out)=[364946, 42925, 32, 14268] model=claude-haiku-5-5 -->
# notes/Research/Pieces/007 Demolition derby.md

**Verdict:** badly stale. The wire facts (17 captured subtypes, the 8/9/17 absence, the 12 Python tests, the checker) still hold. The Rust side has been rebuilt under other names: `DerbySession`, `FinishOutcome` and `RewardOutcome` no longer exist, the test count is wrong, and the "no derby implementation" claim is false.

**Corrections:**

1. `old:` vehicle-hit/config/announcer layouts, `DerbySession`
   `new:` vehicle-hit/config/announcer layouts, `DerbyService` (phase machine; `finish_match` at line 1602)
   `why:` `prototype/osfr-tools/src/derby.rs:1602-1630` (`DerbyService::finish_match`). A grep for `DerbySession` in `prototype/osfr-tools/src` finds nothing. The phase enum is `DerbyPhase` at `derby.rs:739`.

2. `old:` `DerbySession` (local, not historical): lobby/running/finished/abandoned, at most eight unique
   `new:` `DerbyService` in `src/derby.rs` (local, not historical): `DerbyPhase` Lobby/Running/Results/CloseEnabled/Closed/Aborted, at most eight unique
   `why:` `prototype/osfr-tools/src/derby.rs:739-749` (`DerbyPhase`); `derby.rs:23` (`MAX_DERBY_DRIVERS = 8`) and `derby.rs:814` (the 2..=8 bound).

3. `old:` The module moves no currency or items; the caller grants only on `Granted`.
   `new:` `derby.rs` moves no currency or items. `gameplay/derby_session.rs:198-217` (`pay_derby_completion`) pays the flat completion reward once per match through `DerbyGateway::take_completion` and `rewards::apply_grant`. The once-only guard is the gateway ledger; the `FinishOutcome`/`RewardOutcome` types are not in `src/`.
   `why:` `prototype/osfr-tools/src/gameplay/derby_session.rs:190-217`; grep finds no `FinishOutcome`, `RewardOutcome` or `claim_reward` in any `derby*.rs`.

4. `old:` | `prototype/osfr-tools/tests/derby.rs` | 11 tests; includes the module by `#[path]` until the lead registers it |
   `new:` | `prototype/osfr-tools/tests/derby.rs` | 7 tests; uses the registered `osfr_tools::derby` module |
   `why:` `tests/derby.rs` has 7 `#[test]` attributes (lines 185, 309, 350, 388, 450, 521, 558), its first line is `use osfr_tools::derby::{`, and `src/lib.rs:16` has `pub mod derby;`. No `#[path]` remains.

5. `old:` Subtypes 8/9/17 never occur and stay opaque.
   `new:` Subtypes 8/9/17 never occur in the capture. They have typed decoders (`DestroyVehicle`, `KickVehicle`, `ItemExpired`); only unknown subtypes stay opaque (`Unknown`).
   `why:` `prototype/osfr-tools/src/derby.rs:549-550` and `:607`; the opaque fallback is at `derby.rs:619-623`.

6. `old:` and the preserved server has no derby implementation.
   `new:` and the server now has a derby module (`src/derby.rs`, `src/derby_gateway.rs`) that does not write `DerbyResults` rows (no `DerbyResults` writer in `src/derby*.rs`).
   `why:` `prototype/osfr-tools/src/derby.rs`, `src/derby_gateway.rs`, and `src/gameplay/derby_session.rs` all exist; `DerbyService::finish_match` (`derby.rs:1602-1630`) only orders drivers and broadcasts `GameState`.

**Unsure:**

- Scoring. The note says scoring values "stay an explicit gap". The code does track scores and sorts results by score and damage (`derby.rs:1611-1620`; a test asserts `score == 2` after a contact at `tests/derby.rs:378`). Whether those values are policy or recovered was not settled. The note's "labelled tally, not a health model" also sits uneasily with `VehicleState.health` (`derby.rs:262`).
- Recovered fact 3 says the first bout uses a "packed two-byte name length". The decoder reads an `i32` name length for every subtype-10 body (`derby.rs:553`), so the two-byte form is not modelled. I could not tell whether the wire claim is wrong or only unimplemented.
- The "11 passed" and "24 + 11 passed" rows in the commands table are historical run results. I did not rerun them, so I could not check them against the 7-test file.
- The "Status" line ("once-only finish and reward implemented and tested") is only partly true at the new locations: the reward once-guard is in the gateway, and I found no test of it in `tests/derby.rs`.
- Piece 007 checker and test counts (12 Python tests, 12 checks) match the files: `tests/pieces/test_piece_007.py` has 12 `def test_`, and `scripts/pieces/piece_007.py` has the expected subtype tables.
