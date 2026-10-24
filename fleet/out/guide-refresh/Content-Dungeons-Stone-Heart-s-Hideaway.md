<!-- fleet job=guide-refresh id=Content-Dungeons-Stone-Heart-s-Hideaway status=nothing_found turns=19 usd=0.0167 tokens(read,write,in,out)=[498851, 47194, 40, 11636] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Stone Heart's Hideaway.md

**Verdict:** current. The note makes no claims about our Rust code or its build status, and every checkable client, wiki and cross-note claim I tested still holds at the tip.

**Corrections:** none.

**What I checked (all held):**
- Locale ids and texts: 1061411996 and 567675672 (title), 1547462355 (panel), 1323029355 (level 13 line), 813734101 and 756429409 (goals), 419255199 and 945500272 (Stone Heart), 3155888320 (entrance), 2061189905 and 1251788045 (hideout lines), 1476572121 and 2060386145 (story visit), 647024719 (defeat cry), 1447454725 and 2940859742 (flowers), 1732182403 and 219715362 (OnHit and Invuln flags), 2810703753, 1289244022 and 2008038419 (abilities), 3770695936 and 2517159261 (minions), the six level-16 weapon names, 1980584385 and 3597859952 (treasure and roses), and the vday dev-note ids. All resolve in `client:locale/en_us_data.dat`. The "Stoneheart" promo line (808006887) exists. No "Group: Stone Heart" or "Bonus Objective" string exists.
- Wiki claims: level 13 combat job, members-only quote, "repeatable once a day", Tier 5 and Tier 1 for the two battles, the "Blasted birds" and "Invaders! Changelings!" quotes, and the level-16 weapon "Hideway" spelling all appear in `refs:freerealms-wiki/wikitext`. The attack damage values 2372, 2609 and 6575 also match the wiki.
- Repo consistency: `notes/Build Guides/Content/Dungeons/Dungeons.md:147` lists Stone Heart's Hideaway as 5 / 13 / Merry Vale, which matches this note. `prototype/osfr-tools/data/content/field_battles.json` (around lines 829–922) uses level 13, difficulty 5, and the western-side entrance, consistent with the note.

**Unsure:**
- Video ids `GR0ORW4cWts/00008` and `Gk3v5EcwUBc/00014`. The video frames are not in the repo, so I could not confirm them. `NPCs - Merry Vale.md:208` cites `Gk3v5EcwUBc/00000` for the same Softening the Stone tracker, so one of the two citations may be off.
- "No lobby frame was found" and "no wiki page of its own" could not be checked against the video index or wiki index.
- The "Sleeping Pixie" quest row (Cudip, wake Arianna) was not checked against the locale.
- The repo has a built and tested slice of this instance (`prototype/osfr-tools/tests/dungeon_stone_heart.rs`, plus `field_battle_roster.rs`). The note never mentions it, so this is a coverage gap, not a false claim.
