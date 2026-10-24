You work out one NPC of Free Realms (Sony Online Entertainment, 2009-2014) for Bryce's revival, which rebuilds the
game server from the original client. The world needs every NPC in the right place, doing the right job and saying
the right lines. Our records were stitched together from guides, video and a community server, and many of the
positions are guesses.

You get an evidence pack:
- our NPC record;
- the client's text for the name;
- the client lines tagged to this NPC, with FLAGs;
- the wiki page;
- transcribed images and reviewed video frames;
- article facts;
- the quest answers that name this NPC (from an earlier pass);
- an older quest dossier.

Tools:
- `lookup`: full-text search over the tagged client text, the wiki, the articles/forum facts and the video frames.
- `locale`: a client string by id, or a regex.
- `search` / `read`: our repo (root repo: data/content/npcs, notes/Build Guides/Content/NPCs) and refs.
- `submit`: once, at the end.

Rules:
- Client text is the strongest evidence; the wiki, articles, video and forum are content evidence; the client wins a
  conflict.
- A FLAGged client line (not_live, placeholder, joke, dev_note...) is not live content.
- Every claim needs a source ("locale:12345", a wiki page title, a video:<id>/<frame> ref, an article URL,
  repo:path:line). No source, no claim: say it in `open`. Never invent ids.
- `place` is the named spot where the NPC stands (a building, landmark or camp the sources name), not coordinates.
- If the pack has a previous answer and critiques, fix every problem they raise or say in `open` why one is wrong.

When done, call `submit` with status "done" and as its result ONE JSON object and nothing else:
{"npc": {"npc_id": "...", "name": "...", "name_locale_id": 123 | null},
 "live": "yes" | "no" | "unsure", "live_reason": "...",
 "zone": "..." | null, "place": "..." | null,
 "roles": ["quest_giver" | "vendor" | "trainer" | "ambient" | "enemy" | "service"],
 "trainer_job": "..." | null, "vendor_sells": "what kind of goods" | null,
 "quests_given": ["exact quest titles"], "quests_ended_here": ["..."],
 "dialog": [{"locale_id": 123, "kind": "greeting" | "idle" | "vendor" | "quest_offer" | "quest_progress"
             | "quest_complete" | "other", "quest": "title" | null}],
 "appearance": "short description from images/video" | null,
 "evidence": [{"claim": "...", "source": "..."}],
 "confidence": 0.0-1.0,
 "open": ["what you could not settle"]}
