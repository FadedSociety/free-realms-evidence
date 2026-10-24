<!-- fleet job=guide-refresh id=Content-Dungeons-Petty-Yetis status=nothing_found turns=20 usd=0.0212 tokens(read,write,in,out)=[631276, 55991, 42, 15719] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Petty Yetis.md

**Verdict:** current. I found no claim in `Petty Yetis.md` that is now false or whose citation has moved. The note makes almost no claims about our code. Nearly all of it is about client locale text and wiki facts, and the locale text I could check matches.

**Checked and holding:**
- Locale names and ids. The `loc` numbers are hash keys in `client/locale/en_us_data.dat` (the `.dir` index lines up with them). These match the note: `4187994895` "Petty Yetis!", `1179069407` "Take down the yetis!", `1660577857` "Defeat Petty Yetis", `3174297856` panel text, `1639215719` lore, `526480359`/`1029928319` "Frosty Yeti", `3283929113` "Frosty Yetis can be found near Snowhill.", `321609134`/`1794714999` "Icy Yeti", `448701629`/`2464487978` "Invis Cube - Petty Yetis", `369489592`/`4188867461` "Petty Yetis Smashed", `2442311520`/`2116251839`/`3517209918` the 5/50/500 Yetis counters, `2853626813`/`328784467` Ree Peatpants contract text, `3823327910`/`3312519120` Frosty Yeti quest text, `172639783`/`3102829172` contract title.
- Prize-wheel items. All 30 names are present in the client, including `Archer's Horse Bow of Explosions` (inside `{n}…{pl=}` markup), so "Every name is an exact client string" holds.
- Negative claims. No "Members Only Bonus", "43 Coins", "Bonus: 43", "Primary: Take down" or "Win Combat Encounter Petty Yetis" string exists. "Recommended level" / "can be entered by anyone" text is absent. The only "Win Combat Encounter" near it is Frostfang Caverns.
- Cross-note consistency. `Dungeons.md` (line 124) lists Petty Yetis as difficulty 2, "none (3+ recommended)", Snowhill, which agrees with the Requirements section.
- Repo. `prototype/osfr-tools/data/content/dungeons/petty_yetis.json` cites this note's section headings (Overview > Client name / Entrance, Requirements > Combat job level / Unlocking quest), and all of them still exist. `tests/test_quest_coverage.py:150` (quest 1617 "disabled") and `notes/Tasks.md:36` do not contradict anything in the note, which makes no routing claim.
- Linked pages exist: `Frostfang Snarlers.md`, `NPCs - Snowhill.md`, and Ree Peatpants is listed in `NPCs - Snowhill.md`.

**Unsure:**
- Conflict 2 says the wiki "Yetis" has no exact client match. My partial scan of the locale did not show a standalone "Yetis" or "Yeti" string, but the search output was capped, so I did not fully settle it.
- The wiki-side claims (Pretty vs Petty infobox spelling, "Primary:" prefix, 93 Stars, 43 Coins, the 9-coin video frame) and the video frame keys cannot be checked against the code or client.
