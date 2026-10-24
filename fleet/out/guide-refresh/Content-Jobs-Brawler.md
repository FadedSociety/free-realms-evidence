<!-- fleet job=guide-refresh id=Content-Jobs-Brawler status=done turns=26 usd=0.0300 tokens(read,write,in,out)=[1117188, 76902, 54, 18374] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Brawler.md

**Verdict:** minor drift. The note's code-facing claims mostly hold at the tip. Its `max_level 20`, `members_only: false`, dungeon difficulties and minimum-level figures, and the job's trainer and quest data all match the repo. What is stale is five wiki link targets that no longer resolve to a file, because the vault names those pages without the "!" or with a different title.

**Corrections:**

1. `old:` [[King of the Ring!]] (Carlos), [[Hewey's Escape]] (Harold or Archy), [[Cursed Graveyard!]] (Caitlyn)
   `new:` [[King of the Ring]] (Carlos), [[Hewey's Escape]] (Harold or Archy), [[Cursed Graveyard]] (Caitlyn)
   `why:` repo:notes/Build Guides/Content/Dungeons/ has "King of the Ring.md" and "Cursed Graveyard.md" with no "!" (the directory listing). The Cobblestone NPC page already links [[King of the Ring]] without the "!" (repo:notes/Build Guides/Content/NPCs/NPCs - Cobblestone Village.md:76). The dungeon data is at repo:prototype/osfr-tools/data/content/dungeons/king_of_the_ring.json and cursed_graveyard.json.

2. `old:` | [[King of the Ring!]] | 1, removed |
   `new:` | [[King of the Ring]] | 1, removed |
   `why:` same as correction 1. The difficulty of 1 matches repo:prototype/osfr-tools/data/content/dungeons/king_of_the_ring.json (field_battles.json:1483 also gives difficulty 1).

3. `old:` | [[Cursed Graveyard!]] | 1 |
   `new:` | [[Cursed Graveyard]] | 1 |
   `why:` repo:notes/Build Guides/Content/Dungeons/Cursed Graveyard.md exists; there is no "Cursed Graveyard!.md". The dungeon JSON is repo:prototype/osfr-tools/data/content/dungeons/cursed_graveyard.json.

4. `old:` | [[Bandit Hideout!]] | 4 |
   `new:` | [[Bandit Hideout]] | 4 |
   `why:` repo:notes/Build Guides/Content/Dungeons/Bandit Hideout.md:11 says "This guide's page name drops the '!'". The difficulty of 4 matches repo:prototype/osfr-tools/data/content/dungeons/bandit_hideout.json:61.

5. `old:` See [[NPCs - Blackspore]].
   `new:` See [[NPCs - Blackspore Swamp]].
   `why:` the file is repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md (the NPC listing). No "NPCs - Blackspore.md" exists. The Cobblestone NPC page already uses [[NPCs - Blackspore Swamp]].

**Unsure:**

- **Trainer count (Overview, "Three trainers can start the job, one per starting area").** repo:prototype/osfr-tools/data/content/jobs.json:303-318 lists 14 `trainer_npc_ids` for Brawler, including Flanders (9000000090), Petra (9000000428) and the E1 giver (9000000014). `job_trainers.json` has no Brawler row. This may only be a content-data list, not a menu trainer list, so I left the sentence alone.
- **Level-5 gate on Petra.** The note's "Blocks until level 5" rests on client objective text. repo:prototype/osfr-tools/data/content/quests/brawler.json has no level field for any record, and line 626 says the C6 hand-off carries no job gate. The gates are therefore not proven in our data. The one code gate found is the Warrior trainer's rank 5 (`job_trainers.json:92`), which is a different job.
- **Carlos spawn (outside this note).** repo:notes/Design/Build Ledger.md:88 says "Carlos Brazenfist doesn't spawn, which blocks the Brawler chain". repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:5-9 now has a drawable spawn for 9000000042 (Carlos), and the brawler_mongo_chain test drives him. The Ledger line may be stale, but this note makes no spawn claim.
- **"No longer in game" for Flanders and Ashley.** I could not check this against code. The E1 and E2 quest records are `enabled: false` (brawler.json:51, 102), which is consistent with it.
