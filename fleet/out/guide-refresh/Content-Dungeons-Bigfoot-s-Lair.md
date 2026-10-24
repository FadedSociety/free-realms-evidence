<!-- fleet job=guide-refresh id=Content-Dungeons-Bigfoot-s-Lair status=nothing_found turns=18 usd=0.0227 tokens(read,write,in,out)=[713086, 71218, 38, 13233] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Bigfoot's Lair.md

**Verdict:** current. The note is almost entirely client, video and wiki evidence, and the code side is consistent with it. I found no claim about our code or status that is now false, and no path:line citation that moved.

**Corrections:** none.

**What I checked:**
- Client strings quoted in the note exist in the locale table: "Defeat Bigfoot!", "Goals (1)"-era goal text, "Requires a level 5 combat job", "You must have a combat job of at least level 5 to play this battle", "Bigfoot Rock Throw", "Bigfoot Rage Resist", "Bigfoot is Robbie Proc", "Speak to Counselor Edmond", "Return to Chatty", "Talk to Bob", "Confront Bigfoot", "Camp Chatty Hat", and the Robbie/Chatty prize-item names. The dialogue lines quoted in the In-instance table all match locale text.
- The game-data name id `591464176` in the note matches `name_string_id` in `prototype/osfr-tools/data/content/dungeons/bigfoot_s_lair.json:7`. The "Goals (1)", difficulty 3, 990-coin and 102-star figures agree with `notes/Build Guides/Content/Dungeons/Dungeons.md:30` and `:38`.
- The index note (`Dungeons.md:7`) still lists the entry, which matches Conflict 2.
- No code under `prototype/` (Rust or data) implements or routes Bigfoot's Lair. Its only data is the reconstructed `bigfoot_s_lair.json` stub, with empty goals and rewards. The note does not claim otherwise, so there is nothing to correct.

**Unsure:**
- **Locale hash ids.** The note cites hashed ids such as `loc 1087603867`, `loc 2145075890` and `loc 591464176`. The locale tool takes row numbers (for example 428981 = "Defeat Bigfoot!"), so I could not confirm the hashed ids directly. The text they point to does exist.
- **Quest-complete and reward strings.** "Quest Completed! Confronting Bigfoot" and "You receive 1 Camp Chatty Hat" did not appear in a locale search, so the `loc 3789252990` citation is unverified.
- **Coin comparison (Conflict 3).** "The other level-5 entries in this guide pay 26 to 117 coins" is only partly supported. `Dungeons.md` gives 112 for Bone Bog Cemetery (difficulty 3). I did not check the wheel coins of the other level-5 pages (for example Snatching Snappers, Mushroom Gigas, Return to Sender), so I cannot confirm the range.
- **Dangling links.** The "NPCs:" line links `[[Counselor Edmond]]`, `[[Counselor Tyra]]` and `[[Robbie]]`, and the "Related quests" table also links `[[Counselor Edmond]]`. No such files exist under `notes/Build Guides/Content/NPCs/`. The Dungeons index says unwritten pages are linked anyway, so this may be intended. Only `[[NPCs - Greenwood Forest]]` exists.
