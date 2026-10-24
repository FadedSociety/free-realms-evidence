<!-- fleet job=guide-refresh id=Content-Dungeons-Cursed-Graveyard status=done turns=15 usd=0.0195 tokens(read,write,in,out)=[521121, 58511, 32, 13981] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Cursed Graveyard.md

**Verdict:** minor drift. The note's client, locale and quest citations hold up, and the zone, wheel and goal claims match the vault's own index. Two sentences are false.

**Corrections:**

1. Overview, "Panel description" row.
   - `old:` No locale id was found for it.
   - `new:` The client locale has the text too (locale row 115823, next to the name string at 115822; the hash id was not recovered).
   - `why:` The locale lookup returns `115823: Something sinister is moving about this graveyard. Venture in and defeat the ominous presence!`, next to `115822: Cursed Graveyard!`. The search was for the exact text, so the "no locale id" claim is wrong. The hash id is still unknown, so the replacement says so.

2. Conflicts, item 3 (Achievements).
   - `old:` The other difficulty 1 dungeons all have them.
   - `new:` Hewey's Escape, also difficulty 1, has none either.
   - `why:` `repo:notes/Build Guides/Content/Dungeons/Dungeons.md:72` lists Hewey's Escape at difficulty 1 with no achievement, and `Dungeons.md:168` names Hewey's Escape among the entries with no encounter trophies. The "all have them" claim is false.

**Unsure:**

- **Dangling links.** `[[Caitlyn Gravefog]]` and `[[Graveyard Wraith]]` (Related quests and NPCs section) have no page. `repo:notes/Build Guides/Content/NPCs/` has no Caitlyn or Wraith file. Both NPCs are covered only as rows in `NPCs - Stillwater Crossing.md` (lines 44 and 90). Retarget the links there, or create the pages. I did not edit them.
- **Locale id scheme.** The `locale` tool returns sequential ids (for example 115822), and it rejects the hashed ids the note cites (`275385206: (no such id)`). I confirmed the text of most cited strings (name, win text, goal, quest texts, item names, "Wraith Scream", "Saved by the Bell Brawler Gloves") but could not confirm the id numbers themselves.
- **"Unlocking quest: None" (Requirements).** `repo:notes/Build Guides/Content/Jobs/Brawler.md:111` says the S1 quest "Unlocks the job," and the note's own quest table calls that quest the "Main Brawler task." The note's row is about dungeon access, so I left it. A reader could take "None" to mean the quest chain is not required. Consider rewording.
- **Not checked.** Video frames, the wiki's star and coin figures, and the Atlas icon were out of reach from the repo and client.
