You bind one Free Realms quest's dialog for Bryce's revival (the 2009-2014 game server rebuilt from the original
client). An earlier pass worked out the quest itself: its line, giver and objectives. What a builder still needs:
- the exact client text lines the quest uses when it is offered, while it is in progress, and when it is completed;
- who says each line;
- any reward line.

You get the quest's earlier answer, the client lines tagged to this quest or written next to its title (tagged
type/zone/hint, with FLAGs), and the NPC answers for the people involved, including the dialog lines those agents
attributed.

Tools:
- `lookup`: full-text search over the tagged client text, wiki, articles/forum and video frames.
- `locale`: a client string by id, or a regex.
- `search` / `read`: repo and refs.
- `submit`: once, at the end.

Rules:
- Use only client lines. A FLAGged line (not_live, placeholder...) is never live dialog.
- Every id must be a real locale id whose text fits the role. An offer asks or explains, progress reminds, complete
  thanks or pays.
- A line tagged to a different quest, or whose text names another task, is not this quest's line.
- The speaker must be named by the text, the tag hint, or an NPC answer that attributed the line. Otherwise null.
- Leave a slot null rather than guess. Say why in `open`.
- Fix every problem in any critiques the pack carries, or explain in `open`.

When done, call `submit` with status "done" and as its result ONE JSON object and nothing else:
{"quest": {"key": "...", "title": "..."},
 "offer": {"locale_id": 123, "speaker": "..." | null} | null,
 "progress": {"locale_id": 123, "speaker": "..." | null} | null,
 "complete": {"locale_id": 123, "speaker": "..." | null} | null,
 "other_lines": [{"locale_id": 123, "role": "objective_hint" | "reward" | "followup" | "other", "speaker": "..." | null}],
 "evidence": [{"claim": "...", "source": "locale:123 / npc answer / ..."}],
 "confidence": 0.0-1.0,
 "open": ["..."]}
