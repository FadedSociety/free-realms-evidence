# Quest lines (client text index, flags, inferred quests)

Built 2026-10-23 by the lead with the Haiku fleet and Jev. Inputs: the client locale (85,932 strings), our 660 quest
records, NPC records, the wiki harvest, the archived articles and forum, the earlier per-NPC quest dossiers. Content
evidence only: every answer cites its sources, client text wins, and "live: unsure" means exactly that.

| File | What |
|---|---|
| `index.sqlite` | `strings`: every client line tagged by Haiku (type, zone, hint = the quest or NPC it belongs to, flag); `jev`: Jev's independent tags; FTS5 `strings_fts` |
| `flags.tsv` / `flags.json` | 17,748 lines that are probably NOT live content (cut "NOT LIVE" quests, test/sample text, dev notes, jokes, fragments), quest-typed lines first; `by` says whether Haiku, Jev or both flagged it (10,172 both) |
| `disagreements.tsv` | 6,956 quest-typed lines Haiku and Jev tag differently (often genuinely ambiguous) |
| `packs.json` | the evidence pack each quest agent got (912: 660 records + 252 wiki-only quests) |
| `quests.json` | per quest: status (final / unresolved), the answer (line previous/next, giver, zone, objectives with locale ids, dialog ids, rewards, evidence, open questions), last critiques |
| `quest_lines.json` | lines assembled from final answers' previous/next links (272; 77 with 3+ quests) |

## How it was made

1. `fleet.py locale-tag` (Haiku, $2.59) then `quests/locale_index.py ingest`; `locale_index.py jev` (Jev, $2.49);
   `locale_index.py flags`.
2. `quests/quest_lines.py prepare` then `run`: one Haiku agent per quest (`fleet/jobs/quest-infer.md`, tools
   lookup/locale/search/read); critics rotate lenses evidence -> lines (`fleet/jobs/quest-critic.md`); a failed answer
   is redone by a fresh agent with the critique, the chain conflicts with other quests and a model-free id check; a
   quest is final when its current answer passes both lenses. 12 rounds, about $42.
3. Rounds 1-6 required "a builder could wire it"; rounds 7-12 passed answers that are true as far as they go
   (honest unknowns in `open`) and record `wireable` separately, so early finals carry no wireable rating.

Result: 755 of 912 final (462 live, 277 unsure, 10 not live), 153 unresolved with their last critiques, 4 unanswered.

## The other passes (2026-10-23/24)

Each pass produced one record per row, plus its last critiques. Every answer cites its sources; "final" means TRUE as
far as it goes, and `wireable` says whether a builder can use it now.

| File | Unit | Final | Wireable | How it ran | Notes |
|---|---|---|---|---|---|
| `npcs.json` | NPC record (1,173; pure enemies excluded) | 975 | 542 | API fleet, `world_lines.py --domain npc`, 8 rounds | zone, place, roles, quests given, own dialog |
| `dialogs.json` | quest (897 answered, not dead) | 854 | 440 | API, `--domain dialog` | offer/progress/complete line ids + speakers; 402 with offer and complete |
| `lines.json` | cluster of still-unbound dialog lines (2,962) | 2,754 | 1,114 | API, `--domain line` | 9,644 lines get a speaker and stage; 3,376 named NPC, 183 player replies |
| `enemies.json` | enemy name (312) | 264 | 27 | Claude subscription Haiku workflows, `collect_workflows.py` | zones and places, bosses, quests that target it; health, levels and drops are mostly unknown (R) |
| `event-state.json` | live event (513, from article facts) | 396 | 206 | subscription workflows, then API (`resume_from_workflows.py` + `--domain event`) | dates by year, recurrence, items, quests, activities |
| `items.json` | wiki item article (2,216) | 2,007 | 1,225 | API, `--domain item` | sources: Marketplace 732, prize wheel 417, Coin Shop 329, vendor 231, membership 146, event 144, promotion 89, quest 44, drop 39 |

The packs are in `<domain>-packs.json`, and the agents' tool is `fleet.py lookup` (client, wiki, articles, video).
Video frames are indexed in `video.sqlite` (`quests/video_index.py`). Subscription agents used the same tools through
`quests/quest_cli.py`. Total API spend for all passes, harvest included: about $169.
