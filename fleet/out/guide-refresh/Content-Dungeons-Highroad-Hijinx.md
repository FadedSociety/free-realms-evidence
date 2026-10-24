<!-- fleet job=guide-refresh id=Content-Dungeons-Highroad-Hijinx status=done turns=12 usd=0.0148 tokens(read,write,in,out)=[275017, 47566, 26, 12121] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Highroad Hijinx.md

**Verdict:** minor drift. The note is almost entirely client-locale and wiki sourcing, and nearly every quoted string and id I spot-checked matches the locale. Two claims are false as written. The note makes no build-status claim about our server, so there is no "built / not routed" statement to correct.

**Corrections:**

1. `old:` No standalone "Mac" name string was isolated in the locale.
   `new:` The locale holds standalone "Mac" name entries (`Mac` at locale lines 15368, 5100344 and 5100362), plus the line "Mac is the leader of these Hooligans that have been stirring up so much trouble." (line 15238). The NPC pages cite Mac's name ids (`ucdt` 652126593 and others) in [[NPCs - Wilds]] and [[NPCs - Cobblestone Village]].
   `why:` Locale search for `^Mac$` returns exact "Mac" entries at 15368, 5100344 and 5100362. Line 15238 is the Mac description line. The notes `Content/NPCs/NPCs - Wilds.md:217` and `NPCs - Cobblestone Village.md:77` already cite the Mac name ids.

2. `old:** None (difficulty 2: "recommended levels 3 and higher, but can be entered by anyone"). No level-3 string exists in the client. | [wiki: Dungeons] [client] |`
   Use this cell-level replacement. The `old` text is the phrase `No level-3 string exists in the client.`
   `new:` No dungeon recommended-level string for level 3 exists in the client. The client's only "level 3" strings are gear-wearability text, such as "Wearable by a level 3 or higher Archer." (locale 42431, 48423).
   `why:` Locale search for "level 3 or higher" returns many item-tooltip strings (42431–42584, 48423, 71974–71978). The recommended-level line is wiki-only. The old sentence is literally false and invites a search that will hit gear text.

**Unsure:**

- The "Collin" mini-boss identity (Overview and Conflicts 2) is a judgement the note already flags as uncertain. I could not find a client string that ties Collin to the dungeon's mini-boss role. The locale has "Collin" (5100267), "Oy! What did you chumps do to Collin?" (38431) and "NPX 4.0 NewbieZone Collin Character Flag AOE Grant" (5100334), which is consistent with the note.
- Locale ids in the note (`loc 2605610771` and similar) are hashes. The locale tool takes line numbers, so I could confirm texts by content only, not by id. Every quoted text I checked matched the locale content: the panel descriptions, Defeat Mac!, the Kazuo, Henry, Vicki, Maple, Dolly and radio quests, the win, group and bonus-objective strings, and the weapon-rack strings.
- Prize-wheel items: all 30 item names I checked exist in the locale (Archer, Medic, Wizard and Warrior rows). The wheel contents themselves are wiki-sourced and I did not verify them.
- Stars cap (118), the 26 and 49 Coin rewards, the 4 weapon racks and the members-only coin bonus are wiki-only. Nothing in the repo or client settles them.
- Repo context, not a correction: `data/content/dungeons/highroad_hijinx.json` (main encounter `goals: []`, `rewards: []`) and `dungeons_unresolved.json` (owner `highroad_hijinx`) carry this note's facts, but the dungeon's goals and rewards are not wired into our server data. The note does not claim otherwise. Its citations at `Highroad Hijinx.md:19,48` (cited by `data/content/field_enemies.json:69,734`) still point at the story-hook and enemy lines.
