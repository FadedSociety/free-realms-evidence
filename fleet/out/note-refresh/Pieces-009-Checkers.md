<!-- fleet job=note-refresh id=Pieces-009-Checkers status=done turns=15 usd=0.0184 tokens(read,write,in,out)=[461062, 62890, 32, 11788] model=claude-haiku-5-5 -->
# notes/Research/Pieces/009 Checkers.md

**Verdict:** minor drift. The status, file paths, test counts and the recovered constants all match the tip. Only the validation order is misstated.

**Corrections:**

- `old:` piece ownership, compulsory capture, chain continuation, destination)
  `new:` piece ownership, chain continuation, compulsory capture, destination)
  `why:` `prototype/osfr-tools/src/restoration/piece_009.rs:617-633`. `validate` checks the chain-continuation case (`stopped_early`, `CaptureContinuationRequired`) before the compulsory-capture case (`CompulsoryCapture`). The note lists them the other way round.

**Verified as current (no change needed):**

- `prototype/osfr-tools/src/restoration/piece_009.rs` exists, is std-only, and has `Board`, `Action`/`Jump`, `CheckersEvent`, `CheckersSession`, `encode_move_payload` and `decode_move_payload`. `CheckersSession` derives `Clone` and `PartialEq`.
- `prototype/osfr-tools/tests/piece_009.rs` has 15 `#[test]` functions and includes the module by `#[path]`, so no `lib.rs` edit (lines 12-13).
- The module is not registered anywhere in `src/`, which matches the "Register `pub mod piece_009;`" integration step.
- `tests/pieces/test_piece_009.py` has 10 tests (7 in `RealSourceTests`, 3 in `DriftTests`).
- `scripts/pieces/piece_009.py` has 38 `MOVIE_MARKERS` entries in the `game` tuple, and the `EXPECTED_GAME_IDS` are `21, 68, 69, 70, 541, 542`.
- Constants match: `GAME_ID = 21`, `STORAGE_NAME = "checkers_data"`, `END_GAME_DELAY = 3000`, `VERSION = "v1.12 May21"`, tutorial `"11"`.
- Event ids match `piece_009.rs:57-78`.
- Locale 900 is `Checkers`, 901 is the description text, and 917 is `Elite Pink First Aid Pants` (the ICON_ID quirk is real).
- Geometry, compulsory capture, chain lock, promotion on rows 0/7, and destination-only `MOVE_KING` match `piece_009.rs:313-349`, `388-418`, `442-445` and `639-692`.
- "No draw rule" is consistent with `settle()` (`piece_009.rs:694-703`), which only ends the game on no legal action.

**Unsure:**

- Line 62 says `ProxyReset` puts "the non-red side on spots 0..=11 and the red side on 20..=31". The next lines say red occupies 0..=11, and `piece_009.rs:275-296` (`Board::initial`) puts red on 0..=11. The note contradicts itself here. I could not check the ActionScript because the movie scripts are under `lab/`, which is outside my roots. The author should decide which side the movie's `ProxyReset` actually uses.
- The evidence directory `lab/reports/piece-009-20261009T024655Z/` and the logged results (`15 passed`, `10 tests OK`, `games=6 markers=38 scripts=55`) are outside my roots, so I did not check them. The counts in the source files agree with them.
- `GameServer.IsJump` returning `EMPTY_SPOT = -1` and the `SpotToNetwork`/`SpotFromNetwork` mirror (`31 - spot`) are movie-level claims. The Rust port returns `None` for a one-row step (`piece_009.rs:425-439`) and has no mirror function, so I could not verify either.
- `MIN_PLAYERS = MAX_PLAYERS = 0` and the six TYPE 7 rows were not checked against the shipped `MiniGameData.txt`, which is not in the client root.
