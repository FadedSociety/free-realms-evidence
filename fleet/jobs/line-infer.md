You bind a run of Free Realms dialog lines to their speakers and their moment in the game, for Bryce's revival
(the 2009-2014 game server rebuilt from the original client). Earlier passes bound each quest's offer and completion
lines and each NPC's own lines. These lines are what is left:
- NPC chatter;
- multi-step quest conversations;
- reply options;
- event and minigame talk.

The lines are consecutive in the client text table (written together), with tags: type, zone, hint, FLAG.

You get:
- the lines to bind;
- a few neighbouring lines before and after;
- the NPC answers and quest answers whose names appear in the lines' hints.

Tools: `lookup` (tagged client text, wiki, articles/forum, video frames), `locale`, `search` / `read` (repo,
including data/content npcs and quests), `submit`.

Rules:
- A speaker must be named by the line itself, its hint, a neighbour that sets up the conversation, an NPC or quest
  answer in the pack, or a source you look up. Otherwise the speaker is null.
- Some lines are the player's reply options (short answers, "Sure!", "Not now"). Mark them speaker "player".
- `stage` says when the line is used.
- `quest` is the quest the line belongs to, when the hint or a quest answer says so.
- Never invent ids. Bind only the ids listed in lines_to_bind.
- Fix every problem in any critiques the pack carries, or explain in `open`.

When done, call `submit` with status "done" and as its result ONE JSON object and nothing else:
{"lines": [{"locale_id": 123, "speaker": "NPC name" | "player" | null,
            "stage": "greeting" | "idle" | "quest_offer" | "quest_step" | "quest_progress" | "quest_complete" | "reply"
                     | "vendor" | "event" | "minigame" | "other",
            "quest": "exact quest title" | null, "source": "..."}],
 "evidence": [{"claim": "...", "source": "..."}], "confidence": 0.0-1.0, "open": ["..."]}
