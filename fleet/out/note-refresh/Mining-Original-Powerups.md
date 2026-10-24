<!-- fleet job=note-refresh id=Mining-Original-Powerups status=done turns=15 usd=0.0185 tokens(read,write,in,out)=[496701, 61086, 32, 11704] model=claude-haiku-5-5 -->
# notes/Research/Mining Original Powerups.md

**Verdict:** badly stale. The note was written when `mining.rs` had no powerup code. The tip now implements the four clickable powerups (`950..=953`) behind authored content. The three collected powerups (`900..=902`) are still unimplemented, and the note's "none of the seven" and the comparison table are wrong.

**Corrections:**

1. `old:` The current engine implements **none** of the seven.
   `new:` The current engine implements the four clickable powerups (`950..=953`) when content authors them. The three collected powerups (`900..=902`) are refused at load and have no effect.
   `why:` repo:prototype/osfr-tools/src/mining.rs:1076-1096 (`validate_powerup_definitions` refuses 900..=949); repo:prototype/osfr-tools/src/mining.rs:776-800 (`OnActionMsg` for 950..=953).

2. `old:` It carries a `powerup_percent` field that `mining_spec()` sets to `0`, never spawns a `900..=953` tile, never emits `OnPowerupInitMsg`, never registers a powerup icon with `OnTileInfoMsg`, has no `OnActionMsg` handler and has no `OnLevelEventMsg 40` handler.
   `new:` It carries a `powerup_percent` field that `mining_spec()` sets to `0` (shipped content spawns none). Authored `powerup_definitions` enable a weighted spawn roll for `950..=953`, emit `OnPowerupInitMsg` at level start, and handle `OnActionMsg`. No powerup `OnTileInfoMsg` is emitted, and there is still no `OnLevelEventMsg 40` handler.
   `why:` repo:prototype/osfr-tools/src/mining.rs:1039 (`powerup_percent: 0`); :254 (`powerup_definitions`); :1474-1488 (`random_tile` spawn branch); :1380-1395 (`OnPowerupInitMsg`); :776-800 (`OnActionMsg`). No `"40"` arm in the inbound `OnLevelEventMsg` match (:830-853).

3. `old:` The `900..=953` arm in `valid_value` only means such a value would load without complaint; nothing can produce or act on one.
   `new:` Authored powerup values must be `950..=953`. `900..=949` is refused at load, and only `950..=953` can be produced or acted on.
   `why:` repo:prototype/osfr-tools/src/mining.rs:1092-1098 (range checks in `validate_powerup_definitions`); :1801-1807 (`apply_powerup_action` dispatch).

4. `old:` | Seven powerup definitions with duration/power | absent — `Type8BoardSpec` has only a scalar `powerup_percent` |
   `new:` | Clickable powerup definitions with spawn_chance/duration/power | present for `950..=953` only, as private `powerup_definitions` (`Type8PowerupDefinition`); `Type8BoardSpec` still has only a scalar `powerup_percent`; the collected `900..=902` are refused |
   `why:` repo:prototype/osfr-tools/src/mining.rs:160, 254, 261-275, 1092-1096.

5. `old:` | `powerup_percent` spawn roll | parsed and validated, but `mining_spec()` ships `0` and `random_tile()` never consults it |
   `new:` | `powerup_percent` spawn roll | `random_tile()` consults it and draws a weighted authored powerup; `mining_spec()` still ships `0`, so shipped boards spawn none |
   `why:` repo:prototype/osfr-tools/src/mining.rs:1474-1488 and 1039.

6. `old:` | `OnPowerupInitMsg` at level start | never emitted |
   `new:` | `OnPowerupInitMsg` at level start | one `OnPowerupInitMsg value, duration, power` per authored definition, ascending by value |
   `why:` repo:prototype/osfr-tools/src/mining.rs:1380-1395 (`initialize_board`, called from the `OnStartLevelMsg` arm at :653).

7. `old:` | `OnActionMsg` handler | absent — the match falls through to `unsupported or malformed mining message` |
   `new:` | `OnActionMsg` handler | present for `950..=953` only: `apply_powerup_action` validates the pressed tile, power and coordinates, then runs the effect; other indices are refused |
   `why:` repo:prototype/osfr-tools/src/mining.rs:776-800 and 1773-1813; the fallthrough is `_ =>` at :913.

8. `old:` | `900..=902` fall-through collection | absent — `collect_fall` requires the bottom-row value to match a goal, so a powerup fall would error rather than fire its effect |
   `new:` | `900..=902` fall-through collection | absent — `collect_fall` returns `Ok` early for `900..=949` without removing the tile or applying any effect (no error, no timer, no score) |
   `why:` repo:prototype/osfr-tools/src/mining.rs:1568-1575.

9. `old:` | Chain collection of a powerup | impossible — `validate_chain` requires `400..=499` or `200` |
   `new:` | Chain collection of a powerup | still impossible (no change): `validate_chain` requires `400..=499` or `200` |
   `why:` repo:prototype/osfr-tools/src/mining.rs:1748-1754. (Listed only to show this row is still true; no edit needed.)

10. `old:` | `HasMove()` counts a pressable powerup | absent — `has_move` considers only `400..=499` and `200` |
    `new:` | `HasMove()` counts a pressable powerup | present — `has_move` returns true for any `950..=953` cell, and the reshuffle branch runs only once none remain |
    `why:` repo:prototype/osfr-tools/src/mining.rs:2092-2098 (`has_move`); :1809-1811 (reshuffle after an action when no move remains).

**Unsure:**
- The "Current file SHA-256 `da3b5b…`" line (note line ~198) can't be recomputed here. `mining.rs` is now 2434 lines with the powerup code above, so the recorded hash is stale for the tip. Please recompute it before trusting it.
- I did not read `valid_value`, so I could not confirm whether it still accepts `900..=953`. Correction 3 depends only on the `validate_powerup_definitions` range checks.
- Implementation-plan items 1, 2, 3, 5 and 6 under "Minimal faithful capabilities" (content schema, spawn, level-start advertisement, action handler, `has_move` fix) now exist in code and tests (`tests/mining_powerups.rs` covers defaults, authored spawn, malformed definitions, and dynamite). Their "build it" wording is out of date, but I did not rewrite the plan. The "Testable contract" items 1-4, 7-9 have partial coverage in that file; I did not audit each assertion.
- The client-side citations (`GameLevel.as`, `Grid.as`, etc.) and the original-game claims were not checked, since they are outside the code at the tip.
