<!-- fleet job=guide-refresh id=Build-Guides status=nothing_found turns=10 usd=0.0123 tokens(read,write,in,out)=[183459, 46615, 22, 9293] model=claude-haiku-5-5 -->
# notes/Build Guides/Build Guides.md

**Verdict:** current. Every checkable structural claim holds at the tip. One headline count could not be settled and is listed under Unsure, not corrected.

**Corrections:** none.

What I checked:
- **Generator path:** `scripts/native_map/build_guides.py` exists (the note's `project/` prefix is the workspace root, as in the Native Map note). The script's behaviour matches the note: it writes the index, keeps the NARRATIVE block on re-run, and regenerates only the tables (`scripts/native_map/build_guides.py:105-168`).
- **Link targets:** all 23 Gameplay, 4 World, 4 Network, 9 Client Engine and 5 Libraries guides linked from the index exist under `notes/Build Guides/<section>/`. `[[Content]]` resolves to `notes/Build Guides/Content/Content.md`.
- **Per-guide counts:** all 45 index lines match the "N accepted functions: X confirmed, Y likely" headers inside the guide files (for example Kart Racing 319/82/98, Command System 2873/1492/812, Containers 17623/5290/6174). The Kart count also matches a direct query of the client label table for the `minigame.kart` / `game.vehicle` / `physics.vehicle` / `net.vehicle` prefixes (319).
- **Total functions:** 199405 matches `Native Map/Native Map.md:19` and the client `fn` table row count.
- **Sum check:** the 45 per-guide function counts sum to exactly 69641, so the index is internally consistent.

**Unsure:**
- **"69641 accepted labels"** (`notes/Build Guides/Build Guides.md:10`). The index was generated 2026-10-12 and its per-guide sums agree with it, so it is correct for that run. Two other sources disagree:
  - The client label table reports 99,894 rows, all `status='accepted'` (a different export, so it may not be the same run).
  - `notes/Design/Build Plan.md:123` records 68,411 accepted labels on 2026-10-16, after the 10-12 generation.
  
  I could not reconcile these. The count is a dated snapshot, so it may just be stale. A re-run of the script would settle it, which I could not do.
- **Mapping status.** "Mapping is still in progress" is consistent with the Native Map coverage table (pending 81,916), but I did not check its current state.
