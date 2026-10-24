<!-- fleet job=bug-hunt id=src-encounter-field-rewards-rs-L1 status=nothing_found turns=13 usd=0.0160 tokens(read,write,in,out)=[285561, 42030, 28, 15690] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter/field_rewards.rs lines 1-540 of 540

No defect I can tie to lines 1-540 of `prototype/osfr-tools/src/encounter/field_rewards.rs` survives tracing to its callers.

Checked, and why each is not a defect:

- **Content load (`load`/`read_bounded`/`parse`, lines 112-183):** the size is bounded by the metadata check, a bounded read and a `parse` length check. Vec sizes are capped by the 1 MiB file, and serde_json's depth limit covers recursion. Band and override sorting plus the adjacent-pair overlap and duplicate checks are sound: after sorting by `min_level`, any overlap implies an adjacent overlap. `binary_search` runs on a sorted, unique key set. Every error returns before `Self` is built, so there is no partial state. The content is server-side, not client input.
- **`reward_for` (187-202):** the level is range-checked before use, and `band.min_level >= 1` and `min <= max` are validated at load.
- **`validate_source` (206-217):** the `&&`/`||` precedence is as intended.
- **`credit_field_kill` (227-281):** `who` is built from `hits` (inserted only by the authenticated `shared_sender`, with `dealt > 0`), `engaged` (the server's `f.target`, chosen from valid players in `field.rs:868-881`) and the killer. The killer is excluded from credits, so the killer is paid once. Double-kill payout is blocked by the `s.health == 0` early return at `encounter.rs:1872`. The credit map is bounded: `MAX_CREDITS` evicts the oldest entry, and `retain_casters` (`shared.rs:165-184`) prunes by TTL and departure. `saturating_add`/`saturating_sub` are used on `now_ms`.
- **`claim_kill_credits` (288-321):** the credit is removed with `remove`, so a second claim pays nothing. Expiry is checked against `now_ms`. The defeat event is pushed only for unexpired credits with `definition > 0`.
- **`retain_after_leave` (63-68):** the returned bool matches the `retain_casters` use.

Weak item I did not report: the `reward_for` doc (lines 185-186) says a level no band covers "pays nothing", but a definition override pays at any level 1..=20 regardless of band coverage. The override-first precedence is stated in the same doc, the shipped bands cover 1-20 contiguously (`data/content/field_kill_rewards.json`), and a client cannot reach this path, so I did not count it as a defect.
