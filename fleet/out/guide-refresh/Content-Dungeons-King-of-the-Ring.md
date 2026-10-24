<!-- fleet job=guide-refresh id=Content-Dungeons-King-of-the-Ring status=nothing_found turns=13 usd=0.0130 tokens(read,write,in,out)=[294913, 45121, 28, 8900] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/King of the Ring.md

**Verdict:** current. The note makes almost no claims about our code or build status; nearly every claim is about the client, the wiki, or the video. The repo claims it does make hold at the tip, so I have no corrections to apply.

**Corrections:** none.

What I checked (all hold):
- **Field battle is built.** The note says the fight is in Cobblestone Village behind Carlos, with difficulty 1 and a 19-coin reward. `repo:prototype/osfr-tools/data/content/field_battles.json:1420-1455` has the Brawling Ring battle (id 12400, `name_id` 24276, gate about 5 m behind Carlos), the Mongo boss, and `reward_coins: 19`. `repo:notes/Autopilot/T252.md` records the Brawler start (Carlos, Mongo, Brawling Ring) as built.
- **Wheel and rewards.** The "3 slots per job", 19-coin slot, Brawler "Saved by the Bell Brawler Gloves" and Warrior "no Mystery Pack" rows match `repo:prototype/osfr-tools/data/content/dungeons/king_of_the_ring.json:579-1172`. The Cursed Graveyard cross-reference matches `repo:prototype/osfr-tools/data/content/dungeons/cursed_graveyard.json:601`.
- **"Full group" and bonus claims.** The "[client: no match]" claims hold. The locale has no "King of the Ring Bonus Objective" string, and no "Complete the King of the Ring encounter with a full group" string (the full-group strings list the other dungeons only). `notes/Build Guides/Content/Dungeons/Dungeons.md:57` also lists King of the Ring! among the dungeons with no bonus string.
- **Gap and conflict wording.** "Mongo Smash" and "Mongo's Glowy Axe" exist in the locale. The "Bell Brawler" conflict matches the client name used in our data.

**Unsure:**
1. **Combat job level.** The note says "None. Difficulty 1." Our dungeon record sets `minimum_combat_job_level: 1` (`repo:prototype/osfr-tools/data/content/dungeons/king_of_the_ring.json:107-108`), while the field battle sets `required_combat_level: 0` (`field_battles.json:1420`). Both mean no real requirement, so I did not flag it, but the two values differ.
2. **Mongo's stats in our build.** The note's gap "Mongo's health, attack list and any phases" is about the original game, and it is still true. Our build uses a reconstructed 900 HP and 4 damage (`field_battles.json:1450-1451`, marked `(R)`). This is not a false claim, but a reader might take it as a gap in our build.
3. **Carlos spawn.** `notes/Design/Build Ledger.md:88` says "Carlos Brazenfist doesn't spawn, which blocks the Brawler chain." That is about the build, not this note. Carlos is placed in `field_battles.json:1483` (`9000000042`), so the Ledger line may be stale. I did not verify the runtime spawn.
4. **Locale IDs.** The note cites raw hash IDs (for example `loc 422538418`). The locale lookup tool does not resolve those, so I could only confirm the English text by searching for it (for example "King of the Ring!" and "Knock out Mongo!"), not the hash itself.
