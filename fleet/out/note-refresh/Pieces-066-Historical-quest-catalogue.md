<!-- fleet job=note-refresh id=Pieces-066-Historical-quest-catalogue status=done turns=17 usd=0.0201 tokens(read,write,in,out)=[570333, 60915, 36, 13554] model=claude-haiku-5-5 -->
# notes/Research/Pieces/066 Historical quest catalogue.md

**Verdict:** Mostly current. Minor drift in one remaining-gate line. The catalogue defect, the lead-registration gate, the counts and the file paths all still hold at the tip.

**Corrections:**

- `old:` `4. Crate-wide \`cargo check --tests\` currently fails on other workers' in-flight targets (\`piece_044\`, \`piece_062\`, \`piece_065\`, \`piece_068\`, \`piece_092\`
   reference modules that do not exist yet).`
  `new:` `4. Crate-wide \`cargo check --tests\` failed on 2026-10-09 for other workers' in-flight targets (\`piece_044\`, \`piece_062\`, \`piece_065\`, \`piece_068\`, \`piece_092\`, which \`#[path]\`-include \`src/restoration/piece_0NN.rs\`; those files are missing in the 2026-10-09 snapshot). At the tip all five source files exist, so this gate is stale and needs a fresh \`cargo check --tests\` before it is cited.`
  `why:` repo:prototype/osfr-tools/src/restoration/ lists piece_044.rs, piece_062.rs, piece_065.rs, piece_068.rs and piece_092.rs; repo:prototype/osfr-tools/tests/piece_044.rs:46-48, piece_062.rs:34-36, piece_065.rs:30-32, piece_068.rs:25-27 and piece_092.rs:11-12 include those files by path.

**Checked and still true (no change):**
- The four deliverable files exist: `src/restoration/piece_066.rs`, `tests/piece_066.rs`, `scripts/pieces/piece_066.py`, `tests/pieces/test_piece_066.py`.
- The module is not registered in `src/lib.rs`. `tests/piece_066.rs:25-30` uses the `#[path]` include.
- The test counts hold: 11 `#[test]` functions in `tests/piece_066.rs` and 11 `test_` methods in `tests/pieces/test_piece_066.py`.
- The wiki prerequisite defect is still present in the catalogue: `notes/Research/original-quest-coverage.json:1402` ("Quest:Learn") and `:1376` ("Quest:Your"). The Rust validator emits `unresolved wiki prerequisite` (`piece_066.rs:654`), and the Python checker flags `wiki-opening-chain` (`piece_066.py:416`).
- The corpus totals match the JSON `corpus_totals` block: 25, 42, 10, 58, 13, 16, 52, 2, 17, 51, 2.
- The native-accepted count is 12, code-only is 5 (JSON lines 1479-2287 and 2367-2699; `coverage.native_acceptance`, lines 2763-2767). Every local stage has `original_quest_id: null`, and `coverage.local_binding` is 0 of 17.
- The blocked claim for quest 1617 holds: `enemy_definitions: [0]` (JSON lines 2706-2711) and `blocked_claims` status `disabled` (lines 2770-2779).
- The stdlib-only checker's CLI accepts `--output` (`scripts/pieces/piece_066.py:684`).

**Unsure:**
- The lab report directory `../lab/reports/piece-066-20261009T043320Z/` and its logs (`report.json`, `check.txt`, RED/GREEN logs) lie outside the repo, so I could not confirm them. The "defects 1, checks 6" figure is also unverified; I did not run the checker.
- The commands use `scripts\cargo.ps1` with cwd `prototype\osfr-tools`. That file lives at repo-root `scripts/cargo.ps1`, and `prototype/osfr-tools/` has no `scripts/` directory. This is probably a snapshot-era cwd detail in a historical log, so I left it alone.
- The community facts (13 hub registrations, 6 region-1 stickers) rest on `FreeRealms-Legacy` in refs. I did not re-read `StartingZone.cs`.
