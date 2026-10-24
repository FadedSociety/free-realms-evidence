<!-- fleet job=note-refresh id=Smelting-Native-Control-Geometry status=nothing_found turns=12 usd=0.0141 tokens(read,write,in,out)=[255833, 50947, 26, 10423] model=claude-haiku-5-5 -->
# notes/Research/Smelting Native Control Geometry.md

**Verdict:** current. Every checkable claim about our code and status still holds at the tip; no corrections needed.

**Checked and holding:**
- **"Current reconstructed phase selects 5Ore"** (table, Initial five Copper ore row). `scripts/prepare-smelting.py:46` gives phase 1 `[1, 5, 1, 1, 0, 20, 2, 3, 50, 100, 200]`, so the ore value is 5. The recipe consumes `[2739, 5]` (line 68), matching the note's "Copper ore5" context in `notes/Research/Native Smelting Controls.md:17`.
- **"Current 65% tuning"** (Fill target line row). `scripts/prepare-smelting.py:47` has phase 2 starting with `65`, and `Native Smelting Controls.md:11` describes the 65% measure line under the same local phase row.
- **"goal100 and loss1 heat/second"** (Heat numerical control, and the Bellows note's gain paragraph). `scripts/prepare-smelting.py:48` has phase 3 `[100, 1, 500, ...]`.
- **Phase order and stage IDs.** `Native Smelting Controls.md:7` (break, fill, heat, mold; stage IDs 101–104) matches `prototype/osfr-tools/src/smelting.rs:459-460`, which maps stages 101..=104 to rounds 0..3.
- **Follow-up link.** `notes/Research/Smelting Bellows Coordinate Review.md` exists and states the same conservative pair (843,515)→(740,534), the 860×860 outer Lua window at (210,50), and the numerical pivot (488.75,251.95). It supersedes the art-pivot alternatives as this note says.
- **Arithmetic.** I recomputed the derived client coordinates from the stated values: scale 860/768 ≈ 1.1198 and origin (210,50); numerical pivot → client (757,332); art pivot → (596,332); radius-180 points at 65° and 90° → (843,515) and (757,534); bounds centres (649,598) and (649,721) match the listed centres. All agree within rounding.
- **"Cooking Measure and Stir both worked in the actual client".** Supported by `notes/Research/Original Cooking.md:52` and `notes/Reviews/Native Cooking Finish and Mae 171251.md:22`.

**Unsure (not settled from the repo):**
- The XML geometry, the `lab/reports/smelting-controls*.xml`/`.json` proofs, the `extract-smelting-controls-geometry.py` reproducer and the SHA256 values all live under `lab/`, outside the repo. I could not verify them, so I did not check the bucket, table, ore and pour-region coordinates against source.
- `bFollow` starts true and `doAction` requires no press (Heat row). This is in the AS2 source, which is private. The Bellows note's review says the same, but I could not inspect the AS2 directly.
- "Current 65% tuning selects authored mcMeasure frame 65" depends on the AS2 frame mapping, which is also private. The 65 value itself is confirmed above.
