<!-- fleet job=note-refresh id=Bartle-to-Queen-Main-Road-Route status=done turns=9 usd=0.0130 tokens(read,write,in,out)=[162565, 43984, 20, 11740] model=claude-haiku-5-5 -->
# notes/Research/Bartle to Queen Main Road Route.md

**Verdict:** minor drift. The note's later sections (route receipt, Queen endpoint, 7065 datagrams, 490 input matches, stage 12 rewards) agree with the tip. Several earlier paragraphs still describe the uphill, bridge, Queen and Bartle-menu steps as open gates, and the 203139 acceptance has since closed them. The code-checkable claim (12 m NPC interaction radius) holds.

**Corrections:**

1. `old:` the uphill approach and original lilypad bridges remain native gates.
   `new:` the uphill approach and original lilypad bridges were later observed natively in run 203139 (see "Final native203139 road, climb and bridge acceptance" below).
   `why:` repo:notes/Reviews/Native Queen and Prompt 203139.md:21-23 (route receipt binds 38 route logs, 36 arrivals, 490 input matches, endpoint 9.473425 m from Queen); repo:notes/Current Progress.md:130 ("Off to the Queen is complete").

2. `old:` Actual approach/menu remains a native gate.
   `new:` Actual approach/menu was observed natively in run 203139; the Queen X menu completed stage 12 at about 9.47 m.
   `why:` repo:notes/Reviews/Native Queen and Prompt 203139.md:15 and :25 (Queen X/menu/choice at about 9.47 m completed talk and turn-in).

3. `old:` and will inspect Bartle's actual menu.
   `new:` and Bartle's actual menu was then inspected in run 193318: the stage 9 turn-in and the next-quest choice were accepted.
   `why:` repo:notes/Reviews/Native Bartle and Artifacts 193318.md:9-12 (proximity menu observed at about 7.75 m to 5.7 m; stage910009 completed; stage910010 accepted); repo:notes/MODLOG.md:366.

4. `old:` This still does not accept the complete current road/artifact/Queen route or final transport.
   `new:` This prefix alone did not accept the complete road/artifact/Queen route or final transport; the 203139 final receipt below accepts the observed road-to-Queen path, and final transport is covered in the Queen review.
   `why:` repo:notes/Reviews/Native Queen and Prompt 203139.md:23 and :29 (final route receipt and final transport/state receipt, 7,065 datagrams).

**Checked and holding:**
- Queen interaction radius 12 m: repo:prototype/osfr-tools/src/npc_interaction.rs:52 (`INTERACTION_RADIUS: f64 = 12.0`) and :973.
- Artifact3 direct west hillside success and the unplayed gentler detour: repo:notes/Research/Artifact3 Native Interaction Approach.md:15-23 and repo:notes/Reviews/Native Bartle and Artifacts 193318.md:28.
- Linked notes exist: repo:notes/Research/Pappy to Bartle Main Road Detour.md, repo:notes/Research/Queen to Mae Main Road Return.md, repo:notes/Research/Artifact3 Native Interaction Approach.md.
- The 713 fence jump is described as a separate event, consistent with repo:notes/Research/Pappy to Bartle Main Road Detour.md:3.
- The 7065 datagrams, 490 input matches, 36 arrivals plus 2 guard stops, and the 259 coins / 300 XP / 775 HP checkpoint all match the Queen review and MODLOG.md:378-384.

**Unsure:**
- Whether run 193318's Bartle menu was reached by the southern fallback `(-1836,333) → (-1852,333) → (-1854,337)` that the note recommends. The review confirms the menu, not the approach path. The Pappy note's line 3 implies the southern fallback was used.
- Lab-only figures (1577 sources, 985.48 m candidate, 99 frames, nearest pose 9.428430 m, the 5 m Artifact2 approach distances, and all `C:/Users/...` report hashes) cannot be checked from the repo.
- Artifact positions and distances in the Bartle/artifact section (for example the 6.219 m and 10.391 m figures) need the client actor data, which I did not check.
