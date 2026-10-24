<!-- fleet job=guide-refresh id=Content-Dungeons-Bergram-Stumpfinger-s-Ghost status=nothing_found turns=13 usd=0.0162 tokens(read,write,in,out)=[336313, 49521, 28, 13225] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Bergram Stumpfinger's Ghost.md

**Verdict:** current. The note makes no claims about our server code, so I checked its client-locale, dungeon-record and cross-note claims. None are false at the tip.

**Corrections:** none.

**What I checked and confirmed:**
- Dungeon status and level: `notes/Build Guides/Content/Dungeons/Dungeons.md:142` gives difficulty 5, level 13, Blackspore Swamp, Special Spawn. `prototype/osfr-tools/data/content/dungeons/bergram_stumpfinger_s_ghost.json` (difficulty 5, zone name "Blackspore Swamp (tombstone north of Mire's Edge)") agrees with the note. The record has `entry_requirements: []`, which is consistent with the note's "no unlocking quest" line, but the level-13 gate is not encoded in our content. That is a gap, not a note error.
- Locale strings, by text: "Defeat Bergram Stumpfinger." (90113), "Defeat Bergram Stumpfinger - if you can!" (90114), "Bergram's Bones" (90394), the hidden-objective string (90517), "You dare disturb my bones?" (91032), "Curse you! I'll take you down with me!" (90987), "You'll never beat me like that." (91062), "Look what we found here!" (90417), "Graverobber" (90413), "Tombstone" (76373), "Requires a level 13 combat job" (4201), the bone explosion, blue beam, shambler slay and stunned-and-immune strings (90414, 90453, 91056/91057, 90989), the quest and story strings (418755, 418757, 418758, 418760, 418761, 418766, 383024, 383025, 383031, 383032), and "I used to have a partner named Bergram Stumpfinger..." (94088).
- No plain "Necrowart Zombies" string exists; "Necrowart Zombie2", "Necrowart Zombie3" and "Mini Necrowart Zombie" do (118945–118947). The only other hit is "Ancient Necrowart Zombie" (442328), which the note does not mention.
- Medic wheel: "Energy Transfer Medic" exists only as Jacket, Boots, Gloves, Helmet, Fatigues and Backpack (133128–133133). No "Pants". The note's Conflict 1 is correct.
- Prize-wheel item names: every name I checked exists exactly (Archer's Raptor Bow of Firebomb, Upshot Archer Leggings, Brawler's Atlas Hammer of Stars, Medic's Shockrod of Lasers, Ninja's Shadow Blade of Deception, Warrior's Warlord Axe of Thunder, Wizard's Ornate Wand of Transmutation, Chunin Ninja Hakama, Action Power Warrior Breeches, Adept Wizard Slacks, Bare-Knuckle Brawler Pants, Battle Item Mystery Pack, and the Necklace of Bark Skin V, Necklace of Energy Font and Power Shard of Vitality V names for each job).
- Conflict 3: `notes/Build Guides/Content/Dungeons/Briarheart Caverns.md:73` has "311 Stars or less", so the cited figure is right.
- Hash mappings: `notes/Autopilot/T034.md:53,63` maps the boss and dungeon name hashes to locale 90419, which matches the note's boss-name line.

**Unsure:**
- The `loc` hash ids in the note cannot be resolved with the `locale` tool, which takes sequential indexes. Only the text was checked, not the hash values. The note's "game data" hash `1090123129` is listed under the boss. `T034.md:53` maps that same hash to the dungeon name ("Bergram Stumpfinger's Ghost"), and `bergram_stumpfinger_s_ghost.json` uses `name_string_id: 90419`, which the locale resolves to plain "Bergram Stumpfinger", not the ghost title (78143). The hash-to-entity assignment cannot be settled from the tools here.
- "UI `loc 1000218528`": the `ui` root has no Bergram or Stumpfinger match, so this UI reference is unverified.
- Wiki-only claims (stars, coin payouts, the two graverobbers, the dwarf ghost with white eyes, the tombstone spawn rule) and video claims (frame keys, 37 m marker, Adventurer 9–11, "Find the loot - 0/5" counter) were not checkable from the repo or client.
