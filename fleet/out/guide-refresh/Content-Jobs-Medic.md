<!-- fleet job=guide-refresh id=Content-Jobs-Medic status=done turns=26 usd=0.0331 tokens(read,write,in,out)=[1229901, 88311, 54, 19557] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Medic.md

**Verdict:** minor drift. Most of the page is client-text and wiki material that the code does not contradict. The code-checkable claims (unlock by Naia, the level-5 Gordon gate, ability level locks 1/5/10/15, the Triage/Incision starter numbers, Gordon and Naia as givers) match the tip. The one stale area is the non-member level cap, where the note says no source gives a cut-off, but the server pins one.

**Corrections:**

1. `old:` So: non-members can try Medic to about level 4 or 5, and the job is members only beyond that.
   `new:` So: non-members can try Medic to level 4, and the job is members only beyond that.
   `why:` repo:prototype/osfr-tools/src/restoration/piece_043.rs:580-581 (`NON_MEMBER_JOB_LEVEL_CAP: u32 = 4`) and :490-498 (`member_level_cap()` returns 4 for non-members); repo:prototype/osfr-tools/src/restoration/piece_042.rs:36-37 (same cap, "level 4 if you are not a member"). The client string 348625404 that the note already quotes also says "up to level 4".

2. `old:` The first-gate quest at level 5 (row 6) is likely where the non-member stop falls.
   `new:` The server caps non-members at level 4 (community-documented, not first-party), so the stop is level 4, one level before the level-5 gate (row 6).
   `why:` repo:prototype/osfr-tools/src/restoration/piece_043.rs:490-496 and :580-581; repo:prototype/osfr-tools/src/restoration/piece_042.rs:36-37.

3. `old:` The exact level at which non-members stop is not stated by any source.
   `new:` The server caps non-members at level 4 (repo:prototype/osfr-tools/src/restoration/piece_043.rs:581, citing the community wiki Jobs page). The client's 348625404 also says level 4. Only the "level five" string (2065313732) disagrees.
   `why:` repo:prototype/osfr-tools/src/restoration/piece_043.rs:490-496, :580-581; repo:prototype/osfr-tools/src/restoration/piece_042.rs:36-37. The note's own quote of 348625404 already contradicts "not stated by any source".

**Unsure:**

- Conflicts 12 says "The wiki gives no cut-off level." The code cites the fandom Jobs page for a level-4 cap ("level 4 if you are not a member for most jobs", piece_042.rs:36). I could not find that wiki quote in refs (searched freerealms-wiki wikitext and the raw JSON), so I left the wiki sentence alone.
- The "Title ids" column lists raw locale hashes. The server has since replaced several of them with Global.Text ids, for example Palatable Pills 3179409013 → 77437, Take Your Vitamins 2261927574 → 23019, Achieve Level 5 1924758543 → 387463 (repo:prototype/osfr-tools/data/content/npcs/sanctuary.json, the "title_string_id corrected" evidence lines). The column's own description (line 16) is still true, so I did not change it. A builder should use the Global.Text id, not the hash.
- Gaps "No coin, XP or item rewards are known for any quest…": repo:prototype/osfr-tools/data/content/quests/medic.json:27-40 carries reconstructed coin and Medic-XP fallbacks (for example 5 coins and 15 job XP on quest 3090001), labelled "(R)" and not sourced from the guide. The note's "unknown" cells remain accurate as to sources, but the fallback values exist.
- The ability level locks (First Aid 1, Target Vitals 5, Vitamins 10, Shock Paddles 15) match repo:prototype/osfr-tools/src/opening_abilities.rs:74 and repo:prototype/osfr-tools/data/content/job_abilities.json:38/80/126. I did not find a Shock Paddles entry with min_level 15 in job_abilities.json, so that level rests on the Build Plan and opening_abilities.rs only.
- Not checked: the wiki dungeon difficulty gates, the Seaside and Callahan quest order (rows 29 to 33), the weapon tier lists, and the video frame claims.
