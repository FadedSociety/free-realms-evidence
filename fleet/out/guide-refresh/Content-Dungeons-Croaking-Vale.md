<!-- fleet job=guide-refresh id=Content-Dungeons-Croaking-Vale status=done turns=17 usd=0.0208 tokens(read,write,in,out)=[603826, 65679, 36, 13162] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Croaking Vale.md

**Verdict:** minor drift. Nearly all client-sourced claims hold. Almost every `loc` id cited resolves to the stated text in the shipped locale table (`refs:opening-harvesting-native-20261009T132512Z/locale/en_us_data.dat`), including the "Hanna" panel line (933164626), "Requires a level 9 combat job" (1291047686), "Defeat Han and Hannah in the Croaking Vale!" (2047754171), "Free any captured frogs you find!" (3578722944), the boss names, the internal "croaked vale 59" strings, and the quest descriptions. The note makes almost no claims about our server code. The one stale statement is a gap that the Archer job page has since partly closed. `data/content/dungeons/croaking_vale.json` has empty goals and rewards, which matches the note's "gaps" framing and is not a false claim.

**Corrections:**

- `old:` - Which quest owns each description above (titles) and their rewards.
- `new:` - Which quest owns each description above (titles) and their rewards. The Orson description `3907807754` is quest 26, "Archer: Remain Vigilant" (title `ucdt 464590162`), per the Archer job page; the other rows are still unowned.
- `why:` `repo:notes/Build Guides/Content/Jobs/Archer.md:121` maps `3907807754` to quest 26 and gives its title; `464590162` resolves to "Archer: Remain Vigilant" in `refs:opening-harvesting-native-20261009T132512Z/locale/en_us_data.dat:12349`. Archer.md:189 also lists this dungeon under quest 26.

**Unsure:**

- **Level 9 panel line.** The note says the Croaking Vale panel reads "Requires a level 9 combat job" (`loc 1291047686`). Several sibling dungeon notes (Shady Smugglers, Moldy Shamblers, Darvon's Descent, Frostfang Caverns, Prince of Low Tide) call that same string generic per tier and not tied to a dungeon by name. The locale confirms the string exists (`4200: Requires a level 9 combat job`), but I could not confirm that this panel is the Croaking Vale one.
- **"Member's Only Bonus!" heading.** The locale has "This special reward is only available to members!" (427738) and "If you were a member, you'd receive this special bonus!" (427737). I did not find the exact heading "Member's Only Bonus!" in the locale. It may be a UI string under another id.
- **Wiki and video figures** (202/304/308/583 coins and stars, group size, enemy counts, "Goals (2)", member/non-member screens, the prize-wheel drops). I could not check these from the repo or the cached refs. `refs:freerealms-wiki/wikitext-newline-correction.json:3400` only holds a hash for the wiki page, not its text.
- **Entrance and atlas.** The "Click the barrier in Nettleseed, Briarwood" claim agrees with `prototype/osfr-tools/src/restoration/piece_059.rs:165`, but I did not check the "Atlas icon exists" claim.
