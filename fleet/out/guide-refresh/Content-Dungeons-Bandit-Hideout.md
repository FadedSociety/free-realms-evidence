<!-- fleet job=guide-refresh id=Content-Dungeons-Bandit-Hideout status=nothing_found turns=15 usd=0.0219 tokens(read,write,in,out)=[558021, 68429, 32, 15503] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Bandit Hideout.md

**Verdict:** current. No claim in this note about our code or build status is false at the tip. The note makes almost no code claims, so most of what it says is client, wiki or video evidence that I could not re-check against the repo.

**Corrections:** none.

What I checked and found consistent with the tip:
- Combat-job level 9 gate: `prototype/osfr-tools/data/content/dungeons/bandit_hideout.json` `entry_requirements.minimum_combat_job_level` = 9; the test file `tests/bandit_hideout_dungeon.rs:1-2` and `:1111` ("This activity needs level 9.") agree.
- Difficulty 4: same JSON (`difficulty` = 4); `field_battles.json:1524` battle `12360`, `difficulty` 4, `required level` 9 (per `notes/Autopilot/T353.md:77`).
- Name id `3272503457` used as the game-data name in the JSON (`name_string_id`), as the Overview says.
- Panel text, "Defeat Muggenstomp!", and the bonus-goal text are in the locale. Numeric ids 6995, 6997 and 139346 match the text quoted in the note. The note's `loc` hashes are a different key system and could not be matched to numeric ids here.
- Achievements: bronze 5 points "Complete the Bandit Hideout! encounter." and silver 10 points "Group: Bandit Hideout!" with a full group (`data/content/achievements.json:3540-3551`, `4404-4414`).
- Prize-wheel item names (for example "Medic's Megasaw of Triage", "Sensei Ninja Gi", "Threat Range Warrior Tunic", "Bodkin Archer Hoodie") exist in the locale. The wheel rows are unresolved to item ids (`dungeons_unresolved.json:432-557`), which the note does not claim otherwise.
- The 60-coin wheel slot matches battle 12360's 60-coin payout (`T353.md:81`).

**Unsure:**
- **Current build vs. Gaps.** The note never says whether the dungeon is playable. Since T353 it is: battle `12360` in `field_battles.json:1524`, with a test file and a 5-actor kill-all roster (Muggenstomp plus four Big Bandits, not five). The Gaps list ("Group size, wave layout, and how many total enemies spawn"; "Boss health and ability effects") still holds for the retail game, so I did not change it. Adding a build-status line would be an omission fix, not a correction.
- **Quest titles (Gaps: "Which quest owns each description").** `notes/Build Guides/Content/NPCs/NPCs - Greenwood Forest.md:170` assigns description `2928282136` to the "Searching the Hideout" title, but only "by position". The gap still stands as written.
- **Client-text citations.** The note cites `loc 3675449079` for "Defeat all of the Big Bandits!" and `loc 3532766773` / `485238779` for the story-hook text. The locale's numeric ids are 139346 for the bonus line and 442126 for "Muggenstomp and her band of thugawug bandits have been stopped." I could not confirm that the hashes map to these strings.
- **Level-1 Brawler set (Conflict 1).** The note calls "Saved by the Bell Brawler Shirt" a level-1 set. `Dungeons.md` lists those dungeons at gear tier I, which supports this, but I did not confirm the set's level directly.
