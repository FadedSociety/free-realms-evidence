<!-- fleet job=guide-refresh id=Content-Dungeons-Tanglewood-Fort status=nothing_found turns=19 usd=0.0218 tokens(read,write,in,out)=[674772, 63790, 40, 14132] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Tanglewood Fort.md

**Verdict:** current. I found no false claims in `notes/Build Guides/Content/Dungeons/Tanglewood Fort.md`. The note makes almost no claims about our code, so I checked its client-text, status and cross-note claims against the locale, the dungeon data and the vault.

**Corrections:** none.

**What I checked and found consistent:**
- Quoted client strings exist in the locale. Examples: the goal texts "Defeat the Chugawug Archers and Soldiers!", "Speak with Chef Truffenglug.", "Wrangle up the escaped boars!", "Defeat Blacksmith Brix!", "Defeat Commander Kluggenkrush!", "Check in with the Chugawug Lookouts on the battlements!" and "Tanglewood Fort Bonus Objective". Also the Overview and Quest texts, "Captain Chugug in Briarheart, beyond Tanglewood Fort", "Tanglewood Fort Back Door", "Campaign 6: Tanglewood Fort" and "Win Combat Encounter Tanglewood Fort". (locale text table, by quoted text)
- Combat job level 13 matches the locale ("You must have a combat job of at least level 13 to play this battle"). The Dungeons index also says difficulty 5, level 13 (`notes/Build Guides/Content/Dungeons/Dungeons.md:110`).
- Coins and members bonus match `prototype/osfr-tools/data/content/dungeons/tanglewood_fort.json:825` (77) and `:855` (287). The "62 Stars" wording matches the JSON at about line 733.
- Prize-wheel item names, including Necklaces of Bark Skin V, Energy Transfer Medic Helmet, Action Power Warrior Helm, Stopping Power Medic Backpack and Adept Wizard Hat, all exist in the locale. The JSON mirrors the note's wheel (`dungeons_unresolved.json` ~L23896 onward).
- Difficulty 5 pages (Dark Spore Depths, Forest Troll Fort, Mudshell, Chugawump) show Rings of Regeneration, which supports the "other difficulty 5 pages" claim.
- Dev notes exist: "elite Archer primary attack", "elite archer extra attack", "Elite Soldier Whirlwind", "mini boss extra attack", "volley damage", and the Kluggenkrush regen note.
- The JSON's `goals: []` and `rewards: []` are consistent with the note's statement that page goals are not mapped. The note does not claim they are.

**Unsure:**
- The `loc <id>` numbers in the note do not resolve in the `locale` tool (for example `589428532` returns "no such id"). I matched by quoted text only, so the note's ID hashes are unverified.
- The "boss ability" dev note (`339606570`) is in the locale as "tanglewood fort 158: boss ability" (id 388144). The note's wording is close enough that I did not flag it.
- Video claims (`eS3bRs9fR5k`, `ns0rlvCjXtU`, `rGbK7YgD1w0`, `JYoSoRzyLrI`, marker distances, the Campaigns screen with "SC 500") could not be checked from the repo. Only the notes cite them.
- The "Campaign 6 is a separate paid minigame, probably card-based" claim is consistent with the vault's Treasure War and Trading Card Game notes. It is hedged there too, so I left it alone.
