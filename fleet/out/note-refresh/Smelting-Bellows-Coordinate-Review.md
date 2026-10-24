<!-- fleet job=note-refresh id=Smelting-Bellows-Coordinate-Review status=done turns=17 usd=0.0201 tokens(read,write,in,out)=[568760, 68715, 36, 11687] model=claude-haiku-5-5 -->
# notes/Research/Smelting Bellows Coordinate Review.md

**Verdict:** minor drift. The phase-row goal, the 157-second HEAT statistic, the superseded-note link and the absence of fresh native acceptance all hold at the tip. One unit claim is wrong. Most of the note's evidence (original AS2, the Lua UI, the `lab/` proof files and the input log) is private or client-side and cannot be checked from the repo, so those claims are left alone.

**Corrections:**

- `old:` The current reconstructed phase row has goal100 and loss1heat/second.
  `new:` The current reconstructed phase row has goal100 and loss multiplier1, which is 0.05 heat per tick (not per second).
  `why:` repo:scripts/pieces/piece_013.py:446-447 computes `loss = data[1] * ORIGINAL_HEAT_FURNACE["loss_rate"]` and labels it "heat loss {loss:g} per tick". repo:prototype/osfr-tools/src/restoration/piece_013.rs:124 sets `loss_rate: 0.05`. The live row is `[100, 1, 500, ...]` at repo:scripts/prepare-smelting.py:48 and repo:prototype/osfr-tools/tests/piece_013.rs:33. The goal of 100 is confirmed by both files.

**Checked and holding:**

- Goal 100 and the stage-103 row: repo:scripts/prepare-smelting.py:48; repo:prototype/osfr-tools/tests/piece_013.rs:33.
- The "157 seconds" HEAT statistic and the full Smelting completion: repo:notes/Reviews/Native Gear Up and Smelting 173814.md:23 (`103 Heat Furnace: [0,0,0,157]`) and line 28.
- The link to [[Smelting Native Control Geometry]] resolves to repo:notes/Research/Smelting Native Control Geometry.md, which is itself marked as superseded by this note.
- Arithmetic: 4 × 29.7 = 118.8. The 65°/95° integer-pair angles and the radius-180 mapping also reproduce from the stated centre (757,332), the 1.12 client scale and the 90° point (757,534).
- No Build Ledger or Autopilot entry claims fresh native acceptance of the HEAT margin pair, so "pending" stands.

**Unsure:**

- The "Heat authored pivot", "original gain" and "≥90° / ≤80° rearm" claims come from original AS2 (`SmeltingGameClient`, `Core.Round.onMoveMouse`, `RoundHeatFurnace`). The client's Lua UI and client_sql do not contain these symbols, and the private `lab/decompiled` tree is not in the repo. Not checkable here.
- The outer 860×860 window at (210,50) and the `min(canvasWidth/1024, ...)` scale come from `wndMiniGameFlash.xml` and Lua that are not in the `ui` root (ScriptsBase.lua has no matching minigame scaling).
- The `lab/reports/smelting-bellows-geometry-v3/guide-v4.json` proof, its SHA256 and `review-smelting-bellows-geometry-v4.py` are not in the repo. The repo search returned only this note.
- "Both saved 173814 HEAT screenshots are 1279×960" and the input-log row 53 at 17:58:16.455 UTC are not present in any repo note I could reach.
