<!-- fleet job=note-refresh id=Cooking-Later-Phase-Geometry status=done turns=8 usd=0.0089 tokens(read,write,in,out)=[120277, 37053, 18, 6153] model=claude-haiku-5-5 -->
# notes/Research/Cooking Later Phase Geometry.md

**Verdict:** badly stale on status. The coordinate figures match the sibling notes, but the note's framing says the later rounds still lack a control review and that its risks are open. Native run 164218 has since accepted phases 4–6 with normal mouse input.

**Corrections:**

1. `old:` This is geometry evidence only. The Cooking agent's separate original AS2 control review is required before claiming the later rounds are playable.
   `new:` This is geometry evidence only. The original AS2 control review now exists in [[Original Cooking Later Controls]], and native run 164218 completed Measure, Add and Stir with normal mouse input (see [[Reviews/Native Cooking Six Rounds 164218]]).
   `why:` notes/Research/Original Cooking Later Controls.md:3 and :23-25 (actual native controls accepted in164218); notes/Reviews/Native Cooking Six Rounds 164218.md:3 and :7-14 (phases 4–6 with normal root-operated mouse play); notes/Research/Original Cooking.md:52.

2. `old:` Important unresolved risks: sprites560/1758/2205/2206 contain no pt-prefixed named placements, no clipActions placements and no DoAction tags in any frame.
   `new:` Historical static observation, not a live blocker: sprites560/1758/2205/2206 contain no pt-prefixed named placements, no clipActions placements and no DoAction tags in any frame. Native run 164218 completed Measure and Stir with the unchanged movie, so this must not justify a movie patch.
   `why:` notes/Research/Original Cooking Later Controls.md:17 ("Historical static observation… not a live blocker… must not justify a movie patch"); notes/Research/Original Cooking Later Controls.md:11 (Default mold has no named mcMeasureLine; runtime target to be checked live, now superseded by the accepted run).

3. `old:` Geometric center coordinates do not bypass this evidence gap.
   `new:` The geometric center candidate was exercised by native run 164218: Stir pressed at (693,534), then ten counterclockwise circles of radius 67 around (626,534), with the original movie counting ten perfect turns.
   `why:` notes/Research/Original Cooking Later Controls.md:25 (Stir pressed(693,534), radius67 and center(626,534)); notes/Reviews/Native Cooking Six Rounds 164218.md:3 (Stir 10/10).

**Unsure:**

- The cited artifacts (`lab/reports/cooking-later-phase-geometry-v2.json`, SHA256 `62d221…1a50fd`, and `extract-cooking-later-phase-geometry.py`) are not in the repo tip. `lab/` is not a directory in this checkout, so I could not verify the hash, the script or the sprite/placement figures (bucket (642.69,327.67), mold (743.08,702.36), Add (643.02,520.84), Stir bowl (626.28,534.27), bounds, mcBowl1732/mcHitZone1744 offsets). They agree with the sibling note's figures (Original Cooking Later Controls.md:11–15, :21), but that is not independent proof.
- Line 16's "this does not resolve control-entry behavior" may now be outdated, since native 164218 drove the Stir loop. The sibling note still calls the exact runtime dispatch "untraced" (Original Cooking Later Controls.md:3, :17), so I left it unchanged.
- The "Final proof" wording and the claim that no movie repair or control/source/save/input changes were attempted could not be checked from code here.
