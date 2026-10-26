# Next API passes (Bryce, 2026-10-26: "Do the enemy health from gameplay video first then do the other ones")

Budget: claude-api/budget-usd 336, about $304 spent; run the fleet with --cap 334. Jev is uncapped (OpenRouter).
Lesson (memory fleet-pack-joins): pre-join every candidate into the packs with a local resolver before paying.

1. **DONE 2026-10-26** (`quests/enemy_hp_video.py`, job hp-frame, 1,593 frames, about $1.2; evidence
   `references/quest-lines/enemy-hp-video.json`; builder brief `enemy-health-from-video-fit`). **Enemy health from gameplay video** (memory enemy-hp-from-video): per enemy and level, count the hits to defeat
   in the indexed gameplay video (`references/quest-lines/video.sqlite`, `quests/video_index.py`), cross-check the
   health-bar fraction and known hit damage (combat tables, balance-final-era memory). Pack per enemy: enemies.json
   / field_enemies.json rows (actor_kind_id, level, current max_health (R)), the video frames that name it, and the
   damage numbers and bars visible around them. Output: a cited health estimate per enemy and level; a builder brief
   then updates enemies.json (values stay tunable data, marked (R) where estimated).
2. **needs_spawn objects** (94 objectives, objective-specs-fixed.json): local resolver over the reference spawn
   tables by object or model name, then Haiku for the ambiguous ones.
3. **"No evidence yet" objectives** (244): Jev screens wiki, articles and video for each target and count; Haiku
   only on the promising ones.
4. **The 45 test files the audit left unresolved or unanswered** (`world_lines.py run --domain testaudit`, then hand
   them to T733).
