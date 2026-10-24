<!-- fleet job=note-refresh id=Pieces-072-Starting-area-historical-coverage status=done turns=25 usd=0.0273 tokens(read,write,in,out)=[933323, 76134, 52, 16828] model=claude-haiku-5-5 -->
# notes/Research/Pieces/072 Starting area historical coverage.md

**Verdict:** minor drift. The core claims hold at the tip: the module, the 45/10 and 45/7 wire shapes, the unbound journal-close gate, the Lua line numbers and the test counts all match. Two statements are stale or mis-cited.

**Corrections:**

1. `old:` A plain `cargo test` currently stops on the concurrently edited
   `new:` A plain `cargo test` stopped, at the time of this run, on the concurrently edited
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_047.rs:419` now derives `PartialEq` on `DecodedItemStat` (`#[derive(Clone, Copy, Debug, PartialEq)]`), so the blocker named here is closed at the tip.

2. `old:` (missing `PartialEq` for `DecodedItemStat`), which belongs
   `new:` (this gap is now closed: `DecodedItemStat` derives `PartialEq` at `piece_047.rs:419`), which belonged
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_047.rs:419`. Correction 1 and this one must be applied together. The sentence should not present the failure as current. I did not re-run `cargo test`, so whether the plain run is green now is unverified.

3. `old:` `` `content/opening.json`, SHA256 `4e6ac15c…0ad1` ``
   `new:` `` `lab/references/opening-anvil-placement-v1/content/opening.json`, SHA256 `4e6ac15c…0ad1` ``
   `why:` `repo:scripts/pieces/piece_072.py:66` pins the file at `references/opening-anvil-placement-v1/content/opening.json` under the lab root. No `content/opening.json` exists in the repo tree; the repo's `data/content/` has no `opening.json`. The short path is misleading. This is a citation fix, not a change of substance.

**Checked and holding (no change):**
- `src/restoration/piece_072.rs` exists. It contains `STORY_BOOK_CLOSE_OBJECTIVE_ID: Option<i32> = None` (line 76) and `ORIGINAL_TUTORIAL_GATES` with seven rows (line 127). The 45/10 framing is at lines 437–451, and strict 45/7 decoding (exactly 7 bytes, opcode and type checked, no trimming) is at lines 459–470. The 45/8 and 45/9 layouts are not encoded: only the constants exist, which matches the "not implemented" claim.
- `lib.rs` does not register the module, which matches "lead-owned integration". The test harness includes it by `#[path]` in `tests/piece_072.rs:41`.
- `ScriptsBase.lua`: `StoryBook:Hide` is at 14689, `IsInNPXTutorial` at 14716, the four timers at 14718–14721, and `onStoryBookClose` at 14722 (`repo:ui` ScriptsBase.lua). The event string occurs once in the `.lua` file.
- The trigger-kind list matches `OpeningTrigger` in `src/opening.rs:67–100`, which has no UI-event variant. `piece_068.rs:18` shows `defeat`→kill and `dungeon_completed`→game, so the note's list is consistent.
- The test counts match: `tests/piece_072.rs` has 12 `#[test]`, and `tests/pieces/test_piece_072.py` has 19 `def test_`.
- The commands point at existing files: `tests/piece_043.rs` (`piece_043`), `opening.rs`, `opening_journal.rs`, `opening_world.rs`, and the `scripts/pieces/piece_072.py` and `tests/pieces/test_piece_072.py` files.
- The wiki links `[[Original Opening Microtutorial Recovery]]`, `[[Original Quest Coverage]]` and `[[Opening Historical Coverage Ledger]]` resolve to files in `notes/Research/`.

**Unsure:**
- The bound-chain counts (17 stages, 51 objectives, 27 actors, 4 discoveries, 0 `original_quest_id`) are not checkable in the repo, because `opening.json` lives under the lab root. `notes/Research/Opening Historical Coverage Ledger.md:5` states the same counts, and `piece_068.rs:45–79` shows opening objectives for stages 910001–910016 only, so it does not settle the 17-stage count.
- The Lua callback and `CodeStringMappings.txt` line references (40598–40819, 1438–1453) and the SHA256 values point at lab files that are not in the repo, so I could not check them.
- `notes/Research/Pieces/072…` says the event string "occurs exactly once in the whole file". That holds for `ScriptsBase.lua`, but `ScriptsBase.asm` also carries `onStoryBookClose` (k38, lines 75647 and 75756). The note should say "the `.lua` file" if the assembly is in scope.
- The "Native-verified" 17-stage opening is recorded in `notes/Design/Build Ledger.md:79`. The note does not contradict it; I did not assess whether the Build Ledger status is consistent with the note's "unaccepted" framing.
