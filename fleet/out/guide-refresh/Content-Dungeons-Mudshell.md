<!-- fleet job=guide-refresh id=Content-Dungeons-Mudshell status=done turns=11 usd=0.0130 tokens(read,write,in,out)=[233314, 47445, 24, 9543] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Mudshell.md

**Verdict:** current, with one minor quote drift. Every client string I could resolve matches the locale data, and the repo's Mudshell records (`prototype/osfr-tools/data/content/dungeons/mudshell.json`, `Dungeons.md` row 144) agree with the note's level 13 / difficulty 5 / Blackspore figures. The note makes no claim about server code or routing, so there is nothing about implementation to contradict.

**Corrections:**

- `old:` You defeated Mudshell? That's great news!
  `new:` You defeated Mudshell!? That's great news!
  `why:` The locale text for `loc 2348679444` is "You defeated Mudshell!? That's great news! <BR><BR>Hopefully that takes a little pressure off the people trying to make their living out here!" (`refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat:61745`, hash 2348679444). The note's quote drops the "!?".

**Checked and holding:**
- Name hashes: `loc 2340649041` and `134101591` both map to 78144 "Mudshell" (`notes/Autopilot/T034.md:56`, `:69`). `Mudshell Test` 111570095 / 1628495246 / 380435073 exist.
- Goals: "Defeat Mudshell." (4152822208) and "Defeat Mudshell" (1759338718) are both in the locale data.
- Requirement line "Requires a level 13 combat job" (1323029355) exists as written.
- Quest text: The Hunt for Mudshell title (3656682846 / 1810667295), the two quest-side objectives, and the Chloe follow-up (668849672) all match.
- Ability strings (1689306040, 3901275544, 4287042850, 4085900906) match.
- Prize wheels: every item name in the six wheel lists exists in the client locale, including the Brawler and Archer items named in the Conflicts section. "Bare-Knuckle Brawler Shoulderpads" is 500631404 / 132908 and "Brawler's Atlas Hammer of Rage" is 841605518 / 131942.
- Briarheart Caverns = 311 stars (`notes/Build Guides/Content/Dungeons/Dungeons.md:33`), which the note's Conflicts item 3 cites correctly.

**Unsure:**
- The Archer wheel lacking a Battle Item Mystery Pack, and the wiki's "Bare-Knuckle Brawler Shoulder Pads" and "14 Stars" / "Members Only Bonus: 95 Coins" figures. These come from the fan wiki. I found the Mudshell wiki page only as a title in `refs:freerealms-wiki/wikitext-newline-correction.json:8555`, with no readable body, so I could not check them.
- Video-only claims (the 48 m red marker, the Hunt for Mudshell chat sequence, no quest reward shown). I did not check the recordings.
- The `dungeons_unresolved.json` entries for the wheel items (`owner: mudshell`) confirm that those items are named but have no item IDs. That is a data gap, not a note error, so I did not correct the note for it.
