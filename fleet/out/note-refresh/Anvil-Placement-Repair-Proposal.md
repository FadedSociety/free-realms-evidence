<!-- fleet job=note-refresh id=Anvil-Placement-Repair-Proposal status=done turns=9 usd=0.0158 tokens(read,write,in,out)=[210208, 54173, 20, 13814] model=claude-haiku-5-5 -->
# notes/Research/Anvil Placement Repair Proposal.md

**Verdict:** Badly stale on status, current on code. The helper, hashes, actor delta, rejection count and Cooking-migrator limit all match the tip. The header, the "pending" lines and the acceptance checklist describe the state before the migration and native runs of 2026-10-08, which have since landed.

**Corrections:**

1. `old:` `**Placement approved; new private package prepared, active migration pending.**`
   `new:` `**Placement approved; new private package prepared and migrated at the safe boundary; the moved anvil was accepted natively at run 183551.**`
   `why:` MODLOG.md:343-344 (snapshot migrated, native 183551 uses anvil-placement-v1 content); MODLOG.md:351; notes/Reviews/Native Wolves and Anvil 183551.md:5, 13.

2. `old:` `Root keeps current181715 on old content until the next safe boundary.`
   `new:` `Root later moved the active save to the new content at the safe boundary; native 183551 runs on anvil-placement-v1.`
   `why:` MODLOG.md:343-344; notes/Reviews/Native Wolves and Anvil 183551.md:5.

3. `old:` `- Visible anvil clear of boulder, grounded sensibly and approachable normally.`
   `new:` `- Visible anvil clear of boulder, grounded sensibly and approachable normally. **Accepted at native 183551** for visibility and ordinary X/menu/Interact approach; see [[Reviews/Native Wolves and Anvil 183551]].`
   `why:` notes/Reviews/Native Wolves and Anvil 183551.md:13 ("The new anvil is unobstructed… Normal X/menu/Interact requests reached it"); MODLOG.md:351.

4. `old:` `- Normal X/menu/Blacksmith gate and genuine Forging139 start, with no duplicate material grant.`
   `new:` `- Normal X/menu/Blacksmith gate: **accepted at native 183551** (Brawler receives "Switch to Blacksmith before forging"; no session or material change). Genuine Forging139 start from the moved anvil and the no-duplicate-grant check remain pending.`
   `why:` notes/Reviews/Native Wolves and Anvil 183551.md:13, 17; notes/Reviews/Remaining Opening Preflight.md:28 ("the repeat forging has not been replayed there").

5. `old:` `- Independent completion of full Forging win/results/player Close/quest turn-in/restart after the Windows save-lock repair.`
   `new:` `- Forging win/results/player Close/quest turn-in/restart: **completed at native 181715 and restart 193318, but on the pre-move anvil**. A full Forging replay from \`[-2088,-54.79,200]\` is still required.`
   `why:` MODLOG.md:336 (Native 181715 win, Close, Cleetus turn-in); MODLOG.md:362 (restart 193318); notes/Reviews/Native Wolves and Anvil 183551.md:17 ("forging from the new position has not been replayed").

6. `old:` `- Actual walking from clear camp staging through the wolf route. No geometry-only claim substitutes for this.`
   `new:` `- Actual walking from clear camp staging through the wolf route: **done at native 183551** (five wolves defeated by ordinary key input; Cleetus reward 18 coins / 25 Brawler XP). No geometry-only claim substitutes for this.`
   `why:` MODLOG.md:345-351; notes/Reviews/Native Wolves and Anvil 183551.md:3, 7, 11.

7. `old:` `Native walk candidate to stage7 wolves`
   `new:` `Native walk candidate to stage7 wolves (pre-migration guidance; the walk was later performed, see Acceptance)`
   `why:` MODLOG.md:350-351 (anvil approached on foot after the move; wolves engaged). This is a pointer, not a falsehood, so apply only if the note is revised as a whole.

**Checked and current:**
- `scripts/anvil_placement.py:19-25`: proposal SHA, source inventory SHA, OLD `3e6f42…`, NEW `4e6ac1…`, mapping `ed985d…`, GUID, BEFORE/AFTER positions all match the note.
- `scripts/anvil_placement.py:104-108`: only the three campaign/journal `opening_sha256` bindings are replaced, each required to occur exactly once.
- `scripts/anvil_placement.py:196-201, 222, 228`: stopped-process check runs before and after the migration.
- `scripts/anvil_placement.py:186-188`: the hash must occur exactly once; the replacement is one raw byte replacement.
- `scripts/anvil_placement.py:236-242`: a NEW destination is required, and an existing identical output is accepted idempotently.
- `scripts/check-anvil-placement.py`: the 44 rejection cases counted in the file, six completed stages (index < 6), the progressed fixture and the byte-exact rollback all match.
- `scripts/migrate-cooking-campaign.py:25-38`: requires `cef512` and refuses any stage id ≥ 910004 that is touched. This supports the note's "cannot migrate this progressed placement change."
- Wiki links `[[Farnum Stage7 Route Geometry]]`, `[[Stage7 NPC Grounding Semantics]]`, `[[Reviews/Native Forging Layout 173814]]` resolve to existing notes.

**Unsure:**
- Spawn yaw −0.023182, the 0.443669 clearance radius and the clearance and floor numbers (lines 17–19): no matching code or data found in the repo; these live in the lab proof JSON, which is not in the repo.
- Pinned community revisions (lines 29–33), the proposal JSON SHA and the package marker SHA (lines 25, 47): lab artifacts, not checkable here.
- `lab/reports/propose-anvil-placement.py` (line 25): not in the repo; `scripts/anvil_placement.py` does not implement it.
- Line 55 ("Real snapshot migration, Rust runtime restore and native render/approach remain pending") is accurate for its moment. The next paragraph supersedes it, so I did not correct it.
