<!-- fleet job=pin-audit id=tests-piece-053-rs status=nothing_found turns=3 usd=0.0020 tokens(read,write,in,out)=[7331, 8872, 8, 1581] model=claude-haiku-5-5 -->
# tests/piece_053.rs

No findings in `prototype/osfr-tools/tests/piece_053.rs` for the screened lines 59, 60 and 61.

- **Line 59 (`AGGRO_MOVE_SPEED`, 3.0):** the test compares against the constant defined in `src/restoration/piece_053.rs:38`. That constant is hard-coded in the module, not read from data. `data/content/enemies.json` and `behaviours.json` also have `move_speed: 3.0`, but nothing links the two. Retuning those rows would not change the constant, so the test would not break while the code is still right. Not a finding.
- **Line 60 (`AGGRO_STEP_CLAMP_MS`, 250):** defined at `src/restoration/piece_053.rs:40`. No data file has a matching value. Not a finding.
- **Line 61 (`AGGRO_TICK_INTERVAL_MS`, 100):** defined at `src/restoration/piece_053.rs:42`. No data file has a matching value. Not a finding.

Side note, not a test finding: these reconstructed tunables (and the related `AGGRO_PURSUIT_RANGE` 40.0, which matches `aggro_radius` in `enemies.json`) live as code constants in `src`, not in `data/content`. That goes against Bryce's rule that gameplay values stay in data. The fix belongs in the module, not the test.
