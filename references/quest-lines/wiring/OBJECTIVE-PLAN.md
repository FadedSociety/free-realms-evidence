# Objective completion plan (lead, 2026-10-25)

Goal: every live quest the evidence supports gets objectives the server can run (`talk_to_npc`, `visit_position`,
`defeat`, `gather_resource`, `craft_recipe`, `complete_dungeon`, `finish_minigame`, `job_level`, `client_reported`),
so the zone briefs enable quests by pasting checked specs instead of rebuilding them one by one.

## Where it stands

- `objective-specs.json` drafts the 1,260 objectives of the 603 final quests with client ids. 185 quests resolve
  completely. Resolved per kind: job_level 45/45, talk_to_npc 322/476, finish_minigame 75/155, gather_resource 58/135,
  defeat 41/108, visit_position 36/156, craft_recipe 15/35, client_reported 0/107.
- The drafts are good but not final: a spot check found "defeat the snakes and floren" folded into one enemy with count 1.
- The data/content quest files ship only 142 runnable objectives across 664 records. That gap is why most quests are disabled.

## Steps, in order

1. **Client ids with IDA (DeepSeek, about $60 of DeepSeek credit on hand).**
   - `client-ids/worklist-*.json` holds 12 lists, written by `quests/client_id_worklists.py`. Each worker writes `client-ids/result-<list>.json`, with an IDA address or file:line for every id.

     | List | Objectives | What each worker finds |
     |---|---|---|
     | trigger | 107 | what the client sends for `client_reported` objectives, and the client_id rule |
     | minigame | 80 | MiniGameData.txt and MiniGameGroupData.txt ids |
     | model | 67 | enemy model ids (Models.txt), split per enemy type, with counts |
     | item | 77 | item definition ids and quantities; flags objectives that are really deliveries |
     | place | 120 | zone and position from the extracted FabledRealmsAreas.xml, map and POI data, or an NPC's camp |

   - The lead reviews samples of every result file before merging. A worker's summary is not evidence.
   - **Interim, 2026-10-25 02:05Z (9 of 12 lists in):**
     - `quests/client_ids.py` checks every row against the client tables (MiniGameData.txt, Models.txt, the item catalogue, the server's ClientTrigger shapes). It rejects low confidence, multi-target rows and positions that are our own reconstructed NPC offsets.
     - `objective_specs.py resolve` applies the accepted rows as an overlay. Rejected rows stay on the spec as `candidate` with the reason.
     - Every id found so far exists in its table. 8 positions were rejected as reconstructed offsets.
     - Complete quests: 185 → 251. finish_minigame 142/155, visit_position 72/156, gather_resource 75/135, defeat 56/108.
     - Spot checks: the MiniGameData rows, item ids and POI positions are all confirmed. One known miss: "restock Fizzlesticks' potion shop" is four items (the turn-in line 74841 names punkin, sunleaf, rainleaf, gummyfruit), but the worker gave one. So the fix pass gets each quest's neighbouring locale lines (offer, progress, turn-in) pre-joined.
   - **Final, 2026-10-25 12:40Z (all 12 lists):**
     - Accepted: minigame 67, model 38, place 74, item 17, trigger 1.
     - Rejected: 211 not found, 21 low confidence, 13 multi-target, 9 reconstructed offsets.
     - Complete quests: 185 → **279**. Resolved per kind: defeat 79/108, visit_position 110/156, finish_minigame 142/155, gather_resource 75/135.
     - Samples: the high and medium model ids name the right enemy, and the bad guesses were all low (rejected). Counts still default to 1 on plural targets ("Shadow Talon Apprentices"), which the fix pass corrects from the neighbouring lines.
     - Server check, done: `defeat` maps to `KillActorKind{actor_kind_id}`. That is the enemy definition id, **not** the model id (Hooligan Wolf: actor_kind 3156, model 3284; `enemies.rs`). The specs' `model_id` values must be translated through `enemies.json`, or become new enemy rows from the reference Npcs.json definition that shares the model.
     - The 107 trigger rows turn out to be: clicking a world object 73, server-side state 18, minigame or script outcome 11, item use 1, UI event 1, settled trigger 1, other 2. A click maps to `interact_npc` on the object's actor, so the fix pass needs object spawns in its pack.
   - **client_reported is mostly mislabelled (trigger lists).**
     - The client reports only four things: 45/6 look-at, 45/10 UI event (seven Lua `Ui.OnObjectiveEvent` names), 45/11 first movement, and 45/12 housing-fixture move. 45/12 is not in our ClientTrigger yet.
     - The `client_id` comes from the server's own registration packet, so there is nothing to recover. Any unused id works, (R).
     - Most of these objectives are server-judged instead: item use, clicking a world object, a scripted or minigame outcome, a state constraint ("don't lose any parts"). The fix pass reclassifies them.
     - The server already has the kinds these need, which the drafts' 9-kind schema left out (`quest_engine.rs` ObjectiveKind):
       - `use_item{item_id}`, `interact_npc{npc_id}` (clickable actors), `collect_item{item_id}`, `equip_item{definition_id}`, `select_job{profile_id}`;
       - `reach_poi{poi_id}` and `enter_area{area_id}`. Many place results cite a PointOfInterests id, so `reach_poi` beats a raw position where a POI exists.
     - The fix pass gets the full kind list. A builder brief is needed only for 45/12 and for a kind nothing covers.
2. **Local resolvers (free).**
   - NPC placement, done 2026-10-25: `quests/talk_spawns.py` writes `wiring/talk-spawns.json`.
     - The 614 unplaced NPC rows (poi_anchor, unanchored) are matched to the FreeRealms-Legacy and Sanctuary-main `FabledRealms.lua` spawns. A match is by the spawn's Npcs.json NameId text, or by a character model file that names the NPC.
     - The old join matched only our row's name_string_id, so it missed rows that carry other locale tables.
     - 213 rows now have spawn candidates, 181 of them at one location. Each candidate cites file:line and records the zone of the nearest NPC we already draw (`near_zone`), because about a third disagree with the row's own zone, mostly sub-region names.
     - Talk objectives: 74 of 154 get a placeable target (60 unique, 14 to choose); 80 stay open. Group targets ("residents of Sanctuary") and NPCs whose spawn has no NameId stay with the fix pass.
     - Placing them completes 35 more quests (185 → 220).
     - The placements go into the round-3 zone briefs, per zone file, so they do not collide with the round-1 builders editing `npcs/*.json`. Positions are legacy data, (R).
   - Merge the DeepSeek results into `objective-specs.json`, re-run the resolvers, and recount the complete quests.
3. **Haiku fix pass (API, an estimated $4–8 of the about $16 left; the fleet cap stops it at $302).**
   - One agent per quest, with the evidence pre-joined, so no exploring is needed:
     - each objective's client text and the quest's text cluster;
     - the draft spec;
     - candidate ids: NPC rows, model ids, item ids, minigame ids, positions.
   - Each agent returns a corrected spec: it splits multi-target objectives, fixes counts and kinds, chooses among candidates, and names what is still unknown.
   - One critic round runs on the changed specs.
   - **Running since 2026-10-25 13:05Z:** `world_lines.py run --domain objfix --rounds 3 --cap 306`. Inputs:
     - packs from `quests/objfix.py` (`objfix-packs.json`, 324 incomplete quests);
     - prompts `jobs/objfix-infer.md` and `jobs/objfix-critic.md`.
   - Pilot: 4 quests for $0.025, 2 final. Answers split multi-target kills and choose reference spawns. They keep honest statuses: needs_enemy_row, needs_placement, needs_spawn, needs_server. Output: `objfixs.json`.
   - **Result, 2026-10-25 (fix pass $3.48 + check pass $3.01 + redo $0.48; API total $300.48 of $310):**
     - `quests/apply_objfix.py` writes `objective-specs-fixed.json`, the builders' input:
       - it takes the critic-passed answers (`objfixs.json` for incomplete drafts, `objchecks.json` for complete ones);
       - it checks every id against our tables and downgrades an id that is not there (16 invented or stale NPC ids);
       - it restores a draft minigame or item id the fixer withdrew only for want of a citation, when the id's client name matches the target (39 objectives).
     - **109 quests are wireable now** (97 checked; 12 drafts the check could not settle) and **219 after the talk-spawns placements**.
     - The checks showed the "complete" drafts were not all wireable. Kill targets were model ids, counts were unknown and some item ids were loose name matches, so the honest count fell from 279 to 109.
     - Blocking objectives, each with its reason in `note`:

       | Status | Objectives |
       |---|---|
       | unknown (no evidence) | 244 |
       | needs_server (a rule the server must judge) | 138 |
       | needs_spawn (a clickable object or NPC to spawn) | 94 |
       | needs_enemy_row (the reference Npcs.json definition is named) | 66 |
       | needs_npc_row | 19 |
       | needs_placement (talk-spawns) | 268 |

     - Next briefs, one data brief each, for the DeepSeek builders: placements (talk-spawns, per zone file), enemy rows (66), object spawns (94).
4. **Rebuild `objective-specs.json`** from the fixed specs and point the zone briefs at it (round 1 T660-T667 and T500-T502, round 2, and a round 3 for quests newly complete).
5. **Builders wire the quests:** quest record, giver, objectives, dialog ids and rewards (cited, or the job ladder (R)), with menu-path tests.
6. **Native checks,** zone by zone, of the enabled quests in the real client.

## Rules

- Client evidence beats every inferred answer.
- Nothing from `lab/` is copied into the repo as text; only ids, numbers and positions with their citations.
- Lesson from 2026-10-24: join known data into every pack before paying for model passes (memory: fleet-pack-joins).
