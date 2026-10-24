<!-- fleet job=note-refresh id=Pieces-039-Gathering-job-progression status=nothing_found turns=17 usd=0.0186 tokens(read,write,in,out)=[531662, 54026, 36, 13029] model=claude-haiku-5-5 -->
# notes/Research/Pieces/039 Gathering job progression.md

**Verdict:** current. Every checkable claim about our code and status holds at the tip. The only open points are about the original client data, which I could only partly settle, and are listed under Unsure.

**Corrections:** none.

What I confirmed:
- Module, tests and checker paths exist as cited: `prototype/osfr-tools/src/restoration/piece_039.rs`, `prototype/osfr-tools/tests/piece_039.rs`, `scripts/pieces/piece_039.py`, `tests/pieces/test_piece_039.py`.
- "GREEN: 16 passed": `tests/piece_039.rs` has 16 `#[test]` functions (lines 65 to 322). `src/restoration/piece_039.rs` has none.
- "GREEN: 11 passed": `tests/pieces/test_piece_039.py` has 11 `def test_` methods (lines 109 to 292).
- The module is not registered yet, as the note's Next gate 1 says. No `piece_039` appears in `src/restoration/mod.rs` or `src/lib.rs`; the test file says the same (`tests/piece_039.rs:28-32`).
- The API the note names exists: `GrantLedger::authorize` (`piece_039.rs:482`), `GrantKey::mining`/`harvesting` (`:419`, `:429`), `GrantDecision::Duplicate`, `rank_for_xp` (`:209`), `RankProgress::percent` (`:199`, floored share, 100 at cap), `NON_MEMBER_RANK_CAP` (`:51`, documentation only).
- The ladder, caps and reward sets match `Resources/FactoryRanks.txt` (60 rows; the 58/63/60 values, the rank-5 members-only switch, and the 4274/4381 starts all agree). `FactoryPlots.txt` matches too: plots 3/5/7 bind 58/63/60, the ranch has misfortunes at 0, and plots 4/6/8 and instance 57 have no rank rows.
- `Resources/Requirements.txt` rows 17..20 are `CheckRankLastProfileByType`, operator 6, profile type 9, at ranks 5/9/13/17.
- Locale 1663..1666 read Tin 4, Iron 8, Silver 12, Gold 16, and 435461 is `Briarwood Farm`.
- `Profile_DS` (`ScriptsBase.lua:2850-2858`) has Rank 4, StarsAvailable 5, StarsEarned 11, RankPercent 12. `FactoryHandler:OnFactoryRankUp` exists (`ScriptsBase.lua:13131`).
- The "reconstructed 100-xp curve" in Next gate 2 is real: `src/profiles.rs:227-229` and `:332`.
- The Miner `Type8Run::instance_id` exists (`src/mining.rs:180-181`).

**Unsure:**
1. **Miner vein gate text is incomplete.** The note says the locale rows 1663..1666 are the original gate text and the wiki's 1/5/10/15/20 table conflicts with them. The locale also has a second set of "Sorry, you need to be at least a level N Miner" strings: 71451 Tin 5, 71453 Iron 10, 71455 Silver 15, 71457 Gold 20 (the wiki's values), plus 71459..71465 with 2/3/4/5. The note mentions neither set. It should say the client ships both sets, so the "locale rows win" call is not one-sided. I did not change the note because it is not false.
2. **`NON_MEMBER_RANK_CAP` in a sibling piece.** The note's claim that the cap is "documentation only" holds for `piece_039.rs`. But `src/restoration/piece_041.rs:64` defines its own `NON_MEMBER_RANK_CAP: u8 = 4`, used live at `:239` and tested at `tests/piece_041.rs:153`. Anyone reading the note alongside 041 may be misled.
3. **Evidence paths outside the repo.** `lab/reports/piece-039-20261009T040246Z/`, `lab/decompiled/...` (FactoryRanks/Requirements loader, `ClientPcData.cs`) and `scripts/`-side output are not in the repo or refs roots I could search. The `ClientPcData.cs` copy I found is at `refs:OpenSourceFreeRealms/ofrserver/Gateway/Login/ClientPcData.cs` and has `JobLevelTotalXP` (line 1363). I could not confirm the `lab/...` citations, the sha256 values, or the "piece 039 evidence ok" checker output.
4. **Native facts not re-verified.** The native constructor length 0x12 for `ClientUpdatePacketUpdateProfileRank`, the `FUN_00402ff0` loader, and the wiki-sourced Farmer and Stars statements were not checked against code.
