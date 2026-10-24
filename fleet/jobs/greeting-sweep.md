You look for ONE non-player character's greeting in a Free Realms revival. The original game shipped every line
of dialogue in the client's text table (the `locale` tool), but which character says which line was decided by the
old server, and that table is lost. So a line may be bound to a character only when outside evidence PROVES that
character speaks it. You can only read; you change nothing.

## Sources (tools)

- `locale`: the client's English strings by id or regex. Candidates are first-person lines that fit the
  character's role, place and quests.
- `search` / `read` over `repo`: `notes/Build Guides/Content/NPCs/NPCs - <Zone>.md` (rows quoting what NPCs say,
  cited like M45), job guides `notes/Build Guides/Content/Jobs/<Job>.md`, `notes/Research/NPC Greetings*.md` (how
  earlier greetings were proven), quest content `prototype/osfr-tools/data/content/quests/*.json` (a quest's intro
  text id belongs to its giver), the NPC files `prototype/osfr-tools/data/content/npcs/*.json`.
- `search` / `read` over `refs`: cached wiki pages `freerealms-wiki/raw/*.json` and the community servers.

## Proof (one is enough; a line that only sits near the name in the file is NOT proof)

1. A guide, research note or wiki page quotes the line and attributes it to this character.
2. The line names its speaker as this character ("The name's Reed Stillwater").
3. The line is the intro text of a quest whose giver is this character (quest data or a guide row).

Never bind a line another character already uses as its greeting (check the NPC files for that string id).

## Result (call `submit` once)

`status`: `done` when you found a proven line, `nothing_found` when you did not (this is a normal outcome, report
what you checked). `result`, in Markdown:

- **NPC:** npc_id, name, zone.
- **Greeting:** `locale <id>`: "the exact text" (copy it from the `locale` tool).
- **Proof:** which rule (1/2/3) and the evidence with path:line (or wiki file), quoting the attributing words.
- **Checked and rejected:** other candidates and why they are not proven.

Prefer 6-15 tool calls. Never invent ids or quotes.
