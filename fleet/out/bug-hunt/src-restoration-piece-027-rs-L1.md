<!-- fleet job=bug-hunt id=src-restoration-piece-027-rs-L1 status=nothing_found turns=4 usd=0.0039 tokens(read,write,in,out)=[21306, 14729, 10, 3622] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_027.rs lines 1-226 of 226

No reachable defect in `prototype/osfr-tools/src/restoration/piece_027.rs` lines 1-226.

What I checked:
- **Reach:** `piece_027` is not compiled into the server. No `mod`/`#[path]` include references it under `src/` (`lib.rs`, `housing_service.rs`, and the other restoration includes are the only consumers, and none names 027). Its public items (`GridSnap::snap_position`, `BuildBounds::validate/contains`, `HousingFixtureLimits::denial`, `RotationDirection::signed_step`) have no callers anywhere in `prototype/osfr-tools`. The notes (`notes/Reviews/Delegated Housing Readiness.md:30`) confirm the module is awaiting lead registration. No client packet can reach this code today.
- **Panics (line 103-111, 180):** `spacing_cm` is private and only set via `new` (rejects 0), `on()` (25) or `off()` (5), so `step` is never zero or NaN from a valid instance. `f32` `trunc`/division/comparison do not panic on NaN or inf. No indexing depends on client values (`axis` is 0..3 over fixed arrays).
- **Validation (163-175):** `validate` rejects non-finite values and inverted min/max. `contains` returns false for NaN or inverted boxes, so no false containment.
- **Limits (192-209):** `allows_*` uses `<` against the max, which is the correct comparison for "one more fits". The fixture check runs first, as the doc says.
- **Rotation (141-151):** the sign and step match the doc comment (clockwise negative, 15 degrees).
- **Snap arithmetic (108-111):** `trunc()` gives the documented toward-zero behaviour. Dividing by `step` instead of multiplying by `1/step` is a float-rounding difference only, not a logic defect.

No finding meets the bar, so nothing is reported.
