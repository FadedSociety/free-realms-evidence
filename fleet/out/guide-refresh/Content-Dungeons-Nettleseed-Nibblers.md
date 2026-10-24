<!-- fleet job=guide-refresh id=Content-Dungeons-Nettleseed-Nibblers status=done turns=13 usd=0.0140 tokens(read,write,in,out)=[278516, 45735, 28, 10900] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Nettleseed Nibblers.md

**Verdict:** minor drift. Almost every claim in this note is client-locale or wiki text, and those check out against the locale. One conflict item is stale because the repo now holds a source for the enemy's model.

**Corrections:**

1. `old:` Both are client or wiki text; no source says which the model is.
   `new:` The repo's enemy row (reconstructed, not a client or wiki source) gives model_id 3250, which maps to `maneatingplant.adr` (Models.txt row 2436), via the Legacy NPC NameId 45945 crosswalk. So the model is a man-eating plant (R), which fits the quest's "ferocious weeds" wording.
   `why:` repo:prototype/osfr-tools/data/content/enemies.json:536-559 (`w58_nettleseed_nibbler_l5_enemy`, model_id 3250, name_string_id 45945, source "Models.txt row 2436 maps model_id=3250 to ADR=maneatingplant.adr"); repo:prototype/osfr-tools/data/content/npc_spawns_extra.json:24521-24534 (Legacy Npcs.json Id=2831, ModelId=3250, ModelFileName=maneatingplant.adr, NameId=45945); repo:notes/Research/World Enemies.md:91 (930015 Nettleseed Nibbler, 45945, 3250, `maneatingplant.adr`).

**Checked and holding (no change):**
- "No 'Nettleseed Nibblers Bonus Objective' or 'Win Combat Encounter Nettleseed Nibblers' string exists": the locale search returns no matches for either phrase.
- The level-5 strings ("Requires a level 5 combat job", "...combat job of at least level 5 to play this battle") and "Defeat the Nettleseed Nibblers!", "Knock out Nettleseed Nibblers", "Nettleseed Nibblers" (quest/monster name without "!") and "Members Only Bonus!" and "Bonus: 34 Coins!" all exist in the locale.
- Every prize item in the job table is present in the locale (Archer's, Brawler's, Medic's, Ninja's, Warrior's, Wizard's, Drifting Archer Hoodie, Catchweight Brawler Jacket, Emergency Medic Shirt, Combat Bonus Warrior Tunic, Scholar Wizard Medium Cloak, Nusumi Ninja Gi, Battle Item Mystery Pack, and all Regeneration III rings and shards).
- The vault has no `Private Chaggis` NPC page, which matches "no wiki page found".

**Unsure:**
- The `loc <id>` numbers (for example 3406377541, 2871998889, 3459805504, 3982023502) could not be checked. The locale tool does not resolve them ("no such id"), and the client_sql label table has no matching record. Their texts exist, but the number-to-string link is unverified.
- Nothing in the repo or Build Ledger mentions a node-battle implementation for Nettleseed Nibblers. The note makes no build-status claim, so I left status alone.
- The note's Gaps item "Respawn behaviour of the Nibbler nodes" is partly answered by the repo's reconstructed `respawn_ms: 30000` (enemies.json:551). That is (R) only, so I did not change the gap.
