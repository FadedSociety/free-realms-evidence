<!-- fleet job=guide-refresh id=Content-Dungeons-Trail-of-Betrayal status=done turns=27 usd=0.0275 tokens(read,write,in,out)=[1028050, 63951, 56, 18411] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Trail of Betrayal.md

**Verdict:** current. Only minor drift: one client name is singular in the locale, and the code-side facts (difficulty, level, entrance) still match the tip.

**Corrections:**

- `old:` Chugawug Tower Sentries (`loc 1633204506`)
  `new:` Chugawug Tower Sentry (`loc 1633204506`)
  `why:` locale/en_us_data.dat:43212 reads `1633204506 ucdt Chugawug Tower Sentry` (singular). Not a code claim; it is the cited string.

**Checked and holding:**

- Difficulty 5: `prototype/osfr-tools/src/restoration/piece_059.rs:180` (row 43, "Trail of Betrayal", 5, entrance barrier at "Nettleseed, Briarwood"). Matches the Overview and Requirements rows, and the Dungeons.md index (line 111: 5 / 13).
- Entrance "barrier" in Nettleseed, Briarwood: `piece_059.rs:180`, same as above.
- Combat job level 13: `prototype/osfr-tools/data/content/dungeons/trail_of_betrayal.json` (`minimum_combat_job_level` value 13); the client string "Requires a level 13 combat job" exists at locale line 4201.
- Members-only false: same JSON, `members_only` value false.
- Name id 554510225 and the name "Trail of Betrayal": JSON `name_string_id`, and locale/en_us_data.dat:14705.
- Brutus the Brute is a separate entry: `data/content/enemies.json:172` (`w58_brutus_the_brute_l13_enemy`) and `enemies_unresolved.json` ("Not the boss").
- About 40 `loc` ids in the note were checked against `client/locale/en_us_data.dat` (the file the note's ids come from; the `locale` tool does not accept them). All match their quoted text, including the goal ids 1974916392, 3613783047, 2033240396, 3314983866, 1480933034, 1783747877, 4055902817, 4131419431, the escort lines, the 25% heal note, the quest ids and the prize-wheel item names.
- Prize-wheel items: every name I checked exists in the locale ("Soke Ninja Wristguards", "Energy Transfer" as the set name, "Ninja's Shadow Blade of Shadow Armies", etc.).

**Unsure:**

- The note says nothing about zone ids, but `piece_059.rs:180` gives Trail of Betrayal a zone definition (`bw_trail_of_betrayal`, 4078, 35, 6_629_059). `trail_of_betrayal.json` leaves `zone_id` null with the reason "Guide names a region/subregion but gives no ContentDb zone ID." The two disagree; the note does not make the claim, so I did not correct it.
- Goal counts, the "seven lines" panel, "Trolls! Get ready!", "We take towers again!", the 307/551 coin and 336 star figures, and the 3-lines-then-7 recording: video or wiki claims with no code or client-data check available. The JSON has the 307 and 551 coin rewards as wiki-sourced text (lines 855, 866), but it does not verify the amounts.
- Sampson Idlefist as a boss here: the client quest texts (877479789, 3663462466) point at him in the Trail, but no code or data shows him as an encounter boss. Left as the note has it.
