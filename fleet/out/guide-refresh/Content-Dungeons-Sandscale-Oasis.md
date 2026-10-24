<!-- fleet job=guide-refresh id=Content-Dungeons-Sandscale-Oasis status=done turns=18 usd=0.0217 tokens(read,write,in,out)=[720008, 72545, 38, 10890] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Sandscale Oasis.md

**Verdict:** current, with one minor false negative. The note makes few claims about our code. Its status claims (no "Sandscale Oasis Bonus Objective" string, no "Complete the Sandscale Oasis encounter" achievement, Sandscale Oasis absent from the objective-locale block) agree with the repo's own records: `tests/pieces/test_piece_059.py:137` (`objective_locale` None), `scripts/pieces/piece_059.py:64,108`, and `notes/Build Guides/Content/Dungeons/Dungeons.md:57,168`. Its client quotes and locale strings (quest text, boss abilities, dev strings, Sandscale NPC names, the "Defeat Cactus Bandits" pair) match the client locale table.

**Corrections:**

1. `old:` No level-3 string exists in the client.
   `new:` No dungeon-entry level-3 string exists in the client. Level 3 appears only in item-wearability text ("Wearable by a level 3 or higher Archer.") and mining text ("at least a level 3 Miner to mine Iron").
   `why:` Client locale rows 42431 and 42461 ("Wearable by a level 3 or higher ...") and 71461 ("you need to be at least a level 3 Miner"). The note's blanket negative is false as written, and it is the basis for the "None" requirement.

**Unsure:**

- The hashed `loc` ids the note cites (e.g. 3894478291, 1685846669, 2403828476, 295992266, 1281695675, 1165566846) do not resolve in the `locale` tool, which takes row numbers. The strings they label do exist under other row numbers (e.g. "Sandscale Oasis" at row 8794, "Defeat Sandscale Scavengers" at 439804). I could not confirm the id mapping.
- The video-based claims (bonus counter 0/10 to 4/10, "Cactus John" misread, Archer 13 play, entrance marker distances) were not checked. They are not code claims, and the video frames are outside the tools I can query.
- The wiki-sourced claims (210 Stars, 35 Coins, "recommended levels 3 and higher", "Every other difficulty 2 page has a wheel") were not checked. The locale search for the "recommended levels 3" wording returned nothing, which is consistent with a wiki source.
- "Atlas icon exists" and the "Stars/Coins" figures were not checked.
- The repo's `data/content/dungeons/sandscale_oasis.json` and `enemies_unresolved.json` cite this note's section headings (Overview > Entrance, Requirements > Combat job level, Enemies and boss > Boss, Rewards > Prize wheel by job > Wizard). All of those headings still exist, so no citation has moved.
