<!-- fleet job=note-refresh id=Pieces-067-Quest-prerequisite-engine status=done turns=14 usd=0.0179 tokens(read,write,in,out)=[440818, 58178, 30, 12440] model=claude-haiku-5-5 -->
# notes/Research/Pieces/067 Quest prerequisite engine.md

**Verdict:** minor drift. The engine, the validation rules, the gate order, the file paths and the Rust test count (11) all match the tip. Two stated counts/commands are off.

**Corrections:**

1. `old:` `$py = '..\lab\tools\universal-modder-env\Scripts\python.exe'`
   `new:` `$py = '..\lab\tools\wiki-env\Scripts\python.exe'`
   `why:` `repo:scripts/pieces/piece_067.py:30` gives the checker's usage line with `lab/tools/wiki-env/Scripts/python.exe`, and `repo:tests/pieces/test_piece_067.py:5` names the same `wiki-env` interpreter for the unittest command. The note's "Commands (actual)" block names a different env.

2. `old:` `21 tests over the real corpus plus rejection fixtures`
   `new:` `20 tests over the real corpus plus rejection fixtures`
   `why:` `repo:tests/pieces/test_piece_067.py` has 20 `def test_` methods (lines 51–271: 11 in `ClassificationTests`, 9 in `RealCorpusTests`). No other test definitions appear in that file.

3. `old:` `Results: Python 21 tests pass;`
   `new:` `Results: Python 20 tests pass;`
   `why:` same as correction 2. Only the run log could show a different number, and no such log is in the repo.

**Checked and holding:**
- `repo:prototype/osfr-tools/src/restoration/piece_067.rs` exists. `PrerequisiteTable::new(rows, external)`, `availability`, `accept` and `UnmetRequirement` match the integration seam (lines 212–335).
- Gate order in `accept` and `blocks` (lines 290–401): already completed/active, then branch exclusions, then prerequisite, then requirements in row order. Availability reports every block.
- Definition validation (lines 221–278, 201–208): self-prerequisite, self-exclusion, duplicate exclusion, unknown prerequisite/exclusion, zero level, zero days and empty event name are all rejected. Longer cycles are not scanned.
- Cooldown uses `DAY_MS = 86_400_000` (line 48). Award-free: no reward fields are read.
- `prototype/osfr-tools/tests/piece_067.rs` exists with 11 `#[test]`s and uses the `#[path = "../src/restoration/piece_067.rs"]` include (line 30). The module is not registered in `src/` (no `mod restoration` / `piece_067` in `lib.rs`), so "module not yet registered" holds.
- `scripts/pieces/piece_067.py` exists and reads the Rust constants (lines 358–385).
- `QuestProgress.accepted` exists in `repo:prototype/osfr-tools/src/quests.rs:52`, so the integration seam names the right field.
- `notes/Research/original-quest-coverage.json` lines 1376 and 1402 hold the truncated `Quest:Your` / `Quest:Learn` values.
- `content/opening.json` (17 stages) and `content/quest-inventory.json` (25 records) match `scripts/audit-quest-coverage.py:498-500`.

**Unsure:**
- The gate-order parenthetical "(membership, job level, ride, cooldown, event window)" reads as a fixed order. The code (`repo:prototype/osfr-tools/src/restoration/piece_067.rs:361`) iterates the row's `requirements` in row order, so the fixed list is only the order in the opening rows. I left it alone because the note's wording "in source order" is correct.
- The `lab/` paths (`lab/references/freerealms-wiki/quest-pages.json`, `lab/reports/piece-067-20261009T050538Z/`) and the corpus counts (52 pages, 36 rows, 29 prerequisite rows, 6 unresolved) are outside this repo, so I could not verify them. The checker pins only the corpus SHA-256 (`scripts/pieces/piece_067.py:68`), not the row counts.
- The "Rust 11 tests pass" and "checker exits 0" run results cannot be re-run from here.
