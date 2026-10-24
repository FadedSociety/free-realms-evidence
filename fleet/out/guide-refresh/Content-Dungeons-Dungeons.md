<!-- fleet job=guide-refresh id=Content-Dungeons-Dungeons status=done turns=9 usd=0.0132 tokens(read,write,in,out)=[151165, 44772, 20, 12158] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Dungeons.md

**Verdict:** minor drift. The index's page links and the "written" column hold up against the vault. Two statements are stale: one says Precursor Ruins still needs a page, and one says every entry has a page. The category counts are not settled by anything at the tip.

**Corrections:**

1. `old:` It needs a page of its own.
   `new:` It has its own page now: [[Precursor Ruins]] (Sunstone Valley, about 94 lines, written from the client text).
   `why:` repo:notes/Build Guides/Content/Dungeons/Precursor Ruins.md:1-30 (the page exists and opens with its overview and requirements). The index's own row at line 108 already marks it **written**, so line 160 contradicts line 108.

2. `old:` Every entry now has a page; the gaps above apply across them.
   `new:` Every dungeon and battle row now has a page. The exceptions are Cakenstein (still pending, no page yet, as `Cakenstein Attacks`) and the Battle Item Mystery Pack (no page needed). The gaps above apply across the pages.
   `why:` repo:notes/Build Guides/Content/Dungeons/ holds no `Cakenstein*.md` file (directory listing at the tip). Line 154 of this note already lists Cakenstein as pending.

**Unsure:**

- **Entry counts (lines 7, 13 and the "All 72 entries" heading).** Line 13 says "Written (all 70 combat entries)". The vault has 74 entry pages plus the index, and the tables carry 43 dungeon rows (including Precursor Ruins, which is outside the category) and 31 battle rows (including The Rumbledome, also outside). That gives 42 + 30 = 72 category combat entries, plus the 2 stray entries. The "70" and "72" figures match neither the vault nor the wiki category in a way I could verify, so I did not propose a number. The wiki category count itself cannot be checked from the repo.
- **Trophy coverage (Conflicts item 4).** Client search for "Complete the X encounter" returned exactly 30 hits (capped at 30), so I could not confirm whether Tanglewood Fort or Trail of Betrayal lack one.
- **Bonus-objective strings (line 57).** The "Bonus Objective" search also returned capped results. The absences listed for Cursed Graveyard, Hot Springs Haven, Sandscale Oasis, King of the Ring and Hewey's Escape are consistent with the rows I saw, and Bone Bog, Tavern Cellar and Misty Mountain are present as the note says, but I did not count the full 37.
- **Client IDs in the requirement table (line 46).** The locale tool did not resolve the numeric ids cited there (for example 2145075890 and 3173661191), while the matching text is present (for example "Requires a level 5 combat job" at 4199, and the level 5/9/13 refusal strings at 4189–4191 and 4203–4205). These ids look like a different hash scheme, so I could not confirm them. The strings themselves exist.
