<!-- fleet job=note-refresh id=Pieces-032-Brawler-progression status=nothing_found turns=20 usd=0.0292 tokens(read,write,in,out)=[940792, 80719, 42, 19474] model=claude-haiku-5-5 -->
# notes/Research/Pieces/032 Brawler progression.md

**Verdict:** current. Every checkable claim about our code and status that I could reach matches the tip. No corrections.

**Corrections:** none.

**Checked and holding (evidence):**
- Files exist: `prototype/osfr-tools/src/restoration/piece_032.rs`, `tests/piece_032.rs` (`#[path]` include at line 29), `scripts/pieces/piece_032.py`, `tests/pieces/test_piece_032.py`.
- Test counts: `tests/piece_032.rs` has 15 `#[test]` functions plus one `#[ignore]` private gate (lines 103–372). `test_piece_032.py` has 7 `def test_` methods, five of them fail-closed (lines 148, 161, 174, 201, 210). Module Registration 2026-10-13 agrees (15 / 0 / 1).
- Not registered: no `piece_032` or `restoration` module declaration in `src/lib.rs`, so the "lead integration" gate is still open.
- Module behaviour matches the note: `RankComparator` codes 6 and 4 (`piece_032.rs:224–240`); development-row exclusion, rank-0 unrestricted rows and rank-21 violations (`:688–687`, `:680–686`); mixed-type, inverted-window and out-of-range refusals (`:329`, `:361`, `:333`); `unlock_curve` (`:748`); creation kit with `class_wieldable` (`:714`); `experience_gaps` (`:793`).
- Test-asserted numbers match the note: 907 live rows, 447 rank-1, 11 rank-20, 17 development rows, 6 unrestricted, 24 gates, 8 combat gates, 6 windows, and the six bounds table (`tests/piece_032.rs:461–519`). Development-only ranks are 2, 10, 18 (`:467`).
- Requirements: 24 `CheckRankLastProfileByType` rows; groups 3={3,4} and 4={5,6}; sets map to groups 1–6 (`client:Resources/RequirementGroups.txt`, `RequirementSets.txt`). Rows 21–24 are type 12, so Blacksmith 12 is correct.
- Identity: `ItemFilterOptions.txt` row 11 is `11^2873^0^43^0^0^` (client).
- Locale: 420938 "Bruising Strikes", 420939 "Savvy", 420941 "Resilience"; 420940 is absent (locale lookup). The note's gap statement is right. Locale 3 is "You receive #count([*experience*]) and #count([*coins*])".
- Ceiling: `EquipmentSlotDefinitions.txt` row 15 has `MIN_PROFILE_RANK` 20 (MoonRune); row 7 is `Weapon` (client).
- Classes: `ItemClasses.txt` in refs carries name id 2873 on classes 5, 25, 71 (and 42, 52 per locale). Class 50 and 69 are borrowed (17372 / 17373). Classes 183 and 999 have profile name id 0. Locale names for 2925, 23266, 2870, 2235 and 2247 match the note.
- Wire side: `src/profiles.rs:229` and `:340` use `(1 + xp / 100).min(20)`. Packets 38/14 and 38/18 are at `:331`, `:345`, `:350`. The comment at `:343` says the rank notification precedes the full update. The client's decompiled strings include `JobLevelsGained` and `RankPercent` (`FUN_00c8f2b0`).
- Checker: `scripts/pieces/piece_032.py` computes sha256 (`:94`, `:449`) and exits 2 on a refused check (`:483`).
- No Autopilot report mentions piece_032 after the note was written.

**Unsure:**
- `lab/reports/piece-032-20261009T032529Z/` (the RED/GREEN logs and `brawler-progression.json`) and `lab/references/...` are not reachable from my roots, so I could not check the logs or the exact row counts (58,795 catalogue rows, 907 live weapons). The cargo and unittest result lines are unverified beyond the test-file counts above.
- `Resources/ItemClasses.txt` is not in the `client` root's Resources listing. It exists only in the community copies under `refs`. The note cites it as "the supplied client", which I could not confirm from the client tree.
- The wiki claims (revision 48172, weapon and trait levels, and the trait quest names) are community material and cannot be checked from the tip.
- The Brawler trait text ids 420962–420965 were not checked.
