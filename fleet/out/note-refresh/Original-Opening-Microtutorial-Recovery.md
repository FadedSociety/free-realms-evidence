<!-- fleet job=note-refresh id=Original-Opening-Microtutorial-Recovery status=done turns=16 usd=0.0179 tokens(read,write,in,out)=[530631, 50983, 34, 12358] model=claude-haiku-5-5 -->
# notes/Research/Original Opening Microtutorial Recovery.md

**Verdict:** minor drift. The journal-close chain, the wire shapes, the NPX prompt IDs and the "no production source changed" framing still match the tip. One mechanism claim about the 45/6 LookAt offset is now contradicted by the code and the later F158 evidence, and one function citation is off by a line.

**Corrections:**

1. `old:` or a float vertical offset for an actor target
   `new:` or an i32 vertical offset in tenths of a world unit for an actor target
   `why:` The client converts an integer at the actor-form slot: `repo:notes/Autopilot/F158.md:51-64` (the wire field is an i32 in tenths, "not an f32"; the F124/T003 "raw f32" reading was contradicted). Client pseudocode for `009be130` shows `(float)local_158 * _DAT_017e795c`, where `local_158` is an integer, so the 0.1 scale is applied to an integer (`client_sql fn 009be130`). The server encodes it as `offset_tenths: i32` (`repo:prototype/osfr-tools/src/quest_engine.rs:354-356`, `:2871-2876`, comment "i32 offset in tenths").

2. `old:` Original `StoryBook:Hide` at ScriptsBase.lua14688 returns when Hide is disallowed or the book is already hidden.
   `new:` Original `StoryBook:Hide` at ScriptsBase.lua14689 returns when Hide is disallowed (line 14691) or the book is already hidden (line 14697).
   `why:` `ui:ScriptsBase.lua:14689` is the function header and `:14688` is blank; the two early returns are at `:14691` and `:14697`. The `:14722` objective-event line is correct. The reference copy in `repo:scripts/pieces/piece_072.py` and `prototype/osfr-tools/src/restoration/piece_072.rs:7` already uses 14689.

**Checked and holding:** the `StoryBook:Hide` tutorial-only emit at `:14722` (`ui:ScriptsBase.lua:14716-14722`); `00c1f0a0`→`009aaf50`→`00c43140` dispatch; `00cf3900` IString compare and `00cf3920` UIEvent ctor; `00cffba0`→`00cff7d0`→`00cffa70` send path; `00cf36a0` calling `00cffba0` (the LookAt camera completion emits the same 45/7); `008a89a0` setting +0x780 and creating the tutorial manager, and `008a9200` as the clearing setter; the 45/7, 45/8, 45/9 and 45/10 layouts against `quest_engine.rs:2863-2889` and `restoration/piece_072.rs:21-27`; the NPX prompt IDs and sounds (`piece_072.rs:127-190`); the rockbarrier and invisible_cube model IDs (`client:Resources/Models.txt:876, 3380`); and the piece_072 objective-ID gap (`piece_072.rs:72-76`, `tests/piece_072.rs:81`), which is still unrecovered in the tip code.

**Unsure:**
- The note's claim (line 32) that the 45/6 and 45/10 branches in `009be130` do not need an active MiniGameState. I did not isolate the MiniGame predicate in `009be130` (the `FUN_009b5890` reader is a bounded-record reader, not obviously a state check). Not settled.
- `Ui.IsInNPXTutorial` (`00c16fb0`) and `Ui.TutorialCancelled` (`00c16ff0`) are not in the decompiled `fn` table, so I could not confirm the player+0x780 read or the `008a9200` clear from the `00c16ff0` side.
- The lab-side hashes, reproducer and independent-review counts (lines 9-11, 58) live outside the repo and cannot be checked from here.
- No production 45/7 handler was judged against the note's acceptance section (line 54). The tip has one (F124, T003, F158), but the note states requirements, not status, so I made no correction.
