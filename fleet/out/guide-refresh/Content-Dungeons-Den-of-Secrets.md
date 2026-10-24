<!-- fleet job=guide-refresh id=Content-Dungeons-Den-of-Secrets status=done turns=22 usd=0.0229 tokens(read,write,in,out)=[796396, 61198, 46, 14583] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Den of Secrets.md

**Verdict:** current, with one minor drift. The note is almost entirely client-locale and video evidence, so there are few claims about our own code to check. I checked the code-facing claims (difficulty, entrance, zone, dungeon record, enemy and goal names) and a sample of about 90 `loc` IDs against the locale mirror in `refs`. Nearly all hold. The one false statement is a literal overstatement in the Requirements table.

**Corrections:**

- `old:` No level-3 string exists in the client.
  `new:` No dungeon level-recommendation string exists in the client (the "recommended level" search finds nothing). The only "level 3" strings are gear tooltips, e.g. "Wearable by a level 3 or higher Warrior." and a miner message, so the level-3 wording comes from the wiki.
  `why:` The client does contain level-3 strings, just not for dungeons. `refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat` has "Wearable by a level 3 or higher Warrior/Archer/Medic/..." and "Sorry, you need to be at least a level 3 Miner to mine Iron." The difficulty-2 recommendation comes from `repo:prototype/osfr-tools/src/restoration/piece_059.rs:9` (wiki policy: "2 recommends level 3"), which matches the note's Requirements row.

**Checked and holding (no change):**
- Dungeon difficulty 2, zone Merry Vale, barrier entrance: `repo:prototype/osfr-tools/src/restoration/piece_059.rs:148` (`row(11, "Den of Secrets", 2, false, Some(30445), None, Some("mv_den_of_secrets"), E("barrier", ...Merry Vale...))`).
- Stub zone only (84-byte header stub, no real map): `repo:prototype/osfr-tools/src/restoration/piece_059.rs:18` and `:25-26`. The note does not claim otherwise.
- Achievement "Complete the Den of Secrets encounter." and "Group: Den of Secrets" with the full-group wording: `repo:prototype/osfr-tools/data/content/achievements.json:3207-4072`.
- Two "NOT USED" entries (`2614537499` ugdt, `2906953785` ucdt): confirmed in the `refs` locale dat.
- Locale IDs for the Den name, panel text, Liana, pillars, quest descriptions, Shaggy/Mayor/Tumbolina/Meliee lines, boss ability and orb names, and the necrowart enrage text: all match the `refs` locale dat.
- Prize-wheel item names (all 12 sampled) exist in the client locale.

**Unsure:**
- The note cites video `Sy-W_AHbwcw/00010 to 00398` for the Warrior 7 run (Seen playing at, Main goal). `repo:notes/Build Guides/Content/Jobs/Warrior.md:188` gives `00010 to 00396`, and `repo:prototype/osfr-tools/data/content/enemies_unresolved.json:11416` cites `00366 to 00398`. The frame ranges disagree between notes, and I could not check the video frames. Confirm the end frame before aligning the two notes.
- The dungeon JSON (`repo:prototype/osfr-tools/data/content/dungeons/den_of_secrets.json`) cites this note's sections as its evidence. Its main encounter has no goals or rewards, so it does not contradict the note. Nothing in the repo shows Den of Secrets as playable or built, and the note makes no such claim.
- Video-only claims (Warrior 7, counter values, 5:42 purchase, frame ranges) and the wiki-only claims (74 Stars payout, 26 and 73 coins, Sammy) were not checkable against the code.
