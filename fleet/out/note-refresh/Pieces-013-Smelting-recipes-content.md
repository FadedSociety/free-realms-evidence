<!-- fleet job=note-refresh id=Pieces-013-Smelting-recipes-content status=nothing_found turns=11 usd=0.0115 tokens(read,write,in,out)=[219437, 40324, 24, 8596] model=claude-haiku-5-5 -->
# notes/Research/Pieces/013 Smelting recipes/content.md

**Verdict:** current. Every checkable claim about our code and status that I could reach still holds at the tip. No corrections.

**Checked (all hold):**
- Files exist at the cited paths: `scripts/pieces/piece_013.py`, `tests/pieces/test_piece_013.py`, `prototype/osfr-tools/src/restoration/piece_013.rs`, `prototype/osfr-tools/tests/piece_013.rs` (the `scripts/pieces`, `tests/pieces` and `restoration` listings and the WorkItems 013 entry match).
- Not registered in `lib.rs`: no `mod piece_013` anywhere in `prototype/osfr-tools/src`, and `lib.rs` has no piece modules (`repo:prototype/osfr-tools/src/lib.rs`). The "not yet registered" gate is accurate.
- Rust counts: `tests/piece_013.rs` has 5 `#[test]` functions plus 1 `#[ignore]` private check, which matches "6 owned tests (5 ordinary + 1 opt-in)" (`repo:prototype/osfr-tools/tests/piece_013.rs:39,62,82,118,135,158`).
- Python count: 16 test methods in `tests/pieces/test_piece_013.py` (2+1+2+4+2+2+3), matching "16 stdlib tests".
- Constants: ores 1-5 with break clicks, measure percents 65/70/75/80/85 and 50 ml per ore; furnace scalars (0.3, 0.7, 150, 100/130, 8/3, 2.5, 5); heat furnace (30, 0.05, 65/90/115) all match `repo:prototype/osfr-tools/src/restoration/piece_013.rs:48-130`.
- Payload surface: the 15 client-to-server names and 8 handler names match `piece_013.rs:134-162`.
- Phase rules in the note's table (stage 101 clip ranges and score floor/chain/cap, stage 102 precision and score rules, stage 103 and 104 checks) match `classify_phases`, `piece_013.rs:226-377`.
- `STAT_GAME_QUANTITY` = 8 and `GAME_WON_QUANTITY_LITERAL` = 10 (`piece_013.rs:31,33`). The script re-checks the mold-round `nQuantity = int(... / 20)` derivation and the `UpdateStats` call (`repo:scripts/pieces/piece_013.py:708-723`).
- All seven source digests in the Provenance section match `scripts/pieces/piece_013.py:40-70`.
- Preload count 278 is asserted by the real-corpus test (`repo:tests/pieces/test_piece_013.py:211`).
- Material IDs 2739/879/21785 are used in the code and fixtures (`repo:prototype/osfr-tools/tests/fixtures/save_schema/current-v2.json:253,264,352`; `repo:prototype/osfr-tools/data/content/mining.json:39`). Singing Coal has no movie-side ore entry, consistent with the note.
- Linked notes `[[Original Smelting]]` and `[[Native Smelting Controls]]` exist under `notes/Research/`.
- Nothing in `notes/Autopilot/` or `notes/Design/Build Ledger.md` has changed the piece's status.

**Unsure (not settled from the tip):**
- The 2739 serialization difference "at two bytes (offsets 80 and 130)". The test asserts offset 80 (`test_piece_013.py:226`). I found no check for offset 130 and the pinned Legacy catalogue and live inventory are in the lab, not in the repo.
- The `../lab/reports/piece-013-20261009T030014Z/` evidence bundle sizes (24,231 B and 1,921 B) and the `smelting.json` cell classification are in the lab, outside the repo. I could not check them.
- The 19-column `OnLevelData` order and the per-stage meaning of data columns come from the original AS2. The AS2 is not in the repo or refs. The script's column list (`piece_013.py:78-83`) agrees with the note but is not independent evidence.
- The `SmeltingGameClient.as:303` line citation and the `rustfmt` and `cargo` run results are not reproducible from the tip alone.
