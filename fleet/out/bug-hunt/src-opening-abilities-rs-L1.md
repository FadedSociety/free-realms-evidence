<!-- fleet job=bug-hunt id=src-opening-abilities-rs-L1 status=nothing_found turns=6 usd=0.0090 tokens(read,write,in,out)=[54632, 23812, 14, 10891] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/opening_abilities.rs lines 1-453 of 453

No defects found in `prototype/osfr-tools/src/opening_abilities.rs` lines 1-453 that I could tie to a client-reachable path.

What I checked:

- **Indexing (`job_bar`, line 270; `job_slot`, lines 281-285):** `bar[(ability.slot - 1) as usize]` is safe because `load_job_abilities` (lines 245-246) requires `a.slot == i + 1` and `a.valid()` (slot in 1..=7). `job_slot` converts the client `slot` with `usize::try_from(..).ok()?.checked_sub(1)?` and then uses `.get(index)`, so negative or large slots return `None`.
- **Client slot to weapon check (`weapon_matches`, lines 290-304):** for a job slot with no ability, `required` is `None`. `equipped_weapon_matches` (abilities.rs:32) returns false for `None`, so the cast is refused (fails closed). Callers at gameplay.rs:509, 4655 and 4723 use the server's active profile (gameplay.rs:479-482, 4619), not a packet field.
- **Client slot lookup and failure (gameplay.rs:4641-4682):** an empty or locked slot returns `unsupported_cast_failure` with no state change, so `job_slot` returning `None` is handled.
- **Load atomicity (`load`, lines 162-213; `load_job_abilities`, lines 217-260):** every error return happens before `self.jobs` is replaced, and the mutations before the error are local. A failed reload keeps the previous roster.
- **Size bounds:** both file reads are capped (`take(65537)`, `take(MAX_JOB_CONTENT + 1)`) with length checks. The counts are capped (`basics` ≤16, `jobs` ≤32, `slots` ≤7, `effects` ≤4). The fixed 160-byte `definition` and the `[0; 32]` noncombat fill have offsets that stay in bounds.
- **Overflow:** `index as i32 + 1` operates on 0..7 only. The `u32` level comparisons have no subtraction that can underflow (`unlocks_between` only compares).
- **Default-filling (lines 175-193):** `weapon_class` and `weapon_definition_id` are filled from the built-in roster and then validated as non-zero/in range, so a missing value cannot leave a combat job unarmed.

Observations I did not report, because I could not show a defect:

- `activation_with_power_up` (lines 326-401) shows a held power-up only for combat jobs (the `if let Some(basic)` branch). Noncombat jobs get eight empty slots. The use path at gameplay.rs:4644 does not check `supports_basic`, so a noncombat player can trigger the power-up on key 2 without seeing it on the bar. This looks like a UI or design gap rather than a security or corruption defect, and it sits mainly outside this window.
- `load` does not check `definition_id` uniqueness across basics. The campaign file is operator-authored, not client input, so I did not count this.
