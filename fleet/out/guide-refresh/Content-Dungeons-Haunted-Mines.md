<!-- fleet job=guide-refresh id=Content-Dungeons-Haunted-Mines status=done turns=24 usd=0.0268 tokens(read,write,in,out)=[1032745, 70216, 50, 15425] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Haunted Mines.md

**Verdict:** minor drift. Nearly every code-checkable claim holds at the tip. One conflict entry is stale because the sibling Briarheart note has since changed its position on the campaign.

**Corrections:**

1. `old:` [[Briarheart Caverns]] reads "Campaign 2: Haunted Mines" as a dungeon campaign. The video evidence above points to the Treasure War card campaign. Both pages should be reconciled by the lead.
   `new:` [[Briarheart Caverns]] now treats "Campaign 2: Haunted Mines" as unproven as a gate and does not build it as a requirement. The video evidence above points to the Treasure War card campaign, which that page also records. Both pages agree the meaning is unresolved.
   `why:` repo:notes/Build Guides/Content/Dungeons/Briarheart Caverns.md:30 ("Unproven either way. Do not build it as a gate.") and repo:notes/Build Guides/Content/Dungeons/Briarheart Caverns.md:114 ("reworded above as unproven and not a gate"). The client string is in locale 39523, which only names the campaign and does not say it is a dungeon gate.

**Checked and holding (no change):**
- Difficulty 5, members false, entrance "barrier" in "Blackspore Swamp": repo:prototype/osfr-tools/src/restoration/piece_059.rs:176.
- Level 13 job rule for difficulty 5 (ranks 3/4/5 require 5/9/13): repo:prototype/osfr-tools/src/restoration/piece_059.rs:9-10, and repo:prototype/osfr-tools/data/content/dungeons/haunted_mines.json (`minimum_combat_job_level` = 13).
- Bronze trophy 5 pts and silver 10 pts: repo:prototype/osfr-tools/data/content/achievements.json:3852-3862 and :4716-4726.
- Prize wheel items for all six jobs and the "Bonus: 77 Coins!" string: repo:prototype/osfr-tools/data/content/dungeons/haunted_mines.json (the wheel item values, and the 77 Coins slot at about lines 683-705). Locale 118394 is "Bonus: 77 Coins!"; locale 139310 is "Defeat the Spider Queen, Necrosis!".
- No "Bonus: 270 Coins!" locale string exists (search returned no matches).
- Campaign row: "Campaign 2: Haunted Mines" appears in locale 39523 only, as the Briarheart prerequisite.

**Unsure:**
- The NPC wiki-links in "Related quests and NPCs" ([[Foreman Ironfist]], [[Necrosis]], [[Sven Fardreamer]], [[Hiram]], [[Iliya]], [[Vrock Gravelfist]]) have no matching note pages under notes/. The NPC data lives in repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md. This is a link problem, not a false claim, so I did not propose a text change.
- The campaign video citations differ between the two notes. This note cites JYoSoRzyLrI/00156, 00042, 00164; Briarheart cites 00042, 00156, 00618. I cannot check the frames from the repo, so I left them alone.
- The game-data IDs (`976802498`, `45497422`) and the client `loc` IDs are not searchable with the locale tool, which keys by row number, so I could not verify those IDs directly. Text matches were checked instead.
- The video claims (frame keys, marker distances) and the wiki revision date could not be checked from the code.
