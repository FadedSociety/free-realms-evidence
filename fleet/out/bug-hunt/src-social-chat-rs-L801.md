<!-- fleet job=bug-hunt id=src-social-chat-rs-L801 status=nothing_found turns=18 usd=0.0256 tokens(read,write,in,out)=[602878, 66019, 38, 22677] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/social_chat.rs lines 801-1475 of 1475

No reportable defects in `prototype/osfr-tools/src/social_chat.rs` lines 801-1475. I read the whole window and checked its callers (`bin/osfr-gateway.rs` 1793-1945, 2109-2340; `Reader` and `NameData` helpers at social_chat.rs 259-318 and 153-197; `chat_candidates`/`chat_session` at osfr-gateway.rs 837-878; `IgnoreLists::ignores` at social_chat.rs 792).

Candidates checked and dropped:

- **`resolve_recipients` Tell arm (`target.unwrap()`, line 834):** safe. `target` is `Some` exactly when `channel == Tell`, and a missing target returns earlier.
- **Area / Guild / MembersOnly / Group checks (lines 848-878):** the client-supplied `area_id` and `claimed_guild_guid` are compared against server session state before use. `is_member`, `group_id` and `guild_id` come from the server-side `ChatSession`.
- **`resolve_quick_chat_recipients` (888-933):** Channel mode builds its `ChatRequest` from server values. Quick-chat channels are filtered by `quick_chat_sendable` at social_chat.rs:533 and 558, so Yell/System/Whisper cannot slip through.
- **`server_chat_message` (940-977):** `sender.guild_id.ok_or(...)` is reached only after the guild check. Sender identity is rebuilt from the session.
- **`ChatHistory` (997-1017):** the per-speaker deque is capped at 10 and `pop_front` keeps it bounded.
- **`decode_report_request` (1025-1046):** the count is rejected when negative or above 10, and the `Vec` capacity is therefore bounded. Strings are capped by `Reader::string`.
- **`intake_report` (1066-1101):** `inbox.0.push` is unbounded, and the name-to-guid lookup can prefer history over the online session. Neither is reachable from a client packet: `intake_report` has no caller in `src/`, only tests in `tests/social_chat.rs`. Dropped.
- **`decode_settings_request` (1182-1218):** sub 32/33 maps to on/off correctly (`sub == 32` means on). Strings are bounded, trailing bytes are rejected, and the bubble ranges are checked. The client's u64 is ignored.
- **`ChatSettings::apply` / `valid` / `load` / `save` (1240-1307):** the in-place bubble compare is correct, the file read is size-capped, and the schema and guid are checked on load.
- **`ChatSettingsBook::handle` / `join` / `listeners` / `save_changed` (1325-1382):** `listeners` never drops the sender's echo and matches the test at tests/chat_settings.rs:238-290. In the gateway, `handle` runs on the staged world (osfr-gateway.rs:1904 → 2127), and `save_changed` at 1941 compares it with the live world, so a failed save drops the change. Only one character can change per message, so the early `?` in `save_changed` cannot leave a partial multi-character write.

Notes outside the defect categories, not reported: `NameData::matches` (typed Tell, per-field compare) and quick-chat Tell (`display_name` compare) match names differently. `NaN` positions would silence only the sender's own Say. `chat_session` always sets `chat_area_id: None`, so the Area channel never delivers. That is a documented (R) choice, not a defect.
