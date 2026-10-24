<!-- fleet job=guide-refresh id=Content-Dungeons-Bixie-Hive status=nothing_found turns=14 usd=0.0153 tokens(read,write,in,out)=[356455, 48839, 30, 11291] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Bixie Hive.md

**Verdict:** current. I found no claim about our code or its status that is now false. The note is almost entirely client-locale, wiki and video facts, and the few code-adjacent statements agree with the tip.

**Corrections:** none.

**Checked and consistent:**
- Difficulty 1, no required level: `repo:prototype/osfr-tools/src/restoration/piece_059.rs:138` (row 1 "Bixie Hive", difficulty 1, zone `sg_bixie_hive`, entrance "door" in Queensfields, Sanctuary). T354 records "required combat level 0" (`repo:notes/Autopilot/T354.md:39`).
- Coin payout 68: `repo:prototype/osfr-tools/tests/bixie_hive_dungeon.rs:65` (`REWARD_COINS: u32 = 68`). The note's Rewards table and Conflicts item 3 agree with this.
- Roster names: `SOLDIER_NAME 440711` and `MAGE_NAME 440712`, `BOSS_NAME 38510` (`bixie_hive_dungeon.rs:77-79`). The locale returns "Bixie Soldier" for 440711, "Bixie Battlemage" for 440712 and "Drone Fauzz" for 38510, matching the note's Enemies row.
- Title "Bixie Hive" (locale 5702), objective "Save the Queen from unruly Bixies." (locale 16791), and the panel description (locale 15336, "...take their own queen hostage. Enter the Bixie Hive and save her!") are all in the locale and match the note's wording.
- Five enemy definitions and a marker: `bixie_hive_dungeon.rs:66-76`.
- Medic quest "revive twelve wounded bixies" matches locale 15586.

**Unsure:**
- The note's `loc <number>` keys (e.g. `loc 3412228782`, `loc 1777163323`, `loc 755996992`) do not resolve in the locale tool, which only accepts the sequential ids that T354 uses (5702, 15336, 16791). I could not confirm them, so I left them alone. The note may use a different hash key space; whoever owns the convention should say which.
- The note has no implementation-status line. The repo does ship Bixie Hive as a level-1 field battle, battle 12370, with its own test suite (`repo:notes/Autopilot/T354.md:1,34`; `repo:prototype/osfr-tools/tests/bixie_hive_dungeon.rs`). That is a gap, not a false claim, so I did not propose a correction. If the vault wants status on each note, a line like "Built as a level-1 Queensfields field battle (battle 12370, T354)" would be the addition.
- The Gaps item "Fauzz's real ability list and health" still stands. Our roster uses an authored 260 HP / 10 damage, marked (R) (`repo:notes/Autopilot/T354.md:45-46`), not a recovered value.
