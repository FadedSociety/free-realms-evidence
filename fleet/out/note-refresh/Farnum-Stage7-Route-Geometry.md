<!-- fleet job=note-refresh id=Farnum-Stage7-Route-Geometry status=nothing_found turns=11 usd=0.0160 tokens(read,write,in,out)=[302566, 57047, 24, 11705] model=claude-haiku-5-5 -->
# notes/Research/Farnum Stage7 Route Geometry.md

**Verdict:** current. Every repo-checkable claim I could test still holds at the tip. The route coordinates, wolf positions and grounding findings are either confirmed in code or delegated to private `lab/` artifacts that cannot be read from the repo.

**Checked and holding:**
- **Cleetus registration `(-2078.389, 200.7649)`**: matches `prototype/osfr-tools/src/dev_teleport.rs:726` (`[-2078.389, -55.64841, 200.7649]`) and `data/content/npcs/farnum_farmstead.json:1225`.
- **Five wolves at Y −45.98195, X +4 and Z +3 per wolf, starting at `(-2100.965, 456.7631)`**: matches `prototype/osfr-tools/data/content/encounters.json:30-117`. The wolf definition is 3156 with 5 wolves in stage 910007, and `tests/pieces/test_piece_051.py:46,185,270` asserts the same position.
- **Offset arithmetic in the wolf table** (e.g. wolf 1 +0.051754, wolf 5 −1.777297): arithmetic is consistent with −45.98195 minus the listed floors.
- **`scripts/prepare-opening-encounters.py` exists** and copies the first original enemy position, adding `4*index` to X and `3*index` to Z (lines 56-60). It does not change Y, which matches the note.
- **Community GCNK `LoadCollision` is a `TODO Bullet Physics` placeholder returning true**: confirmed by `scripts/pieces/piece_079.py:307-317`, `prototype/osfr-tools/src/restoration/piece_079.rs:20,56` and `scripts/pieces/piece_080.py:11,587`. The reader revision `9c06714c…` also matches `piece_080.py:586`.
- **FreeRealms.exe SHA256 `26cc1c52…`**: matches `scripts/pieces/piece_080.py:589` and the grounding note.
- **Grounding follow-up** `notes/Research/Stage7 NPC Grounding Semantics.md` exists. Its HasTilt=false, VerticalOffset −0.1 and native Y+2 → Y−2000 collision-hit findings match `scripts/pieces/piece_080.py:590-593` and `piece_080.rs:21-23`. Its "not proved for initial spawn" caveat is preserved.
- **`notes/Research/Stage7 Native Return Routes.md` exists** and contains the three recorded Space presses and the superseding of the straight north connector (line 17). Both match this note's line 60.
- **Pappy `(-2184.513, -31.537, 328.111)`**: matches `data/content/npcs/farnum_farmstead.json:5473` and `tests/sheep_watch_dungeon.rs:82`.
- **No Autopilot task or content change** has altered the wolf Y values, the route or the grounding status. `data/content/encounters.json` still carries −45.98195.

**Unsure:**
1. **Path of the prepared encounters file.** The note says "Prepared `rust-opening-cooking-original-assets/encounters.json`". `scripts/prepare-opening-encounters.py:21,90` writes to `lab/references/rust-opening/encounters.json`, and `scripts/pieces/piece_051.py:17,60` agrees. The `rust-opening-cooking-original-assets` directory is a later derivative (`scripts/prepare-cooking-campaign.py:16`). It plausibly carries the file forward, but I could not confirm that from the repo. Left uncorrected.
2. **Collision decoding in our repo.** The note says the analysis "does not decode Bullet collision", scoped to the community reader. That remains true. However, `prototype/osfr-tools/src/restoration/piece_080.rs:1-25` now contains our own partial decoder of the GCNK collision section (BVH nodes and a column query). The note does not mention it. This is an omission rather than a falsehood, so I made no correction.
3. **Lab-only claims** (proof SHA256s, terrain Y values, clearances 0.314 / 1.558 / 1.718 / 3.375, the 285.6-unit A* candidate, object `1360108822`, the MAP node count 2,019, the MAP SHA256 `edd298b4…`). These live in `../lab/` and are not in the repo. I could not check them.
