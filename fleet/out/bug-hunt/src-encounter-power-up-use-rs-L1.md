<!-- fleet job=bug-hunt id=src-encounter-power-up-use-rs-L1 status=nothing_found turns=10 usd=0.0102 tokens(read,write,in,out)=[151645, 28249, 22, 10343] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter/power_up_use.rs lines 1-150 of 150

No reportable defect in `prototype/osfr-tools/src/encounter/power_up_use.rs` lines 1-150.

What I checked, and why each candidate was dropped:

- **Held kind is server-owned.** `held_power_up` is only set from a drop (`encounter.rs:2231`). The client cannot choose the kind, and `use_power_up` looks it up in the server's `power_ups` tables. Unknown kinds take the stale-hold branch (lines 57-69), which clears the hold.
- **Position and refusal order.** `valid_position` (line 54) runs before anything is consumed. The dead-player and not-Fighting refusals (lines 70-81) return before the hold is cleared, so a refused request keeps the kind. This matches the doc comment at lines 43-44.
- **Atomicity of the strike loop.** Line 105 uses `?` on `strike_damage`, which could look like a partial-mutation risk. I read `strike_damage` (`encounter.rs:1846-2085`). Every path returns `Ok`, and the function ends with `Ok(out)` at line 2084, so the `?` never propagates an error. The kind is consumed at line 83 before any effect, so there is no double-spend.
- **Arithmetic and casts.** `battle_tier()` clamps to 1..5, so `- 1` at line 88 cannot underflow. Float-to-`u32` casts saturate in Rust and do not panic. `saturating_add` is used for the timers (lines 133, and in `apply_dot`/`apply_stun`). `area_targets` uses `partial_cmp(...).unwrap_or(Equal)`, so NaN cannot panic it.
- **Tier indexing.** `damage_by_tier.get(tier)` (line 99) is a checked `get`, so a short table skips damage rather than panicking.
- **Super Shield invulnerability.** `taken: 0.0` (line 135) is folded with `min` in `mitigation()` (`skills.rs:73-78`) and works as the doc comment says. The `speed_pct` display-only note matches the module doc.
- **Burn and stun targets.** `apply_dot` and `apply_stun` re-check `health > 0` and `!shielded`, so a target killed by the strike earlier in the same call does not gain a DoT or stun.

Out of window, not pursued: `encounter.rs:1937` has an `unwrap()` on `states.iter_mut().find(...)`. I did not establish that a power-up request can reach a guid missing from that list, so I am not reporting it.
