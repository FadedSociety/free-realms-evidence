<!-- fleet job=guide-refresh id=Content-Dungeons-Snakes-in-a-Maze status=nothing_found turns=16 usd=0.0177 tokens(read,write,in,out)=[431366, 50223, 34, 14297] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Snakes in a Maze.md

**Verdict:** current. Every checkable claim I tested holds at the tip; I found no false statement and no moved citation.

**Corrections:** none.

**What I checked:**
- **Repo code.** No code, test or Autopilot report implements or mentions Snakes in a Maze, so the note makes no code-state claim to check. The only repo references are other notes, plus the generated `dungeons_unresolved.json` / `enemies_unresolved.json`, which cite this note. The note's own link target, `The Snarling Hedges.md`, exists, and so does its index entry in `Dungeons.md`.
- **Name and description IDs.** `1748558207` ("Snakes in a Maze"), `2702431099` and `3583000408` ("Snakes in a Maze!"), `3779511659` and `350402694` ("NOT LIVE - Snakes In a Maze"), `4050579400` (panel description), `4283649743` ("Defeat all of the snakes!"), `580361275` and `3342657809` (maze and "hegde" variants) all match `client:locale/en_us_data.dat`.
- **Level strings.** `2145075890`, `1291047686` and `1323029355` are "Requires a level 5 / 9 / 13 combat job". `3137861621` is "Required".
- **Enemies and abilities.** The Asp and Cobra names (`1935444348`, `4167186094`, `105919611`, `3862166462`), the quest text `2810740797`, the hints `911492415` and `4023818094`, and the ability strings `629344352`, `3073611076`, `3916944133` and `4188969632` all match.
- **Rewards.** `2664870581` is "Bonus: 37 Coins!". No "Win Combat Encounter Snake…" string exists, which supports the no-achievement claim.
- **Prize wheel names.** Every item the note lists exists in the client locale, including the less obvious ones (for example "Warrior's Cudgel of Cleaving" `2631981262`, "Ninja's Training Sword of 1000 Storms" `3618070379`, "Archer's Power Shard of Vitality I" `2240045890`, "Medic's Ring of Energy I" `2139428201`, "Saved by the Bell Brawler Pants" `3572606308`, "Kusa Ninja Hakama" `2674969453`, "Novice Wizard Skirt" `3177266515`, "Standard Action Warrior Breeches" `4059144472`). The conflict claims also hold: "Hen Feather Archer Pants" and "Stable Condition Medic Fatigues" have no client match, while "Hen Feather Archer Leggings" (`493943759`, `2986377167`) and "Stable Condition Medic Pants" (`1980737962`) do.

**Unsure:**
- The "Client level strings exist only for 5, 9, 13" claim is not contradicted, but the client also has battle-gate text at IDs 4189–4205 ("You must have a combat job of at least level 5 to play this battle", and so on) for the same three levels. The word "only" is broader than the evidence; I left it alone.
- Video claims (Amazing Asp markers at 46–62 m, `piWfe7lXZ9I/00057`, `00096`), the wiki-only rows (difficulty, "Required: Level 1, Any Combat Job", 74 Stars, 37-coin members bonus), and the "Members only: No" row. These cite the fan wiki or video frames, which I did not re-check.
