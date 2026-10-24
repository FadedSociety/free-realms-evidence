<!-- fleet job=guide-refresh id=Content-Dungeons-Snatching-Snappers status=nothing_found turns=18 usd=0.0195 tokens(read,write,in,out)=[466066, 55080, 38, 15939] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Snatching Snappers.md

**Verdict:** current. The note makes no claims about our server's implementation status (no "built / missing / not routed" statements, no code paths). Its checkable claims are about client strings, the wiki and video, and these hold at the tip.

**Corrections:** none.

**What I checked and confirmed:**
- Client names and panel text: "Snatching Snappers!" (`loc 1259532086`, `3091471312`), "Bothersome crays are stealing…" (`3024485759`), "Defeat the Cray Snappers." (`2923271887`), "Bonus: Pop all of the bubbles" (`3583207144`), "Find a way to pop the bubble!" (`31303853`), bonus group names (`2372301333`, `2637611448`), "Cray Snapper" (`1585721449`, `3120660947`), "Requires a level 5 combat job" (`2145075890`). All present in `repo:` ... `FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat`. The `loc` IDs in the note are the `.dat` IDs, not the keys of the `locale` tool, so they do not resolve there. That is a convention issue, not an error in the note.
- Duane's quest text (`3225763451`), "Return to Duane…" (`2932791523`), "Come back again tomorrow night…" (`100264`), and the "Finding the Raiders" title (`3524069531`, game data `922726292`).
- Prize wheel: all 24 gear names exist in the locale, as the note says (e.g. `Archer's Composite Bow of Stunning`, `Ninja's Scythe of Shadow Armies`, `Scholar Wizard Shoes`). The wheel also has "Battle Item Mystery Pack" and "2 Coins". Matches `refs:freerealms-wiki/wikitext/4633-49836-472e162ee5bf.wiki` lines 20–66.
- Wiki claims in the note match wiki revision 4633: "Sand area", "Levels 5 and higher", "(5)" bubbles, "74 Stars", "Members Only Bonus: 31 Coins", difficulty 3, Special Spawn and Seaside categories, and "only found during night".
- Our content file `prototype/osfr-tools/data/content/dungeons/snatching_snappers.json` cites this note for name and difficulty. The note's claims agree with it.

**Unsure:**
- `You receive 10 stars and 7 coins` (video `nDX88pgHwSg/00068`): not in the locale file. The note already marks it low-confidence. "Goal Update" and "New Goal" exist as separate locale strings, so the video chat lines are plausible.
- Video-only claims (marker distance 43–62 m, "Enemies Defeated 10", "Knockouts Remaining 3/3", the 100000 total) could not be checked from the repo. The arithmetic adds up: 3000 + 67000 + 25000 + 5000 = 100000.
- Conflict 2 says other pages infer 5 knockouts. That is true for Briarheart Caverns, Snowy Canyon and Dungeons.md. But Seaside Swoopers and Stealthy Despoilers also show "Knockouts Remaining 3/3" in video, and Feisty Floren shows 1/3, which supports the note's doubt about the 5 figure.
- Line 20 "Click a Snatching Snapper (red enemy marker)" and the "Story hook" citation of `3225763451` (Duane's quest line, not a story line) are not checkable or are minor.
