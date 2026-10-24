<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Greenwood-Forest status=done turns=15 usd=0.0190 tokens(read,write,in,out)=[420154, 58844, 32, 14915] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Greenwood Forest.md

**Verdict:** minor drift. The note is mostly client-locale and wiki material, and almost none of it makes checkable claims about our server code. The one checkable status claim that is now false is the list of "not yet written" pages in the header. The rest of the checkable claims I sampled hold.

**Corrections:**

- `old:` Pages not written yet that these rows point to: [[NPCs - Farnum Farmstead]], [[NPCs - Cobblestone Village]], [[NPCs - Merry Vale]], [[NPCs - Wugachug]], [[NPCs - Lakeshore]].
  `new:` Pages these rows point to, all now written and present in the NPCs folder: [[NPCs - Farnum Farmstead]], [[NPCs - Cobblestone Village]], [[NPCs - Merry Vale]], [[NPCs - Wugachug]], [[NPCs - Lakeshore]].
  `why:` repo:notes/Build Guides/Content/NPCs/ directory listing shows `NPCs - Farnum Farmstead.md`, `NPCs - Cobblestone Village.md`, `NPCs - Merry Vale.md`, `NPCs - Wugachug.md` and `NPCs - Lakeshore.md`. The Greenwood note's own cross-reference table (lines 124–142) links to them, and the Wilds note (repo:notes/Build Guides/Content/NPCs/NPCs - Wilds.md:325) still says those pages may be unwritten. That line is outside this note's scope.

**Checked and holding:**

- Dev chapter labels: the note says the client holds 20 "SGRevamp - Wilds South - N-M - Title" entries. The locale search returns exactly 20 (ids 441755 to 441899, chapters 1-1 to 4-5). Chapter 2 and chapter 3 titles match the note's list.
- Table counts: Part A has 13 NPC rows (lines 39–51). The cross-reference table has 19 rows (lines 124–142). The town and open-world quest table has 42 rows (lines 152–193).
- Part headings A–E, "Tied to Greenwood…", "Town and open-world quests", "Notes", "Conflicts" and "Gaps" exist at the lines the note's cross-references imply (lines 33, 53, 78, 95, 106, 118, 146, 195, 204, 222).
- Cross-references resolve: the Dungeon pages Bigfoot's Lair, Bigfoot Defender, Bandit Hideout, Fleetfoot Ninja and Danger Peaks exist; the Job pages Archer, Blacksmith, Miner, Ninja, Chef, Postman, Adventurer, Warrior and Card Duelist exist; NPCs - Wilds has Part I (line 203) and conflict 14 (line 308); NPCs - Highroad Junction and NPCs - Briarwood exist.
- Fleetfoot Ninja page (repo:notes/Build Guides/Content/Dungeons/Fleetfoot Ninja.md:20, :87) does record the "Sacred Grove" objective, as the note says.
- Locale strings for Camp Chatty / Camp Robbie / Summer Camp names and the Glugmort "west of the Lavender Coast Pass warpstone" line (locale 4420141) are present.

**Unsure:**

- Part B (18 rows), Part C (10 rows), Part D (4 rows) and Part E (5 rows) counts were not fully verified. My table-row search came back truncated, and I did not read those sections line by line.
- The `ucdt`/`ugdt` numeric ids quoted throughout (e.g. 166769791, 3550878236, 2504933996) do not resolve through the locale tool, which takes row numbers. I could not check the id citations, only the wording where it matched.
- Video frame references and the wiki-based claims (level gates, repeatable flags, opening dates) are outside what I can check in the repo.
