<!-- fleet job=note-refresh id=Native-Quest-Journal-UI status=done turns=22 usd=0.0203 tokens(read,write,in,out)=[736815, 57423, 46, 11429] model=claude-haiku-5-5 -->
# notes/Research/Native Quest Journal UI.md

**Verdict:** minor drift. Most code-side claims hold at the tip. One sentence about helper selection persistence is false.

**Corrections:**

- `old:` Server persistence of manual helper selection was not established; reconnect currently selects the first active campaign entry by reconstruction policy.
  `new:` The server persists the client's 47/12 helper selection in `QuestState.selected_quest_id`, which is saved with the character, and login rehydration marks that quest as selected (`quest_engine.rs:1451`). Reconnect does not pick a first-active entry; no such fallback was found in `quest_engine.rs`.
  `why:` `repo:prototype/osfr-tools/src/quest_engine.rs:422` (field), `:408-409` (`QuestState` derives `Serialize`/`Deserialize`), `:1539-1557` (`select_quest` sets `selected_quest_id`), `:1451` (login packet writes `selected == quest_id`), `:1457-1470` (`active_login_packets` rehydrates active quests from saved state). Also `repo:notes/Autopilot/T101.md:173` and `repo:prototype/osfr-tools/src/quest_journal.rs:102` (`JournalRequest::Select` calls `engine.select_quest`).

**Checked and holding:**

- Opcode 209 chapter/sticker metadata is unrestored. The default snapshot leaves regions, hubs, hub_quests and stickers empty (`repo:prototype/osfr-tools/src/startup_snapshot.rs:166-171`). The builder exists and is emitted (`startup_world.rs:382-407`, `startup_snapshot.rs:349`), but it sends no original content.
- Reserved IDs 910001+ are reconstructed opening quests (`repo:prototype/osfr-tools/src/restoration/piece_068.rs:45-47`).
- The campaign-restart review matches the note's 70 coins, eleven item entries, encounter 411, quest 910002 and the 153,719-byte payload (`repo:notes/Reviews/Native Campaign Restart 084544.md:9,15`).
- Linked notes and the review file exist (`Native Journal Live Objective Keys`, `Native Opening Quest Journal`, `Native Creator Delivery Proof`, `Reviews/Native Campaign Restart 084544`).

**Unsure:**

- The claim that the Brawler-selection goal uses locale ID 0 could not be confirmed. I found no goal text ID for that objective in `opening_journal.rs` or `opening.rs` (only the `43 => "Brawler"` name mapping at `opening.rs:642`).
- The client-side claims (Lua/native addresses, `UserOptions.ini`, datasource behaviour, the StoryBook movie details, and the `Native Journal Live Objective Keys` 49/9+10 repair status) are outside this repo's code and were not checked against the decompiled client.
