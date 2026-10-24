<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Merry-Vale status=done turns=17 usd=0.0231 tokens(read,write,in,out)=[635091, 69403, 36, 16165] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Merry Vale.md

**Verdict:** minor drift. Most of the note is client-locale and wiki sourcing that the code does not contradict. Two statements about trainers are misleading against the server's job table, and two lines say the Necronomicus and Stone Heart's Hideaway dungeon pages do not exist, but both now exist. The row counts (27 cross-reference rows, 50 quest rows) match the file.

**Corrections:**

1. Line 238 (Notes: quest givers and trainers)
   - `old:` - **Chef Jarvie** and **Postmaster Vixie** are the job trainers.
   - `new:` - **Chef Jarvie** and **Postmaster Vixie** are the level 5 to 10 band quest givers. The server's learn-menu trainers are **Simone** (Chef, Cobblestone Village) and **Flitter** (Postman, Sanctuary).
   - `why:` repo:prototype/osfr-tools/data/content/job_trainers.json:11-17 (Chef learn row, npc 9000000467 = Simone) and :96-101 (Postman learn row, npc 9000000091 = Flitter). Jarvie (9000000044) and Vixie (9000000174) are only quest givers: repo:prototype/osfr-tools/data/content/quests/chef.json:1175,1227,1277 and quests/postman.json:580,634,684. Simone is named as the Chef trainer at repo:notes/Build Guides/Content/Jobs/Chef.md:36, and T407 (repo:notes/Autopilot/T407.md:25-45) records that Vixie is not the Postman trainer.

2. Part B, Chef Jarvie row, "Title / role" cell
   - `old:` Chef trainer for levels 5 to 10; **blocks until level 10**
   - `new:` Chef band quest giver for levels 5 to 10; **blocks until level 10**
   - `why:` repo:prototype/osfr-tools/data/content/quests/chef.json:1175,1227,1277 (giver 9000000044, Jarvie, for the band 2 Chef quests). The Chef learn-menu row is Simone, repo:prototype/osfr-tools/data/content/job_trainers.json:11-17.

3. Part B, Postmaster Vixie row, "Title / role" cell
   - `old:` Postman trainer for the level 5 to 10 band
   - `new:` Postman band quest giver for the level 5 to 10 band (the learn-menu trainer is Flitter in Sanctuary)
   - `why:` repo:prototype/osfr-tools/data/content/quests/postman.json:580,634,684 (giver 9000000174, Vixie); repo:prototype/osfr-tools/data/content/job_trainers.json:96-101 (Postman row, Flitter 9000000091); repo:notes/Autopilot/T407.md:27-45.

4. Row for "Ronnie" or the Necronomicus Unleashed quest row (quest table, "Necronomicus Unleashed" row)
   - `old:` No dungeon page exists yet.
   - `new:` The dungeon page now exists at Dungeons/Necronomicus Unleashed.md (combat instance, zone Merry Vale).
   - `why:` repo:notes/Build Guides/Content/Dungeons/Necronomicus Unleashed.md:1-11.

5. Gaps section
   - `old:` **No dungeon page** for Necronomicus Unleashed or Stone Heart's Hideaway.
   - `new:` **Dungeon pages exist** for Necronomicus Unleashed and Stone Heart's Hideaway (Dungeons/Necronomicus Unleashed.md, Dungeons/Stone Heart's Hideaway.md). The rows on this page should link to them.
   - `why:` repo:notes/Build Guides/Content/Dungeons/Necronomicus Unleashed.md:1-11 and repo:notes/Build Guides/Content/Dungeons/Stone Heart's Hideaway.md:1-11 (both `type: content-dungeon`, `zone: Merry Vale`, `combat: true`).

**Unsure:**
- The "66 NPC rows" total (line 25 and line 280). I confirmed the cross-reference table at lines 149-175 has 27 rows and the quest table at lines 183-232 has 50 rows, but I did not count the Part A to H rows one by one.
- Whether Chef Jarvie (npc 9000000044) is drawn in the world. merry_vale.json:3596 says `presence: "listed"`, and I did not check spawn data.
- The Den of Secrets boss statements (Liana, Mayor McFairy) in Conflicts 2 were not checked against the Den page or the server's dungeon data.
- The note's client-locale quest and NPC claims (ids, quotes) are outside what the code can settle, so I did not check them.
