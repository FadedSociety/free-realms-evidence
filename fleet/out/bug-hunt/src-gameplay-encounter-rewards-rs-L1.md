<!-- fleet job=bug-hunt id=src-gameplay-encounter-rewards-rs-L1 status=nothing_found turns=10 usd=0.0069 tokens(read,write,in,out)=[98645, 20511, 22, 6693] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/encounter_rewards.rs lines 1-44 of 44

No reportable defect in `prototype/osfr-tools/src/gameplay/encounter_rewards.rs` lines 1-44.

What I checked:

- **Coin overflow (line 24):** `can_grant_coins` (inventory.rs:852-857) uses `checked_add` and caps the total at `i32::MAX`, which matches the wire `i32` field. `grant_coins` (inventory.rs:859-866) re-checks the same predicate before `+=`, so no panic and no wrap.
- **XP overflow (lines 25-29):** `can_add_experience` (profiles.rs:309-317) uses `checked_add` against the active job's current total. `award_job_xp` (gameplay.rs:5168-5194) reads the same active profile, so `add_experience` (profiles.rs:319-329) cannot fail after the gate passes. The `unwrap()`s on `profiles` in `award_job_xp` are only reached when `xp_fit` is true, which requires `profiles` to be `Some` whenever `job_xp > 0`.
- **Refusal atomicity (lines 30-37):** both gates run before any mutation, and a refusal returns `Ok` with one system line and nothing granted. Nothing is half-applied.
- **Ordering (lines 38-41):** `grant_reward` runs first. `grant_bundle` (inventory.rs:1045-1059) stages on a clone and commits only on success, so an item error leaves the inventory untouched. XP is only awarded after the coin/item step succeeds, and it cannot fail after the gate.
- **Trust (encounter.rs:2002-2020, 636-641):** `coins`, `job_xp` and `items` are built from server battle data (`d.reward_coins`, `d.reward_items`, `d.prizes`, `BATTLE_JOB_XP`). The client supplies only the fact that a battle was won, not the amounts.

One observation I did not count as a finding: item-grant errors (unknown definition, or quantity above max stack, from `grant_with_tint` at inventory.rs:972-984) still propagate through `?` at line 38 and `apply_encounter` (gameplay.rs:4892), so the shared tick sees an `Err`. Line 18 of the module doc says item refusals keep the existing `grant_bundle` rule, so this looks deliberate. Its only trigger is bad server content data, not a remote packet, so I could not show a remote-reachable crash or save corruption.
