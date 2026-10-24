<!-- fleet job=note-refresh id=Pieces-070-Quest-journal-wire status=nothing_found turns=10 usd=0.0112 tokens(read,write,in,out)=[222194, 44099, 22, 7022] model=claude-haiku-5-5 -->
# notes/Research/Pieces/070 Quest journal wire.md

**Verdict:** current. Every repo-checkable claim in `notes/Research/Pieces/070 Quest journal wire.md` still holds at the tip. The note's "not yet integrated" status is still accurate, so no corrections are needed.

**Checked and holding:**
- **Files exist at the cited paths:** `prototype/osfr-tools/src/restoration/piece_070.rs`, `prototype/osfr-tools/tests/piece_070.rs`, `scripts/pieces/piece_070.py`, `tests/pieces/test_piece_070.py`.
- **Integration seam still open (the note's key gap):** `prototype/osfr-tools/src/opening_journal.rs:178` still has `root_unknown: [u8; 8]`. It is set at `:231` and re-emitted at `:282` (`journal.extend(self.root_unknown)`). The captured bytes are still copied in production, as the note says.
- **Module not registered:** `prototype/osfr-tools/src/lib.rs` has no `restoration` or `piece_070` declaration. The test reaches the module through `#[path]` (`tests/piece_070.rs:22-24`), which matches the note's "register `pub mod piece_070;`" step. `notes/Research/Module Registration 2026-10-13.md:185` also lists `tests/piece_070.rs` as 3 pass / 0 fail / 1 ignored.
- **API names:** `JournalRootTail` with `opening_campaign`, `with_recovered_fields`, `from_span`, `replace_in_span`, `locate`, `parse`, `write` and `to_bytes` (`src/restoration/piece_070.rs:51-219`). Constants `10`/`30` are at `:40` and `:43`. Tail is 17 bytes (`:30`).
- **Validation rules:** completed count non-negative, selected id `-1` or positive, bool bytes exact (`piece_070.rs:118-126`, `:150-154`). Matches the note's "domain-only" description.
- **Test counts:** `tests/piece_070.rs` has 3 `#[test]` plus 1 `#[ignore]` (`:103`, `:134`, `:164`, `:251-252`), matching "3 passed; 1 ignored". `tests/opening_journal.rs` has 8 `#[test]` of which 2 are ignored (`:520-521`, `:551-552`), matching "6 passed; 2 ignored". `test_piece_070.py` has 13 test methods across 5 classes, matching "Ran 13 tests".
- **Oracle variants:** `scripts/pieces/piece_070.py:431-432` uses `recovered-pair` (0, 910001, False, 10, 30) and `altered-pair` (7, -1, False, 7, 45), as the table states.
- **Audit subtype lengths:** `scripts/pieces/piece_070.py:80-85` gives 10 / 27 / 23 / 10 for subtypes 4 / 9 / 10 / 12, matching the note.
- **CLI flags:** `--run`, `--content`, `--reports-dir` exist (`piece_070.py:839-846`).
- **Reference span hash:** `1b36c0f5de284ea28a206b9c10162a2e73c9ea582e559eb6f3aa951a42871037` appears in `scripts/pieces/piece_070.py:58` and in `refs` `opening-journal-text-v2/content/quests.json:53`, matching the note's "sha256 `1b36c0f5…1037`". The 7,970-byte size matches `piece_070.py:8`.
- **Autopilot:** no `notes/Autopilot/` report touches piece 070's files or the opening-journal root tail. The only hits for "070" are unrelated IDA addresses or content IDs.

**Unsure:**
- The native pseudocode line citations (`pseudocode.c` 1104250-1104421, the `0x1100`/`0x1104` hit lines, and the `1589775` line), the `lab/` decompiled serializer lines, and the run-171251 frame numbers (3876, 3877, 4071, 4072) and totals (4158 frames / 4156 CRCs). These live under `lab/`, which is not in the repo roots I could search, so I could not verify them. The scripts reference the same run name and the 49-subtype logic, but I did not find the frame numbers in the repo.
- The `Unknown4`/`Unknown5` writer order (`ClientPcData.cs` quest block, lines 1492-1529). The reference-span provenance in `refs` agrees with the note's `quests.json` line 97 ("supplied ClientPcData.cs lines1492-1529"), but I did not open the decompiled source itself.
