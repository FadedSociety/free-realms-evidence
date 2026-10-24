<!-- fleet job=note-refresh id=Native-Journal-Live-Objective-Keys status=done turns=21 usd=0.0196 tokens(read,write,in,out)=[643651, 55745, 44, 12287] model=claude-haiku-5-5 -->
# notes/Research/Native Journal Live Objective Keys.md

**Verdict:** minor drift. The core claims hold at the tip: `opening_journal.rs` rekeys incremental 49/9 and 49/10 by definition ID, and full self and QuestAdd keep tuple ordinals. The native address chain also checks out. Only the test count and the scope of the Gateway.dll oracle claim are stale.

**Corrections:**

1. `old:` All5 focused journal tests pass, including the entire patched self payload compared with the original supplied Gateway.dll `ReadFromJSON` serializer output.
   `new:` All six non-ignored focused journal tests pass (two private tests are ignored by default). The entire patched self payload comparison with the original supplied Gateway.dll `ReadFromJSON` serializer output is not part of the default run. It is the ignored private test `private_captured_journal_loads_and_only_the_proven_span_changes`, which asserts it only when `OSFR_JOURNAL_ORACLE` is set.
   `why:` `repo:prototype/osfr-tools/tests/opening_journal.rs:215,271,324,370,387,480` are six `#[test]` functions. Lines 521 and 551 are `#[ignore]`. The Gateway.dll comparison is at lines 535-538, inside the ignored test at 521. `repo:notes/Reviews/Native Cooking Preparation 154503.md` and `repo:notes/Design/Build Ledger.md` do not contradict this. Suite Status lists `tests/opening_journal.rs | 6 | 0 | 2`, which is 6 passed and 2 ignored.

**Checked and holding (no change):**
- `repo:prototype/osfr-tools/src/opening_journal.rs:356-358`: incremental keys use `goal.id` (definition ID) for subtypes 9 and 10. The comment cites 00BAF380 and 00C7A990/00C7AA10. Lines 368-370 use the same key for subtype 10.
- `repo:prototype/osfr-tools/src/opening_journal.rs:486-488`: full records write `index + 1` as the wire tuple key and `goal.id` as the definition ID. `quest_record` is used by the subtype 3 QuestAdd path at line 346.
- `repo:prototype/osfr-tools/tests/opening_journal.rs:423-425` and `:449`: the fixture asserts definition 12001 for live key and 12002 for the second objective.
- Client pseudocode (`client_sql`): `FUN_00baf380` calls `FUN_00baba60(iVar1,iVar1)` for each node; `FUN_00bab950` writes `+0xf0 = *param_2`; `FUN_00c7a990` looks up the quest by ID and then the objective at `+0xf0`; `FUN_00c7aa10` writes state `+0xd0 = 2` only after a match; `FUN_00cf7b70` reads `+0xf0`. All match the note's table.
- Note's links `Native Opening Quest Journal`, `Native Farm Completion 151602` and `Native Cooking Preparation 154503` resolve to files in `notes/`.

**Unsure:**
- `lab/reports/trace-journal-incremental.py`, `journal-incremental-trace.json` and `journal-incremental-disassembly.txt` (line 24) and the run references in the 151602 and 154503 reviews. `lab/` is a sibling of the repo (`.gitignore:27-28`), not in `repo`, so I could not check them.
- The disassembly byte details (`00baf458 push edi`, `00bab98e`, `00bab990`). I checked the pseudocode, not the bytes.
- "The optional update/completion booleans control toast/chat behavior." This is a client behavior claim I did not check.
- "ID0 text labels remain a separate presentation failure." `repo:notes/Reviews/Native Cooking Preparation 154503.md:7` reports `<STRING 0 NOT FOUND>` for two custom goals, which agrees. I did not check whether the later text overlay has changed this.
