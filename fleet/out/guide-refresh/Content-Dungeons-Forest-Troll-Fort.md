<!-- fleet job=guide-refresh id=Content-Dungeons-Forest-Troll-Fort status=nothing_found turns=26 usd=0.0333 tokens(read,write,in,out)=[1339400, 82969, 54, 19017] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Forest Troll Fort.md

**Verdict:** current. I found no checkable claim about our code, data or status that is now false. The note is almost entirely client-locale and video evidence, and the parts I could test match the tip.

**Corrections:** none.

**What I checked (all held):**
- **Level 13 requirement and difficulty 5.** `prototype/osfr-tools/data/content/dungeons/forest_troll_fort.json` sets `minimum_combat_job_level: 13` and `difficulty: 5`. `notes/Build Guides/Content/Dungeons/Dungeons.md:106` gives `5 | 13 | Northern Wilds`. The locale has "Requires a level 13 combat job" (line 4201).
- **Entrance.** `prototype/osfr-tools/src/restoration/piece_059.rs:175` has the row `Forest Troll Fort, 5, ... E("wood barrier", ... "northeast Wilds", Some("Wilds"))`, which matches the "wood barrier, northeast Wilds" text. The JSON zone is "Northern Wilds", which matches the note.
- **Achievements.** `achievements.json:3831-3832` ("Forest Troll Fort" / "Complete the Forest Troll Fort encounter.") and `:4695-4696` ("Group: Forest Troll Fort") match. "Win Combat Encounter Forest Troll Fort" exists in the locale at id 119175.
- **Score weights.** The fort's weights (3,000 / 50,000 / 120,000 / 25,000) match the index at `Dungeons.md:53` and the Briarheart note.
- **Prize wheel.** Every item I checked (Raptor Bow of Lightning, Upshot Archer Hoodie, Bull's-Eye Archer Hat, Knockdown Brawler Mask, Stopping Power Medic Helmet, Chunin Ninja Gi, Jonin Ninja Cowl, Warrior Warlord Axe, Archmagus Wizard Talisman, and others) exists in the locale. "Adept Wizard Robe" (133450) and "Adherent Wizard Long Cloak" (133434) match Conflict 3. "Energy Transfer Medic Jacket" (133128) matches Conflict 4.
- **Boss and sub-bosses.** The strings "Defeat Verda, Queen of the Trolls!", "Verda is briefly stunned at 66% and 33%...", the proximity slam, "Verda's Guardian Seerdoctor", "Pogush, the Mighty Seerdoctor", "Blutin, the Roughguard Captain" and "Videez, the Master Sneakscout" all exist in the locale. So do the dev strings "forest troll fort - Queen Verda primary attack", "- elite proc attack" and "- pogosh heal".
- **Quest texts.** The Porky, Tido/Dore, Hogosh/Gulsh, Seerdoctor, Ritualist sigils, Brawler and Archer lines all match locale text. "Queen Varda" (419360) and "Vera" (139525) also match.
- **Enemy and boss records.** `prototype/osfr-tools/data/content/enemies.json:1316` has `w58b_queen_verda`, which backs the boss row.

**Unsure:**
- The person links in "NPCs" (`[[Queen Verda]]`, `[[Blutin]]`, `[[Videez]]`, `[[Pogush]]`, `[[Bluz]]`, `[[Bowman Bilter]]`, `[[Rourke]]`, `[[Gulsh]]`, `[[Hogosh]]`, `[[Kazuo]]`) do not resolve to any page in `notes/`. Only the area pages under `Content/NPCs/` exist. This is a link problem, not a false claim, so I did not propose a change.
- The note's `loc` numbers (e.g. 1323029355, 4268759390) are not the locale tool's sequential ids, so I matched those strings by text instead of by number. The text matches, but I could not confirm each id.
- The Stars, coin payouts, group size and the video-frame claims (panel levels, "Knock outs Remaining 4/5") are not in our code, so I could not check them.
