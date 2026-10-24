<!-- fleet job=guide-refresh id=Content-Dungeons-Darvon-s-Descent status=nothing_found turns=22 usd=0.0220 tokens(read,write,in,out)=[713908, 59306, 46, 14910] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Darvon's Descent.md

**Verdict:** current. I found no claim that is false at the tip, and no citation that has moved.

**Checked and holding:**
- **Code and data.** `repo:prototype/osfr-tools/src/restoration/piece_059.rs:166` has `row(29, "Darvon's Descent", 4, false, Some(30462), None, None, E("barrier", Some("Memorial Caverns"), "Sanctuary", ...))`. That matches the note's difficulty 4, members-only No, the barrier entrance in Memorial Caverns, Sanctuary, and the zone.
- **Entry requirement.** `repo:prototype/osfr-tools/data/content/dungeons/darvon_s_descent.json` sets `minimum_combat_job_level` to 9 and `members_only` to false, and gives the name id 96595886.
- **Achievements.** `repo:prototype/osfr-tools/data/content/achievements.json:3612-3622` is the Bronze 5-point trophy "Complete the Darvon's Descent encounter." `:4476-4488` is the Silver 10-point "...with a full group." Both match the Rewards section.
- **Prize wheels.** The item names in the note match `repo:prototype/osfr-tools/data/content/dungeons_unresolved.json:6961+` and the locale. This includes "Ninja's Necklace of Vitality IV" (locale 131132). The wiki's "Neckace" misspelling is at `refs:freerealms-wiki/wikitext/3252-49144-bfb3a731b170.wiki:63`.
- **Wiki-sourced rewards.** The 364 Stars, 229 members coins, 132 coins per wheel, the bonus clothing sets and the Archer/Brawler/Medic/Ninja/Warrior/Wizard wheels all match `refs:freerealms-wiki/wikitext/3252-49144-bfb3a731b170.wiki:30-92`. The wiki also says "Levels 9 or higher" and "Memorial Caverns, Sanctuary".
- **Client text.** I confirmed these by text search in the locale: "Knock out Darvon!", "Free the captured Pixies", the bonus cage text, the barrier clue, "Darvon's Spot", "behind the Great Tree", "at least level 9", the four changeling and bat names, the Darvon ability names, the developer-string names, and the quest texts for Kazuo, Ceri, the artifacts, the shock paddles, and Sampson. I also confirmed "Battles in the Forgotten Caves grant bonus rewards!" (locale 424997), so the Tooltip row holds.
- **Collectible.** `repo:prototype/osfr-tools/data/content/collections.json:1620` puts "Darvon's Spot" in the water to the left of the dungeon, which matches Conflicts #4.
- **Cross-links.** `repo:notes/Build Guides/Content/Jobs/Medic.md:184` agrees on difficulty 4, level 9, Memorial Caverns and Boss Darvon. `repo:notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md` has Clover and Sampson. Build Ledger "Dungeons beyond the cave" (`repo:notes/Design/Build Ledger.md:78`) says none are playable; the note makes no playability claim, so nothing needs changing.

**Unsure:**
- The `loc <id>` numbers in the note (for example `2871702877`, `1291047686`, `3095697270`) do not match the locale tool's index numbers, so I could not check the ids themselves, only the text they point to.
- "Page revision 2025-09-08" (Overview). I could not find the revision timestamp for this wiki page in `refs`.
- The Atlas icon and the wiki's "Darvon's Spot" exploration placement were not checked against anything beyond the collections data.
- The video claims (frame keys, the red and blue markers, the banner) were not re-checked. The repo has no video index that I could search.
