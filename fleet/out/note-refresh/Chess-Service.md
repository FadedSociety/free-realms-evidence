<!-- fleet job=note-refresh id=Chess-Service status=done turns=15 usd=0.0173 tokens(read,write,in,out)=[398034, 52549, 32, 13589] model=claude-haiku-5-5 -->
# notes/Research/Chess Service.md

**Verdict:** stale in the solo-play and integration claims. The solo computer-move path was rewritten after this note (F116, F140, F152), and the "not registered in lib.rs" gap is closed. The rules, perft, castle-encoding, draw, and terminal-event claims still hold against the tip.

**Corrections:**

1. `old:` In solo play, a legal human move is sent to the client engine as MOVE_DATA, then the service requests the computer proposal with MOVE_REQUEST and the row's skill. The service rejects an illegal engine proposal without changing the board and requests another. It validates and applies a legal proposal before emitting the move event.
   `new:` In solo play, a legal human move is sent to the client as MOVE_DATA. The server then picks the computer reply itself (`server_move`: one-ply score, a near-equal window widened by the row's skill, the table's RNG), applies it, and emits the normal move event. MOVE_REQUEST (30) is never sent, and a client `OnMoveComputerMsg` is ignored.
   `why:` repo:prototype/osfr-tools/src/chess.rs:1471-1477 (human move sent as MOVE_DATA); :1287-1300 (`play_computer_turn`, `server_move`, with the note that the server never sends event 30); :1404-1406 (`OnMoveComputerMsg` is inert). Notes/Autopilot/F116.md:10-11, 26-28 and F152.md:116-118 say the same.

2. `old:` validates every human move and client-engine proposal against legal moves
   `new:` validates every human move against legal moves; the client-engine proposal path was removed, and `OnMoveComputerMsg` is inert
   `why:` repo:prototype/osfr-tools/src/chess.rs:1282-1286 and :1404-1406; notes/Autopilot/F116.md:39 ("removes the client-proposal path").

3. `old:` The server must validate this proposal itself before relaying it.
   `new:` This server does not use the proposal: it ignores `OnMoveComputerMsg` and chooses its own reply (see Server implementation).
   `why:` repo:prototype/osfr-tools/src/chess.rs:1404-1406 (inert), :1300 (`server_move`).

4. `old:** ` is not used. The integration gap is:
   `old:` - `src/chess.rs` is not registered in shared `lib.rs` under this task's ownership boundary. The lead must review and integrate that registration.
   `new:` - `src/chess.rs` and `src/chess_service.rs` are registered in shared `lib.rs` (`pub mod chess;`, `pub mod chess_service;`). Remaining integration work is the pairing, timeout, and reward items below.
   `why:` repo:prototype/osfr-tools/src/lib.rs:10-11.

**Unsure:**

- The test result "**12 passed, 0 failed** in 1.06 seconds" (Verification) could not be re-run. `tests/chess.rs` now has 19 `#[test]` functions (lines 185-1040, none `#[ignore]`). Notes/Autopilot/F152.md records 17 passed at its tip. The count in this note is probably stale, but I did not run the suite, so I did not correct the number.
- The "Native `00f49480` ... Rust uses destination 2->8" claim matches `engine_move_bytes` (`2 => 0x08`, `6 => 0x10`, `58 => 0x01`, `62 => 0x02`, `Some([0, 0x3e, 0, flag])`) at repo:prototype/osfr-tools/src/chess.rs:905-913. The "piece_008 clears the destination after placing a capturing mover" claim also matches (piece_008.rs:910-921). I did not check the 2053 Kiwipete figure, which is a diagnostic run.
- The "settle_player delegates to MinigameRuns::finish" claim was only partly checked. The body at chess.rs:1689-1720 matches the duplicate-settlement and winner-only grant behaviour, but I did not trace the delegation to `minigame.rs:518`.
