<!-- fleet job=note-refresh id=Pieces-090-Guild-lifecycle status=nothing_found turns=23 usd=0.0241 tokens(read,write,in,out)=[872943, 72100, 48, 12607] model=claude-haiku-5-5 -->
# notes/Research/Pieces/090 Guild lifecycle.md

**Verdict:** current. Every checkable claim I tested about our code and status still holds at the tip; no corrections.

**Checked and holding:**
- **Files exist:** `prototype/osfr-tools/src/restoration/piece_090.rs` (974 lines), `prototype/osfr-tools/tests/piece_090.rs`, `scripts/pieces/piece_090.py`, `tests/pieces/test_piece_090.py` (repo:notes/WorkItems/090.md lists the same paths).
- **Not registered:** no `mod piece_090` / `pub mod piece_090` anywhere under `prototype/osfr-tools/src`. The Rust test pulls the module in with `#[path]` (repo:prototype/osfr-tools/tests/piece_090.rs:32-34). So the "lead must register `pub mod piece_090;`" gate still stands, and nothing routes guild main 129 to the parser.
- **Rust test count:** 9 `#[test]` functions in repo:prototype/osfr-tools/tests/piece_090.rs (lines 71-502), matching "9 passed".
- **Python test count:** 18 `def test_` methods in repo:tests/pieces/test_piece_090.py (5 in ServerEnumTests/NativeClientTests/CommunityWireTests/CrossCheckTests as counted, 3+5+4+6 = 18), matching "Ran 18 tests".
- **Sub-opcode table:** 28 entries in `SUB_OPCODES` (piece_090.rs:90-119). Ids 12, 23, 27, 28 and 33 are absent, as the note says.
- **Parser boundary:** `parse_client_request` handles 1, 3-10, 13-16 (13 bodies, piece_090.rs:360-416). It refuses 2, 11 and 26 with `UnrecoveredBody` (line 417), and refuses 17-32 as server-bound (line 418). This matches "the parser refuses them" and "13 handled".
- **Reply encoders:** `guild_error` (23), `can_create_guild` (32), `player_status` (31), `name_update` (18), `paid_rename_reply` (30), `member_status` (17) exist (piece_090.rs:467-534). There is no encoder for 22 (`GuildDataFullPacket`), which matches the gap text.
- **Policy claims:** `accept_invite(player, guild_guid, tick, timeout_ticks)` takes the window from the caller (piece_090.rs:756-762). Guild ids come from a monotonic `next_guild_id` (lines 594-695). `promote` cannot mint a Leader because `Officer.step_up()` returns `None` and yields `CannotPromoteToLeader` (lines 158-164, 835-837).
- **Native base ids:** `FUN_00a09b70` writes `param_1[1] = 0x81` (client_sql fn 00a09b70), matching 129 = 0x81.
- **Lua schema:** `GuildsListDsColumns` (GuildGuid, Name, MessageOfTheDay, CanCreateGuild) and the 15-column `GuildMembersListDsColumns` match repo-independent client Lua at ScriptsBase.lua:3973-3995.
- **Community class count:** 25 `BaseGuildPacket` classes in the pinned Sanctuary tree (refs), matching "community 25". The 13 handled subtypes match the note.
- **Checker output:** the print format at scripts/pieces/piece_090.py:561-568 matches the note's sample line. The `--reports-dir` flag exists (line 531). The three bundle files are written (lines 540-559).
- **Hashes:** all eight SHA-256 values in the evidence table match `EXPECTED_SHA256` in scripts/pieces/piece_090.py:77-84.
- **GuildErrorPacket and the two notification classes:** the note says the native client owns these classes. The Native Map notes (repo:notes/Native Map/Shards/S0336...) and the test at test_piece_090.py:225-228 support this.

**Unsure:**
- The note says "The checker asserts set equality between the server enum and the client constructors." In piece_090.py:459 this is recorded as a boolean finding (`native_confirms_enum_only`), not a hard assertion in the checker. The unit test does assert it (test_piece_090.py:273). This is a wording nuance, not a false claim, so I left it.
- I could not verify the lab-side input files (`decompiled/`, `working/`, `references/`) directly; they are not in the repo. I checked only the hashes the checker pins.
