<!-- fleet job=note-refresh id=Pappy-to-Bartle-Main-Road-Detour status=nothing_found turns=8 usd=0.0120 tokens(read,write,in,out)=[139856, 37665, 18, 11806] model=claude-haiku-5-5 -->
# notes/Research/Pappy to Bartle Main Road Detour.md

**Verdict:** current. I found no repo-checkable claim that is now false. Most of the note cites lab proofs under `C:/Users/.../lab/reports/`, which are not in the repo, so those hashes, sample counts and run results can't be settled here.

**Corrections:** none.

**Checked and holding:**
- Note links resolve: `notes/Research/Stage7 Native Return Routes.md`, `Bartle to Queen Main Road Route.md` and `Pappy to Bartle Route Candidates.md` all exist. The Route Candidates note (line 5) points forward to this detour, as this note points back.
- Bartle's configured position `[-1860.185,-51.30442,341.1369]` matches `prototype/osfr-tools/tests/fixtures/quests/opening.json:117-125`. The same position is used in `tests/piece_018.rs:392` and in `Stage7 Native Return Routes.md:82`.
- Bartle's `interaction_radius` is 12.0 (`opening.json:127`). `prototype/osfr-tools/src/npc_interaction.rs:52` sets `INTERACTION_RADIUS = 12.0`.
- Distance arithmetic. The eastern point `(-1850, -53.174776, 342)` is 10.391 m in 3D from Bartle, as stated. The 2D sums of the listed render-floor X/Z points reproduce the stated lengths: connector ≈70.49 m, original road chain ≈420.74 m, final approach ≈12.42 m (716→eastern point). The three segments add to the stated 503.63 m.
- Waypoint count: the table has 18 rows, matching "18 road-detour waypoints".
- The "old eastern Bartle point selects Artifact2 first" and "stalled on the crystal" statements agree with `notes/Research/Bartle to Queen Main Road Route.md:3` and `:33`.
- The 713 fence jump is described consistently across this note and `Bartle to Queen Main Road Route.md:7` and `:11`.

**Unsure:**
- "within his 12m interaction radius; interact from this eastern side". The 12 m figure is the server guard and is written into the actor packet at `prototype/osfr-tools/src/opening_world.rs:75` (`bytes[237..241]`). However, `notes/Research/Native Interaction Acquisition Range.md:28` records that, before that patch, the native X prompt defaulted to about 7 m, and line 38 says a fresh native session must still prove 12.0 in the actual packet. This note does not claim native proof, so I left it alone. A reader might still take 12 m as native-verified. Adding "(server guard; native X prompt proof pending)" would make that explicit.
- The reverse-descent sample counts (22 logs, 21 arrivals, 75 moving samples, 3.11604 m Y drop) and the hashes come from lab artifacts outside the repo. I could not check them.
- The 130 DME meshes / 873 scene objects figure is not in the repo, and it differs from the 465 / 5118 figure in `Bartle to Queen Main Road Route.md:39`. Those are different corridors, so this is not a contradiction, but I could not verify either number.
