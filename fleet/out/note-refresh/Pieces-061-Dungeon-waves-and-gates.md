<!-- fleet job=note-refresh id=Pieces-061-Dungeon-waves-and-gates status=done turns=11 usd=0.0145 tokens(read,write,in,out)=[300501, 50931, 24, 10251] model=claude-haiku-5-5 -->
# notes/Research/Pieces/061 Dungeon waves and gates.md

**Verdict:** current, with one minor drift (a broken cross-link path). The code, tests, checker and status claims all match the tip.

**Corrections:**

- `old:` `[[../Design/MMO Worker Contract]]`
  `new:` `[[../../Design/MMO Worker Contract]]`
  `why:` `repo:notes/Design/MMO Worker Contract.md` is the file's location. From `notes/Research/Pieces/`, `../Design` resolves to `notes/Research/Design/`, which does not exist (`notes/Research/` has no `Design/` folder). Obsidian may still resolve the link by basename, so this is low severity.

**Checked and holding (no change needed):**

- `src/restoration/piece_061.rs` exists. It holds the four room boxes, `DOOR_01`/`DOOR_02` with object ids 1358893701/1362704680, the clip lists, the verb sounds, `DungeonChain`, `record_clear`, `request_gate` and `report_position`. Per-room wave counts are caller-supplied (`WaveSpec::new`); there is no shipped count constant. (`repo:prototype/osfr-tools/src/restoration/piece_061.rs:62-332`)
- Policy behaviour matches the note:
  - `record_clear` rejects instance 0, out-of-order rooms and duplicate instances. It opens the gate only on the room-completing clear (`piece_061.rs:393-426`).
  - `request_gate` refuses while the room behind the gate is uncleared, and is idempotent otherwise (`:433-439`).
  - `report_position` names the earliest closed gate on the path (`:447-466`).
  - `WaveSpec` coverage is validated in `DungeonChain::new` (`:336-362`).
- `tests/piece_061.rs` exists and includes the module through `#[path = "../src/restoration/piece_061.rs"]` (`:32-34`). It has 10 `#[test]` functions, which matches "10 passed".
- Nothing registers `piece_061` yet. `src/lib.rs` has no restoration module, and no `src/restoration/mod.rs` exists, so "lead registers it" is still the open step.
- `scripts/pieces/piece_061.py` exists, with the six finding ids the note lists (`:374-432`), `catalog_checked`/`catalog_missing` output (`:524-525`), and the `--stamp`/`--reports-dir` flags (`:534-535`).
- `tests/pieces/test_piece_061.py` has 18 `def test_` methods, matching "Ran 18 tests". The manifest CRCs and sizes for the two verb sounds (3970310398/40416, 4238711397/36240) appear in the test fixtures (`:61-62`, `:178-179`).
- The pinned door-tile SHA-256 `5f26ced5...` and area-table SHA-256 `aae003c3...` appear in the checker (`scripts/pieces/piece_061.py:56,59`).
- The derived distances hold: 316 − 314.99448 ≈ 1.006, and 351 − 345.52478 ≈ 5.475.
- The `[[../../MMO Work Queue]]` and `[[../Starting Dungeon Audit]]` links resolve to existing files.

**Unsure:**

- The original-asset facts (the 20 `AreaDefinition` records, the 20-row manifest with 18 CRC matches, the door tile's runtime objects, and the source sizes/hashes beyond the two pinned in the checker) come from `lab/extracted/` and `lab/working/`. Those paths are not reachable from the repo tool root (`lab/reports` returns "not a directory"), so I could not re-verify them. The checker's own pins are consistent with the note.
- The `lab/reports/piece-061-20261009T051230Z/` raw evidence files could not be opened, so the run output quoted in the Verification section is unconfirmed.
- No `notes/Autopilot/` report mentions piece 061 at the tip, so no later work has changed this piece.</result>
