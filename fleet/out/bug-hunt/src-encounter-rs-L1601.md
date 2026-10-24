<!-- fleet job=bug-hunt id=src-encounter-rs-L1601 status=nothing_found turns=23 usd=0.0389 tokens(read,write,in,out)=[989160, 81096, 48, 37726] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter.rs lines 1601-2400 of 3158

No reportable defects in `prototype/osfr-tools/src/encounter.rs` lines 1601-2400. I read the whole window and checked the candidates below against their callers and guards.

Candidates examined and dropped:

- **Panics on `unwrap`:** `encounter.rs:1662`, `1755`, `1793`, `1937`, `1989`, `2275`, `2276` and `2399` all look like they could panic, but each is guarded.
  - `dungeon()` (`encounter.rs:1347`) is `Some` only when `state.active` is `Some`, and `begin()` (`:1372`) and load (`:1022-1032`) keep `encounter_id` in `content.dungeons`.
  - `with_shared_fields` puts the shared field path in `enemy()` (`:1780`); that path is reached only through `gameplay.rs:527`, which returns early when `engine.active()`. So the `states.iter_mut().find(...).unwrap()` at `:1937` always finds the guid.
  - Load-time `validate_enemies` (`:1046`, `:1016`, `:2767`) keeps the state and actor vectors parallel, so `:2399` holds.
- **Length checks:** `inner[..]` indexing in the `handle` match arms (`:1620-1622`, `:1637`, `:1647-1648`, `:1686-1701`) comes after `len()` checks, and `||` short-circuits the `inner[12]` read.
- **Client-controlled targets:** `attack()` (`:1822`) validates position and slot; `enemy()` filters dead, dormant and returning enemies; retry requires `Lost` (`:2614`).
- **Unbounded growth:** pickups are capped by `max_alive_per_instance`, which is validated to 1..=32 (`power_ups.rs:213`); `fight_log` is capped (`:1212`); field `kills.hits` is bounded by enemies and cleared on kill.
- **Arithmetic:** `prizes` indexing is guarded by `is_empty`; `heal_with_number` (`:2092`) subtraction can underflow only if `player_health > max_health`, which the save path and `set_level` (`:1192-1199`) prevent, so it is not client-reachable.
- **Atomicity:** `strike_damage` (`:1846-2085`) has no `?` that can fail after mutation. `tick_job_effects` (`skills.rs:432`) `?` is unreachable in practice because `strike_damage` always returns `Ok`.
- **Self-target selection (`:1706-1743`):** it could pick a `Returning` field enemy in the non-shared branch. It is unreachable: `handle` is called only from `gameplay.rs:546` inside `with_shared_fields`, where `enemy()` excludes `Returning`.
- **Prize wheel on a repeat cave win (`:2002-2041`):** the wheel can show an ungranted prize, but prizes exist only on field battles (`field_battles.json`), which are repeatable, so the case does not arise.

I found no high or medium defect that a remote client can trigger in this window.
