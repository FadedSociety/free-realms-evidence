<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Farnum-Farmstead status=nothing_found turns=24 usd=0.0335 tokens(read,write,in,out)=[1180126, 94764, 52, 19664] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Farnum Farmstead.md

**Verdict:** current. I found no claim about our code or status that is now false, and no path:line citation that has moved. I checked only about 25 claims, so this is a sample, not a full audit.

**Corrections:** none.

**What I checked and found consistent:**
- Table counts. Parts A to F have 8, 4, 4, 3, 4 and 7 rows, which is 30. Part G has 18 rows. The "23 people" figure matches the names listed. The Quest index has 19 full-row entries (24 quests counted individually) and 22 page-only rows.
- Cross-links to job pages. Adventurer A4 to A11, B1 to B5 and D3 exist with the titles given. Archer rows 10 to 13 cover the four Vicki and Hilforn quests. Card Duelist rows 26, 27 and 66 match. Ninja X1 (3801319221) and Brawler BC1 exist. Brawler M15 is "I Want My Money!". Medic contract 3291191374 is in Medic.md. Chef E5 is Farming 101. Soccer Star row 10 is Sidekicks Steal.
- Dungeon links. Sheep Watch, Highroad Hijinx and Bandit Hideout all exist under `notes/Build Guides/Content/Dungeons/`. Sheep Watch Conflicts 3 is the boss-count item the note cites.
- Other NPC pages linked from the note (Cobblestone Village, Wilds, Greenwood Forest, Sanctuary, Lakeshore, Merry Vale, Briarwood) exist.
- Locale spot checks: the "southwest of Cobblestone Village" lines, the Garden Defense table line, the Gummyfruit/Rainleaf line and the "southwest of Queensfields" line all match the note's quotes.

**Unsure:**
1. **Coin rewards.** The note says the only known coin rewards are 3 coins for The Last Best Hope and 4 for Saving Farnum's Farm (from video), plus the wiki's 16 and 18. Repo design notes record different amounts from native test runs: `notes/Design/Opening Playthrough.md:62` (25 coins at Pappy's turn-in, 5 at discovery 2) and `notes/Reviews/Native Wolves and Anvil 183551.md:11` (18 coins from Cleetus). These look like our reconstructed test policy, which the note says it excludes, so I left the note unchanged. A reviewer who wants original-game values should look at them.
2. **Video-only claims.** I could not check frame keys or video distance labels, so I did not verify any `3caQP-As968/...` citation.
3. **Locale IDs.** The `locale` tool answers text searches, not the hashed ucdt/ugdt ids the note uses, so I could not confirm the numeric ids themselves. The quoted text does match.
4. **Wiki dates and revision stamps** (Rocky and Estus 6 August 2013, Vela 15 October 2013, page revision dates) are outside the repo and I did not check them.
