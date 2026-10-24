<!-- fleet job=guide-refresh id=Content-Dungeons-Frostfang-Snarlers status=nothing_found turns=13 usd=0.0114 tokens(read,write,in,out)=[262408, 37250, 28, 8294] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Frostfang Snarlers.md

**Verdict:** current. The note makes no claims about our Rust code or build status (no path:line, routing, or "not built" statements), and every client-side claim I could check matches the shipped locale and the repo data.

**Corrections:** none.

**Checked and matching:**
- Locale strings: "Frostfang Snarlers!" (ugdt 2846538967; ucdt 2082814897), "Knock out all Snarlers!" (2232341340), "Defeat the Snarlers!" (1394128387), "Frostfang Snarler" (1287937882), panel text "A pack of hungry wolves are endangering travelers!…" (text present at locale line 78097; the id is not checkable by the lookup tool), "Hungry Wolves" (1946868430, 101972945), "Frostfang Wolf" (1464698360, 1467111981), "Frostfang Alpha" (2559120146, 3628885318), "Contract: Trouble in Snowhill" (172639783), "Warrior: Warrior Warm-up" (1777367688, 1775539410), "Bonus: 70 Coins!" (1931562791), "Members Only Bonus!" (1925651180), "Battle Item Mystery Pack" (1225426704, 1725853870). Source: `refs:opening-journal-text-v2/locale/en_us_data.dat`.
- Direction lines: south-east at 937190059, 1962735708 and 3693529699 (three lines); west at 2218766120 (one line). Source: the same .dat file and the locale lookup (lines 77222, 77224, 91735, 100580).
- "Requires a level N combat job" exists only for 5, 9 and 13 (locale lines 4199 to 4201).
- No "Win Combat Encounter Frostfang Snarlers" string. The only match is "Win Combat Encounter Frostfang Caverns" (locale line 119157).
- Contract text "Ree Peatpants has asked you to defeat wolves and yetis in Snowhill." (locale line 388401).
- Wheel item names (Archer's Bow of Blizzards, Medic's Reflex Hammer of Vitals, Ninja's Training Sword of 1000 Storms, Wizard's Sparkle Twig of Glaciers, Saved by the Bell Brawler Gloves, Stable Condition Medic Gloves, Kusa Ninja Armwraps, Standard Action Warrior Gauntlets, Novice Wizard Gloves, Hen Feather Archer Gloves) all exist in the client's item strings.
- Repo: no Rust code mentions Frostfang Snarler or node battles (search of `*.rs` and all repo files). The only node-battle content is the reconstructed record `prototype/osfr-tools/data/content/dungeons/frostfang_snarlers.json`, which has empty goals and rewards. That matches the note's "not built" posture, though the note itself does not claim it.

**Unsure:**
- Ids `loc 4197571244` (Frostfang Snarler), `2857140979`, `2505559730`, `3912700565` (Warrior Warm-up objectives) and `2246368084` (panel text id) did not show up in the journal locale files I searched. The text is present elsewhere or under another file, so I could not confirm the ids.
- The wiki-sourced figures (86 Stars, 70 Coins as a members-only payout, "Level Varied", difficulty 1) cannot be checked against the tip. They are outside this audit.
- Video frame keys (`v1bVCKWiSvw/00000`, `DRoB1oX61Os/00100`, etc.) were not opened.
