<!-- fleet job=guide-refresh id=Content-Dungeons-Forgotten-Caves status=nothing_found turns=20 usd=0.0197 tokens(read,write,in,out)=[667033, 56650, 42, 11816] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Forgotten Caves.md

**Verdict:** current. I found no claim that is false at the tip. The note is almost entirely client-locale and wiki text, and the parts I could check against our code and data agree with it.

**Corrections:** none.

**Checked and holding:**
- Client text, matched by wording. The locale tool did not resolve the numeric `loc` ids the note cites (for example `669488071`, `2145075890`), so I matched the quoted text instead. These all exist: "Forgotten Caves" (5703), "Archmage Petulia foolishly ventured…" (16114), "Requires a level 5 combat job" (4199), "You must have a combat job of at least level 5…" (4189), "Defeat Amoranth" / "Defeat Amoranth." (416980, 16355), "Enter the Forgotten Caves and defeat Amoranth." (416979), "Bonus: 80 Coins!" (426602), "Battles in the Forgotten Caves grant bonus rewards!" (424997), "Forgotten Caves Bonus Objective" (140170), "Do not allow Petulia to be knocked out." (400096), "If petulia is knocked out, she will be unable to finish her quest." (400098), "Changeling Berserkers are among the strongest…" (40156), "Changeling Arcanus" (16181), "Changeling Marauder" (15996), "Changeling Ninja" (427035), and "Petunia" in the Archmage line (388672). The Petunia dog NPC also exists (11495). The "Forgotten Caverns" (416984) and "Changeling Caverns" ability names (40565, 40567) are present.
- Achievements: `repo:prototype/osfr-tools/data/content/achievements.json:3420-3432` gives Bronze 5 points for "Complete the Forgotten Caves encounter." and `:4284-4296` gives Silver 10 points for the full-group version. Both match the note.
- Prize wheel item names: all 18 item names I spot-checked are in the locale (for example "Archer's Composite Bow of Volleys", "Ninja's Scythe of Dragonstrike", "Scholar Wizard Fez"), so the note's "every item name was found" claim holds for those.
- Dungeon data: `repo:prototype/osfr-tools/data/content/dungeons/forgotten_caves.json` has difficulty 3, combat-job level 5, zone "Sanctuary (Memorial Caverns)", and members_only false. It also records `goals: []` and `rewards: []`, with the goal detail kept in the note. This matches the note's Gaps section, and the note makes no claim about the code's playability.
- Build Ledger, `repo:notes/Design/Build Ledger.md:78`: "None are playable" is a repo status, not a claim in this note.

**Unsure:**
- Video citations `g6mBk_gSfu4/00004`, `00008` and `zIwAzf-mdqY/00308` (Overview "In video" row). `g6mBk_gSfu4` appears nowhere in refs or the repo outside this note, so I could not verify the markers or the distances.
- Wiki facts with no client or repo counterpart: the page revision date 2025-09-07, the "Difficulty-3 rule" for level 5, the 151-coin members bonus, "210 Stars or less", and the wiki's "Changeling Arcarus" spelling. The refs roots hold no copy of the wiki page for this dungeon, so I could not check these.
- Exact tie between the wiki's "Bonus: Escort Archmage Petulia." line and the client. The note already flags this as unconfirmed, and I found no client string that contains both parts.
