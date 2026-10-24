<!-- fleet job=note-refresh id=Pieces-008-Chess status=done turns=10 usd=0.0112 tokens(read,write,in,out)=[186064, 38247, 22, 9187] model=claude-haiku-5-5 -->
# notes/Research/Pieces/008 Chess.md

**Verdict:** badly stale in one place (the "not wired" gap), with minor drift elsewhere. The file paths, the `src/lib.rs` non-registration, the session API and the Rust test coverage list still hold.

**Corrections:**

1. `old:` Native acceptance: no client run; the module is not registered in `src/lib.rs`, and no gameplay or gateway wiring exists for chess yet.
   `new:` Native acceptance: no client run; `piece_008.rs` is not registered in `src/lib.rs` and nothing in `src/` references it. The live chess table is separate and is wired into gameplay: `src/chess.rs`, `src/chess_service.rs` (`ChessService`), and `Gameplay` (`src/gameplay.rs:197` field, `:2228` dispatch, `:3484` `handle_chess`).
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:197, :2228, :3484; repo:prototype/osfr-tools/src/chess_service.rs:245; repo:notes/Autopilot/F116.md:8 and :47 (`chess_route` gateway -> gameplay test); repo:notes/Autopilot/F140.md:157-159. `grep piece_008` over `src/` finds only the file itself, and `src/lib.rs` has no `restoration` module.

2. `old:` Board index is `y * 8 + x` with 0 = a1 (`Position.FromModelIndex`); the second player
   `new:` Board index is `y * 8 + x` with 0 = a8 and 63 = h1 (the client's shared frame; white's king starts on 60, black's on 4); the second player
   `why:` repo:notes/Build Guides/Gameplay/Chess.md:113 and :258 ("Vault note 008 puts index 0 at a1 (wrong; a8)"); repo:prototype/osfr-tools/src/restoration/piece_008.rs:27 (`sq()` converts to "the client engine's a8 = 0 frame"); repo:prototype/osfr-tools/tests/piece_008.rs:24 and :65 (`board_coordinates_match_the_clients_a8_origin`); repo:notes/WorkItems/Candidate Evidence Reconciliation.md:9. The cited `Position.FromModelIndex` is not in the client DB (no fn match).

3. `old:` 14 focused tests; `#[path]`-includes the module until the lead registers it in `src/lib.rs`
   `new:` 17 focused tests; `#[path]`-includes the module until the lead registers it in `src/lib.rs`
   `why:` repo:prototype/osfr-tools/tests/piece_008.rs has 17 `#[test]` functions (lines 49 through 459); repo:notes/WorkItems/Candidate Evidence Reconciliation.md:53 reports `piece_008: 17 passed`.

4. `old:` | `prototype/osfr-tools/tests/piece_008.rs` | 14 focused tests (the whole row is the cell to match)
   `new:` | `prototype/osfr-tools/tests/piece_008.rs` | 17 focused tests (see correction 3)
   `why:` same as correction 3. Use this only if the script needs the table row; otherwise apply correction 3.

5. `old:` #### Verification: `# GREEN after implementation and rustfmt: 14 passed, 0 failed, exit 0`
   `new:` `# GREEN after the board-frame fix: 17 passed, 0 failed, exit 0` (keep the RED/GREEN log references as historical)
   `why:` repo:notes/WorkItems/Candidate Evidence Reconciliation.md:9-10 and :53 (the frame change and the 17-pass run); repo:prototype/osfr-tools/tests/piece_008.rs (17 tests). The 14-pass run predates the a8 change.

**Checked and holding:**
- `src/restoration/piece_008.rs`, `tests/piece_008.rs`, `scripts/pieces/piece_008.py` and `tests/pieces/test_piece_008.py` all exist at the cited paths.
- The python test count of 15 is correct (`def test_` count in `tests/pieces/test_piece_008.py`).
- The `ChessSessions` store, `reconnect` (rejects unknown ids), `resign`, and `snapshot` exist (`piece_008.rs:1221`, `:1238`, `:1253`, `:1278`).
- The Rust coverage list matches the test names: fool's mate (`:345`), insufficient material (`:366`), threefold (`:376`), turn alternation and post-result lock (`:396`), resign (`:424`), reconnect (`:437`).

**Unsure:**
- "The emulator server decompilation contains **no** chess handler" (note line 118; `piece_008.rs:31`). I did not search the emulator server source, so I could not confirm or refute it.
- The `Build Ledger.md:109` row ("Soccer, chess, derby, housing, pets | Built (registered, not routed)") conflicts with the gateway-routed chess evidence above. It is outside this note, so I did not change it, but its owner should check it.
