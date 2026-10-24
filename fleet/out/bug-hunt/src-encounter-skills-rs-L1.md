<!-- fleet job=bug-hunt id=src-encounter-skills-rs-L1 status=done turns=27 usd=0.0300 tokens(read,write,in,out)=[966330, 55784, 56, 26684] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter/skills.rs lines 1-514 of 514

Reviewed `encounter/skills.rs` 1-514 in full and traced the callers. Most of the window is sound: the `JobAbility`/`JobEffect` validators bound DoT interval (>=500 ms) and duration, so the catch-up loop in `tick_job_effects` terminates; the energy check and the 285/287/288 refusals all run before any mutation; the heal math cannot underflow because `set_player_job` keeps `player_health <= max_health`. I found one candidate that I could trace through most of its links, but one link is unverified, so it is reported as medium, not high.

- **[medium] `prototype/osfr-tools/src/encounter/skills.rs:432-453` - `tick_job_effects` ticks a field-owned DoT while the engine is in an active dungeon encounter, and the DoT's target is not in that encounter's enemy list, so the strike panics at `encounter.rs:1937` (`.unwrap()`).**

  **Failure scenario:**
  1. Player A is in the shared field (no encounter). A casts a DoT ability on a field enemy X. `shared_job_ability` → `job_ability` → `apply_dot` stores `(X, def_id)` in `runtime.dots[A]` (`encounter/shared.rs:420-435`).
  2. A enters a dungeon. `begin()` calls `reset_session()`, which clears only the engine's own `skills` (`encounter.rs:1334-1336`). `runtime.dots[A]` is untouched. It is removed only when X dies or evades (`shared.rs:442-450`).
  3. While A's engine is active (`state.active = Some`), the gateway's field tick calls `tick_shared_effects` → `shared_effects` → `with_shared_fields`, which swaps `runtime.dots[A]` into the engine (`shared.rs:420-423`) and sets `shared_sender = Some(A)`. No active-encounter guard exists on this path (`gameplay.rs:560-572`, `osfr-gateway.rs:3093-3095`).
  4. `tick_job_effects` line 444: `self.enemy(X)` returns the field actor, because with `shared_sender` set, `enemy()` searches `field_sim` regardless of `active` (`encounter.rs:1779-1786`). Health > 0, so the strike proceeds.
  5. `strike_damage` (`encounter.rs:1920-1937`): `field_index` is `None` because `state.active.is_some()`, so it searches `active.enemies` for X and calls `.unwrap()`. X is a field guid, not a dungeon enemy, so this panics.

  **Reach:** a client packet sets up the DoT (`job_ability` target, `gameplay.rs:534`). The panic needs step 3 to run for A, i.e. A is still a ready, loaded participant of the field instance (`osfr-gateway.rs:3025-3030`) while in a dungeon. **I did not confirm this.** I did not find the code that moves a player's membership out of the field instance on dungeon entry. If entering a dungeon removes A from that instance, the path is unreachable and this finding should be dropped. Step 4 (`enemy()` resolving field actors with `shared_sender` set, regardless of `active`) and the DoT-survives-`begin()` behaviour are verified.

  **Fix:** in `tick_job_effects`, skip or drop DoTs when `self.state.active.is_some()` (or when `shared_sender` is set and the engine is active). Also clear `runtime.dots[sender]` on dungeon entry. As defence in depth, replace `.unwrap()` at `encounter.rs:1937` with a `let Some(..) else { return Ok(default) }`.
