<!-- fleet job=note-refresh id=Soccer-Kick-Direction-Binding status=done turns=12 usd=0.0292 tokens(read,write,in,out)=[438239, 82722, 26, 28877] model=claude-haiku-5-5 -->
# notes/Research/Soccer Kick Direction Binding.md

**Verdict:** minor drift. The dataflow anchors, offsets, vtable slots and the sub-13 offset correction all match the pinned client pseudocode. The problems are a gate overstatement in the state-setter bullet and the "Unresolved" list, which still reports as open things the follow-on section resolved.

**Corrections:**

1. `old:` emits a sub-14 packet.
   `new:` calls the sub-14 sender (`FUN_00cdc5c0`), which emits a packet only when `player+0x2A8` and byte `player+0xC0` are set.
   `why:` client `fn 00cdc5c0`: `if ((param_1[0xaa] != 0) && (param_1[0x27] = param_1[0x26], (char)param_1[0x30] != '\0'))` gates the `FUN_00b746b0` packet fill. The note's own Verified chain (line 31) states the same gate, so "every state change ... emits" overstates it.

2. `old:` The `+0x38` getter body was not decompiled this pass, and whether the live object overrides
   `new:` The `+0x38` getter is `FUN_00cd9df0` (decompiled in the follow-on below); whether the live object overrides
   `why:` client `fn 00cd9df0` is the target-directed getter (scans for `+0x1C == 3`, returns `(1,0,0,1)` when no target). The note's own vtable table (line 182) lists it. Reviewer `notes/Reviews/Soccer Direction Semantics Review.md:21` confirms the `+0x38 -> 0x00CD9DF0` slot.

3. `old:` Native writers of `player+0x20..0x2C` and `player+0x30..0x3C` were not located in this bounded
   `new:` Native writers of `player+0x20..0x2C` were not located in this bounded
   `why:` The follow-on (note lines 155-157) names writers of `+0x30..0x3C`: `FUN_010748a0`, `FUN_010727d0`, and the `FUN_01074b50` fallback `param_1[0xc] = param_1[0x14]`. The fallback is confirmed in client `fn 01074b50`. `FUN_010748a0` and `FUN_010727d0` exist in client `fn`. Only the `+0x20..0x2C` writer is still open (note line 191; reviewer line 38-39).

4. `old:` only provenance is proven. Not "aim", "velocity", "position" or "facing" in this note.
   `new:` only provenance is proven in the first pass; the follow-on below assigns dataflow roles (vecA action direction, vecB steering vector, vecC horizontal coordinates) and still names no unit or game meaning.
   `why:` The follow-on "Resolved this pass" section (note lines 144-158) assigns those roles. Client `fn 01072610` writes `+0x50..+0x5C` from `+0xF0..`, and `fn 01074b50` dot-products `+0x50..` with `+0xF0`. The first-pass bullet now reads as if no role was recovered.

**Checked and holding (no change):**
- Sender gate, `+0x9C` save, packet field sources (`+0x98`, `+0xA4` x255, `+0xB0`, `+0x30..+0x3C`, `+0x20..+0x2C`, getter `+0x30` to `+0xF0..`): `client fn 00cdc5c0`, `fn 00cd8080`.
- Reader order and receive map (`FUN_00b80ac0` case 0xe: state to `+0x9C`, word to `+0xB0`, aux to `+0xA4`, vecA to `+0xF0`, vecC to `+0x70`): `client fn 00b80ac0`.
- Kick/back test `DAT_018144d0 <= dot` gives `0x16`, else `0x17`; vecB norm test gives `0x23`/`0x24`; `+0x78` and `+0x7C` call paths: `client fn 01074b50`, `fn 00cd8f50`, `fn 01074590`, `fn 01072610`.
- Ball impulse ctor `FUN_00b73790` (`0xd`) and sub-14 ctor `FUN_00b746b0` (`0xe`): `client fn`.
- `soccer_match::apply` refuses `sender != intent.player()`: `repo:prototype/osfr-tools/src/soccer_match.rs:598-600`.
- Cross-linked notes exist; `0 of 2978` sub-13 matches `notes/Research/Soccer Kick Pass Wire Mapping.md:141`.

**Unsure:**
- Lab artifacts and hashes (lines 12-18, 20-25, 89-93, 121-127, 134-138) are outside `repo`. I could not check them.
- Constant values `DAT_017e795c = 0.1`, `DAT_017ed9d0 = 255`, `DAT_017f1ae4 = 1/255`, `DAT_018144d0 = -0.2`: the reviewer's raw-byte check (review line 20) agrees, but I did not read the bytes myself. `DAT_0175b420 = 1.0` is consistent with the clamps in the code.
- Line 173 "(1, 0, 0, 1)": the no-target branch returns `uVar9` for x, which is `DAT_01762a34` when `FUN_01071fc0() == 1`. I did not check `DAT_01762a34`, so the constant `1` is unconfirmed for that branch.
- Line 107 "no subsystem `+0x7C` consumer": the player's own `+0x7C` is now resolved (`FUN_01072610`). I could not tell whether the note means a different subsystem object, so I left it.
