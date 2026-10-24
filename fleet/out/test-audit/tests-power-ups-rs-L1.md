<!-- fleet job=test-audit id=tests-power-ups-rs-L1 status=done turns=9 usd=0.0068 tokens(read,write,in,out)=[93914, 19682, 20, 6723] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/power_ups.rs lines 1-171 of 171

Window: `prototype/osfr-tools/tests/power_ups.rs` lines 1-171. Code under test read: `src/power_ups.rs` (`from_json` 157-165, `validate` 203-237, `Kind::valid`, `Roll::valid`, `Table::valid`, `Rng`, `roll_scaled` 346-357) and `data/content/power_ups.json`.

- **[medium] tests/power_ups.rs:89 non_finite_and_unknown_fields_and_oversize_are_rejected - the oversize assertion is satisfied by a document that is invalid JSON, so it does not test the size cap.**
  - Why it cannot catch a regression: `vec![b' '; 1_048_577]` is all whitespace, and `serde_json::from_slice` rejects it with EOF anyway. Deleting the `bytes.len() > MAX_JSON_BYTES` check at `src/power_ups.rs:158` leaves this assertion passing. The same is true of the `"not json"` line.
  - Fix: take the valid shipped document and pad it with trailing whitespace to 1_048_577 bytes, then assert `is_err()`. Also assert that the shipped document padded to exactly 1_048_576 bytes is accepted. Without the cap, the oversize case would parse and fail the assertion.

- **[medium] tests/power_ups.rs:116 guaranteed_drops_always_come_first_and_skip_the_rolls - the name claims ordering and skipped rolls, but the body only uses the shipped boss table.**
  - Why it cannot catch a regression: the shipped `boss` table (`data/content/power_ups.json:73-76`) has one guaranteed kind and no `health_roll` or `other_roll`. Only one item is ever returned, so "guaranteed first" is never exercised, and there is no roll to skip. A `roll_scaled` or `roll` change that appends guaranteed drops after the rolls, or that consumes RNG for guaranteed entries, still passes.
  - Fix: build an inline table with two or more guaranteed kinds plus a roll with `chance` 0.5 (for example via `parse(&json!(...))`). Assert that the result starts with the guaranteed kinds in order, and that a fresh `Rng` seeded the same way advanced by exactly the roll draws, for example by comparing the next `next_u64()` with a reference stream.

- **[low] tests/power_ups.rs:89 non_finite_and_unknown_fields_and_oversize_are_rejected - "non-finite" is not exercised; the NaN case fails at serde type-checking.**
  - Why it cannot catch a regression: `chance = "NaN"` is a string in a `f64` field, so deserialization rejects it before `in_range`'s `is_finite()` (`src/power_ups.rs:377`) runs. Removing `is_finite()` leaves the test green. Non-finite values cannot come from JSON, so the guard is only reachable through direct construction of `Roll` or `Kind`.
  - Fix: either rename the test to drop "non_finite", or construct the struct directly (if its fields are reachable) and assert that `validate` rejects `f64::NAN` and `f64::INFINITY` for `chance`, `radius` and `scale`.

Checked and not reported: the bound cases in `every_bound_rejects_a_bad_file` match the constants in `validate` and `Kind::valid`, and each one resolves to a real pointer. The pinned splitmix64 value is the standard first output for seed 0. The distribution test's tolerances are sound for n=400k, and the shipped pools are disjoint, so the shared `counts` map is valid. `zero_chance_never_drops` is a valid test, though weak at `next_f64() < 0.0`.
