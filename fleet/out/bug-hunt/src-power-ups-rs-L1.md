<!-- fleet job=bug-hunt id=src-power-ups-rs-L1 status=nothing_found turns=6 usd=0.0053 tokens(read,write,in,out)=[51574, 18071, 14, 4961] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/power_ups.rs lines 1-386 of 386

I read `prototype/osfr-tools/src/power_ups.rs` lines 1-386 in full and traced the callers that matter (`encounter.rs:2126-2147` drop path, `encounter/power_up_use.rs:25-80` slot and use path, `chess.rs` and `encounter.rs:1109` RNG seeding). I found no defect I could tie to a client-reachable input.

Checked and cleared:
- **Loader bounds (`load`/`from_json`, 148-165):** the file read is capped with `take(MAX_JSON_BYTES + 1)` and re-checked on the byte length. Serde types have no recursion, so there is no attacker-depth issue. Collection sizes are capped by `MAX_KINDS`, `MAX_TABLES`, `MAX_POOL`, `MAX_GUARANTEED`.
- **Burn range (246-250):** `(500..=b.duration_ms)` is safe when `duration_ms < 500` because `RangeInclusive::contains` returns false and does not panic.
- **`slot()` (178-185):** the `DEFINITION_BASE + name_id` addition is `checked_add`, and both `try_from` conversions are checked. Overflow yields `None`, not a panic.
- **`pick` / `roll_scaled` (346-374):** the weight total is at most 64 × 1000, so no overflow. `total` is zero-guarded before `%`. The chance scale comes from a validated `[0.05, 1.0]` multiplier. The RNG is OS-seeded in production (`encounter.rs:1109`), and the drop path takes no client-supplied values into the roll.
- **Pool and guaranteed references (`Table::valid`, `Roll::valid`):** every key is checked against `kinds`, so a roll cannot produce an unknown kind id.
- **Use path (`power_up_use.rs:51-69`):** the kind id comes from server state (`held_power_up`), not the packet, and `slot` failure clears the hold.

Not a finding (config-only, no client path): `validate` does not reject two kinds that share a `name_id`. Those kinds would get the same synthetic `definition_id`. Nothing maps a definition id back to a kind (the use path looks up by the server-held kind id), so no client can exploit it. It would only matter after a bad edit to `power_ups.json`.
