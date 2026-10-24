<!-- fleet job=note-refresh id=Kart-Finish-Line-Binding status=done turns=13 usd=0.0197 tokens(read,write,in,out)=[444874, 69385, 28, 13172] model=claude-haiku-5-5 -->
# notes/Research/Kart Finish Line Binding.md

**Verdict:** minor drift. Most repo-facing claims hold (the kart close is `39/7`, `33/22` and `33/19` are the boost and item requests, `33/22` is answered by `33/23`, `33/7` is the client gate claim, `ScriptsBase.lua:48454` calls `Ui.LeaveMiniGameOrEncounter`, and the Sanctuary `ZoneAreaDefinition.cs` shape and fields match). Two statements are wrong.

**Corrections:**

1. `old:` `` `processor+0x68 (lap limit) <= racer+0x15ec (laps)` ``
   `new:` `` `processor+0x1a0 (lap limit) <= racer+0x15ec (laps)` ``
   `why:` The client decompile of `00ba6530` reads the lap limit as `param_1[0x68]` on an `int *` processor, which is byte offset `+0x1a0`, not `+0x68`. The same mapping appears in `repo:notes/Research/Kart Race Finish Protocol.md:41` (`0x19 | i32 | lap limit -> processor+0x1a0`) and `repo:notes/Build Guides/Gameplay/Kart Racing.md:48` (`+0x1a0`). The repo code has the same unit slip at `repo:prototype/osfr-tools/src/kart_progress_native.rs:292`, which is worth fixing alongside.

2. `old:` `` `26/42` is this project's local `realm exit` dev command, not original traffic. ``
   `new:` `` `26/42` is the native four-byte results Close (writer `0x0092f300`); this project's `realm exit` command also takes the same exit path (`gameplay.rs:2675`). ``
   `why:` `repo:prototype/osfr-tools/src/gameplay/s6_characterization.rs:13` names `26/42` as the original "four-byte 26/42 Results Close writer 0x0092f300". `repo:prototype/osfr-tools/src/derby.rs:1046` and `repo:prototype/osfr-tools/src/chess_service.rs:341` call it the results-panel Close. `repo:prototype/osfr-tools/src/gameplay.rs:2674-2677` treats `realm exit`, `26/42`, the 41/109 quit and the kart `39/7` close as the same exit. The row's "no op26 frames in the capture" fact is still true; only the "not original traffic" wording is wrong.

**Unsure:**

- The S1/S2 "Kart Service review" (addendum, lines 212-225) has no file in `notes/`. I could not confirm what it said, so I could not check the "7-10 m past gate 31" and "150.9 m" references against it.
- The "Practical wiring" advice ("Do not use `realm exit`/`26/42`") conflicts with the repo treating `26/42` as a valid kart exit (`gameplay.rs:2675`). This is a design choice, not a factual error, so I did not change it.
- The `lab/` paths (probe script, reports, `pack_21/003847.xml`, the pinned references) and the client pseudocode line numbers are outside this tree, so I did not verify them. The `StartingLineFloorArea` and `FinishLineFloorArea` names do not appear in the shipped `ScriptsBase.lua`, which supports the note's claim, but I did not check the XML itself.
- Our server counts laps on the last checkpoint of the layout (`repo:prototype/osfr-tools/src/kart_racing.rs:534-546`). This does not contradict the note's open question about the original server's rule, but it is the nearest repo fact to that question.
