<!-- fleet job=note-refresh id=NPC-Location-Hints status=nothing_found turns=13 usd=0.0156 tokens(read,write,in,out)=[335383, 49817, 28, 12052] model=claude-haiku-5-5 -->
# notes/Research/NPC Location Hints.md

**Verdict:** current. I found no repo-checkable claim that is now false, and no path or citation that has moved. Most of the note's numbers come from the lab/ mining outputs (`hints.jsonl`, `summary.json`, `startup.json`, `FabledRealmsAreas.xml`), which are not in the repo tree, so I could not re-derive them.

**Corrections:** none.

**What I confirmed against the tip:**
- The five unresolved refs exist with the names the note gives: Gunther 9000000100 (`npcs_unresolved.json:786-787`), Hilbert 9000000349 (`:2600-2601`, name "Hilbert †"), Jeni Shortfuse 9000000363 (`:2650-2651`), Kade Carmichael 9000000123 (`:836-837`), Sampson Idlefist 9000000453 (`:3511-3512`).
- Simone is regional ID 9000000467 with `zone: "Sanctuary"`, `zone_id: 10`, and position `[-1830.891, -42.04188, 428.7502]` (`npcs/sanctuary.json:54214-54264`). The note's "currently says Sanctuary" and the Legacy-data position are accurate.
- Zone key 7 is Highroad Junction (`data/content/zones.json:88-90`). Zone keys are labelled "reconstructed", which matches the note's caveat.
- Merigold is NPC 9000000402 in `highroad_junction.json:6553`.
- The "three rows typed ambiguous" claim holds (`npcs_unresolved.json` lines 12, 40, 73).
- The 17 quest-content files exist, and their `objectives` arrays are empty (`data/content/quests/`).
- The 578 Legacy-placed regional rows match `notes/Research/NPC Placement.md:11` and `:149`.
- The relation and confidence totals are internally consistent: 310 + 73 + 11 = 394, and 304 + 80 + 10 = 394. The Legacy split 100 + 1 + 477 = 578 is consistent too.

**Unsure:**
1. **Amaranthus POI position.** The note gives POI 76 at `[-385.92633, -68.03617, 1871.8076]` and says it agrees with the existing candidate. The repo's Amaranthus row (NPC 9500000084, `npcs/briarwood.json:422-466`) has `[-384.67633, -68.03617, 1871.8076]`. Only X differs, by 1.25. POI 76 is not in the repo, so I cannot tell whether the note has a typo or the NPC row is the one that differs. Worth a check against `startup.json`.
2. **Jeni Shortfuse POI 24 anchor.** The note gives `[-1490.254, -35.049, 409.188]`. No repo file contains that X value. `npcs/sanctuary.json:5795-5797` has `[-1489.004, -35.049, 409.188]` for a different row. It shows the same 1.25 X offset as item 1, so the pattern may be systematic. I could not identify that row's NPC, so I did not conclude anything.
3. **Lab-only items:** Pixie_Nursery area ID 90 at `FabledRealmsAreas.xml` line 232, POI 7 distance (~75 m), POI 147/16 positions, the 118 unresolved `npc` rows (I could not get a clean count from the search output), and the 1,279 AreaDefinition entries. None of these could be verified in the repo.
