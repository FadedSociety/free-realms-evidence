<!-- fleet job=note-refresh id=NPC-Greetings-Lakeshore-and-Wilds status=no_submit turns=19 usd=0.0215 tokens(read,write,in,out)=[583204, 61867, 40, 15859] model=claude-haiku-5-5 -->
# notes/Research/NPC Greetings Lakeshore and Wilds.md

**Verdict:** minor drift. The code claims hold at the tip. The Wilds greeting count is stale because T378 added a 17th Wilds greeting after this note was written.

**Corrections:**

1. `old:` 58 drawable Wilds rows still have no greeting; most have no recovered first-person
   `new:` 57 drawable Wilds rows still have no greeting; most have no recovered first-person
   `why:` `repo:prototype/osfr-tools/data/content/npcs/wilds.json:37313` has `"greeting_string_id": 94519` on Shakey (`9500000941`), added by T378 (`notes/Autopilot/T378.md:18`; `tests/npc_greetings_lakeshore_wilds.rs:250-252` `LATER_GREETINGS`). The Wilds greeting count is now 17, so one fewer row is blank. The total of 74 is unverified (see Unsure).

2. `old:` - The remaining 58 drawable Wilds rows: vendors, racers, bosses and quest targets whose
   `new:` - The remaining 57 drawable Wilds rows (T378 later bound Shakey, `9500000941`, to `94519`): vendors, racers, bosses and quest targets whose
   `why:` same as correction 1. The 16 greetings listed in this note are still the T298 set; the 17th binding comes from T378.

**Checked and holding:**
- `npc_interaction::dialogue_context` copies `npc.greeting_string_id` into `body_string_id`: `repo:prototype/osfr-tools/src/npc_interaction.rs:886-901`, with the line at 898.
- `gameplay/npc.rs::dialogue_packet_with` writes `context.body_string_id` into `initial_dwords[0]`: `repo:prototype/osfr-tools/src/gameplay/npc.rs:1174-1185`.
- `patch_npc_actor` overwrites bytes 12..20 of 26/3: `repo:prototype/osfr-tools/src/gameplay/npc.rs:1156-1159`.
- `NpcVisibility::load` spawns only `legacy_data` placements: `repo:prototype/osfr-tools/src/world.rs:284-286`.
- The 26/3 test name exists: `repo:prototype/osfr-tools/tests/npc_interaction.rs:395`.
- Talk is the first option in `build_options`: `repo:prototype/osfr-tools/src/npc_interaction.rs:820`.
- Lakeshore has 4 drawable rows (`model_id` at lines 12617, 13758, 15891, 16680). Three carry greetings (41207, 24829, 409412), so "3 of 4" holds.
- The 19 T298 greetings match `NEW_GREETINGS` (19 entries) in `tests/npc_greetings_lakeshore_wilds.rs:34`.
- The client functions `00aa12e0`, `00a9ef10` and `009f5ae0` exist in the decompiled client.

**Unsure:**
- The "74" total for drawable Wilds rows. My searches appear to cap at about 20 hits per file, so I could not recount. The test sets `WILDS_RECORDS = 118` for all records, which does not settle the drawable count.
- The `lab/reports/...` and `lab/working/...` paths cited in Method. They are not in the repo, so I did not verify them. `scripts/quest_text_backfill.py` does exist.
- The `(R)` fixed-default policy and the speaker-proof claims are judgement calls, not code facts, so I did not check them against the locale text.
