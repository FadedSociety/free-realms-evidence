<!-- fleet job=note-refresh id=Pieces-010-Trading-card-game status=done turns=23 usd=0.0243 tokens(read,write,in,out)=[898409, 57891, 48, 16133] model=claude-haiku-5-5 -->
# notes/Research/Pieces/010 Trading card game.md

**Verdict:** minor drift. Nearly every checkable claim holds at the tip (module paths, test counts, opcodes and constructor evidence, client strings, row ids, the "not registered in `lib.rs`" gap, the "no server TCG service" gap). The one real overstatement is the reward rule, which the note describes as "once-only" when the code does not enforce that.

**Corrections:**

1. `old:` Deck catalogue shape + `TcgMatch` rule slice (first to 12 points, replay protection, once-only reward, reconnect snapshot)
   `new:` Deck catalogue shape + `TcgMatch` rule slice (first to 12 points, replay protection, winner-only reward lookup via `reward_card` whose once-only payout is left to the caller, reconnect snapshot)
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_010.rs:579-586`. `reward_card(&self, ...)` keeps no state, so it returns the named card on every call for a finished match. Nothing in the module records a payout. The test named `the_winner_receives_the_reward_named_by_that_deck_row_only_once` (`repo:prototype/osfr-tools/tests/piece_010.rs:265-298`) only checks that a rejected post-game event does not add to `applied()`. It does not test repeated reward calls.

2. `old:` grants exactly the winner's named card and nothing while unfinished or when the row names no card
   `new:` returns exactly the winner's named card (`reward_card`) and `None` while unfinished or when the row names no card; the caller must grant it once
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_010.rs:579-586` (returns `Option<&str>`, grants nothing). The note's own integration item 4 (line 204-206) already says the slice "returns the reward card name and grants nothing", so this sentence should match it.

**Checked and holding (no change needed):**
- `tests/pieces/test_piece_010.py` has 20 `def test_` functions (lines 79-308), matching "20 stdlib tests".
- `tests/piece_010.rs` has 18 `#[test]` functions, matching "18 behavioral tests", and includes the module by `#[path]`.
- No `piece_010` module declaration exists in `src/lib.rs` or anywhere in `src`, so "not registered in `lib.rs`" is still true.
- Packet codes: `PacketCodes.cs` lines 23, 663-678 match all listed values (39, 38, 40, 18, 47, 21, 16, 180).
- Native constructors: `FUN_009a9de0` calls `FUN_008a4420(0x28, …)` with two stored fields; `FUN_009a9ec0` calls it with `0x26` and one field (client_sql fn table).
- Client strings: four `TradingCardGameHandler:On*LoadComplete` stages, `TradingCardMain`, `.\UI\TradingCard\TCCW_Main.swf`, and the Startup/OnDisconnect session-identity log strings are all present.
- `ZPSumExpression::getCardList`, `ZPEachExpression::getCardList`, `BaseCardData`, `FlipCardData` and `SendCardData` exist as client strings and functions.
- `MiniGameData.txt`: TYPE 3 rows 7, 11, 107, 108 exist. Rows 700-703 have `NAME_ID=-1`; row 499 has difficulty `-1`; row 9997 is unnamed.
- `MiniGameTypeData.txt` marks TYPE 3 and TYPE 16 with IS_FLASH=1.
- Locale: 434012 = "Common"; 433462 = "Robgoblin Sorceress".
- Asset lists: `SimpleCardAssets.txt` has `destroyerNinjaOn2s`/`destroyerRobgoblinOn2s`/`destroyerYetiOn2s`; `thumb_anakin_skywalker.dds` appears in `TradingCardAssets.txt:160`.
- `TcgMatch` behaviour matches the note: start gate, positive and over-target checks, replay and out-of-order checks, first side to 12 wins, `MatchFinished` for later events, and reconnect snapshot tests.
- No file under `src/` routes packets 38 or 40 or uses `TcgMatch` as a service. The only other `TcgMatch` reference is the `OutcomeSource` enum variant in `piece_043.rs`, so "server-side TCG service not implemented" still holds.

**Unsure:**
- `TradingCardAssets.txt` (3,864 B) and `SimpleCardAssets.txt` (6,129 B) byte sizes, and the bundle size of 100,879 B: the tools do not expose file sizes, so these were not checked.
- The full TYPE 16 count (124) and the "783/4/124" audit figure: only a subset of rows was enumerated, so the total was not re-counted.
- Locale range counts (433394-433613 = 112 entries; 433836-433887 = 14 entries): spot checks only. 433836 reads "Virtual Reward", which does not obviously fit the "Clone Wars set" description, but I did not verify the set boundaries.
- The `0x1c` scaleform handle for the TCCW movie, and the `0x0` `TradingCardGameHandler` claims: not verified.
- Wiki card-list counts (357 entries, 101 `1L*` codes, 60/60/60/52 rarity split): refs were not searched.
