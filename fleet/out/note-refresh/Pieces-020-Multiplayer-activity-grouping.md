<!-- fleet job=note-refresh id=Pieces-020-Multiplayer-activity-grouping status=nothing_found turns=14 usd=0.0161 tokens(read,write,in,out)=[383465, 54348, 30, 10991] model=claude-haiku-5-5 -->
# notes/Research/Pieces/020 Multiplayer activity grouping.md

**Verdict:** current. Every checkable claim about our code and status holds at the tip; no corrections needed.

**Checked and holding:**
- `src/restoration/piece_020.rs` exists. It defines `ActivityGroupRegistry` (line 411), `parse_family_header` (225), `family_sub_width` (197), `authorize_instance` (788), and the 20-entry `LaunchMessage::ALL` table (105) with sub-opcodes 1–23 minus 10–12 (128–151). It also has `GroupError` (367) with the rejection variants the note names.
- Sub-opcode widths match claim 4: 4 bytes for 175 (`repo:prototype/osfr-tools/src/restoration/piece_020.rs:197-204`), 2 bytes for 40/141, 1 byte for 39/147/167.
- The envelope matches claim 5: `ENVELOPE_PREFIX` = 7 (line 61), `inner_length` counted from the opcode (238).
- `tests/piece_020.rs` has 12 `#[test]` functions (lines 97–540) and includes the module via `#[path = "../src/restoration/piece_020.rs"]` (line 39).
- `tests/pieces/test_piece_020.py` has 12 `def test_` methods, and `scripts/pieces/piece_020.py` exists.
- Not registered: `prototype/osfr-tools/src/lib.rs` has no `piece_020` entry. Only `piece_093` (via `social_chat.rs`) and similar pieces are wired in. This matches "the module is not registered in `lib.rs`".
- The client constructors match claim 1: `FUN_009c0bc0` writes `param_1[1] = 0xaf` and `FUN_009c0c30` writes `param_1[2] = param_2` before the vftable store (`client_sql fn 009c0bc0 / 009c0c30`).
- The community enum conflict in claim 3 holds: `OpenSourceFreeRealms/.../PacketCodes.cs:1111-1112` has both `RemoveMember = 8` and `UpdateMemberState = 8`. `FreeRealms-Legacy/.../PacketReaderExtensions.cs:1153-1154` has 8 and 9. `ClientActivityLaunchBasePacket = 175` is at `PacketCodes.cs:112`.
- `src/cooking.rs:393-409` compares the request's instance id with the active one, as integration step 2 says.
- Reconstructed policy matches the code: owner-only launch and kick (`launch` at 611, `kick` at 580), launch gated on pending invites and readiness (627–640), `AlreadyLaunched` after launch, disconnect behaviour before and after launch (683–750), and the instance closing with its last member (711–717).

**Unsure:**
- Claim 8, `MiniGameData.txt` (783 rows; 779 rows `0/0`, 4 rows `1/1`). The file exists at `client:Resources/MiniGameData.txt` with the `MIN_PLAYERS`/`MAX_PLAYERS` columns, but I did not count the rows, so the exact figures are unverified.
- Claims 4 and 6 (five retail frames, 13 identical 147/1 frames with the stated sha256) and the `lab/reports/piece-020-20261009T0259Z/` artifacts. These sit outside the roots I can read, so I could not check them. The Rust test `activity_profile_payload_is_15_records_of_28_bytes` is the only in-repo support.
- Claim 5 says the same envelope is "what `src/gateway.rs` already tunnels". `gateway.rs:247` has a `tunnel` function that reads the `(outer, inner)` pair, which is consistent, but I did not check the length convention byte for byte.
