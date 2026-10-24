<!-- fleet job=note-refresh id=Native-Forging-Controls status=done turns=13 usd=0.0141 tokens(read,write,in,out)=[318869, 50297, 28, 9220] model=claude-haiku-5-5 -->
# notes/Research/Native Forging Controls.md

**Verdict:** minor drift. The board constants, the 180-second and five-hammer rules, and the 14×14 saved board all match the code. Two status sentences still say native calibration and completion are pending, which the native reviews have since superseded.

**Corrections:**

1. `old:` Actual native forging completion and screen calibration remain pending.
   `new:` Native forging completion (55 chains, five hammers, score 39300, Close and recipe transaction) is recorded in the October 9 update above and in [[../Reviews/Native Opening 17 103605]]; the 18-chain Won/results/Close run is in [[../Reviews/Native Forging Victory 181715]].
   `why:` repo:notes/Reviews/Native Opening 17 103605.md:13 (Forging 139000003, 55 chains, five quota drops, score 39300, real Close 26/42) and repo:notes/Reviews/Native Forging Victory 181715.md:5 (native Won, FRServer_GameOver, 39/18→39/47→39/19, Close). The "pending" line also sits in the same paragraph as the status claims it contradicts.

2. `old:` These are movie-stage coordinates, not yet calibrated desktop coordinates. Confirm the rendered first center and neighboring spacing from a native screenshot before using any screen coordinates; scaling, centering and window borders can change them.
   `new:` These are movie-stage coordinates. The desktop mapping is calibrated from a native 1279×960 screenshot to anchor (497,240) with pitch 43.5 (the October 9 update above); scaling, centering and window borders can change it, so re-measure before reuse.
   `why:` repo:notes/Reviews/Native Forging Layout 173814.md:5–7 (actual board calibration: cell (3,3) ≈ (496.75,239.75), practical anchor (497,240), step 43.5, "subject to fresh screenshot calibration after restart"). The update line at the top of this note says the same.

**Checked and holding:**
- `prototype/osfr-tools/src/forging.rs:20` `SIDE = 14`, so the saved board is 14×14 (matches line 11).
- `scripts/prepare-forging.py:64–67` (generates the Forging 139 content): board left 3, top 3, width 8, height 8, so x/y 3 through 10 (line 9); `duration_seconds: 180`, `quota: 5`, selectable types [1,2,3]. The same values appear in the test fixture at `forging.rs:1243`.
- `forging.rs:592` (`collected >= b.quota` → win) and `forging.rs:576` (hammer collect), so five hammers within 180 seconds (line 7) is the local rule. The config notice at `prepare-forging.py:56–57` marks these values as reconstructed, which the note already says.
- `forging.rs:364` ("StopLevel blocks only board input; keep GFx ticking"), consistent with line 13.
- `notes/Research/Original Forging.md` exists, so the `[[Original Forging]]` link resolves.

**Unsure:**
- `lab/tools/drive-forging-batch.py`, `lab/tools/plan-forging-chain.py`, `forge-plan-01.json` (through 56), the `--anchor/--step` options, and the `lab/decompiled/...` evidence paths are outside Git (`lab/` is not in the repo). I could not check them, so the "private helper" and "never writes a save or sends packets" claims are unverified.
- The update line says the screenshot is 1280×960. The 173814 review measured a 1279×960 image. The 103605 screenshot is not in the repo, so I could not settle the exact resolution.
- Client-side claims (tutorial close invokes StartGame, GameWon schedules GameOver after three seconds, single-click alternate mode) are not checkable from the repo and were skipped.
