<!-- fleet job=guide-refresh id=Content-Dungeons-Frostfang-Caverns status=nothing_found turns=24 usd=0.0320 tokens(read,write,in,out)=[1169418, 93280, 52, 17245] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Frostfang Caverns.md

**Verdict:** current. I found no claim in the note that is false at the tip. I checked about 20 claims, and the note's citations line up with the repo and the client.

**Corrections:** none.

What I checked and found consistent:
- **Entrance, difficulty, members flag:** `prototype/osfr-tools/src/restoration/piece_059.rs:167` has row 30 "Frostfang Caverns", difficulty 4, members false, entrance `barrier` in Snowhill. The note's Overview and Requirements agree.
- **Level 9 requirement:** `prototype/osfr-tools/data/content/dungeons/frostfang_caverns.json:108` has `minimum_combat_job_level: 9`, matching the note.
- **Achievements:** `prototype/osfr-tools/data/content/achievements.json:3636-3650` gives bronze, 5 points, and `:4500-4512` gives silver, 10 points. Both match the Rewards table.
- **Wiki goals, rewards, wheel and bonus clothing:** the cached wiki page `refs:freerealms-wiki/wikitext/4606-49145-7caf7ea6c38d.wiki` lists "Investigate the cavern!", "Bonus: Defeat the giant bat!", "242 Stars or less", "Members Only Bonus: 220 Coins", 97 Coins on every wheel, the six wheel item lists, the bonus clothing sets, and the "Free Realms Combat Design Portfolio" source. All match the note.
- **Wiki 242 Stars on Sweetwater Climb:** the Sweetwater Climb note does print "242 Stars or less", so the note's cross-reference is true.
- **Client text:** I checked about 40 client strings against `client/locale/en_us_data.dat`, including quests, boss strings, crawler and wolf names, the Frostfang bat, the Frostfang Caverns Bonus Objective, group and win strings, and the level-9 lines. They exist with the wording the note quotes.
- **Loc ids:** the note's ids (for example 238419199, 1220971519, 3433368763) are real ucdt/ugdt keys in the client's `en_us_data.dat`. The lab export `locale-id-to-text.json` uses a different sequential id space (for example "Investigate the cavern!" is 6590 there), so the note's ids are not wrong. I would not change them.
- **Enemies:** `enemies.json` has a "Giant Bat" entry, and the note's client placement is consistent with it.

**Unsure:**
- The note's Overview says the wiki's difficulty is 4. The cached wiki page also has a `Category:Difficulty 1` tag on the same page. This is a wiki-side quirk, and the note's "difficulty 4" matches the page text and piece_059.
- The wikilink targets [[Chillblaine]], [[Teek]], [[Wintara]], [[Iris]] and [[Sir Whittington]] were not confirmed as existing note files. I did not find separate pages for them in `notes/Build Guides/Content/NPCs/`, but I did not search the whole vault.
- The note's `Frostfang Caverns` dungeon JSON is marked "reconstructed" for entry requirements and encounters, and the note does not claim it is playable. The Build Ledger says no dungeons beyond the cave are playable. That is consistent with the note, but I did not check it further.
