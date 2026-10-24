<!-- fleet job=note-refresh id=Pieces-053-Aggro-and-leash status=done turns=13 usd=0.0133 tokens(read,write,in,out)=[306958, 41293, 28, 10034] model=claude-haiku-5-5 -->
# notes/Research/Pieces/053 Aggro and leash.md

**Verdict:** minor drift. The module, tests, checker and constants match the tip. One claim about the registered encounter code is false because it covers only part of that code.

**Corrections:**

1. `old:` Item 4 is new relative to production: `encounter.rs` currently freezes a pursuer outside 40 units
   `new:` Item 4 is new relative to the active-battle loop in `encounter.rs`, which freezes a pursuer outside 40 units
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:2398-2436` is the `self.active()` path. Outside 40 units it removes the actor from `moving` and `continue`s, so it freezes. `encounter.rs:2488-2489` runs `tick_field` when `!self.active()`, and that path is separate.

2. `old:` and never walks it home.
   `new:` and never walks it home. The world field path does: `encounter/field.rs` `tick_field` sets `FieldMotion::Returning` when the actor leaves its leash or loses aggro, then walks it to `home` at `run_speed` (`repo:prototype/osfr-tools/src/encounter/field.rs:884-891`, `918-951`). Only the battle loop lacks a return.
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:22` (`mod field;`), `repo:prototype/osfr-tools/src/encounter.rs:2488-2497` (`tick_field` call), `repo:prototype/osfr-tools/src/encounter/field.rs:815-816` ("Field actors roam, chase within a home leash, then evade home and heal").

**Checked and holding:**
- `src/restoration/piece_053.rs` and `tests/piece_053.rs` exist. `scripts/pieces/piece_053.py` and `tests/pieces/test_piece_053.py` exist and contain `LeashReturnEvidenceChanged`.
- Constants match the note: `AGGRO_PURSUIT_RANGE` 40.0, `AGGRO_MELEE_REACH` 2.5, `AGGRO_MOVE_SPEED` 3.0, `AGGRO_STEP_CLAMP_MS` 250, `AGGRO_TICK_INTERVAL_MS` 100, `AGGRO_STOP_MARGIN` 2.4 (`repo:prototype/osfr-tools/src/restoration/piece_053.rs:34-44`). The Disposition values are 0/1/2 (lines 27-31). Typed rejections and `Disengaged` events are at lines 59-77 and 103-106. The return-to-anchor uses the same speed (line 257).
- Module not registered: no `piece_053` mod in `src/lib.rs`. The tests include it via `#[path]`, which matches the integration gate.
- Test counts: 12 `#[test]` functions in `tests/piece_053.rs`; 11 `def test_` in the Python test file.
- Native selector `00a2ac20` references offsets `0x178`, `0x6f8`, `DAT_01762a30` and `FUN_00fd8e20` (client fn table).
- Community `Speed = 6.25f` appears in `refs` Sanctuary `Entities/Npc.cs:96`, and `MovementType => 2` at line 78.

**Unsure:**
- The capture figures (44 attacks, 2.0086/2.4000 distances, SHA256) and `lab/runs/...` / `lab/reports/native-combat-controls.json` are not in the searchable tree, so I could not verify them.
- "Sanctuary implements no server-side aggro at all" and the wiki taunt wording are community/corpus claims I did not check.
- Per the field path, return-to-home uses `run_speed` (3.5), not 3.0. The note does not claim production uses 3.0 for returns, so I made no correction.
