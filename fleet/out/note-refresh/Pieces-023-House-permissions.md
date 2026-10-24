<!-- fleet job=note-refresh id=Pieces-023-House-permissions status=done turns=22 usd=0.0250 tokens(read,write,in,out)=[763082, 67967, 46, 17790] model=claude-haiku-5-5 -->
# notes/Research/Pieces/023 House permissions.md

**Verdict:** minor drift. The module, owned paths, test and probe counts, error codes, role rule and item-006 claims all hold at the tip. Three claims are false (two about level handling, one about the community gateway), and one status snapshot is stale.

**Corrections:**

1. `old:` Levels other than 3 keep their numeric value and grant nothing.
   `new:` Levels below 3 keep their numeric value and grant nothing. Levels above 3 are treated as edit grants (`level >= 3`), so a future level cannot silently lose an existing grant.
   `why:` repo:prototype/osfr-tools/src/restoration/piece_023.rs:149-152 (`can_edit` is `self.level >= PERMISSION_CAN_EDIT`) and :292, :280. The module's own doc at :149-150 says higher values keep the capability. The note's "grants nothing" is wrong for levels above 3.

2. `old:` The neighbouring levels carry no recovered meaning, so this item grants them nothing.
   `new:` Levels below 3 carry no recovered meaning, and this item grants them nothing. Levels 4 and up are treated as edit grants (`>= 3`), as in the module's own rule.
   `why:` repo:prototype/osfr-tools/src/restoration/piece_023.rs:149-152 and :94 (`PERMISSION_CAN_EDIT = 3`). The test at repo:prototype/osfr-tools/tests/piece_023.rs:116-117 covers only levels 3 and 1.

3. `old:` the community handler is the only housing handler the community gateway implements, and it merely echoes the flag with no permission check
   `new:` the community gateway routes two housing inner opcodes, SetEditMode (6) and EnterRequest (19). The SetEditMode handler merely echoes the flag with no permission check, and the EnterRequest handler is a stub that returns true without any check
   `why:` refs:Sanctuary/src/Sanctuary.Gateway/Handlers/BaseHousingPacketHandler.cs:33-35 (both `ClientHousingPacketSetEditMode.OpCode` and `ClientHousingPacketEnterRequest.OpCode` are routed); refs:Sanctuary/src/Sanctuary.Gateway/Handlers/BaseHousingPacket/ClientHousingPacketEnterRequestHandler.cs:26-76 (body is commented out, returns true). The SetEditMode echo is confirmed at refs:…/ClientHousingPacketSetEditModeHandler.cs:32-36.

4. `old:` A whole-crate `scripts/cargo.ps1 test` currently stops in other workers' items
   (`tests/piece_022.rs` has no `src/restoration/piece_022.rs` yet; `src/restoration/piece_016.rs` has
   `E0204`/`E0716` errors).
   `new:` A whole-crate `scripts/cargo.ps1 test` stopped in other workers' items at the time of this run
   (`tests/piece_022.rs` had no `src/restoration/piece_022.rs` yet; `src/restoration/piece_016.rs` has
   `E0204`/`E0716` errors). At the tip `src/restoration/piece_022.rs` now exists, so that particular failure is gone; the piece_016 errors were not re-checked.
   `why:` repo:prototype/osfr-tools/src/restoration/ directory listing (piece_022.rs present) and repo:prototype/osfr-tools/tests/ (piece_022.rs present).

**Verified and unchanged (for the record):** owned paths exist (`src/restoration/piece_023.rs`, `tests/piece_023.rs`, `scripts/pieces/piece_023.py`, `tests/pieces/test_piece_023.py`); 13 `#[test]` in `tests/piece_023.rs`; 8 `test_` methods in the checker tests; 8 checks in `CHECKS` (`scripts/pieces/piece_023.py:354-362`); the `#[path]` include and no `mod restoration` in `src/lib.rs` (module is unregistered, as the note says); opcode values and the 42-member `BaseHousingPackets` enum (refs:OpenSourceFreeRealms/ofrserver/Server/LibSOE/Core/PacketCodes.cs:548-591); `FUN_00ab9080` reads one field and switches with case 2/6 sharing the denial branch; `FUN_00aa4fd0` constructs opcode 0x17 and `FUN_00ac7af0` latches a flag before sending; locale 421055 is "You do not have permission to enter that house."; item 006 `set_permission`/`set_locked` refuse non-owners (repo:prototype/osfr-tools/src/housing.rs:793-830) and `permission_for` uses `>= PERMISSION_CAN_EDIT` (housing.rs:859); client column table `FUN_00cbb310` lists Permission Level (3), In Edit Mode (4), Can Edit (12).

**Unsure:**
- Every `lab/...` citation (for example `lab/decompiled/server/LibSOE/SOE/BaseHousingPackets.cs:78`, `PlayerHousingInstanceData.cs`, `lab/reports/piece-023-…`) could not be opened: `lab/` is not in the repo root listing. The same facts exist in refs (`PacketCodes.cs`, `InstancePermission.cs:9` "3 - Can Edit") under different paths.
- The `pseudocode.c` line numbers (1384085, 1397301-1397491, 1400087/1400096/1400101, 1795998/1796000/1796016, 1409455) could not be matched to the client database, which gives function addresses, not line numbers. The function bodies they point to do match.
- Test pass counts (13, 24 lib, 8 checker), rustfmt exit codes and the negative-control run cannot be re-run from read-only tools.
- The note says the error body's `pseudocode.c:1397303-1397491` range in the module and `1397350` in the test file; these differ slightly but both are in the same range, so I left them alone.
