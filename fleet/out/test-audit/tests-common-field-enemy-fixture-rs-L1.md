<!-- fleet job=test-audit id=tests-common-field-enemy-fixture-rs-L1 status=nothing_found turns=5 usd=0.0037 tokens(read,write,in,out)=[31617, 15227, 12, 2957] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/field_enemy_fixture.rs lines 1-128 of 128

Reviewed `prototype/osfr-tools/tests/common/field_enemy_fixture.rs` lines 1-128. No findings in the five categories.

What I checked:
- **Not a test file.** It is a helper with no `#[test]` bodies and no assertions, so categories 1-3 do not apply directly. Its helpers are exercised by the suites that include it.
- **Template layout matches production.** The fixture's template (`[..4] = 35,0,2,0`, `[133..137] = 100`, `[224] = 1`, sha256 derived from the bytes) matches the template validator at `src/encounter.rs:928-933` and the duplicate builder at `src/encounter/shared.rs:551-553`. The sha256 is computed from the same bytes written to disk, which is the intended fixture behaviour, not a self-check.
- **`spawned()` offset is correct.** It reads the u64 at `packet[4..12]`. The production AddNpc writer at `src/encounter.rs:3137` writes `a.guid` to `b[4..12]`, so the helper reads the same field the engine writes.
- **No silent skips.** Missing fixtures in `load()` (`behaviours.json`, `field_enemies.json`) would panic via `unwrap()`, not pass. No `#[ignore]` or early-return skip paths exist in this window. Searches for `#[ignore]` and early returns in the tests tree found none tied to this helper.
- **Load order.** `load()` follows the production order (encounter, behaviours, field enemies), per the `EncounterEngine::load`, `load_behaviours` and `load_field_enemies` signatures in `src/encounter.rs:907`, `:1128` and `src/encounter/field.rs:70`.
- **Temp dir isolation.** Per-process and per-serial directories under `CARGO_TARGET_TMPDIR`, removed on drop.

Minor notes, not reportable under the categories: the template offsets `133`, `224` and the value `100` are repeated magic numbers, and the doc comment's client address `0x00921A10` cannot be verified from this window.
