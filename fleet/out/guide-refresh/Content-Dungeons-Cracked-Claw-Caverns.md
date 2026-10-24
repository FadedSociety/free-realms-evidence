<!-- fleet job=guide-refresh id=Content-Dungeons-Cracked-Claw-Caverns status=done turns=16 usd=0.0146 tokens(read,write,in,out)=[369966, 41974, 34, 11363] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Cracked Claw Caverns.md

**Verdict:** current, with minor drift. The client quotes, achievement wording and point values, the Tavern Cellar cross-link, and the note's own line-98 citation (cited by `notes/Autopilot/T378.md:130`) all still hold at the tip. The one false item is a set of dead wiki links in the NPC line.

**Corrections:**

1. `old:` NPCs: [[Vasher]], [[Chloe]], [[Bullseye]], [[Petra]]. Zone: [[NPCs - Blackspore Swamp]].
   `new:` NPCs: Vasher, Chloe, Bullseye, Petra (each has a row in [[NPCs - Blackspore Swamp]]). Zone: [[NPCs - Blackspore Swamp]].
   `why:` No vault notes named Vasher, Chloe, Bullseye or Petra exist. The `notes/Build Guides/Content/NPCs/` folder holds only zone pages, and a heading search for `^# (Vasher|Chloe|Bullseye|Petra)$` finds nothing. These NPCs are rows inside `repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md` (Vasher at line 77, Bullseye at line 162). The zone page's own alias `NPCs - Blackspore` is the only link-target for this zone.

**Checked and holding (no change needed):**
- Achievements: Bronze 5 pts "Complete the Cracked Claw Caverns encounter." and silver 10 pts full-group match `repo:prototype/osfr-tools/data/content/achievements.json:3063-3064` and `:3927-3936`. Also matches `repo:prototype/osfr-tools/data/content/dungeons/cracked_claw_caverns.json:598`.
- Client text: the goal "Defeat the ancient cray, Cracked Claw!", the "Release the trapped spirits…" bonus, "Cracked Claw Caverns Bonus Objective", the "Vasher is located outside…" line, the Chloe "Head to Cracked Claw Caverns…" line and the Bullseye archer line all match the locale table, which is the `locale` tool's text table. The table's ids differ from the note's hash-style `loc` ids.
- Objective text on the "Complete the … encounter" achievement is the id `30439` that `repo:scripts/pieces/piece_059.py:45` and `repo:prototype/osfr-tools/tests/pieces/test_piece_059.py:132` use.
- Dungeon JSON `repo:prototype/osfr-tools/data/content/dungeons/cracked_claw_caverns.json` mirrors the note's rows (entrance, goals, boss, rewards).
- [[Tavern Cellar]] has the Wolf House spawner (`repo:notes/Build Guides/Content/Dungeons/Tavern Cellar.md:55`), and [[Briarheart Caverns]] exists as a note.

**Unsure:**
- The achievement is named "Group: Cracked Claw Carverns" (typo) in `repo:prototype/osfr-tools/data/content/achievements.json:3927` and `:10848`, while the locale and the note say "Caverns". The note is right about the client; the repo JSON name is the outlier. Not a note correction.
- The Rust roster `repo:prototype/osfr-tools/src/restoration/piece_059.rs` has no "Cracked Claw Caverns" row (only the Python script `scripts/pieces/piece_059.py` does). The note makes no roster or status claim, so I left it alone.
- I could not resolve the note's hash-style `loc` ids (e.g. `2805440117`, `2018071426`) through the locale tool, which only accepts its own row ids. I confirmed the text by search instead.
