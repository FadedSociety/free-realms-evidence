<!-- fleet job=note-refresh id=Pieces-044-Class-switching-wire status=done turns=20 usd=0.0258 tokens(read,write,in,out)=[808964, 79445, 42, 15549] model=claude-haiku-5-5 -->
# notes/Research/Pieces/044 Class switching wire.md

**Verdict:** minor drift. The code-side claims hold at the tip. One client-side function address is wrong, and the note's own wording is otherwise accurate.

**Corrections:**

1. `old:` `` `FUN_008a28e0` builds `CommandPacketSetProfile` with `0xd` ``
   `new:` `` `FUN_008a29f0` builds `CommandPacketSetProfile` with `0xd` ``
   `why:` The client database has `FUN_008a29f0` as the SetProfile constructor. Its body is `FUN_008a2820(0xd,0);` followed by `*param_1 = CommandPacketSetProfile::vftable;` (client fn `008a29f0`). `FUN_008a28e0` is not a builder. It only restores `BaseCommandPacket`/`BasePacket` vtables and conditionally calls `_free` on bit 0, which is a destructor shape (client fn `008a28e0`). The address also matches `notes/Build Guides/Network/Gateway and Transport.md:3652` (ctor `008a29f0`) and the 26/13 comment at `prototype/osfr-tools/src/bin/osfr_gateway/f261_pickup_reload.rs:104`. The same wrong address appears in `prototype/osfr-tools/src/restoration/piece_044.rs:15` (lines 14-16 of the module doc), so fix it there too when the lead touches that file.

**Checked and holding (no change):**
- `prototype/osfr-tools/src/restoration/piece_044.rs` exists (303 lines). `tests/piece_044.rs` includes it by `#[path = "../src/restoration/piece_044.rs"]` at line 46. `scripts/pieces/piece_044.py` and `tests/pieces/test_piece_044.py` exist.
- `piece_044.rs` is not registered in any module tree. No `mod piece_044` / `pub mod piece_044` appears in `src/`, so "the lead still has to register" is still true.
- Failure payload: `CommandPacketActivateProfileFailed::packet()` emits `[26,0][26,0][profile][reason]` with `reason: 0` (`piece_044.rs:122-134`, `164-174`). This matches the note's `[26,0][26,0][requested profile][0]`.
- Request shape: `decode_switch_request` requires exactly 8 bytes, `[26,0][13,0][int32]` (`piece_044.rs:200-221`).
- Live path: a bad switch sends chat, not the failure command. `gameplay/jobs.rs:153-173` (`stage_job_selection`) pushes `chat::system` for unlocked and activate/outfit failures. It is called from `gameplay.rs:4372-4387` and `gameplay.rs:5355-5367`. No `ActivateProfileFailed` sender exists outside `piece_044.rs`. The note's claim that both paths answer with chat is correct.
- Test counts: `tests/piece_044.rs` has 7 `#[test]` functions, matching "7 passed". `tests/pieces/test_piece_044.py` has 17 `def test_` methods, matching "17 passed".
- Client constructors: `FUN_008a2820` stores `0x1a` in `BasePacket` and writes the two immediates. `FUN_0089d180` stores `0x26` and takes the sub-opcode. `FUN_008a2b20` builds `0x24`. `FUN_008a2ca0` builds `0x1a` and zeroes `param_1[4]` and `param_1[5]`, i.e. two int fields.
- Community refs: `Sanctuary/.../CommandPacketSetProfileHandler.cs` sets `ActiveProfileId`, `Animation = 3001` and `CompositeEffect = 4005`. `ClientPcProfile.cs` has `Abilities` and `Items`. `PacketReaderExtensions.cs` names 13, 26 and 36 for the command family and 21 for the client update.

**Unsure:**
- The `lab/` tree is not present at the repo root (`list lab` returns "not a directory"). I could not check the claimed `lab/reports/piece-044-20261009T044119Z/` logs (red/green/sibling/checker, "55 findings", "0 gaps"), the `lab/captures` scan for `[26,0][13,0]`, or the `lab/decompiled` paths. Other notes reference `../lab` as an external directory, so this may be expected.
- "names the same five sub-opcodes" (note line 43). `PacketReaderExtensions.cs` names 13/26/36 for commands and 21 for the client update. I did not find 1 for `ClientUpdatePacketHitpoints` in the same block, and `piece_044.rs:26` says "three command sub-opcodes", so the five count may be imprecise. It is not clearly false.
- "the lead still has to register `pub mod piece_044;` where the restoration modules are declared". No `restoration/mod.rs` exists yet, and other pieces (`piece_095.rs:57`, `piece_096.rs:34`) describe the same pending registration. The statement is consistent with the tip, but I did not confirm where the lead intends to register it.
