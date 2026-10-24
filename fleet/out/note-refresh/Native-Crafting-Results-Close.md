<!-- fleet job=note-refresh id=Native-Crafting-Results-Close status=nothing_found turns=12 usd=0.0116 tokens(read,write,in,out)=[270857, 38727, 26, 8176] model=claude-haiku-5-5 -->
# notes/Research/Native Crafting Results Close.md

**Verdict:** current. Every checkable claim about the original client that I could reach still matches the decompiled pseudocode and the vault's own notes. No corrections.

**Checked and holding:**
- `Ui.LeaveMiniGameOrEncounter` path: `008d2730` calls `009bd240`, and `009bd240` only runs the `+0x61` encounter branch (`FUN_0092a1b0`) when the state flag is set. It ends with `FUN_0092f300()`, which is the closed-results notification. (`client_sql` fn `008d2730`, `009bd240`)
- `CommandPacketClosedMinigameEndScreen` constructor `008a2eb0` calls `FUN_008a2820(0x2a,0)` (opcode 26, sub 42). `0092f300` calls `008a2eb0`, then `00925c90` when `+0x280` is set. `00925c90`'s callers are only `0092f300`. (`client_sql` fn `008a2eb0`, `0092f300`, `00925c90`)
- `Ui.QuitMiniGame` `00939100`: a nonencounter state goes to `009be8e0`, which calls `009bdc60(6,-1,-1)`. (`client_sql` fn `00939100`, `009be8e0`)
- Server 39/19 path `009bf190`: calls `FUN_009bdc60(7, param_2, -1)` and `FUN_009b7170`, consistent with the note's "39/7 acknowledgment, not the user Close." (`client_sql` fn `009bf190`)
- `beb70` stores its third parameter into `+0x61` (`*(char *)(iVar4 + 0x61) = param_3`). (`client_sql` fn `009beb70`)
- Lua `SetMiniGameEndData` maps Type 9 to `ScoreScreen:Show(status, 9)`. (`ui:ScriptsBase.lua:36677-36678`)
- Packet bytes `1a002a00` match the vault's other Close notes and the community catalogue (`refs:Sanctuary*/PacketReaderExtensions.cs:127`, `OpenSourceFreeRealms/.../PacketCodes.cs:356`).

**Unsure:**
- **JoinGame flag claim (line 14, "ordinary JoinGame009bfdb0 passes0").** The pseudocode for `009bfdb0` reads `FUN_009beb70(local_294,0,local_2d,local_2a0);`. The call shows four arguments against a five-parameter signature, so I cannot tell which argument is the flag. It may be `0`, or it may be `local_2d`. The note's claim is not contradicted, but it is not clearly proven either. Consider softening it to "passes an argument that the decompiler renders as `0`/`local_2d`."
- **Lab artifacts (line 16).** `lab/reports/native-crafting-close-proof.json`, its SHA256, and `trace-native-crafting-close.py` are not reachable from my tools (`repo:lab/reports` is not browsable). I could not reproduce the hash or the script's existence. Other vault notes cite the same SHA256 (`notes/Reviews/Native Crafting Results Independent Review.md:34`), so the citation is at least consistent.
- **Byte-level serialization claim (line 8, "serializes only two u16 values").** `0090ac70` (the writer) is large, and I only read its opening. The "header-only" wording agrees with `notes/Reviews/Native Crafting Results Independent Review.md:9`, but I did not verify the full writer body.
