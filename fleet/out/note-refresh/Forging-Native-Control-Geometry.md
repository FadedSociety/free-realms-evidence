<!-- fleet job=note-refresh id=Forging-Native-Control-Geometry status=done turns=16 usd=0.0180 tokens(read,write,in,out)=[394385, 49011, 34, 15789] model=claude-haiku-5-5 -->
# notes/Research/Forging Native Control Geometry.md

**Verdict:** minor drift. The geometry arithmetic and the code-side facts hold at the tip. The closing "next native gate" is stale, because native Forging runs since the note was written already proved the win, results, Close, consumption and output. The planner anchor is also older than the calibration that later native work recorded.

**Corrections:**

1. `old:` Next native gate remains original139 entry/tutorial, screenshot-calibrated normal chains, queue/gravity without desynchronization, hammer collection/mold progress, genuine quota win/delayed callback/results, actual Close, fixed ingredient consumption, exactly one output/quest update and restart.
   `new:` Next native gate remains original139 entry/tutorial, screenshot-calibrated normal chains, queue/gravity without desynchronization, hammer collection/mold progress and restart. The quota win, delayed results, actual Close, ingredient consumption and single output/quest update were already proved natively: 55 real chains, five hammers and `OnQuotaInitMsg 0 606 5 1 910` in run 103605, then OnGameWonMsg, delayed FRServer_GameOver and a four-byte 26/42 Close with one Hammer30280 completion in run 181715.
   `why:` repo:notes/Reviews/Native Forging Victory 181715.md:5-7 (win, delayed GameOver, actual 26/42 Close, one Hammer30280 and one completion, consumption proof); repo:notes/Reviews/Native Opening 17 103605.md:13,27 (55 chains, five hammer falls, quota 5, YOU WIN Forging page); repo:notes/Research/Native Forging Controls.md:3 (103605 results/Close/recipe pass). Quota 5 and the 606 hammer id also match repo:prototype/osfr-tools/src/forging.rs:25 (`COLLECTABLE: u16 = 606`) and the reconstructed board in repo:prototype/osfr-tools/src/forging.rs:1243.

2. `old:` --anchor 492.243490 232.526042 --step 44.791667 44.791667
   `new:` --anchor 497 240 --step 43.5 43.5
   `why:` repo:notes/Research/Native Forging Controls.md:3 says a fresh 1280×960 screenshot confirmed anchor (497,240) and pitch 43.5 in run 103605, and repo:notes/Reviews/Native Forging Layout 173814.md:7 gives the same practical anchor and step. The static 492.24/44.79 values are the older estimate that the note's own line 15 says drifted. Keep the screenshot check before input.

3. `old:` Fresh runs still require calibration.
   `new:` Fresh runs still require calibration; the practical layout (497,240)/43.5 was already seen at 1280×960 in native run 103605 (see [[Native Forging Controls]]), so use it as the starting point and confirm it from the screenshot.
   `why:` repo:notes/Research/Native Forging Controls.md:3; repo:notes/Reviews/Native Forging Layout 173814.md:7.

**Checked and holding (no change):**
- Stage arithmetic: `mcGame` at (53.05,23), 40-unit tiles, scale 215/192 on a 650×768 movie giving 727.865×860, origin (276.068,50), and cell (3,3) at (492.243,232.526). I recomputed these and they match to rounding.
- Board occupies original indices 3..10. The repo's own tests mirror LEFT=3 and TOP=3 with an 8×8 field (repo:prototype/osfr-tools/src/forging.rs:1224-1227), and the server validates a 14×14 side (forging.rs:20).
- Hammer 606 is not in `selectable_types` (forging.rs:1243). Ordinary Quit goes through sub 6 and cancels only a pre-win run, while the terminal Won/Lost path waits for the real results Close (forging.rs:401-414). The 26/42 Close is distinct from the 39/7 ACK (forging.rs:397-400).
- The Cooking Measure/Stir claim matches repo:notes/Research/Original Cooking.md:52 (Native164218).
- The Tutorial→`TutorialClosed` and `Ui.QuitMiniGame` references exist in the client Lua (ui: ScriptsBase.lua:6317, 7003).
- The MatchThree server balance tables are still absent (repo:notes/Reviews/Harvesting Independent Review.md, repo:notes/Research/Harvesting Border Compatibility.md:43).
- The Layout 173814 link and [[Original Forging]] both exist.

**Unsure:**
- The planner `plan-forging-chain.py` and the reproducer `extract-forging-controls-geometry.py` live under `lab/`, which is not in the repo, so I could not check the "refuses nonidle/terminal" behaviour or the 'All 64 centers pass' result. The 'Native Forging Controls' note describes the same helper.
- "A one-tile quick release within 500ms enters original click mode" and "mold advances 20 frames per collected hammer" are not in the repo. The sibling note gives no 500 ms figure, only "a quick single click".
- The 33 ms tile update interval, the mold art bounds, the Tutorial button centers and the 3-page tutorial asset are client-side and not checked.
