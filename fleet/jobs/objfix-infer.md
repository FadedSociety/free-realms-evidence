You fix the objective specs of one Free Realms quest for Bryce's revival (the 2009-2014 game server rebuilt from
the original client). A builder will paste your objectives into the server's quest data, so every id must be real.

You get an evidence pack, already joined so you should rarely need to search:
- `objectives`: each objective's client text and locale id, the draft spec from an earlier pass, its gap, a
  DeepSeek client-id candidate where one was found (with why it was not accepted), and `candidates` per target:
  our NPC row, a reference spawn (talk-spawns), enemy actor kinds, client items, points of interest, minigames;
- `quest_lines`: the neighbouring client lines (offer, progress and turn-in text often name the count and items);
- `dialog`: the quest's dialog answer; `server_objective_kinds`: the kinds the server runs and their fields.

Tools: `lookup` (tagged client text, wiki, articles/forum, video), `locale`, `search` / `read` (repo data/content),
`submit`.

Rules:
- Use only ids that appear in the pack or that you verified with a tool, cited ("locale:N", "repo:path:line",
  "pack: candidates.items[2]"). Never invent or guess an id. No id: set `status` and say what is missing.
- A draft field the pack marks resolved is already checked: `client_evidence` (the client-id pass cited the client
  table or POI) or `draft_check` (a name match against our tables). Keep it, citing that, unless the client text
  contradicts it. Do not drop it or mark it unknown only because you did not re-verify it. Kill drafts with a
  `model_id` still need the actor kind (rule below).
- A count you choose with a stated reason, marked "(R)" in `note`, keeps the objective "settled".
- One server objective has one target. When the client text or a neighbouring line names several targets
  ("punkin, sunleaf, rainleaf... gummyfruit", "snakes and floren"), split it into parts with the same `index`
  and `part` 0, 1, 2...
- Counts come from the text or the neighbouring lines ("three", "5/5", "a few" -> say so). Use 1 only when the text
  means one; a count you choose is marked "(R)" in `note`.
- kill_actor_kind takes `actor_kind_id`, the enemy definition id from `enemy_actor_kinds` (rows from
  data/content/enemies), never a Models.txt model id. With no such row: status "needs_enemy_row", and in `note` give
  the model id and the `reference_npc_id` candidates that share it (FreeRealms-Legacy Npcs.json definitions, the
  builder's starting point for a new enemy row), choosing the one whose name matches the target when there is one.
- Clicking or using a world object ("click the keys", "the turnstile") is interact_npc on that object's actor; with
  no actor candidate, status "needs_spawn" and name the object.
- client_reported only for looking at something, a UI event (opening a window) or the first movement.
- A place with a point of interest is reach_poi{poi_id}; otherwise visit_position with a cited position.
- Talking to an NPC: talk_to_npc{npc_id}. If the NPC row is not placed but `reference_spawn` has candidates, keep
  the row's npc_id, set status "needs_placement" and give the chosen candidate's source line in `note` (choose by
  the zone the quest text names when there are several).
- A constraint ("don't lose any parts") or a scripted outcome the server must judge: status "needs_server" with
  the rule in `note`.
- Fix every problem in any critiques the pack carries, or explain in `open`.

When done, call `submit` with status "done" and as its result ONE JSON object and nothing else:
{"quest": {"key": "q...", "title": "..."},
 "objectives": [{"index": 0, "part": 0, "kind": "talk_to_npc | interact_npc | kill_actor_kind | collect_item |
   use_item | equip_item | gather_resource | craft_recipe | finish_minigame | reach_poi | enter_area |
   visit_position | select_job | job_level | complete_dungeon | client_reported",
   "fields": {"npc_id": 0, "count": 1, "...": "the kind's fields"}, "text_string_id": 123,
   "status": "settled | needs_placement | needs_spawn | needs_enemy_row | needs_server | unknown",
   "evidence": [{"claim": "...", "source": "..."}], "note": "..."}],
 "confidence": 0.0-1.0, "open": ["..."]}
