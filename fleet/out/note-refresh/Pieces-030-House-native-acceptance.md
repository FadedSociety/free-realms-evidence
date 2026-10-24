<!-- fleet job=note-refresh id=Pieces-030-House-native-acceptance status=done turns=22 usd=0.0247 tokens(read,write,in,out)=[861535, 68135, 46, 15159] model=claude-haiku-5-5 -->
# notes/Research/Pieces/030 House native acceptance.md

**Verdict:** minor drift. The note's status, file paths, counts, gate rules, error-switch mapping and acceptance lot all match the tip. One sentence overstates what item 025 lists.

**Corrections:**

- `old:` undecoded; item 025's `UNRECOVERED_OPCODES` lists them.
  `new:` undecoded; item 025's `UNRECOVERED_OPCODES` lists 28, 39, 40, 41 and 53, but not 2 or 51.
  `why:` `repo:prototype/osfr-tools/src/restoration/piece_025.rs:428-434` lists (28, 39, 40, 41, 53) only. Opcodes 2 and 51 do not appear there, and piece_025.rs has no body handling for them (only `ClientHousingPacketPlaceFixtureRequest` at lines 117 and 371).

**Checked and holding (no change needed):**

- Paths exist: `src/restoration/piece_030.rs`, `tests/piece_030.rs`, `scripts/pieces/piece_030.py`, `tests/pieces/test_piece_030.py`.
- Not registered: `src/lib.rs` has `housing`, `housing_native` and `housing_service` but no restoration/piece_030 module.
- Owned vectors: `tests/piece_030.rs` has 20 `#[test]` attributes. One is `#[ignore = "requires OSFR_PIECE_030_REPORT_DIR…"]` (line 556), so 19 run and 1 is ignored. This matches the note.
- `ACCEPTANCE_WIRE` has 13 rows (1, 2, 3, 5, 6, 19, 28, 40, 41, 45, 46, 51, 53), matching the note (`piece_030.rs:109-188`).
- Base opcode 127: `FUN_00aa4990` writes `0x7f` (client `00aa4990`).
- Error switch: 1→`FUN_00ab54b0`, 2/6→`FUN_00ab5590`, 3→`FUN_00ab5670`, 4→`FUN_00ab5750`, 5→`FUN_00ab5830` (client `00ab9080` switch). `FUN_00ab5590` prints "You do not have permission to enter that house." Locale 421055 carries the same text.
- Acceptance lot: `refs:FreeRealms-Legacy/src/Resources/Houses.json:1-15` gives NameId 6514, ZoneId 1, Min [322.0,-100,392.1], Max [443.3,60.0,477.8]. This matches `ACCEPTANCE_BUILD_AREA` (`piece_030.rs:76`).
- `LOCAL_ACCEPTANCE_MAX_FIXTURES = 64` (`piece_030.rs:79`).
- `native_evidence_complete()` is gated on `EvidenceOrigin::NativeCapture` (`piece_030.rs:442-443`).
- Replay report format and row order: `render()` writes `origin:` and `native evidence complete:` (`piece_030.rs:463-483`). The replay sequence is enter 1/2, edit mode 3, place request 4, place fixture 5 (`piece_030.rs:1244-1287`).
- Checker: 9 probes (`scripts/pieces/piece_030.py:293-533`). 10 tests in `tests/pieces/test_piece_030.py` (7 ParseTests + 3 RealCorpusTests, including the two negative controls).
- Gate rules: move, remove, visit (permitted editor, code-2 refusal, unanswered = UNPROVEN) and restart all match the code (`piece_030.rs:780-1083`).
- Cross-links resolve to existing notes (`notes/Research/Pieces/025…`, `026…`, `023…`, `notes/Design/MMO Worker Contract.md`, `notes/MMO Work Queue.md`).

**Unsure:**

- The `lab/` artifacts cited (`lab/decompiled/...`, `lab/reports/piece-030-20261009T032826Z/`, the RED/GREEN and export logs, the 42-member enum and sha256) are not in the repo, so I could not check them. The Autopilot L045 record (`piece_030 19 (1 ignored)`) and Suite Status (`19 | 0 | 1`) agree with the test counts.
- The wiki `Lots` revision 49783 quote is not in `refs`. I did not search further.
- `scripts/pieces/piece_030.py:15` says the client constructs "43 members". The note's "42" is correct. The 43 is a stale docstring in the checker, not in the note.
</result>
