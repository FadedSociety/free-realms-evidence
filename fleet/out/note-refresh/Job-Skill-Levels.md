<!-- fleet job=note-refresh id=Job-Skill-Levels status=done turns=12 usd=0.0103 tokens(read,write,in,out)=[215308, 40874, 26, 6103] model=claude-haiku-5-5 -->
# notes/Research/Job Skill Levels.md

**Verdict:** Minor drift, but it lands on the note's central roster claim. The Rock Toss row and the roster paragraph say no row was authored; T011 authored one. All level values in the table (Ninja 1/5/10/15, Brawler Pummel 10 / Enrage 15 / Leg Sweep 1, Archer Explosive 5 / Multi-Arrow 1 / Sniper 15 / Stunning 10 / Piercing 20) match the code, and Dragon Strike is still not authored.

**Corrections:**

1. old: `| Brawler | Rock Toss | not authored | absent | absent | 5; confirmed fourth 2009 active skill | B2009; no new ability row authored |`
   new: `| Brawler | Rock Toss | 62024 | absent | 5 | 5; confirmed fourth 2009 active skill | B2009; row authored by T011 (Brawler slot 4, reconstructed (R) effect and balance) |`
   why: repo:prototype/osfr-tools/data/content/job_abilities.json:905-908 (definition_id 62024, min_level 5, slot 4 under profile_id 43); repo:notes/Autopilot/T011.md:16-17 ("The new Brawler entry is Rock Toss (local ability definition 62024) at level 5").

2. old: `Roster edits: **none added, none removed**. Rock Toss is a documented historical omission.`
   new: `Roster edits: **Rock Toss added (T011, local definition 62024, Brawler slot 4, level 5); none removed**. Rock Toss was a documented historical omission.`
   why: repo:prototype/osfr-tools/data/content/job_abilities.json:905-945; repo:notes/Autopilot/T011.md:17, 28 (Rock Toss row in job_abilities.json).

3. old: `A new executable row would require a local identity, slot and effect/balance bindings beyond the seven evidenced level corrections.`
   new: `The Rock Toss row carries a local identity, slot and (R) effect/balance bindings beyond the seven evidenced level corrections; its numeric effects are reconstructed, not recovered from retail.`
   why: repo:prototype/osfr-tools/data/content/job_abilities.json:907-944 (damage_multiplier 1.4, range 18, stun 2000 ms, cooldown 6000 ms all marked (R)); repo:notes/Autopilot/T011.md:65-66.

**Unsure:**

- The "Old" column values (pre-W125) cannot be checked against the tip. I did not check them.
- The job_abilities.json rows for Shadow Minion (62014) carry `"unavailable": true` (line 703). The note says nothing about availability, so I made no correction. Readers may want to know that the ninja Shadow Minion row is not executable.
- Dragon Strike: only weapon names ("Ninja's ... of Dragonstrike") appear in the repo. No ability row exists, so "not authored" still holds.
