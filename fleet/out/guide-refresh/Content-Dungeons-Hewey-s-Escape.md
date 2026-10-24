<!-- fleet job=guide-refresh id=Content-Dungeons-Hewey-s-Escape status=nothing_found turns=22 usd=0.0259 tokens(read,write,in,out)=[840409, 72120, 46, 16925] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Hewey's Escape.md

**Verdict:** current. Every checkable claim about our code and status that I could reach still holds at the tip. No corrections.

**What I checked (all consistent):**
- **Removed status.** The note's "Removed content" callout matches the recovered roster, which marks Hewey's Escape `removed` (`prototype/osfr-tools/src/restoration/piece_059.rs:141`). The test asserts that the only two removed rows are Hewey's Escape and King of the Ring, with no objective locale and no zone (`prototype/osfr-tools/tests/piece_059.rs:83-90`, `:253`). The wiki list also says "(removed)" (`refs:freerealms-wiki/wikitext/2225-46578-c2dd4d3b92d7.wiki:29`).
- **Difficulty 1, no job level.** `piece_059.rs:141` has difficulty 1. The rank-1 entry rule has no minimum combat level (`piece_059.rs` tests, `entry_rule(1)`), matching "Combat job level: None."
- **Name and string IDs.** `data/content/dungeons/hewey_s_escape.json` uses `name_string_id` 241400652, matching the Overview.
- **Coins and stars.** The dungeon JSON has `coins: 36` on the prize-wheel slot (`hewey_s_escape.json:619`). Stars "10 Stars" appears as wiki text (`:527`). Both match the Rewards section and `Dungeons.md:24`.
- **No bonus goal, no achievement.** `Dungeons.md:57` lists Hewey's Escape among the dungeons with no bonus-objective string. `Dungeons.md:168` and the piece_059 "37 of 43" achievement block (`piece_059.rs:11-13`) agree that it has no encounter achievement.
- **Goals (1).** `Dungeons.md:38` matches.
- **Quest and NPC IDs.** `quests/brawler.json:656-664` has "Brawler: Hewey's Escape!" with title IDs 4204217995 / 3490633876. `npcs/highroad_junction.json:369-383` has Archy's line (973814746), the 1605633744 text and the 300747673 / 1107073768 objectives. `highroad_junction.json:5025` has the Harold trainer IDs. The Harold / Archy / Hewey IDs match `NPCs - Highroad Junction.md` and `NPCs - Durango Zoo.md`.
- **Glove names.** `field_battles.json:1467` has "Saved by the Bell Brawler Gloves" (client item). The Conflicts section is consistent with this.
- **Conflict 1 (Adherent Wizard).** The Adherent Wizard set is on the Bandit Hideout wiki page (`notes/Build Guides/Content/Dungeons/Bandit Hideout.md:76`) and on Croaking Vale (`Croaking Vale.md:74`), as the note says.
- **Dungeon not in the achievements list.** `achievements.json` has no Hewey entry (repo-wide search).
- **Entrance IDs.** `hewey_s_escape.json:276` carries the same entrance-sentence IDs (3403732640 and 3216721027 / 321672102…) as the note.

**Unsure:**
- **Entrance trigger type.** The note says "A gate". The recovered roster records the Hewey entrance trigger as `"barrier"` (`piece_059.rs:141`). That field is derived from the wiki entrance sentence, while "gate" comes from the client prompt. The two are not clearly contradictory, so I did not correct it. Someone should decide which label the guide should use.
- **Wikilinks without a note file.** `[[Harold]]`, `[[Assistant Archy]]`, `[[Merigold]]` and `[[Gerold]]` in the Related quests section and the closing NPC line appear to have no standalone note in `notes/` (no `# Harold`-style heading, no aliases). I could not confirm whether Obsidian resolves them some other way.
- **"loc" IDs.** The `loc <id>` numbers in the note (for example 2247616509, 1107073768) do not resolve through the `locale` tool, which uses row numbers. The repo's own records use the same hash-style IDs, so this is probably a convention difference, not an error. I did not verify the client-side IDs independently.
- **Wiki-only claims.** I did not verify the wiki revision date "2025-02-05", the Atlas icon, "Hewey's Bear Claw" as the quest reward, or the Harold coaching lines. These need the video or client sources, not the repo.
