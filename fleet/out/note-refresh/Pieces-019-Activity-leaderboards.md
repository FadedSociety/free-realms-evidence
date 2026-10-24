<!-- fleet job=note-refresh id=Pieces-019-Activity-leaderboards status=nothing_found turns=15 usd=0.0211 tokens(read,write,in,out)=[556098, 73231, 32, 12708] model=claude-haiku-5-5 -->
# notes/Research/Pieces/019 Activity leaderboards.md

**Verdict:** current. Every checkable claim about our code and status holds at the tip. No corrections.

**Checked and holding:**
- Owned module exists at `prototype/osfr-tools/src/restoration/piece_019.rs`, and it is not registered in `src/lib.rs`. Nothing in `src/` references `piece_019` except its own doc comment and `tests/piece_019.rs` (`#[path]` include at `tests/piece_019.rs:13-14`).
- `tests/piece_019.rs` has 8 `#[test]` functions (lines 98-312), matching "8 focused tests".
- `tests/pieces/test_piece_019.py` has 10 `def test_` methods (lines 90-205), matching "10 stdlib tests". `scripts/pieces/piece_019.py` exists.
- Reconstructed policy matches the code:
  - Points rank high to low and elapsed seconds low to high (`piece_019.rs:63-67`, `268-277`).
  - Ties share a competition rank, giving 1, 1, 3 (`piece_019.rs:280-283`).
  - Keep-best with a consumed session (`piece_019.rs:227-237`).
  - Value bounds `0..=9_999_999_999` (`piece_019.rs:41`, `213`).
  - Page size of ten, with `page_payload` returning the total (`piece_019.rs:39`, `297-310`).
  - Session gate: unknown, unfinished and already-committed sessions are rejected, and negative or over-ceiling values are rejected (`piece_019.rs:201-226`).
  - Snapshot JSON with a `version` field (`piece_019.rs:43`, `160-164`), and same-directory temporary-file replacement (`piece_019.rs:425-460`).
- Recovered facts with citations hold:
  - `ClientConfig.ini:40` and `ClientConfig_stage.ini:37` both carry `GameLeaderBoardUrl=http://www.freerealms.com/ingameleaderboard/leaderboardScores.action?`.
  - `MiniGameData.txt` rows 715-725 carry the LEADERBOARD_ID values 91, 93, 95, 97, 99, 109, 111, 113, 115, 117, 119, exactly as the table lists them.
  - `MiniGameGameEndScorePacket = 47` and `BaseMiniGamePacket = 39` appear in the community `PacketCodes.cs` at lines 23 and 663.
  - The ItemDisplay delimiters `##`, `::`, `^` match `score-screen/scripts/__Packages/scorescreen/display/ItemDisplay.as:12-14`.
- Locale ids match the client text table: 430659 "My Leaderboard", 430660 "Leaderboard Name", 430661 "Top Score", 430662 "Character Name", 430669 "Most Recent", 430670 "Leaderboards", 430671 "Select Leaderboard", 430734 "My Rank", 430735 "Change Leaderboard", 409152 (the "view leaderboards in game" text). TCG tie-break text is at 433371 and 433983, which matches the note's description.
- `scripts/cargo.ps1` exists, as the verification block assumes.

**Unsure:**
- The 783-row count and the 772 zero-board count for `MiniGameData.txt` were not counted. Search caps at 60 hits, and the rows that were found agree with the note.
- The pseudocode.c line numbers (1557796, 1704764, 1200331, etc.) and the `ClientLeaderBoardManager` function names were not reachable through `client_sql`. The fn table returned no LeaderBoard or HighScore rows, so those citations stay unverified.
- The `HighScoreItem` field list (`Rank`, `Name`, `Guid`, `Value`, `Id`, `Type`) and the "client never re-sorts rows" inference depend on the FFDec export in the lab, which is not in the repo. I found no `HighScoreItem` source in `ui/`.
- The note's "free of the three wire delimiters" omits two further checks the code makes: a 64-byte length cap and a control-character ban (`piece_019.rs:409-421`). The statement is incomplete, not false, so I did not propose a correction.
- The cross-link `[[../MMO Work Queue]]` has no file at `notes/Research/MMO Work Queue.md`. Obsidian resolves wiki-links by basename, and `[[MMO Work Queue]]` is used elsewhere, so I treat this as harmless.
