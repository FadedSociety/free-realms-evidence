<!-- fleet job=note-refresh id=Starting-Quest-Chains status=done turns=18 usd=0.0176 tokens(read,write,in,out)=[425164, 41262, 38, 16457] model=claude-haiku-5-5 -->
# notes/Research/Starting Quest Chains.md

**Verdict:** minor drift. Most rows match the tip (the DISABLED reasons, the giver absences for 9000000226, 9000000068, 9500000519 and 9000000509, the coin amounts, and the enabled flags for 3000020, 3000059 and 3000060). Three rows and the header are stale: the Snowhill placements, the 3000009 prerequisite and enabled state, and the 3080002 giver.

**Corrections:**

1. Row 3080001 (Burden of Fame), Enabled/reason column.
   - `old:` Chad, Mustang Alli and Burt have only poi_anchor placements
   - `new:` Chad, Mustang Alli and Burt now have legacy_data placements in snowhill.json (Frost Ridge), so the direct-talk sequence is enabled
   - `why:` repo:prototype/osfr-tools/data/content/npcs/snowhill.json:5472 and :5528 (Burt, legacy_data); :7433 and :7486 (Chad, legacy_data); :28707 and :28782 (Mustang Alli, legacy_data); repo:prototype/osfr-tools/data/content/quests/kart_driver.json:128 ("the direct-talk sequence is enabled")

2. Row 3000009 (Fighting the Pack), Prerequisites cell.
   - `old:` | 3000009 | Fighting the Pack | 4420074 | [3000008] |
   - `new:` | 3000009 | Fighting the Pack | 4420074 | [] |
   - `why:` repo:prototype/osfr-tools/data/content/quests/adventurer.json:685 (`prerequisite_quest_ids: []`) and :773 (T241: "this record drops that prerequisite until the crafting path opens")

3. Row 3000009 (Fighting the Pack), Enabled/reason cell. The record is enabled and no longer blocked by 3000008.
   - `old:` Predecessor 3000008 blocked; guide requires switching to Brawler, but split Quest cannot express job requirements/selection. Kill targets exist.
   - `new:` Enabled (`enabled: true`); predecessor 3000008 dropped from the record (T241 playtest entry); Brawler gate stored in the split Quest job field (job 43). Kill targets exist.
   - `why:` repo:prototype/osfr-tools/data/content/quests/adventurer.json:682 (`"job": 43`), :773 (the Brawler gate is stored in the job field), :779 (`"enabled": true`)

4. Header, line 3. The job gate is storable; only a level gate is not.
   - `old:` No level/job gate is invented; the split schema cannot store one.
   - `new:` No level gate is invented; the split schema cannot store a level gate. Job gates use the Quest job field (e.g. job 43 on 3000009).
   - `why:` repo:prototype/osfr-tools/data/content/quests/adventurer.json:682 and :773; repo:prototype/osfr-tools/data/content/quests/kart_driver.json:5-6 (`"job": 48` on 3080001)

5. Row 3080002 (Racing Tutorial), reason cell. The giver is now bound to the placed Mustang Alli key, not the unresolved ref.
   - `old:` Mustang giver 9000000412 absent.
   - `new:` Giver is Mustang Alli 9500000759 (legacy_data at Frost Ridge), not 9000000412, which remains only an unresolved ref.
   - `why:` repo:prototype/osfr-tools/data/content/quests/kart_driver.json:147 (`giver_npc_id: 9500000759`); repo:prototype/osfr-tools/data/content/npcs/snowhill.json:28707 and :28782 (legacy_data); repo:prototype/osfr-tools/data/content/npcs_unresolved.json:3104 (9000000412 is the unresolved Mustang Alli ref)

**Unsure:**
- Row 3080002 says "Do not substitute dev kart race." Autopilot F128 (repo:notes/Autopilot/F128.md:162-169) says the active reconstruction uses a substitute speedway `31` under T017's stand-in policy. I did not settle whether the note's "do not substitute" wording is still true in the code, so I left it alone.
- Row 3000028 says Pux 9500000517 "does not spawn." The sanctuary.json record (:45212) has `presence: "listed"` and I did not find a placement line for it in the part I read, so the claim is probably correct, but I did not confirm it.
- Row 3000011 ("Both Pappy and Bartle do spawn") and the other spawn claims for 9500000941 and 9500000254 were not checked beyond the rows above.
