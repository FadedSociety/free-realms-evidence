<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Highroad-Junction status=done turns=21 usd=0.0265 tokens(read,write,in,out)=[816810, 65929, 44, 20105] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Highroad Junction.md

**Verdict:** minor drift. Most of the note is client-locale and wiki sourcing, which the repo does not contradict. Its one code-visible quest-giver claim (Introduce Yourself) is stale: the repo now binds that quest to Merigold's row. The status and count claims I could check hold (see Unsure).

**Corrections:**

1. `old:` Merigold or Raina Rush
   `new:` Merigold (giver); Raina Rush is the talk target
   `why:` `repo:prototype/osfr-tools/data/content/quests/adventurer.json:1548` gives quest 3000020 `"giver_npc_id": 9000000402` (Merigold's row). Its objective at `:1554` is `talk_to_npc` `npc_id 9000000177` (Raina Rush). `repo:prototype/osfr-tools/data/content/npcs/highroad_junction.json:6553-6591` shows the Merigold row listing 3000020 in `quests_given` and `quest_ids_given`. This was bound by T357 (`repo:notes/Autopilot/T357.md:24`).

2. `old:` giver Merigold or Raina, see [[Adventurer]] C1)
   `new:` giver Merigold (her row lists 3000020; Raina is the talk target), see [[Adventurer]] C1)
   `why:` same evidence as correction 1: `repo:prototype/osfr-tools/data/content/quests/adventurer.json:1548` and `:1554`; `repo:prototype/osfr-tools/data/content/npcs/highroad_junction.json:6588`.

3. `old:` Merigold's quests, Zoren's quest, Auguste's first three quests and all of Alena's quests are linked from wording only.
   `new:` Merigold's Introduce Yourself (3000020) is bound to her row in the repo (`adventurer.json:1548`; `highroad_junction.json:6588`). Her Visit and Meet Merigold quests, Zoren's quest, Auguste's first three quests and all of Alena's quests are linked from wording only.
   `why:` `repo:prototype/osfr-tools/data/content/npcs/highroad_junction.json:6588-6591`; `repo:notes/Autopilot/T357.md:24`. Visit and Meet Merigold have no quest id in the repo.

**Unsure:**

- **Hewey's Escape giver.** The note says Harold is the wiki giver and Archy the client giver. The repo binds Brawler quest 3030011 (Hewey's Escape!) to Harold's row (`repo:prototype/osfr-tools/data/content/npcs/highroad_junction.json:5014-5015`; `repo:prototype/osfr-tools/data/content/quests/brawler.json:701`). That follows the wiki, but the binding cites the Brawler guide, not a separate source, so I did not change the note's stance.
- **Auguste's Cooking 101 (3050004).** The repo binds it to Auguste (`repo:prototype/osfr-tools/data/content/quests/chef.json:156-159`; also 3050011 at `:575-578` and 3050013 at `:713`). Its evidence cites this note's row 47 (`chef.json:175`), so the binding is circular and does not settle the "[inferred]" tag. I could not match 3050004 to the note's "Chef: Highroad Cooking" title ids.
- **Hewey's Escape status.** Conflict 9 says the client and video show it working. The repo's dungeon roster marks it "(removed)" (`repo:prototype/osfr-tools/src/restoration/piece_059.rs:8` and `:141`). This is not a false claim in the note, but a reader of the repo would see the conflict.
- **Sacred Glade tutorial.** The note's "(no longer in game)" fits the research data, which marks it "NOT LIVE" (`repo:notes/Research/original-activity-coverage.json:15091`).
- **Counts.** Part A 3, B 7, C 2, D 4, E 6, total 22; the Quest index has 32 rows; the 7 rows with no job-page entry all match the rows in the table. The "25 have a full row on a job page" figure I did not check.
- **Zoren's and Verill's rows.** The repo has a Zoren row with no quest ids (`highroad_junction.json:10620`). Verill has no row in that file. The note does not claim a repo row for either.
