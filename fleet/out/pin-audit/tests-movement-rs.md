<!-- fleet job=pin-audit id=tests-movement-rs status=nothing_found turns=4 usd=0.0021 tokens(read,write,in,out)=[14575, 10402, 10, 1257] model=claude-haiku-5-5 -->
# tests/movement.rs

No findings in `prototype/osfr-tools/tests/movement.rs` for the screened lines 994 and 995.

- **994 `multiplier(Some(64.0)) == 1.5`:** the 1.5 is the upper clamp bound written in code, `(speed / BASE).clamp(1.0, 1.5)` in `src/movement.rs:94`. The source comment says the 1.5 maximum is wiki-derived, not from a data file. No data file holds a mount multiplier (a repo-wide search for `mount_multiplier` finds only code and tests).
- **995 `SpeedModifiers::riding(None).base_speed_per_second == 10.0`:** the 10 is `const BASE: f32 = 10.0;` in `src/movement.rs:91`, a code constant, not a value read from `data/content`. No data file carries a base speed for this.

Neither value comes from a shipped data file, so retuning data would not break these assertions. They pin code constants, which is outside this audit's rule. Tests that pin code constants are a separate concern and are not reported here.
