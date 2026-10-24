<!-- fleet job=guide-refresh id=Content-Dungeons-Treasure-of-the-Bone-Shaman status=done turns=18 usd=0.0189 tokens(read,write,in,out)=[569413, 54388, 38, 12826] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Treasure of the Bone Shaman.md

**Verdict:** current, with one minor drift. Nearly every client-side fact checks out against the shipped locale table. The note makes almost no claims about our own code, so most checks were against the client data and the other notes it cites.

**Corrections:**

- `old:` No bonus goal on the wiki; no "Bonus" string in the client.
  `new:` No bonus goal on the wiki; no bonus-goal string for this battle in the client. The only "Bonus" strings tied to it are generic reward labels such as "Bonus: 22 Coins!" (`loc 343739712`).
  `why:` The client does contain "Bonus" strings. `locale/en_us_data.dat:9148` (343739712, "Bonus: 22 Coins!") and `:946` (36659497, "Bonus: 42 Coins!") are the two this note itself cites. Other battles carry bonus-goal text, e.g. `locale/en_us_data.dat:7713` "Bonus - Don't get knocked out". The claim as written is false; the narrower version is what the evidence supports.

**Checked and holding:**

- Battle name, panel text, story hook and goal (`2078165185`, `2313181541`, `1171524917`, `2748995221`) match `locale/en_us_data.dat:54760`, `:60868`, `:31004`, `:72423`.
- Level strings: only 5, 9 and 13 exist (`2145075890`, `1291047686`, `1323029355`), matching `locale/en_us_data.dat:56469`, `:34198`, `:35027`.
- Enemy and objective strings exist (`552820187`, `2838100449`, `3444345488`, `3742929397`, `3569821255`, `2703712326`, `798727812`, `3678256854`, `2032978880`, `3319862974`, `3461100541`).
- Bruce's id `255196100` and `533439775` match; the Natali contract titles and text match.
- Every prize-wheel item name exists in the locale table, so "every name above is an exact client string" holds.
- "No 'Win Combat Encounter' string for it": there is none for this battle, only for other dungeons.
- Zone wording: `notes/Build Guides/Content/Dungeons/Dungeons.md:119` files this battle under Blackspore Swamp, which matches Conflicts item 1.
- Cross-links resolve: `Forest Troll Fort.md` exists and gives the Northern Wilds zone; `NPCs - Wilds.md` exists; Natali and Bruce are sections in the NPC notes, not standalone pages.

**Unsure:**

- The `loc <id>` numbers in the note are the hash keys in `client/locale/en_us_data.dat`, not the numbering the `locale` tool uses. The tool returns "no such id" for them, so I verified them by grepping the data file. This is not an error in the note, but a lookup by these ids will fail.
- Stars (104) and coins (22) are wiki figures and cannot be checked from the code or client.
- The Bruce "patched shut" area and the Forest Troll Village position cannot be settled from the repo.
