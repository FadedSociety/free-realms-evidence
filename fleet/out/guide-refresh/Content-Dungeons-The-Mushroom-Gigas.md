<!-- fleet job=guide-refresh id=Content-Dungeons-The-Mushroom-Gigas status=done turns=16 usd=0.0223 tokens(read,write,in,out)=[604637, 69202, 34, 15208] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/The Mushroom Gigas.md

**Verdict:** minor drift. Nearly all locale ids, quoted strings, the level 5 requirement and the item names check out against the client data (`refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat`, `locale` tool). Our code agrees with the note: `prototype/osfr-tools/data/content/dungeons/the_mushroom_gigas.json` (members_only true, minimum combat job level 5, difficulty 3), `data/content/enemies.json:1784` (`mushroom_gigas`, name string 74008 "Mushroom Gigas"), and `npc_spawns_extra.json:24192` (name 76497 "The Mushroom Gigas"). The note makes no claim about a code path, so nothing in it says the battle is built or unbuilt. The three fixes below are wording and link errors.

**Corrections:**

1. `old:` Same item set as [[Seaside Swoopers]] except the Power Shards are tier II and the rings tier III.
   `new:` Same item set as [[Seaside Swoopers]] except the Power Shards are tier II (Seaside's are tier III); the rings are Ring of Regeneration III in both.
   `why:` `notes/Build Guides/Content/Dungeons/Seaside Swoopers.md:66-71` already lists "Ring of Regeneration III" in every job row, so the rings do not differ. Only the shard tier differs. The client has both tiers (`en_us_data.dat`: "Archer's Power Shard of Vitality II" 3832684316, "Archer's Ring of Regeneration III" 2912528986).

2. `old:` Members also get "Members Only Bonus: 74 Coins" (client label `loc 1925651180`)
   `new:` Members also get a "Members Only Bonus!" label (client `loc 1925651180`); the "74 Coins" figure is not in that string
   `why:` `en_us_data.dat` line 50746: `1925651180 ucdt Members Only Bonus!`. The "Bonus: 74 Coins!" string is a separate entry (`1579014258`, line 41790), which the note already mentions.

3. `old:` NPCs: [[Sergeant Cargug]], [[Azure]].
   `new:` NPCs: Sergeant Cargug is on [[NPCs - Briarwood]] (row at line 148); Azure is on the same page (line 224) and is the boss of [[Briar Patch]].
   `why:` No `Azure.md` or `Sergeant Cargug.md` exists under `notes/Build Guides/Content/` (only `Content.md`, `Dungeons/`, `Jobs/`, `NPCs/`). Both names appear only as table rows in `repo:notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:148` and `:224`, so both wikilinks are dead.

**Unsure:**

- The wiki-sourced figures (Stars "77", Members bonus "74 Coins", blank wheel coin slot) and the "Gigas Azure" image. The wiki text is stored only as hashed raw JSON in `refs:freerealms-wiki/`, so I could not confirm them.
- The members-only requirement from the wiki. The client has no string that matches the wiki's "You must have membership or be grouped…" line; generic membership strings exist but are not tied to this battle. The note already says this.
- The client line for the battle is "Win Wandering Combat Encounter The Mushroom Gigas!" (`3348947269`). The note's shorter "Wandering Combat Encounter" is a fair paraphrase, so I left it.
- `enemies.json:1791-1799` gives the enemy reconstructed stats (180 HP, 15 damage, 30 s respawn). The note says "Count and behaviour unknown", which does not conflict, but the note could point to these reconstructed values.
