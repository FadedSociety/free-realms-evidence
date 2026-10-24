<!-- fleet job=note-refresh id=NPC-Greetings-Starting-Road status=nothing_found turns=31 usd=0.0328 tokens(read,write,in,out)=[1270280, 70812, 64, 22466] model=claude-haiku-5-5 -->
# notes/Research/NPC Greetings Starting Road.md

**Verdict:** current. I found no claim that is now false or has a moved citation. Two placement checks are unsettled (see Unsure), and neither changes the note's conclusion.

**Corrections:** none.

**Checked and holding:**
- **Counts and ids.** The table has 16 rows (Farnum 5, Cobblestone 2, Highroad 3, Sanctuary 6). Every id matches its file: `prototype/osfr-tools/data/content/npcs/farnum_farmstead.json` (101014 l.361, 5100125 l.1671, 391041 l.2974, 391391 l.3331, 5100509 l.3940), `cobblestone_village.json` (388245 l.2435, 94388 l.7608), `highroad_junction.json` (436533 l.786, 431140 l.1411, 140509 l.5551), `sanctuary.json` (387246 l.8855, 73782 l.13775, 76747 l.16986, 76438 l.35256, 73360 l.40794, 71435 l.55438).
- **Seven quest-offer rows.** Each intro id is a `intro_text_string_id` in its quest file (`quests/archer.json:596`, `chef.json:1119`, `medic.json:622/674/838`, `warrior.json:1022`, `wizard.json:1782`). Each giver matches the note's NPC id (`archer.json:551`, `chef.json:1076`, `medic.json:577/629/789`, `warrior.json:977`, `wizard.json:1737`).
- **Gaston left blank.** `highroad_junction.json` has no greeting on 9500000333 (l.4510 onward). This matches the exclusion list and `notes/Autopilot/F346.md:62-66`.
- **Open gap.** Rucks (9500000278, l.7611), Peavey (9500000274, l.6014) and Wompugg have no greeting, which matches the "Open gaps" list.
- **Rust path.** `npc_interaction.rs:898` copies `npc.greeting_string_id` into `body_string_id`. `gameplay/npc.rs:1185` writes it into `initial_dwords[0]`. `patch_npc_actor` (`gameplay/npc.rs:1156-1159`) overwrites only bytes 12..20. `encode_dialogue_26_3` is at `npc_interaction.rs:1071`. The test `tests/npc_interaction.rs:395` exists.
- **Spawn gate.** `world.rs:284` skips every placement other than `legacy_data`, which supports the exclusion rule.
- **Client evidence.** `00aa12e0` calls `00a9ef10` and `009f5ae0`. `009f5ae0` calls `008d2ba0` and `0097c1e0`, and passes `*(param_2+0x10)` to `0097c1e0` ahead of `SetDialogText`. `009f5890`, `00aa2360` and `00a36f80` are also present as named functions.
- **Farnum placements.** Anne, Cleetus, Henry, Houston and Mae are all `legacy_data` (`farnum_farmstead.json` l.62, 1236, 2551, 3032, 3481). Eddie, Ricky, Archy, Auguste, Harold, Bordon, Clover, Gordon and Karin fall in ranges whose placement line is `legacy_data` (cobblestone 2048/7233; highroad 403/944/5040; sanctuary 8232/13156/16359/34821).
- **Quest offer reference.** `notes/Research/Quest Offer Reference.md:8` does cite locale 104097 as the bubble body.
- **Helper script.** `scripts/quest_text_backfill.py` exists.

**Unsure:**
- **Naia (9000000161) and Whittington (9000000205) placement.** The Sanctuary records have `legacy_data` placement lines beyond the range my search could return. I could not find their `placement` lines (search results were truncated for that file). Naia's record has a model id (421) and name id (7611), which matches the note. Whittington's record is at `sanctuary.json:54739`. The exclusion "All 16 added rows are `legacy_data`" stands unconfirmed for these two rows.
- **`lab/reports/locale-id-map.json` and `lab/working/...en_us_data.dat`.** These are outside the repo roots I can search, so I could not confirm the hash and line numbers in the Method section. The `scripts/locale_id_map.py` reference suggests the map exists.
- **Quest enabled flags.** `archer.json:598` and `chef.json:1121` set `"enabled": false` for two of the quest-offer rows. The note does not claim these quests are live, so I left it alone.
