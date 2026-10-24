<!-- fleet job=bug-hunt id=src-chess-rs-L1 status=nothing_found turns=5 usd=0.0127 tokens(read,write,in,out)=[51563, 30662, 12, 16711] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/chess.rs lines 1-800 of 2185

Reviewed `prototype/osfr-tools/src/chess.rs` lines 1-800 in full, plus 800-1000 (`apply_unchecked`, `engine_move_bytes`, `move_from_engine_bytes`, `push_pawn`, `push_step`) to judge the window's callers. I found no defect I could tie to a line in the window that a remote client can trigger.

What I checked:

- **FEN parsing (282-373):** `from_fen` is only called from `Position::start()` and the test at line 2110, so the FEN is server-controlled. Even so, the parser is bounds-safe: `file` is checked before every `squares[rank*8+file]` write, the ep square arithmetic stays within 0..63, and `f[1]`/`f[3]` are guarded by the `len() >= 4` check.
- **Attack and bounds code (435-554):** every board index is guarded by a range check before indexing. The pawn-attack row `pr` is checked against 0..8 before use.
- **Pseudo-move generation (627-750):** the double-push `tr` index is only evaluated when `r == start`, so it is always valid. Captures never target a king. Sliders and steps stop at the board edge.
- **Castling (752-800):** the king must be on e1/e8 and the rook must be present on its home square. The path is empty and the king's start, transit and destination squares are unattacked. `apply_unchecked` moves the rook correctly for all four targets (2, 6, 58, 62), and its `unreachable!()` is only reachable from a king move of two files, which only castling generates.
- **Legality and status (556-625):** `apply` checks legality before mutating. `status` orders mate, stalemate, the 100-ply rule and threefold repetition correctly.
- **Scoring validation (208-229) and `Mode::for_row` (240-248):** the bounds match their doc comments, and the nine single-player and three two-player row counts match the doc at line 232.
- **Client-input entry (937-941):** `move_from_engine_bytes` only returns a move that is in `legal_moves()` and whose engine bytes match exactly, so client bytes are never trusted.

Not reported (outside the defect rules): repeated `legal_moves` and history cloning in `move_from_engine_bytes`/`engine_move_bytes` costs O(moves²) per client move. That is a performance concern with no concrete failure at realistic game lengths. Repetition keys also include an ep square even when no ep capture is possible. That is a rules nuance that only delays a threefold draw, not a crash or a gain.
