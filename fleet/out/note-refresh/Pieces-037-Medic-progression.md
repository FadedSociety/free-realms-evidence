<!-- fleet job=note-refresh id=Pieces-037-Medic-progression status=done turns=17 usd=0.0187 tokens(read,write,in,out)=[554382, 56686, 36, 12130] model=claude-haiku-5-5 -->
# notes/Research/Pieces/037 Medic progression.md

**Verdict:** minor drift. Nearly everything checks out at the tip: the four owned paths exist, the module and test file match the stated constants, the First Aid ladder and rank texts match the locale, the revive and knock-out Lua matches, the test counts match (15 Rust, 19 Python), and the Sanctuary community figures match. One present-tense claim about `piece_038.rs` is now false, and one Lua detail is slightly imprecise.

**Corrections:**

1. `old:` (`tests/piece_038.rs` includes a `src/restoration/piece_038.rs` that does not exist yet, and
   `new:` (`tests/piece_038.rs` includes a `src/restoration/piece_038.rs` that did not exist at this run; it exists at the tip (513 lines), and
   `why:` repo:prototype/osfr-tools/src/restoration/piece_038.rs:1 (file present, 513 lines); repo:prototype/osfr-tools/tests/piece_038.rs:27 (its `#[path]` include now resolves).

2. `old:` (logged with `Ui.SetWallOfData("RespawnWindow", "OnNonPaidRevive")`)
   `new:` (logged with `Ui.SetWallOfData("RespawnWindow", "OnNonPaidRevive")`, and only when `isOverworld == 1`)
   `why:` repo:ui ScriptsBase.lua:6457-6460 (the `SetWallOfData` call sits inside `if self.isOverworld == 1`). The same applies to the `OnPaidRevive` branch at lines 6463-6465.

**Unsure:**

- The RED stub run is recorded as "4 passed; 10 failed" (14 results), but `tests/piece_037.rs` contains 15 `#[test]` functions (lines 55-312). The RED line may be miscounted. This is a historical log, so I did not propose a correction.
- The lab-only evidence (`lab/reports/locale-id-to-text.json`, the decompiled `revive_window.gfx`, `wndRespawn.xml`, `ActorCompositeEffectDefinitions.xml`, and the `LibSOE` opcode enums) is outside the repo and could not be checked. The locale strings I could check (3813, 47279-47282, 3784, 3800, 285, 280, 37466, 22112, 408279, 408280, 410188, 4035, 420497, 422736, 422746, 384185, 20463, 73914, 3815) all match the note. `WieldTypeAnimationMappings.txt` line `14^Medic^1099^0` is confirmed in the client resources.
- The "Lead integration" gate is still open: `src/restoration/` has no `mod.rs` registering `piece_037`, and the tests still use `#[path]`, so the gate stands.
- `cargo clippy` availability and the workspace-wide `cargo test` failure list (piece_030 serde error) are historical and could not be re-run.
