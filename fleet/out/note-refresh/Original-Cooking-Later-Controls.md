<!-- fleet job=note-refresh id=Original-Cooking-Later-Controls status=done turns=13 usd=0.0173 tokens(read,write,in,out)=[346836, 52389, 28, 14516] model=claude-haiku-5-5 -->
# notes/Research/Original Cooking Later Controls.md

**Verdict:** minor drift. The code-facing claims hold at the tip; one sentence about the 162238 attempt now reads as if it describes the current evidence.

**Corrections:**

- `old:` Current attempt rejected its reports before the repair and cannot prove a valid recipe reward.
  `new:` The 162238 attempt rejected its reports before the repair and could not prove a valid recipe reward; run 164218, played after the repair (release `393ae59c…`), accepted them.
  `why:` MODLOG.md:305–307 (repair in 162238 follow-up, then 164218 accepted GameWon 5199 with 28 suffixed statistics); notes/Research/Original Cooking.md:46 (162238 "cannot establish a valid recipe completion") versus :56 (164218 accepted). The repair itself is at prototype/osfr-tools/src/cooking.rs:467–469 (StatUpdate value) and :561–562 (StopLevel won).

**Checked and holding:**

- Narrow `)` repair is limited to the final StatUpdate value and StopLevel's final field: `cooking.rs:469` and `cooking.rs:562`. Matches the note and Original Cooking.md:48.
- `FRServer_ScoreSet` binds with no repair needed: `cooking.rs:498–502`. Final `FRServer_GameWon` requires quantity 0 and sends `OnGameWonMsg` plus results: `cooking.rs:504–535`.
- Gates the note says remain (range and order checks, recipe transaction, StopLevel 1..=6 and 0|1): `cooking.rs:474–496`, `:519–531`, `:563–566`.
- Geometry numbers agree with notes/Research/Cooking Later Phase Geometry.md:5–16 and :20 (SHA256 `62d22132…`, Add bounds, Stir bowl and hit AABB, spoon offset, scale 215/192 ≈ 1.1197917). The "V2 corrects nested-mold composition" claim matches that note's line 20.
- Native 164218 facts match notes/Reviews/Native Cooking Six Rounds 164218.md: 28 statistics, 297 s versus 295 summed, score path 800→5199, quest counts `[1,1,1,4,4,1]`, and the finish/Close/Mae/restart items were not accepted in that run.
- Links resolve: `[[Native Crafting Results Lifecycle]]` is notes/Research/Native Crafting Results Lifecycle.md.

**Unsure:**

- Measure thresholds ("Good 152–168 inclusive; Perfect strictly 157–163", pressure formula, "more than 1200 accumulated animation units"), Stir speed and frame timing, and "Correct direction counts Perfect; wrong direction also counts Good". These are AS2 movie behaviour. The client's `ui` root (ScriptsBase.lua) and `client` root contain no AS2 source, so I could not check them. The phrase "strictly 157–163" may be ambiguous, since strict bounds would exclude 157 and 163.
- `RoundClick`, `Bowl.collision`, `mcMeasureLine`, and the 241-export search: not findable in the `ui` or `client` roots. The Phase Geometry note's XML finding (no `mcMeasureLine`, no `pt`-named placements) agrees, but I did not re-verify it.
- Artifacts cited under `../lab/` are outside this repo, so I could not check them: `cooking-later-phase-geometry-v2.json` (the sibling note uses `lab/reports/`, same file), `cooking-later-controls-proof.json`, `native-crafting-stat-suffix-proof-v2.json` (Original Cooking.md:50 gives SHA `a8b0faf1…` for the same file), and `cooking-later-controls-native-acceptance-v2.json`.
- Native 164218 per-round details ("ten counterclockwise circles with 16 interpolated points", the Add drag coordinates) are not in the repo; I did not check them.
