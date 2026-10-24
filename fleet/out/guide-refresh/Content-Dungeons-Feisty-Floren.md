<!-- fleet job=guide-refresh id=Content-Dungeons-Feisty-Floren status=done turns=12 usd=0.0121 tokens(read,write,in,out)=[206543, 34915, 26, 11256] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Feisty Floren.md

**Verdict:** current apart from one overstated negative in the Requirements table (minor drift). The note makes no claims about our Rust code (no path:line, packet or feature-status statements); its checkable claims are about client strings, cross-links and the prize tables, and nearly all of them hold against the client locale.

**Corrections:**

- `old:` No level-3 string exists in the client.
  `new:` No level-3 combat-job gate exists in the client: the battle tier strings are level 5, 9 and 13 (locale rows 4189–4191 and 4199–4201). "Level 3" appears only in equipment text ("Wearable by a level 3 or higher ...", e.g. rows 42431, 42521).
  `why:` client locale rows 4189–4191 ("You must have a combat job of at least level 5/9/13 to play this battle") and 4199–4201 ("Requires a level 5/9/13 combat job"). The literal "no level-3 string" is false because equipment rows 42431+ contain "level 3". The conclusion (no battle gate for this difficulty-2 node) still holds.

**Checked and holding (no change):**
- Client names and panel text: "Feisty Floren!" (141040), "Feisty Floren! Bonus" (141117), "Corrupted Floren are absorbing the life…" (141113), "Defeat the Floren!" (141115), "Restore Nature!" (141120), "@1 Knockouts Remaining" (419881), "Bonus: 37 Coins!" (5538), "Defeat Feisty Floren in the Pixie Nursery." (388440), "Defeat the Feisty Floren" (417354), "Contract: Fending off the Floren" (388408) and its "snakes and floren … near the Pixie Nursery" text (388409), and the lore line about pixies (382988).
- Prize wheel items all resolve as exact client strings: e.g. Ninja's Blade of Shuriken Storm (131978), Warrior's Axe of Earthquake (132008), Wizard's Wand of Firestorm (132038), Archer's Horse Bow of Explosions (131888), Point Blank Archer Quiver (132751), Hedge Wizard Talisman (133409), Battle Item Mystery Pack (6666), and the level-8 Archer's Composite Bow of Splintering (131893).
- Cross-links resolve: [[Floren Forest]], [[Petty Yetis]], [[NPCs - Wugachug]], [[Ree Peatpants]] (NPC notes), [[Ninja]], [[Content]], [[Dungeons]] all exist under `notes/Build Guides/Content/`. No Autopilot report touches this battle.

**Unsure:**
- `Zone: [[NPCs - Wugachug]], Pixie Nursery.` The Pixie Nursery's own NPC section is `notes/Build Guides/Content/NPCs/NPCs - Wilds.md` Part C (line 61), and the Wugachug note sends Pixie Nursery NPCs to `NPCs - Wilds`. The Wugachug note (line 24) does point the Feisty battle back to this page, so the link is defensible. I did not change it; a reader may want both links.
- "Enemies Defeated 2 = 500" is cited to video only. A locale search for "Enemies Defeated" found no row, so the results-row label may be video OCR and not client text. Left as written.
- The note's `loc <hash>` ids (e.g. 2647353816, 945685471) do not resolve in the locale tool, which indexes by row number. I matched the texts by content instead, so the ids themselves are unverified.
- Wiki-only claims (119 stars, 8-coin slot, members-only bonus, the Snow Days toy, the 10-target bonus) cannot be checked against the code or client.
