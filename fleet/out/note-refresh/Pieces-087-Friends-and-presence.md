<!-- fleet job=note-refresh id=Pieces-087-Friends-and-presence status=done turns=11 usd=0.0130 tokens(read,write,in,out)=[268591, 48559, 24, 8480] model=claude-haiku-5-5 -->
# notes/Research/Pieces/087 Friends and presence.md

**Verdict:** minor drift. The module, test and path claims hold at the tip. The integration gate and the ignore-body gap are stale because the live gateway already routes the friend wire through `social_lists.rs`.

**Corrections:**

1. `old:` Remaining integration gate (lead): register the module, route family 74/26 through the gateway, and confirm the roster panel against the actual client.
   `new:` Remaining integration gate (lead): register the module and decide how its codecs relate to the live path. Family 26 friend requests are already routed by the gateway (26/14, 26/15, 26/17, 26/30), 26/21 position requests are parsed in `social_lists.rs`, and family 74 is emitted there. Confirm the roster panel against the actual client.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2867-2898 (`parse_social_request`, `(26, 14)` to `(26, 30)`); repo:prototype/osfr-tools/src/social_lists.rs:26 (`FRIEND_FAMILY = 74`), :1231 (74 frame built), :1486 (`(COMMAND_FAMILY, 21, 4)` to `LocationRequest::FriendPositions`); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2225 (`LocationRequest::FriendPositions` handled). Build Ledger line 68 lists the friend map as "Built and wired (W151)" with `social_lists.rs`.

2. `old:` - the `CommandPacketIgnoreRequest` (30) body (`decode_command` refuses it instead of guessing);
   `new:` - the `CommandPacketIgnoreRequest` (30) body in this module (`decode_command` refuses it instead of guessing, `piece_087.rs:688`); the live gateway parses 26/30 as a u8 flag (0 remove, 1 add) followed by two name strings (`osfr-gateway.rs:2885-2898`), so the wire body is no longer unknown at the tip.
   `why:` repo:prototype/osfr-tools/src/restoration/piece_087.rs:688-689 (`UnrecoveredBody`); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2885-2898.

**Checked and holding:**
- `src/restoration/piece_087.rs` exists and is not registered in `lib.rs` (the lib lists `social_chat` and `social_lists` only).
- `tests/piece_087.rs` includes the module via `#[path = "../src/restoration/piece_087.rs"]` (line 46) and has 17 `#[test]` functions.
- Constants: `FRIENDS_FAMILY` 74, `COMMAND_FAMILY` 26, `ACQUAINTANCE_FAMILY` 72, `IGNORE_FAMILY` 112, `UNUSED_SUB_OPCODES` [4, 8], `MAX_ROSTER_ENTRIES` 128, `MAX_NAME_BYTES` 128 (piece_087.rs:65-80).
- `ROSTER_FIELDS` has 18 entries and `ROSTER_UI_COLUMNS` has 13 (piece_087.rs:83, 105).
- `ScriptsBase.lua:3244` is `FriendsList_DS`, with fields 0 to 17 at 3246-3263.
- The `FriendMessagePacket` = 8 disagreement is present in the community reader (`Sanctuary.Packet.Common/Extensions/PacketReaderExtensions.cs:652`).

**Unsure:**
- Test and command totals (`lib` 24, `bins` 3, `test_piece_087.py` 8) and the `piece_087.py` evidence line were not re-run. I only confirmed the 17 Rust tests by counting.
- The claims about the supplied server (`LoginManager.cs:394-407`, the "170 non-dependency C# files" count, and the sole `FriendsPositionRequest` handler) and the wiki "Ignore Button" page 6988 sit in the `lab/` tree and the wiki corpus, which I did not reach through the roots I could search.
- The supplied server's `BaseFriendPackets.cs` enum (sub-opcodes 0 to 10) and the client line numbers (`pseudocode.c:*`) were not re-read. The `ScriptsBase.lua` line numbers were checked.
