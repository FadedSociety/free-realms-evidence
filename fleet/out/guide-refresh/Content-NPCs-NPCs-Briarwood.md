<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Briarwood status=done turns=19 usd=0.0216 tokens(read,write,in,out)=[714406, 63994, 40, 12868] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Briarwood.md

**Verdict:** minor drift. The note is almost entirely client-sourced NPC content with few claims about our code. One claim about the repo's own NPC index is stale. Every checked client quote and every repo-facing link or citation holds at the tip.

**Corrections:**

1. `old:` - **Sunstone Valley** is not covered here; it has its own placeholder in NPCs.md.
   `new:` - **Sunstone Valley** is not covered here; it has its own page, [[NPCs - Sunstone Valley]], which the NPCs index lists as written.
   `why:` repo:notes/Build Guides/Content/NPCs/NPCs.md:22 reads "| Sunstone Valley | [[NPCs - Sunstone Valley]] | Written (69 rows, 81 NPCs, ...) |". The file repo:notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md exists. No placeholder remains in the index.

**Checked and holding (no change):**
- Greeting test citations into this note: `tests/npc_greetings_seaside_briarwood.rs` (BRIARWOOD_GUIDE, lines 254-313) cites guide lines 32, 60, 61, 79, 100 and 101. Each still carries its hash or the self-identifying Reginald line (repo:notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:32, 60, 61, 79, 100, 101). The Briarwood rows for Freidi, Babbina, Tara, Corflugg, Blari and Reginald match.
- Every job, dungeon and Adventurer link target exists (repo:notes/Build Guides/Content/Jobs/, .../Dungeons/). The Adventurer page has the Part F Briarheart Palace quests (repo:notes/Build Guides/Content/Jobs/Adventurer.md:147-156).
- Client quotes checked in the locale table: "Head into eastern Briarwood to find Lila Darklure" (409172), "Pass the three challenges within Tanglewood Fort" (91175), Sperry's hut lines (45252, 101831), "Speak to Freidi near the Hedge Maze entrance" (90742), Lazi's farm (16541, 46540), and the Thistlerow sub-region name in Bubaba's barrel lines (16463, 24901).

**Unsure:**
- The Slothi/Lazi row says Lazi's farm is "in Bristlewood to the north of Slothi" (client 825261180). The client also has Slothi saying "He lives at a farm in Thistlerow to the north" (locale 16568). The note does not list this in its Conflicts section. It is a possible unlisted conflict, not a false claim.
- Many cited client numbers (for example 299257046, 114883143, 2724454277, 1265014476) do not resolve as locale ids. The `locale` tool found the quoted text by wording, so I could not confirm the id-to-text links. I did not change them.
- The NPC counts (for example "about 128 rows" in NPCs.md:16) are index claims, not claims made by this note. I did not check them.
