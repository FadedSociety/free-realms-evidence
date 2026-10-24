<!-- fleet job=note-refresh id=Original-Quest-Coverage status=done turns=10 usd=0.0157 tokens(read,write,in,out)=[273806, 57537, 22, 11555] model=claude-haiku-5-5 -->
# notes/Research/Original Quest Coverage.md

**Verdict:** Minor-to-moderate drift. The catalogue, file paths, test count and the 1617 block still hold at the tip. The "Implementation states" section is a 2026-10-08 snapshot that the 2026-10-09 native runs have overtaken, and the cave and micro-tutorial lines are also out of date.

**Corrections:**

1. `old:` Implementation states stay distinct (2026-10-08 snapshot, `Current Progress`):
   `new:` Implementation states stay distinct (2026-10-09 `Current Progress`, "Latest native playthrough, October 9 Pacific"):
   `why:` repo:notes/Current Progress.md:92 (all 17 local stages completed/rewarded in `client-baseline-20261009T103605Z`); repo:notes/Current Progress.md:94 (reload with 17 rewards); repo:notes/Design/Build Ledger.md:79 ("Opening (17 stages) | Native-verified").

2. `old:` 12 local stages native-accepted (`910001`-`910012`), 5 code-only
   (`910013`-`910017`);
   `new:` all 17 local stages native-accepted and rewarded (`910001`-`910017`; run `client-baseline-20261009T103605Z`, reloaded in `client-baseline-20261009T111125Z`);
   `why:` repo:notes/Current Progress.md:92 and :94; the 12/5 split matches only the older 14/17 checkpoint at repo:notes/Current Progress.md:106.

3. `old:` and no complete-dungeon acceptance;
   `new:` and has a native complete-dungeon acceptance (cave replay run `client-baseline-20261009T114509Z`: victory, Close, return, unchanged economy; Build Ledger row "Opening cave 411" is Playable);
   `why:` repo:notes/Current Progress.md:98; repo:notes/Design/Build Ledger.md:70. Also "original cave encounter" should read "reconstructed cave encounter": repo:notes/Reviews/Original Tutorial Mode Exit Field Review.md:170.

4. `old:` the original micro-tutorial actions are
   `locale text only.`
   `new:` the original micro-tutorial camera objectives have a recovered native mechanism (45 original native function extracts, Lua ranges and provenance); the three globe and barrier bindings remain missing.
   `why:` repo:notes/Research/Original Opening Microtutorial Recovery.md:3, :9 and :13. The "original micro-tutorial gates" open item in the "Missing originals" section (line 115) is still accurate.

**Checked and holding (no change):**
- `scripts/audit-quest-coverage.py` and `tests/test_quest_coverage.py` exist at the cited repo paths; the test file has 10 `def test_` functions, matching "10 tests pass".
- The 17 local opening stages (`piece_066.rs:14-15`, `test_quest_coverage.py:141`) and `original_quest_id` null on all of them (`tests/pieces/test_piece_066.py:115`).
- Quest 1617 "Harassing the Harassers" / "Defeat Petty Yetis" blocked as `disabled` with engine `enemy_definitions = [0]` (`prototype/osfr-tools/tests/piece_066.rs:234-251`; `tests/test_quest_coverage.py:150-177`).
- `notes/Research/original-quest-coverage.json` exists.

**Unsure:**
- "**0 original quests** have any native acceptance" (line 93): I found no native run that binds an original numeric quest id. Native runs only cover local `910xxx` stages, so I left it unchanged. It was not settled either way.
- "6 unrecovered rules" for the cave (line 94): I could not find this count in `notes/`, so I did not change it.
- `scripts/audit-quest-coverage.py:42` hard-codes `NATIVE_ACCEPTED_LOCAL_STAGES = tuple(range(910001, 910013))`, which is the same stale 12-stage snapshot. The note does not cite it, but any consumer that reads it would be out of date.
- The audit counts (0 errors, 20 warnings) and the SHA-256 pins point to `lab/` artifacts that are not in the repo, so I could not re-run them.
