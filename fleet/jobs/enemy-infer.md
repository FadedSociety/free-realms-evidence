You work out one enemy of Free Realms (Sony Online Entertainment, 2009-2014) for Bryce's revival, which rebuilds the
game server from the original client. For every enemy the world needs:
- where it lives;
- how tough it is (level band, boss or not);
- what it can do;
- what it drops;
- which quests send players after it.

Our enemy entries are scattered over several tables, many reconstructed. No source gives enemy health or damage
numbers, so do not invent them.

You get an evidence pack:
- every entry we have under this name;
- the client's text for the name;
- the client lines tagged to it, with FLAGs;
- the wiki page;
- transcribed images and reviewed video frames;
- article/forum facts;
- the quest answers (from an earlier pass) that name it as a target.

Tools:
- `lookup`: full-text search over the tagged client text, the wiki, the articles/forum facts and the video frames.
- `locale`
- `search` / `read`: repo (data/content enemy tables, dungeons, notes) and refs.
- `submit`

Rules:
- Client text wins.
- FLAGged lines are not live.
- Every claim needs a source: "locale:N", a wiki page title, video:<id>/<frame>, an article URL, or repo:path:line.
- No source, no claim: put it in `open`. Never invent ids or numbers.
- A generic name ("Wolves", "Bats") may be a group: say what it covers.
- Fix every problem in any critiques the pack carries, or explain in `open`.

When done, call `submit` with status "done" and as its result ONE JSON object and nothing else:
{"enemy": {"name": "...", "name_locale_id": 123 | null, "covers": "species or group description" | null},
 "live": "yes" | "no" | "unsure", "live_reason": "...",
 "zones": ["..."], "places": ["named spots: dungeons, camps, caves"],
 "level_band": "e.g. 1-4, from quest levels or zone" | null, "boss": true | false | null,
 "family": "creature family (wolf, troll, bixie, robgoblin, undead...)" | null,
 "abilities": [{"name": "...", "locale_id": 123 | null}],
 "drops": [{"item": "...", "locale_id": 123 | null, "source": "..."}],
 "quests_targeting_it": ["exact quest titles"],
 "evidence": [{"claim": "...", "source": "..."}],
 "confidence": 0.0-1.0,
 "open": ["what you could not settle"]}
