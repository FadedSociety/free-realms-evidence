<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Snowhill status=done turns=21 usd=0.0221 tokens(read,write,in,out)=[710625, 64146, 44, 13916] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Snowhill.md

**Verdict:** minor drift. The note is almost entirely client and wiki sourced, and it makes almost no claims about our code, so there is little to check against the tip. The one stale statement is in the Gaps section, where it says the Postman and Soccer Star job pages are unfinished and that Loryn's quests are wiki-only. Both job pages now carry the Snowhill quest rows.

**Corrections:**

1. old: `Loryn's four quests are wiki-only; Landon's per-quest list is not on this page.`
   new: `Loryn's four Snowhill quests (What a Mess!, A Plea for Help, Biting Back, Summit in Shrouded Glade) are client-matched on the [[Postman]] page (Band 5, quests 21 to 24, with locale ids). Landon's per-quest list is on the [[Soccer Star]] page, not this one.`
   why: repo:notes/Build Guides/Content/Jobs/Postman.md:111-118 (Band 5 "Snowhill (Loryn)", text match "exact" for What a Mess!, Biting Back and Summit, "†" for A Plea for Help, all tagged [client]). The Loryn row in this note still cites only [client][wiki], which is accurate.

2. old: `The [[Postman]] and [[Soccer Star]] job pages were not finished when this page was written.`
   new: `The [[Postman]] and [[Soccer Star]] job pages now hold full quest lists (Postman.md about 290 lines, Soccer Star.md about 321 lines).`
   why: repo:notes/Build Guides/Content/Jobs/Postman.md (290 lines, Band 5 at line 111) and repo:notes/Build Guides/Content/Jobs/Soccer Star.md (321 lines, Manager Landon row at line 40, quest table from line 69).

**Unsure:**

- **Dangling link.** Line 210 of the Snowhill note (Snow Days bullet) says "See [[Snow Days]]", but there is no `Snow Days` note anywhere in `notes/` (no `# Snow Days` heading and no file, and Content.md does not mention it). I did not propose an edit because the intended target may not exist yet.
- **Therin is not a spawned trainer in our data.** The Snowhill row for Therin (line 43) does not say whether he is reachable in our build. repo:prototype/osfr-tools/data/content/job_trainers.json says "Therin is only a poi_anchor, so Mili Ironcall, a spawned Miner trainer at Southvale, is the reachable menu trainer." Smitty and Dewey are consistent with our data. Worth a note in the Miner page, not a change here.
- **Unchecked count.** Content.md says "[[NPCs - Snowhill]] (94 NPCs)". I did not count the rows in this note, so I cannot confirm that figure.
- **Ryn and Mr. Twinkle in Gaps.** Line 242 lists Ryn, Mr. Twinkle, Bert and Ernie as "names only". Each has a row with client text (Ryn line 65, Mr. Twinkle line 68, Bert and Ernie lines 29 to 30). This is a wording issue, not a code issue, so I left it.
