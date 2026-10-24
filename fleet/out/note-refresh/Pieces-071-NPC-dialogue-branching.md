<!-- fleet job=note-refresh id=Pieces-071-NPC-dialogue-branching status=done turns=16 usd=0.0206 tokens(read,write,in,out)=[624632, 69269, 34, 11338] model=claude-haiku-5-5 -->
# notes/Research/Pieces/071 NPC dialogue branching.md

**Verdict:** minor drift. The note's architecture and status claims hold at the tip: the module exists, is test-included rather than registered, the phase mapping and the no-in-progress gap for "Fighting off the Pack" match the code, and the 17-check count holds. Two citations/counts are off.

**Corrections:**

1. `old:` | `tests/pieces/test_piece_071.py` | 22 stdlib tests (fixtures + real-source checks) |
   `new:` | `tests/pieces/test_piece_071.py` | 20 stdlib tests (fixtures + real-source checks) |
   `why:` The file defines 20 `def test_` methods (tests/pieces/test_piece_071.py:58-229, across PhaseLineTests, RustLiteralTests, DefinitionValidationTests and RealInputTests). The Verification block's "Ran 22 tests ... OK" is a historical log quote I could not re-run, so only the file-table count is corrected.

2. `old:` End screen (Lua 15496): exactly one node,
   `new:` End screen (Lua 15501, added only when `self.responseButtons == nil`): exactly one node,
   `why:` ui:ScriptsBase.lua:15501 is the `AddResponseNode(Ui.GetString("questThanks"), 300, 17, 3)` call. Line 15496 is `self:SetNPCDialog(text)`. The call is also guarded by `if self.responseButtons == nil`, which the note omits.

**Checked and holding (no change):**
- `src/restoration/piece_071.rs` exists; `tests/piece_071.rs` has 12 `#[test]`s and `#[path]`-includes the module (tests/piece_071.rs:49-51); `src/lib.rs` has no piece_071 registration (only `pub mod quests;` at line 74).
- `scripts/pieces/piece_071.py` and `tests/pieces/test_piece_071.py` exist; the checker emits 17 findings (1 shape + 3 code-string + 4 locale + 1 window + 4 Lua needles + 3 Lua response + 1 rust-binding).
- Extractor accepts 1..=3 quoted lines and rejects other counts (scripts/pieces/piece_071.py:192-214).
- `quest_phase` mapping matches the note (piece_071.rs:115-123); `QuestProgress` has accepted/counts/completed/rewarded (quests.rs:51-55).
- `select_node` returns `None` for a phase with no node, and `respond` returns `Err` for an empty menu (piece_071.rs:542-576). "Fighting off the Pack" has no in-progress node (piece_071.rs:674-715).
- `original_quest_id` is `None` in both definitions (piece_071.rs:620, 678).
- Constructor names FUN_009f5890, FUN_009f5760, FUN_00a99bd0 and FUN_00a9ad20 exist in the client fn table.
- Lua `AddDialogResponseNodes` at ScriptsBase.lua:15669, with questYes at 15671 and questNo at 15673, is correct. `Main_wndQuestStart_swfQuestStart_OnUserEvent` is at 15695. The `noDecline` gate is at 15672.

**Unsure:**
- The lab-only sha256 hashes, the wndDialog.xml `btn0..btn4` count (the checker's regex would confirm it, but the lab tree is not in the repo), the wiki revision contents and reward amounts (the 16/18 coin figures are not contradicted by the native MODLOG/Tasks notes), and the `InteractionData` `DescString` claim. None of these could be checked from the repo or client tables.
- The Verification block's cargo and unittest run logs: they are historical and the lab report directory is not readable from here.
