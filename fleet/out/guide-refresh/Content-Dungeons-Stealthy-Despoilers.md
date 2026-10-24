<!-- fleet job=guide-refresh id=Content-Dungeons-Stealthy-Despoilers status=done turns=11 usd=0.0103 tokens(read,write,in,out)=[158314, 26836, 24, 10755] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Stealthy Despoilers.md

**Verdict:** current, with minor drift. The note's client text quotes match the locale table, and its item names all match. Its one wrong quote is the Members Only label. The note makes no claims about our Rust code (no code, route or build status for this battle), so the checks were against the client locale and the vault's own files.

**Corrections:**

1. `old:` Members get "Members Only Bonus: 37 Coins" (client label `loc 1925651180`)
   `new:` Members get "Members Only Bonus!" (client label `loc 1925651180`); the 37 comes from the separate "Bonus: 37 Coins!" string
   `why:` The locale has "Members Only Bonus!" as its own entry (locale 427736). No entry reads "Members Only Bonus: 37 Coins". "Bonus: 37 Coins!" is a separate entry (locale 5538), which the note already cites.

**Checked and holding** (locale text matches as quoted): the goal "Find and defeat all of the stealthy ninjas."; the panel line "Ghost ninjas are attacking tourists! Head in and defeat them!"; the story lines for "Stealthy Despoilers, ghosts of ninjas past..." and "The Stealthy Despoliers are lurking outside of the old Flying Dragon Dojo..." (the typo is real); "It seems that the dark legacy..."; the quest wording lines; "Ghost Ninja", "Ghost Ninja Striker" and "Ghost Ninja Elite"; the level-9 tier strings; and all 24 prize-wheel item names. "Stealthy Despoilers Bonus Objective" does not exist. The Ree Peatpants contract lines exist. The Dungeons index row (`[[Stealthy Despoilers]] | 4 | 9 | Seaside | BrawlWiki`) and the neighbour pages exist.

**Unsure:**
- Links `[[Ree Peatpants]]` and `[[Master Kai]]` (NPCs line and Quest table) do not resolve. `notes/Build Guides/Content/NPCs/` has only zone pages, and Kai is named in `NPCs - Seaside.md:35`. This is a dangling link, not a false claim, so I did not propose a change.
- The `loc N` numbers in the note (for example 2099651034 for the goal) do not match the locale tool's keys (the goal is entry 95062). I matched the texts, not the numbers, so the ids are unverified.
- The video-based claims (Medic 8 HUD reading, 12 enemies, the results screen, "You receive 8 coins") and the wiki-only claims (prize wheel, 156 Stars, 32 Coins slot) cannot be checked here. The "You receive N coins" pattern does exist in the locale as a template.
- The "Goals (1)" and "Goals 1/1" panel text was not found in the locale, so it may be built by the UI.
