<!-- fleet job=note-refresh id=Content-Batch-NPCs status=done turns=18 usd=0.0238 tokens(read,write,in,out)=[578509, 59863, 38, 21046] model=claude-haiku-5-5 -->
# notes/Research/Content Batch NPCs.md

**Verdict:** badly stale. The position claims, the `content_jobs` failure, the runtime-consumer claim and most counts describe the W27 snapshot (2026-10-13), not the tip. The file layout, the strict `NpcSpawn` schema and the 17-page structure still hold.

**Corrections:**

1. `old:` so positions remain null. Nearby landmarks and distance text are preserved as location evidence, not converted into coordinates.
   `new:` so no row has a source-backed transform. Each row's `position` is now a `(R)` reconstruction: a POI anchor plus a deterministic XZ offset (for example `placement: poi_anchor` at `blackspore_swamp.json:61`), with `position_reason` and `placement_candidates` recording the method. Nearby landmarks and distance text remain location evidence.
   `why:` `repo:prototype/osfr-tools/data/content/npcs/blackspore_swamp.json:49-53` (position array), `:61-72` (placement and `(R)` reason), `:444-453` (client POI tag plus reconstructed offset). A search for a record-level `"position": null` in `data/content/npcs/` returned no matches.

2. `old:` Every position is unknown.
   `new:` Every regional row now carries a `position` (reconstructed, `(R)`). The per-page columns below are the W27 snapshot.
   `why:` `repo:prototype/osfr-tools/data/content/npcs/blackspore_swamp.json:49-53`; no record-level null position in `repo:prototype/osfr-tools/data/content/npcs/`.

3. `old:` **0 / 1,199**
   `new:` **all reconstructed / 0**
   `why:` same as correction 2. The tip test counts 1,201 page rows, not 1,199 (see correction 8).

4. `old:` The focused `content_npcs` test passes and prints 277 resolved / 188 unresolved references, 403 resolved / 248 unresolved quest-giver occurrences, and 0 known / 1,199 unknown positions.
   `new:` The focused `content_npcs` test passes and prints 295 resolved / 170 unresolved references, 403 resolved / 248 unresolved quest-giver occurrences, and no unknown positions (no null `position` in the page files; the test prints the exact known count).
   `why:` `repo:prototype/osfr-tools/tests/content_npcs.rs:471-472` (295 and 170 asserted), `:239-258` (position counting), `:303` (465 total).

5. `old:` The requested combined run reaches the existing `content_jobs` test, which fails at `tests/content_jobs.rs:62`: it expects all job and quest NPC references to remain in `npcs_unresolved.json`.
   `new:` The requested combined run also reaches the existing `content_jobs` test, which now passes. Its NPC-reference check (`tests/content_jobs.rs:117-122`) accepts a reference that is either resolved or listed in `npcs_unresolved.json`.
   `why:` `repo:prototype/osfr-tools/tests/content_jobs.rs:62` is now the quest-file loop, not an NPC assertion; the check is at `:117-122`. Passing runs: `repo:notes/Autopilot/F390.md:123` (`content_jobs` 1 passed), `repo:notes/Autopilot/T407.md:81` (`content_jobs 1`).

6. `old:` That assertion reflects the old all-unresolved contract and conflicts with this batch's requirement to remove resolved references; the test file is outside W27 ownership and was not changed.
   `new:` That all-unresolved contract is no longer in the test file.
   `why:` `repo:prototype/osfr-tools/tests/content_jobs.rs:117-122`.

7. `old:` The combined command fails on the stale `content_jobs` assertion before `content_npcs` runs.
   `new:` At tip the combined command no longer stops at `content_jobs`, which passes.
   `why:` `repo:notes/Autopilot/F390.md:123`; `repo:notes/Autopilot/T407.md:81`.

8. `old:` projects all 1,199 page rows plus the package references
   `new:` projects all 1,201 page rows plus the package references
   `why:` `repo:prototype/osfr-tools/tests/content_npcs.rs:459` (`assert_eq!(content_npcs.len(), 1201)`, with a comment that T379 appended two repair-guy rows).

9. `old:` This validates the full existing content package and its cross-references, but does not register the regional page format as a production runtime consumer.
   `new:` This validates the full existing content package and its cross-references. The regional page format is also read at runtime: `world.rs` loads every `npcs/*.json` into `RegionalNpc` and keeps rows with a finite `position`, and NPC interaction loads the `npcs/` directory.
   `why:` `repo:prototype/osfr-tools/src/world.rs:112-135` (`RegionalNpc`), `:252-268` (load and position filter); `repo:prototype/osfr-tools/src/gameplay.rs:958-963` (`npcs` directory for `npc_interaction`).

10. `old:** Name and region evidence resolved 277 keys to NPC records; 188 remain in `npcs_unresolved.json`:` (the bold markers are not in the note; use the plain text below)
    `old:` Name and region evidence resolved 277 keys to NPC records; 188 remain in `npcs_unresolved.json`:
    `new:` Name and region evidence resolved 295 keys to NPC records; 170 remain in `npcs_unresolved.json`:
    `why:` `repo:prototype/osfr-tools/tests/content_npcs.rs:471-472` (`resolved_reference_ids.len() == 295`, `unresolved_ids.len() == 170`); `npcs_unresolved.json` has about 5,241 lines, consistent with about 170 records.

11. `old:` Across the 651 quest records,
    `new:` Across the 655 quest records,
    `why:` `repo:prototype/osfr-tools/tests/content_npcs.rs:470` (`db.quests.len() == 655`) and `:474-475` (giver occurrences sum to 655).

12. `old:** Position known / unknown` table header is unaffected; no separate change. (Dropped; see Unsure.)

**Unsure:**
- The 403 resolved / 248 unresolved quest-giver split and the sub-table of remaining reference kinds (136 / 48 / 3 / 1 summing to 188) are not asserted in the tests. The 188 sub-table now conflicts with the 170 total, but I did not verify its rows.
- The per-page NPC row counts (1,199 at W27 versus 1,201 at tip) and the 104 null-zone rows were not recounted per page.
- `lab/content/startup-snapshot/startup.json` (23 AddNpc rows) is not present in the repo root (`lab` is not a directory in the repo listing), so I could not recheck it. The tip records have `capture_match: null` at record level (for example `blackspore_swamp.json:71`), so "None of its transforms was assigned to a regional NPC" still holds for the page records. `npc_spawns_extra.json` does copy capture transforms, but those are a separate file.
- The stated test commands use a path (`lab\build\W27`) that I could not check.
