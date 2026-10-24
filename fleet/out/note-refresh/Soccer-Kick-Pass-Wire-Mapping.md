<!-- fleet job=note-refresh id=Soccer-Kick-Pass-Wire-Mapping status=done turns=18 usd=0.0281 tokens(read,write,in,out)=[704323, 75010, 38, 23444] model=claude-haiku-5-5 -->
# notes/Research/Soccer Kick Pass Wire Mapping.md

**Verdict:** minor drift. The body's code claims hold at the tip: constructors, reader and send-site offsets, the dispatch cases, the vtable slots, the Lua action ids, the sub-14 state classes, the test count (25) and the test and wording assertions all check out. The one misleading claim is the opening verdict, which Revision 2 already contradicts.

**Corrections:**

1. `old:` Kick/pass is a **separate packet**: `SoccerPacketImpulseBall`, family 76 sub 13,
   `new:` Sub 13 is a **separate packet**: `SoccerPacketImpulseBall`, family 76 sub 13 (the server-authored impulse, not the client's kick/pass intent; kick/pass intent travels in sub 14 `UpdatePlayerState`, see Revision 2),
   `why:` The client sub-14 sender `FUN_00cdc5c0` writes the state byte from `player+0x98` (client pseudocode `00cdc5c0`), and the state setter `FUN_01072020` sends it. Our own code classifies kick/pass by sub-14 state codes: `repo:prototype/osfr-tools/src/soccer_match.rs:273-276` (`classify_state`: 16..=26 and 31..=34 are kicks, 27..=30 passes). Sub 13 is refused from clients: `repo:prototype/osfr-tools/src/soccer_match.rs:340-342`. The note's own Revision 2 (`### What the capture shows`) says kick/pass "is ... the sub-14 state byte ... not ... sub 13".

**Checked and holding (no change):**
- `repo:prototype/osfr-tools/src/soccer_match.rs:594-602`: `apply(sender, now, intent)` refuses `sender != intent.player()`.
- `repo:prototype/osfr-tools/src/soccer.rs:178-199`: the sub-13 and sub-14 layouts match the note (36 and 62 bytes).
- `repo:tests/pieces/test_soccer_wire.py`: 25 test methods, including `test_report_claims_a_bounded_search_only` (line 273), which asserts the "never" and "server-to-client only" wording.
- `repo:scripts/pieces/soccer_wire.py:173-202`: 23 pseudocode anchors. `SEARCH_SCOPE` is at line 228 and the 122-site count is measured at line 556.
- Client pseudocode: `FUN_00cde9b0` puts `SoccerBall+0x74` at `+0x20`, `param_5` at `+0x28` and `SoccerBall+0x3C` at `+0x2C`, with `uStack_44 = 0` and a `param_6` gate. The `FUN_00b80ac0` cases 0xd, 0xe and 0x10 exist. `FUN_00b79580` NaN checks are on `+0x20`, `+0x24` and `+0x2C` only. `FUN_00afb4a0` uses the `+0xA0` slot. `FUN_00cde9b0` has no textual callers.
- `ScriptsBase.lua:3035-3045`: `Kick = 2`, `Pass = 6`. The tutorial page logic at `ScriptsBase.lua:5045-5047` and `25753-25775` matches.
- Community name table: `Sanctuary/src/.../PacketReaderExtensions.cs:671` (`13 => "SoccerPacketImpulseBall"`). The pinned `ofrserver` `PacketCodes.cs:47` (`BaseSoccerPacket = 76`).

**Unsure:**
- Line ~343 of the note lists the exe column names as "Ball, Dodge, SuperKick, SlideTackle, Steal, Pass, Call, Powerup", omitting `Kick`. The Lua enum has `Kick = 2` (`ScriptsBase.lua:3039`). I could not check the exe strings, so I cannot say whether `Kick` is missing from the exe.
- The exe-level counts and hashes (122 generic slot-0x18 sites, the 64-entry state table at VA `0x01BA2338`, the 1216/250/2978 corpus counts, the `lab/` paths and the pseudocode line numbers) live in `lab/`, which is not in these roots. I could not verify them.
