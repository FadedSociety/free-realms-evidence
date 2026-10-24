<!-- fleet job=note-refresh id=Pieces-024-Furniture-catalogue status=nothing_found turns=14 usd=0.0154 tokens(read,write,in,out)=[423493, 55125, 30, 8572] model=claude-haiku-5-5 -->
# notes/Research/Pieces/024 Furniture catalogue.md

**Verdict:** current. Every code-checkable claim in `024 Furniture catalogue.md` matches the tip. No corrections.

**Checked and holding:**
- Owned files exist: `src/restoration/piece_024.rs`, `tests/piece_024.rs`, `scripts/pieces/piece_024.py`, `tests/pieces/test_piece_024.py` (also listed in `notes/WorkItems/024.md`).
- Integration gate: `tests/piece_024.rs:18-20` still includes the module by `#[path = "../src/restoration/piece_024.rs"]`. `src/lib.rs` does not register it, and no other source file references it. The "register or move it and drop the include" gate is still open.
- Rust counts: `tests/piece_024.rs` has 6 `#[test]` functions plus 1 `#[ignore]` private gate, matching "6 passed, 1 ignored". The private gate asserts 1167 / [9046, 16872, 16874, 18112, 18136] / [9046, 15978, 18167] / 31 / [17750, 27943] / 1136, matching the note's table.
- Python counts: `tests/pieces/test_piece_024.py` has 7 hermetic tests plus 1 real-source test (`Piece024RealSourceTests`), giving 8, matching the note.
- Housing threshold: `scripts/pieces/piece_024.py:55` sets `HOUSING_CATEGORY_MIN_ROWS = 20` and `:153` derives categories from it, so "derived by membership, not hard-coded" holds.
- Duplicate tolerance: `src/inventory.rs:400-405` accepts byte-identical duplicate definitions and rejects conflicting ones, as the note says.
- Icon-prefix and furniture-selector rules: `src/restoration/piece_024.rs:98-116` matches the note's `hsg_` / `icon_item_<stem>` description.
- Regression counts: `item_categories.rs` has 4 tests with 1 ignored (3 passed, 1 ignored), and `inventory.rs` has 2 ignored. Both match the sweep row.
- Artefact names: `furniture-catalogue.json`, `findings.json` and the `--output` default match the script.
- Status against `notes/MMO Work Queue.md:36` ("Candidate reported; lead review/integration/native pending") is consistent.

**Unsure (could not verify; the data lives in `lab/`, which is not in the repo):**
- The stock-catalogue counts (1,167 furniture rows, 58,795 items, 34 housing non-`hsg_` rows), the 1,647 reconstructed definitions, the 33 records / 31 ids, the 31 wiki title matches, the 68 icon gaps, and the artefact sha256 values.
- The Python RED/GREEN and rustfmt results in the verification table are historical run logs; I did not re-run them.
- The claim that the pool `_complete.agr` models are absent from the packs. The note's own evidence is the pack catalogue, which I did not have.
