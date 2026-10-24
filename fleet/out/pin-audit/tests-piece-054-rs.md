<!-- fleet job=pin-audit id=tests-piece-054-rs status=nothing_found turns=3 usd=0.0024 tokens(read,write,in,out)=[10026, 11993, 8, 1555] model=claude-haiku-5-5 -->
# tests/piece_054.rs

No findings in `tests/piece_054.rs` for the screened lines (101, 153, 227-230). None of these expected values comes from a shipped data file under `data/content/`.

- **101 `MELEE_REPEAT_GATE_MS == 600`**: the value is a code constant, `src/restoration/piece_054.rs:46`. A search of `data/content` finds no repeat-gate field. The `600` in `src/encounter.rs` is also code, which the test checks via `contains`. Not a data-tunable value, so not a finding.
- **153 `player_attack(2.0, 180, 10_600, Some(10_000))`**: the `600` is a literal that matches the code constant above, and the test's own 599 case already uses `MELEE_REPEAT_GATE_MS` for the minimum. Not a data finding. Optional cleanup: write `10_000 + MELEE_REPEAT_GATE_MS`.
- **227-230 `ANY_TO_COMBAT_TIMING` / `COMBAT_TO_STAND_TIMING` ease values (0.2, 0.2, 0.6, 0.2)**: these are `const` rows in `src/restoration/piece_054.rs:209-224`. Their documented source is the client's `AnimationTransitionRules.xml` (header lines 17-19), not a tunable data file. Not a data finding. They are client-recovered constants, so the tests may keep pinning them.

Possible follow-up (not a finding under the rule): the 600 ms gate and the reach values are reconstructed rather than reviewed, and the 600 gate is duplicated in the production encounter code, so a retune would need both places changed.
