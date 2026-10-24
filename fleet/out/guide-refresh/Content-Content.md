<!-- fleet job=guide-refresh id=Content-Content status=done turns=12 usd=0.0146 tokens(read,write,in,out)=[257266, 50564, 26, 11342] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Content.md

**Verdict:** current, with minor drift. The structure holds: every linked job, dungeon and zone page exists, and the 17 zone pages are all written. Only one count overstates what its page says.

**Corrections:**

- `old:` [[NPCs - Sanctuary]] (132 NPCs, with Queensfields, Pixiewood Hills and the Memorial Caverns)
  `new:` [[NPCs - Sanctuary]] (132 table rows, which include an anonymous shop row, three enemy-group rows and 20 hand-in target rows, with Queensfields, Pixiewood Hills and the Memorial Caverns)
  `why:` repo:notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:19 gives "Part A 56 rows, Part B 14 (13 NPCs plus one row for the anonymous shops), Part C 19 (including three rows for enemy groups), Part D 21, Part E 2, Part F 20 (hand-in targets...)". That sums to 132 rows, not 132 NPCs. The same overstatement appears in repo:notes/Build Guides/Content/NPCs/NPCs.md:13, which is not this note.

**Checked and holding:**
- All 17 job links (Archer through Soccer Star) resolve to files in `notes/Build Guides/Content/Jobs/`. `[[Dungeons]]` resolves to `Dungeons/Dungeons.md`, and `[[NPCs]]` resolves to `NPCs/NPCs.md`.
- The 17 zone pages named in the note exist in `notes/Build Guides/Content/NPCs/`, and none is a placeholder.
- Counts that match their pages: Cobblestone 20 (NPCs - Cobblestone Village.md:162), Greenwood 50 rows (NPCs - Greenwood Forest.md:31), Merry Vale 66 NPCs (NPCs - Merry Vale.md:280), Farnum 30 rows (NPCs - Farnum Farmstead.md:184), Wugachug 40 rows (NPCs - Wugachug.md:28), Wilds 109 rows (NPCs - Wilds.md:28), Durango 11 rows (NPCs - Durango Zoo.md:22), Shrouded Glade 67 rows (NPCs - Shrouded Glade.md:249), Highroad 22 NPCs (NPCs - Highroad Junction.md:151), Stillwater 27 NPC rows (NPCs - Stillwater Crossing.md:179), Sunstone 81 NPCs (NPCs - Sunstone Valley.md:25), Seaside "about 164" (NPCs - Seaside.md:207).

**Unsure:**
- `NPCs - Snowhill` "94 NPCs": no count sentence in the Snowhill page. Only the NPCs index (repo:notes/Build Guides/Content/NPCs/NPCs.md:15) states 94, so I could not confirm it.
- `NPCs - Briarwood` "about 128 rows": no count sentence on the page. I did not count the rows.
- `NPCs - Lakeshore` "39 NPCs": the page has no count sentence, and my row search was not reliable enough to count the table.
- The job-page descriptions and the precedence paragraph are design statements and cannot be checked against the code.
