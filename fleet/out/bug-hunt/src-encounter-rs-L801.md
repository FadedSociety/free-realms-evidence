<!-- fleet job=bug-hunt id=src-encounter-rs-L801 status=done turns=32 usd=0.0375 tokens(read,write,in,out)=[1441497, 73468, 66, 27756] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter.rs lines 801-1600 of 3158

Window `encounter.rs` 801-1600 read in full. One finding; everything else I checked is either guarded upstream or unreachable from a client (details below).

- **[medium] prototype/osfr-tools/src/encounter.rs:825 - `bind_run_instance` accepts instance `0` and writes it into a live encounter, but `load()` rejects any saved active encounter with `instance_id <= 0` (encounter.rs:1041).** The guard at 825 is `instance < 0`, while the write at 837-838 (`active.instance_id = instance`) happens unconditionally when an encounter is active.
  - **Failure scenario:** the session has an active arena encounter (`state.active = Some`) and its membership location is gone (the world drops it on disconnect, world.rs:1348). The gateway then calls `bind_run_instance(0, ...)`. The encounter's `instance_id` becomes 0 and the state is saved. On the next login, `load()` reaches encounter.rs:1040-1045 and returns `invalid("invalid encounter return/instance")`, so the character cannot load.
  - **Reach:** osfr-gateway.rs:1745-1755 computes `old_instance` from `membership.player_location`, which is `None` after a disconnect. At 1748 `change` is `None` when `staged_gateway.is_logged_in()` is false (gateway.rs:1383 clears `logged_in` on `reset_session`). At 1780-1786 `.unwrap_or(0)` yields instance 0. At 1790-1791 `bind_run_instance(0, outcome.began_zoning)` is called, and `state_changed |= bound` at 1792 makes the change persist. No upstream check stops the 0. The precondition "a not-logged-in staged gateway that still holds an active encounter reaches commit_outcome" is what I did not fully trace; I did confirm the rest of the chain.
  - **Fix:** in `bind_run_instance`, change the guard at 825 to `if instance <= 0 { return Err(invalid("non-positive encounter instance")); }`, matching the load-time invariant. Optionally also skip the rebind when no world instance is known.

Checked and dropped (no defect shown):
- `bind_run_instance` 839-843: `checked_add` runs after `active.instance_id` is written, so its error path leaves a partial mutation. It only fires at `i32::MAX`, which the world allocator never reaches from a client, so it is not reportable.
- `begin` 1356-1410: `admit_battle` and all validation run before any mutation; `checked_add` is also before the write. `dungeon().unwrap()` is safe because `begin` sets `encounter_id` from a found dungeon.
- `on_zone_ready` 1480-1488 `unwrap`s are guarded by `active()`, and the dungeon is guaranteed by load validation.
- `set_player_job` 1181-1201: the job level is clamped, the health update matches its doc, and `level` is server-derived (`gameplay.rs:5143-5162`).
- `set_world_stage` 1447 takes a server-computed stage (`gameplay.rs:4860-4874`).
- `receive_field_damage` 870-896 is fed by server-side field simulation, and `saturating_sub` covers the arithmetic. Field participants in an active arena are excluded at the gateway, so the missing Lost-phase transition there is unreachable.
- `handle` 1563-1590: `inner[..2]` and `inner[2..4]` are length-checked; `valid_position` runs first.
- `heal_player_percent`, `refuse_weapon`, `log_fight`, `world_initialization`, `debug_win`: no panic or overflow. `debug_win` is gated behind developer command denial.
- `load` 907-1102 and the phase checks: the template offsets are bounded by the length check at 926, and the Won/Lost/Fighting invariants match what `strike` and the knockout path produce (encounter.rs:2023, 2522).
