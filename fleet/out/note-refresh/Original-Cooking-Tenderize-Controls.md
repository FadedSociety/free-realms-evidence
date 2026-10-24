<!-- fleet job=note-refresh id=Original-Cooking-Tenderize-Controls status=done turns=16 usd=0.0120 tokens(read,write,in,out)=[317567, 36459, 34, 8552] model=claude-haiku-5-5 -->
# notes/Research/Original Cooking Tenderize Controls.md

**Verdict:** minor drift. Most of the note is original-movie research (AS2 timings, coordinates, sprite IDs) that I could only check arithmetically, and that arithmetic holds. One status sentence is stale: native Tenderize play has since been run and accepted.

**Corrections:**

- `old:` Native phase play remains pending.
  `new:` Native Tenderize play has been run with normal mouse input: the first native launch recorded Tenderize 0/8 and then 33 bad / 8 good / 0 perfect (the statistic-suffix repair was needed before it could be accepted), and the six-round native run `client-baseline-20261008T164218Z` completed Tenderize with 34 bad / 8 good / 0 perfect (44 s) as one of six accepted phases.
  `why:` repo:notes/Reviews/Native Cooking Launch 162238.md:3 (accepts the original movie launch and Tenderize-to-Chop transition); repo:notes/Research/Original Cooking.md:46 (normal mouse input completes Tenderize, 8 good); repo:notes/Reviews/Native Cooking Six Rounds 164218.md:3, :11 (Tenderize row, all six phases accepted). The `Tenderize 8 good` count also matches the recipe row in repo:scripts/prepare-cooking.py:50 (`[10, 8, 15, 2, 50, ...]`, where 8 is the hit count) and the `STAGES` first entry 1 in repo:prototype/osfr-tools/src/cooking.rs:22.

**Checked and consistent (no change):**
- "The first reconstructed recipe phase uses the original Tenderize Bat Meat movie" and "Eight successful hits complete it": `STAGES = [1, 2, 3, 6, 17, 7]` (cooking.rs:22) with Tenderize first; hit count 8 in prepare-cooking.py:50.
- The 1280×960 mapping: min(1280/1024, 860/768) = 1.1197917; 768×1.1197917 = 860; origin (210, 50). I recomputed the table's expected client coordinates and the ±37.35×20.88 hammer extents; they agree.
- Timings: 9 frames / 35 fps = 0.257 s and 10 / 35 = 0.286 s.
- The note's tie to `prepare-cooking.py` as the source of the tuning is accurate: `TenderizeElem.as` is listed there (prepare-cooking.py:40).

**Unsure:**
- `lab/reports/cooking-controls.xml`, `cooking-tenderize-controls-proof.json`, `prove-cooking-tenderize-controls.py` and the ledger hashes: `lab/` is a sibling directory outside the repo (.gitignore:28), so I could not confirm these files exist. Nothing in repo names them.
- "MiniGameFlash.Resize uses min(canvasWidth/1024, (canvasHeight-100)/768)": the Lua only forwards `MiniGameFlash.commands.Resize` to `MiniGameFlash:Resize` (ui:ScriptsBase.lua:6993-6994); the formula is in native code, which the ui root does not contain.
- Original-movie details (power meter hidden, click only while Idle, bounding-box rather than pixel test, hammer-radius increment 0, the SHA-256 of the original movie): the AS2 sources are not in any root I can read, so I could not check them.
