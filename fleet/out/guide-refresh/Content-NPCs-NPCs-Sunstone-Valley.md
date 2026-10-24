<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Sunstone-Valley status=done turns=16 usd=0.0169 tokens(read,write,in,out)=[455520, 58827, 34, 9888] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md

**Verdict:** minor drift. The NPC rows, job-page pointers and the Blacksmith and Card Duelist row numbers hold. The note's statements that three linked dungeon pages are missing are now false: all three pages exist in the vault, so two status lines need fixing. The note makes no claims about server code (no path:line or packet-routing statements), so the checks were against the vault's own pages.

**Corrections:**

1. `old:` Dungeon pages: [[Sandscale Oasis]] (written), [[The Rumbledome]] and [[Precursor Ruins]] (not written yet).
   `new:` Dungeon pages: [[Sandscale Oasis]], [[The Rumbledome]] and [[Precursor Ruins]] (all three written).
   `why:` repo:notes/Build Guides/Content/Dungeons/The Rumbledome.md:1-19 (full dungeon page, `zone: Sunstone Valley`, overview table); repo:notes/Build Guides/Content/Dungeons/Precursor Ruins.md:1-20 (full dungeon page with overview table); repo:notes/Build Guides/Content/Dungeons/Sandscale Oasis.md:1-20 (full page, already correctly marked written).

2. `old:` **Pages not yet written** that this page links: [[The Rumbledome]], [[Precursor Ruins]], [[NPCs - Shrouded Glade]]. [[Sandscale Oasis]] exists.
   `new:` **Linked pages, all now written:** [[The Rumbledome]], [[Precursor Ruins]], [[Sandscale Oasis]] (in `Dungeons/`) and [[NPCs - Shrouded Glade]] (in `NPCs/`).
   `why:` repo:notes/Build Guides/Content/Dungeons/The Rumbledome.md:7, repo:notes/Build Guides/Content/Dungeons/Precursor Ruins.md:7, repo:notes/Build Guides/Content/Dungeons/Sandscale Oasis.md:7 (each has its `# Title` heading and content); repo:notes/Build Guides/Content/NPCs/NPCs - Shrouded Glade.md:1-9 (exists, same folder listing).

**Checked and holding:**
- Part row counts for Parts A to C: 7, 5 and 5 rows, matching the note (repo:notes/Build Guides/Content/NPCs/NPCs - Sunstone Valley.md:33-39, 47-51, 59-63).
- Blacksmith rows 33 to 42 exist as described (repo:notes/Build Guides/Content/Jobs/Blacksmith.md:152-161).
- Card Duelist Part 5 rows 57 to 62 exist (repo:notes/Build Guides/Content/Jobs/Card Duelist.md:171-176).
- Link targets [[Blacksmith]], [[Miner]], [[Brawler]], [[Card Duelist]], [[Demolition Derby Driver]], [[NPCs - Wilds]], [[NPCs - Blackspore Swamp]], [[NPCs - Briarwood]] and [[NPCs - Sanctuary]] all resolve to existing files.

**Unsure:**
- Row counts for Parts D to J (69 NPC rows, 81 named NPCs), the Gateway's "21 named NPCs and 28 quest rows", and the non-job quest total of 81 were not recounted. The table search output stopped listing rows after line 63.
- The "free to level 20" claim is client-text and is not checked against our code.
- The Pony Vale line of "four wiki quest pages" was not checked; it depends on the refs archive, not the repo.
