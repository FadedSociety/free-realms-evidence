<!-- fleet job=note-refresh id=Bryce-Field-Notes status=done turns=19 usd=0.0237 tokens(read,write,in,out)=[762090, 69323, 40, 14907] model=claude-haiku-5-5 -->
# notes/Research/Bryce Field Notes.md

**Verdict:** minor drift. One claim is plainly false (the job-ability line), and two "Plan:" statements describe work that now exists. The camera, start-screen, spawner, stat and job-level claims I checked still hold.

**Corrections:**

1. `old:` Our server implements only the basic slot so far (Build Ledger: combat authority, one ability family at a time).
   `new:` Our server also implements the job ability slots: 24 skills for six jobs are in `data/content/job_abilities.json`, run through `encounter/skills.rs` `job_ability`. Shadow Minion is marked unavailable and refused (Build Ledger row "Job abilities and level locks").
   `why:` `repo:notes/Design/Build Ledger.md:73` (W101: 24 skills, effects for heal, DoT, area, stun, buff); `repo:prototype/osfr-tools/src/encounter/skills.rs:116`; `repo:prototype/osfr-tools/data/content/job_abilities.json:165` (Shadow Minion "unavailable"). The Build Ledger has no row named "combat authority", so the cited row does not exist.

2. `old:` Plan: field enemies get quest gating (spawn while one of their quests is active).
   `new:` Built: field enemies already carry quest gating. An enemy with `quest_ids` spawns only while one of those quests is active (the four quest-3030007 Hooligans). Enemies with empty `quest_ids` are always-on.
   `why:` `repo:prototype/osfr-tools/data/content/field_enemies.json:396` (quest_ids on 3030007 Hooligans) and `:570` (empty quest_ids); `repo:prototype/osfr-tools/src/encounter/field.rs:653` (`set_active_quests`); `repo:notes/Design/Field Enemies.md:146` (always-on without an active quest is implemented).

3. `old:` Plan: spawners are always visible; the start screen shows the requirement; the server refuses Go (41/108) unless the active job is a combat job at or above the level.
   `new:` Built: spawners are always visible; the start screen shows the requirement; the server refuses Go (41/108) unless the active job is a combat job at or above the level.
   `why:` `repo:prototype/osfr-tools/tests/bandit_hideout_dungeon.rs:1093` (a level-8 combat job cannot start through Go, 41/108 refuses); `repo:prototype/osfr-tools/tests/bixie_hive_dungeon.rs:500` (a non-combat active job is refused at 41/108); `repo:prototype/osfr-tools/src/encounter.rs:541` (difficulty 3/4/5 require level 5/9/13).

**Checked and holding (no change):**
- Dialog camera target at 26/3 dwords 2–3, 49/1 after the reward bundle, 49/13 offset 6, verified in run 233813: `repo:prototype/osfr-tools/src/gameplay/npc.rs:1143-1155`; `repo:notes/Reviews/Native Round5 050310.md:130`.
- Start screen 41/114, Go 41/108: `repo:prototype/osfr-tools/src/encounter.rs:532-533`.
- "Hooligan Bullies!" spawner NameId 74753: `repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:45796-45797`.
- Hooligans 220 HP / 8 damage and wolves 180 / 25: `repo:prototype/osfr-tools/data/content/field_enemies.json:390-391, 1146-1147`.
- Player HP 1000 baseline: `repo:prototype/osfr-tools/src/encounter.rs:44`.
- Medic First Aid lvl 1, Target Vitals 5, Vitamins 10, Shock Paddles 15: `repo:prototype/osfr-tools/data/content/job_abilities.json` (min_level at 38/80/126/173; Triage is slot 1, First Aid slot 2).
- Job-level lock enforced when the bar is built: `repo:prototype/osfr-tools/src/opening_abilities.rs:265-275`.

**Unsure:**
- "Weapon abilities (Incision, Triage ...) come with the weapon, not the job level." `job_abilities.json:38` gives Triage `min_level: 1`, and its source notes say it is weapon-gated (slot 7). Level 1 makes the lock moot, but I did not settle whether that matches the note's intent.
- Line 116 says every job skill carries a minimum level. I confirmed the field exists on the Medic, Warrior and Ninja entries I read, but did not count all rows.
- Names and IDs for Ty, Grosh, Len Tyril, Laggosh and Vergosh were not checked against the NPC data.
