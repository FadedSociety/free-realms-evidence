<!-- fleet job=guide-refresh id=Gameplay-Chess status=done turns=14 usd=0.0229 tokens(read,write,in,out)=[552846, 72471, 30, 16594] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Chess.md

**Verdict:** badly stale on the server side. The client-side description (Sections "How the client implements it", "Engine", "Data and formats") still holds against the code I checked. The "What our server already does" line and the server-behaviour sequences are false: chess is built and routed for single-player rows, and the server now picks computer replies itself and never sends `MOVE_REQUEST`.

**Corrections:**

1. `old:` **What our server already does.** Nothing for chess.
   `new:` **What our server already does.** Chess is built and routed for the single-player rows. `chess.rs` holds the table rules, the movie text protocol and the server-chosen computer reply; `chess_service.rs` holds entry, family-39 routing and the coin ledger. `gameplay.rs` loads `data/content/chess.json` when present (line 932) and publishes its rows through the activity portal (line 945). Only rows 20, 66 and 67 are published; two-player rows 65, 546 and 550 are refused as unsupported. The vault note 008 model (`src/restoration/piece_008.rs`) is still not registered in the build and is not used here. `Original Activity Coverage` lists all 12 chess rows as having no captured receipt.
   `why:` repo:prototype/osfr-tools/src/chess.rs:1-9, 1282-1291; repo:prototype/osfr-tools/src/chess_service.rs:1-18, 355-389; repo:prototype/osfr-tools/src/gameplay.rs:928-945; repo:prototype/osfr-tools/data/content/chess.json:1-39; repo:prototype/osfr-tools/src/lib.rs:10-11 (no `restoration` module registered).

2. `old:` then event 30 (`MOVE_REQUEST`) with a `skill` argument.
   `new:` which runs `validate` then `make_player_move` in the engine. The shipped server does not send event 30 (`MOVE_REQUEST`): `server_move` picks the reply itself and sends it as a normal move event. The host path described next is what the client does if a server asks for it.
   `why:` repo:prototype/osfr-tools/src/chess.rs:1282-1291 (the comment says "this server never sends it"), 1300-1328 (`server_move`), 1468-1477 (human move relayed to the engine as `EVENT_MOVE_DATA`, single-player only); `EVENT_MOVE_REQUEST` is defined at chess.rs:125 and not sent anywhere.

3. `old:` [if the computer is white: `MOVE_REQUEST`, wait for `OnMoveComputerMsg`, send it as a move event]
   `new:` [if the computer is white: the server picks the reply itself and sends it as a move event; no `MOVE_REQUEST`]
   `why:` repo:prototype/osfr-tools/src/chess.rs:1256-1263 (`LOCAL_AI`, then `play_computer_turn` when the computer is white), 1287-1291.

4. `old:` send `MOVE_REQUEST` with a `skill` for each computer turn, and expect `OnMoveComputerMsg` with four engine bytes. Treat an all-zero reply as "no move found" and decide the result yourself.
   `new:` send `LOCAL_AI` with the computer's side code (0 for white, 1 for black), then choose every computer reply on the server (`server_move`) and send it as a normal move event. Do not send `MOVE_REQUEST`, and never trust `OnMoveComputerMsg`.
   `why:` repo:prototype/osfr-tools/src/chess.rs:1256-1257 (`computer_side.code()`), 1282-1299 (the client's proposed move "is never an input here").

5. `old:` A server can also skip the client engine entirely and send move events for a server-side computer player (R): the movie treats a network move the same either way.
   `new:` The server now does this: it skips the client engine for computer turns and sends move events for a server-side computer player (`chess.rs:1282-1291`). The movie treats a network move the same either way.
   `why:` repo:prototype/osfr-tools/src/chess.rs:1282-1291.

6. `old:` where 100 or more disables random captures, and tune by playing the real client.
   `new:` where 100 or more disables random captures in the client engine. The server now uses the same value (`chess.json` gives 20, 60 and 100) to widen its near-equal move window, so tune it by playing the real client.
   `why:` repo:prototype/osfr-tools/src/chess.rs:251-252 (`skill_for_row`, "Easy 20, Medium 60, Hard 100 (R)"), 242-244, 1313-1321 (window = margin + margin × (100 − skill) / 100); repo:prototype/osfr-tools/data/content/chess.json:19-37.

7. `old:` **Two-player flow.** Pair players for rows 65, 546 and 550,
   `new:` **Two-player flow (not routed yet).** `chess.rs` has a two-player table (`TableMode::TwoPlayer`), but `chess_service.rs` refuses rows 65, 546 and 550 ("Two-player chess needs another player at the table."). Pairing is still open. Pair players for rows 65, 546 and 550,
   `why:` repo:prototype/osfr-tools/src/chess_service.rs:16-18 (two-player rows "not published"), 70-72, 374-375; repo:prototype/osfr-tools/src/chess.rs:1123-1136, 1266.

**Unsure:**

- **Build Ledger conflict (not this note's claim, but it will mislead builders).** `notes/Design/Build Ledger.md:109` says "Soccer, chess, derby, housing, pets | Built (registered, not routed)". The code shows chess routed through `gameplay.rs` (lines 932, 945, 2231, 3490) and `tests/chess_route.rs` (per `notes/Autopilot/F152.md`). Worth flagging to the lead.
- **`LOCAL_AI` argument.** The server sends the computer's side code (0 white, 1 black; `chess.rs:1257`). The note's open question about what `start(int)` means on the client is still open; I did not settle it.
- **Achievement and draw closure.** I found no code that grants "Chess Master" (no chess reference in the achievement path that I searched), so item 10's instruction is still undone. I did not confirm that draws and stalemates close the session on the wire (`EndReason::Draw`/`Stalemate` exist at `chess.rs:991-996`, but I did not trace the close path).
- **Skill values.** The note says the original values are unknown. The server uses 20/60/100 as reconstructed (R) values, which the note should label as ours.
