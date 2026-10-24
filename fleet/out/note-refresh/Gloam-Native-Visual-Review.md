<!-- fleet job=note-refresh id=Gloam-Native-Visual-Review status=nothing_found turns=7 usd=0.0070 tokens(read,write,in,out)=[86735, 28551, 16, 5137] model=claude-haiku-5-5 -->
# notes/Research/Gloam Native Visual Review.md

**Verdict:** current. The note is a visual-evidence review of an external recording and report, not a claim about our server code. Nothing in the tip contradicts it, and I found no code, status, or path:line claim that is now false.

**Corrections:** none.

**What I checked and found consistent:**
- Run 183551 Gloam evidence matches the Gloam combat review: `repo:notes/Reviews/Native Gloam Combat 183551.md:7` cites the same visual-review SHA `4f6b898a…d23851` and the same nominal 188/190/192/193 s frames. It says the review does not establish the full corpse/death animation, a per-frame animation ID, or exact video-to-packet sync. That matches this note's caveats.
- HP sequence (1000 → 965 → 930 → 895) and the three 35-damage hits match `repo:notes/Reviews/Native Gloam Combat 183551.md:3` ("Three incoming hits of 35 left the character at 895 HP") and `:7`.
- Frame numbering is internally consistent: 80 frames at 2 fps from 170 s gives 0.5 s spacing, so frame0031 = 185 s, frame0037 = 188 s, frame0047 = 193 s.
- Kill and reward status (Gloam defeated, Pappy turn-in 164→184 coins, restart 193318) is consistent with `repo:notes/Reviews/Native Gloam Combat 183551.md:9-13` and `repo:MODLOG.md:358`.
- The note's exclusions ("no source, active content/save, release, native input, movie or shared decoder output was changed") are process claims. I could not check them from read-only access, and I found nothing that contradicts them.

**Unsure:**
- The owner "combat_results" appears only as a reviewer name in `repo:notes/Research/Mac Native Visual Review.md:24` and this note. The packet/checkpoint proofs it is said to own were not located by name in the repo, so I could not confirm the ownership.
- The original video SHA `47261abe…f70c3`, the FFmpeg run, and the lab report paths (`C:/Users/Bryce/…/lab/reports/gloam-visual-183551-v1/`) sit outside the repo. I could not re-hash them. The only cross-reference is the visual-review SHA, which matches the Gloam combat review.
- No `notes/Autopilot/` report covers this visual review or changes Gloam code after it, so I found no later drift.
