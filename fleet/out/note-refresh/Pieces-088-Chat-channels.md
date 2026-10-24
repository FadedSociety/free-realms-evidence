<!-- fleet job=note-refresh id=Pieces-088-Chat-channels status=nothing_found turns=31 usd=0.0342 tokens(read,write,in,out)=[1618240, 76687, 64, 16765] model=claude-haiku-5-5 -->
# notes/Research/Pieces/088 Chat channels.md

**Verdict:** current. The module, tests, checker, counts and the "not wired" boundary all match the tip. The one open point is the "only four client-confirmed numbers" claim, which other vault notes dispute; I could not settle it from the decompile, so it is under Unsure, not corrected.

**Corrections:** none.

**Checked and holding:**
- `src/restoration/piece_088.rs` exists. It defines `parse_request`, `route`, `Peer`, `Delivery`, `Refusal`, `Route`, `CHANNELS`, `CHANNEL_FACTS`, `MAX_MESSAGE_BYTES` = 2048 and `MAX_NAME_BYTES` = 128 (`repo:prototype/osfr-tools/src/restoration/piece_088.rs:51,53,349,447,494`).
- `tests/piece_088.rs` has 12 `#[test]`s, matching "12 passed" (`repo:prototype/osfr-tools/tests/piece_088.rs:95..384`). It pulls the module in with `#[path]` (line 27).
- `tests/pieces/test_piece_088.py` has 11 test methods, including 9 `test_fails_when_*` tamper cases, matching "Ran 11 tests" and "nine tamper cases" (`repo:tests/pieces/test_piece_088.py:93..242`).
- `lib.rs` has no `mod restoration`, and there is no `restoration/mod.rs`. That matches "the lead's registration is adding …" (`repo:prototype/osfr-tools/src/lib.rs`, `repo:prototype/osfr-tools/src/restoration/`).
- The module is not referenced from `gateway.rs`, `gameplay.rs` or the gateway binary; only the module and its test use it. That matches "not wired into `gateway.rs`".
- `crate::chat::request` exists and reads the same shape: the `channel == 8` trailing u32 (`repo:prototype/osfr-tools/src/chat.rs:45-58`).
- `ChannelFacts` has `client_number_confirmed: true` for exactly WorldTrade 6, WorldLfg 7, WorldArea 8 and WorldMembersOnly 10, and `false` for the rest (`repo:…/piece_088.rs:116-227`). This matches the four-numbers statement.
- Client facts: the `ChatLog` filters and `ChatBubbles` channel constants match (`ui:ScriptsBase.lua:10576-10582, 30929-30937`). `Ui.IsMember()` gates `ChannelOn(MO_CHANNEL)` (`ui:ScriptsBase.lua:10927`). `/groupsay` and `/tell "…"` compose strings are present (`ui:ScriptsBase.lua:7542`, `k47`). `OnReceiveWhisper` and `AddWhisper` exist. `OnReceiveSay` bubbles only outside the five chat-log-only channels, which is consistent with the note's description.
- Client `FUN_00b978b0` assigns WorldArea, WorldTrade, WorldLfg and WorldMembersOnly (`client_sql fn 00b978b0` string pool).

**Unsure:**
- **"Four confirmed numbers / only four are proven"** (`Original facts`, `Reconstruction boundary`, and the `MMO Dispatch Ledger`'s "4 of 11"). The vault says the opposite in two places: `notes/Build Guides/Gameplay/Social (Friends, Guilds, Chat).md:281` says all eleven are pinned by the receive switch and calls "only four are proven" outdated; `notes/Research/Chat Core.md:8` says `00b14350` maps channels 0–10. I could not confirm either. `00b14350` (`BaseChatPacketReceiveDispatcher`) switches on payload mode 1–5, not on channel, so the cited receive switch does not show the channel mapping. I found no decompiled function that pins channels 0, 2, 3, 4, 5 or 9. Someone with the full decompile should settle whether the note's "only four" is still true, and whether the vault's "all eleven" claim is right.
- **ChatSpeed defaults** (Any 330 ms, Dup 1000 ms, Dup3 2000 ms, Max 30000 ms): I searched `ui` for `ChatSpeed` and found no match in `ScriptsBase.lua`. The values may live in a config table I did not search.
- **Artifact SHA-256 hashes** and the `lab/…` evidence paths: outside the repo or not computable with my tools, so not checked.
- **Checker counts** ("11 channels, 4 client-confirmed numbers, 15 command registrations, 6 gaps"): not re-run. The 15 aliases do match the note's list, and the 11 channels match `CHANNELS`.
