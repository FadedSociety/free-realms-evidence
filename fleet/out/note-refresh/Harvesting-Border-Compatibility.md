<!-- fleet job=note-refresh id=Harvesting-Border-Compatibility status=done turns=13 usd=0.0130 tokens(read,write,in,out)=[235903, 36032, 28, 12231] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Border Compatibility.md

**Verdict:** badly stale on the geometry half. The note's "current" shape (10x10, playable from index 0) and its "proposed, not applied" 11x11 padding are both out of date. The tip already emits the padded 11x11 shape from the writer and refuses unpadded borders at load. The shared engine's bounds, gravity and `in_board` logic are still as described, but the line numbers have moved.

**Corrections:**

1. `old:` `- Current package shape (10x10): rows 0..8 = `1`, row 9 = `4`.`
   `new:` `- Writer output shape (11x11, border 1): row 0 and column 0 = `0`, playable `1`s at x1..10 / y1..9, drop row 10 = `4` at x1..10 (`padded_engine_shape` at `:910`, `write_content` at `:1044`). The pre-border 10x10 shape is refused by `validate_border` and the load gate.`
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:765-776` (RECONSTRUCTED_BOARD_WIDTH/HEIGHT = 11, PLAYABLE_ROWS = 9, BORDER = 1), `:910-921`, `:992-997`, `:1044-1048`, `:1104`, `:1300-1320`; `repo:prototype/osfr-tools/src/gameplay.rs:1011-1014`.

2. `old:` `Derived bounds (`mining.rs:960-1027`): `left 0, top 0, width 10, height 9`, drop row 9.`
   `new:` `Derived bounds (`validate_spec`, `mining.rs:1130-1280`, returns `Bounds` at `:1274-1279`): for the current writer shape `left 1, top 1, width 10, height 9`, drop row 10. (`mining.rs:951-1040` is only the Mining18 `mining_spec` reconstruction, not the derivation.)`
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1130`, `:1212-1247`, `:1259-1279`, `:951`.

3. `old:` `` `mining.rs:1198-1247` `gravity` compacts and refills only inside the derived bounds, so with ``
   `new:` `` `mining.rs:1502-1552` `gravity` compacts and refills only inside the derived bounds (column loop `:1512-1514`), so with ``
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1502-1514`. Lines 1198-1247 are now the shape-code and bounds validator.

4. `old:` `` `in_board` (`:1443`) ``
   `new:` `` `in_board` (`mining.rs:2151-2156`) ``
   `why:` `repo:prototype/osfr-tools/src/mining.rs:2151`. Line 1443 is now inside `category_tile`.

5. `old:` `## Proposed minimal padded shape (private proposal; not applied)`
   `new:` `## Minimal padded shape (applied: the writer emits it)`
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:765-776` and `:992-997`. The writer's output is the 11x11 padded shape. `notes/Reviews/Harvesting Runtime and Border Review.md` lines 28 and 118-120 record the same for package `c08f264e…`.

6. `old:` `(cols 0..9 / rows 0..8 playable, drop row 9) exposes index 0 as playable, and the real engine`
   `new:` `(cols 0..9 / rows 0..8 playable, drop row 9) was the pre-border v1 shape; it exposed index 0 as playable, and the real engine`
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:1295-1320` and `:765-776`. The current writer no longer produces this shape, and the load gate refuses it. The engine itself still accepts index-0 chains (`mining.rs:1130-1280` has no border check).

7. `old:` `top = 0` and `left = 0` row 0 and column 0 are full participants`
   `new:` `for the pre-border 10x10 shape (top = 0, left = 0) row 0 and column 0 were full participants; the current writer shape has top = 1, left = 1`
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1512-1514` (loop bounds) with `harvesting.rs:765-776`.

**Unsure:**
- The `harvesting.json` hash `280f5cd7…` and the `lab/reports/…` probe logs and fixtures cited in the note are outside the four roots I can read, so I could not verify them. The review note reports the current package as `c08f264e…` (11x11), which would replace the hash in the Sources and Limits sections.
- The AS2 line citations (`ServerGrid.as`, `Grid.as`) live in `lab/decompiled`, which is not in my roots, so I did not check them.
- The probe results (rows 60-63) are true of the shared engine (`mining.rs:1736` still gives `mining chain outside board or repeated tile`), but they were measured on the pre-border spec. I did not re-run them.
