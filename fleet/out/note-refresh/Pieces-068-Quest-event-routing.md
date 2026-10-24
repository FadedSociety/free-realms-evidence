<!-- fleet job=note-refresh id=Pieces-068-Quest-event-routing status=done turns=14 usd=0.0163 tokens(read,write,in,out)=[362193, 50255, 30, 12833] model=claude-haiku-5-5 -->
# notes/Research/Pieces/068 Quest event routing.md

**Verdict:** minor drift. The core status and structure claims hold at the tip. Two claims are stale: the `piece_097` compile failure and the Python test count.

**Verified as current (no change needed):**
- Router module, Rust test file, checker script and checker test file all exist at the paths in the note's table (`prototype/osfr-tools/src/restoration/piece_068.rs`, `prototype/osfr-tools/tests/piece_068.rs`, `scripts/pieces/piece_068.py`, `tests/pieces/test_piece_068.py`).
- Not registered and not wired: `piece_068` appears in no `src/` file except its own module, `QuestEventRouter` has no caller in `src/`, and `src/lib.rs` has no `restoration` declaration.
- Route table: 36 rows in the embedded JSON (`piece_068.rs:44-79`). By kind: talk 10, interact 8, visit 1, kill 4, gather 6, craft 6, game 1. This matches the note.
- Rust tests: 9 active `#[test]` plus 1 `#[ignore]` cross-check (`tests/piece_068.rs:52-519`). This matches "9 tests pass + 1 ignored".
- Behaviour: `new()` refuses kill `definition_id <= 0` and zero identifiers (`piece_068.rs:332-347`). Radius is checked against `0.1..=1000` (`:357`). Gather and craft credit `min(quantity, required)` (`:412`, `:419`). Malformed events are refused in `validate()` (`:177-219`). `load_json` ignores extra keys and rejects a foreign schema version (`:369-376`).
- Petty Yeti negative test drives 1294, 3156, 920001, 920002, 920100 and an unknown id, and asserts none credits 14096 (`tests/piece_068.rs:260-268`).

**Corrections:**

1. `old:` A full `cargo test` currently fails to compile another worker's `src/restoration/piece_097.rs` (two `E0308` type mismatches at lines 463/474); that file is outside this item's paths.
   `new:` A later full build no longer fails on `piece_097.rs`. `cargo test --no-run` exited 0 across 372 test executables; the earlier failure was resolved after this item.
   `why:` `repo:notes/Autopilot/T445.md:105-108` records `cargo test --no-run` exit 0 with 372 test executables. At the tip, the push sites at `repo:prototype/osfr-tools/src/restoration/piece_097.rs:462-474` pair `(i32, String)` values, matching the field types at `:405` and `:408`. This note is dated 2026-10-09, so the claim is point-in-time history that has since moved. I did not compile the crate, so treat the replacement as well supported but not re-run.

2. `old:` * Python: 18 tests pass.
   `new:` * Python: 17 test methods in `tests/pieces/test_piece_068.py` (3 in `ModuleApiTests`, 7 in `SyntheticDerivationTests`, 7 in `RealCorpusTests`).
   `why:` `repo:tests/pieces/test_piece_068.py:38-393` defines 17 `def test_` methods. The count of 18 does not match the file at the tip.

**Unsure:**
- The 25 quest records / 42 objectives, the 6 checker warnings, and the 36 routes from `scripts/pieces/piece_068.py --check` depend on the private `../lab` tree. I could not run the checker or inspect `content/quest-inventory.json`.
- Focused run counts (`--lib` 24, `opening` 7, `opening_journal` 6, `piece_066` 11, `piece_069` 9) are run results. I did not re-run them.
- Sanctuary row 3156 "Hooligan Wolf, model 3284" at the pinned rev: `Sanctuary/src/Resources/Npcs.json` contains "Hooligan Wolf" entries, but I did not confirm row 3156, model 3284, or the pinned revision. Locale `5100200` = "Hooligan Wolf" was confirmed.
- The integration suggestion that `gameplay.rs` has hard-coded per-id checks (`recipe_id == 2001`, `resource_id == 1003`) is only partly supported. Such ids appear in `src/gameplay/t013_objective_events.rs` and `s6_characterization.rs`, not as literal `==` checks in `gameplay.rs`. I left it unchanged.
