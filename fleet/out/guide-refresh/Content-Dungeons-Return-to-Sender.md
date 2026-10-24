<!-- fleet job=guide-refresh id=Content-Dungeons-Return-to-Sender status=nothing_found turns=15 usd=0.0163 tokens(read,write,in,out)=[427087, 52642, 32, 10965] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Return to Sender.md

**Verdict:** current. I found no false claim about our code or status in `Return to Sender.md`. The note makes almost no claims about the repo, and the ones it makes about the client and the wiki hold up against the tip.

**Corrections:** none.

**What I checked and found to hold:**
- Client strings: "Knock out all of the evil postmen!", "Return to Sender Encounter", the six dev mechanic strings ("Return to Sender 219: ...", "Drop Letters on death", "Mock throw into fire", "Drop Stack of Mail on death proc effect", "On Death Drop Package", "Drop Package triggered by on death ability 2825"), "The Postal Chaos Alliance is wreaking havoc...", "PCA Operative", "Mailbit", "Requires a level 5 combat job", "Bonus: 37 Coins!", "Members Only Bonus!", the three PCA lines, "as much mail as possible", the "15 letters or packages" line, and "evil postmen that can be found wandering the wilderness". All are present in the locale table.
- Prize-wheel item names: Drifting Archer Cap, Nusumi Ninja Cowl, Scholar Wizard Fez, Emergency Medic Cap, Catchweight Brawler Helmet, Combat Bonus Warrior Helm, Battle Item Mystery Pack, Ninja's Scythe of Dragonstrike and Wizard's Bone Wand of Shock all match.
- Our data agrees with the note: `prototype/osfr-tools/data/content/dungeons/return_to_sender.json` (minimum combat job level 5, members_only false, the "59 Stars" and "37 Coins" rewards, the "Knock out..." goal, Mailbit listed as unresolved boss, quest left null), and `npcs/wilds.json:27678` (Mailbit, zone 16, "Boss of Return to Sender").
- Nothing in `prototype/osfr-tools/src` or `data/content/field_battles.json` references Return to Sender. The note does not claim that it is routed or built, so its silence is accurate. The Build Ledger has no entry for it either.

**Unsure:**
- The note's ten-digit `loc` ids (for example `loc 4062420947`, `loc 3300949067`, `loc 4248947857`) use a different key space from the locale tool, which only accepts the small ids (for example "Evil Postman" is 384822). I matched those strings by their text, not by id. Our repo's enemy row uses `name_string_id 384822` (`data/content/enemies.json:385`).
- `Gaps` says the spawn is unknown. Our data has an Evil Postman NPC spawn from the Legacy Lua source (`data/content/npc_spawns_extra.json:44476`, position -513, 0.5, 877, NameId 384822). It is a plain NPC row and does not show the battle's entrance, so the gap line still stands.
- `NPCs: [[Mailbit]]` points to a page that does not exist in `notes/` (no `# Mailbit` heading found). This is a dangling link, not a code claim, so I left it alone.
