<!-- fleet job=bug-hunt id=src-opening-rs-L1 status=nothing_found turns=12 usd=0.0212 tokens(read,write,in,out)=[400503, 52515, 26, 21330] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/opening.rs lines 1-800 of 879

No reportable defects in `prototype/osfr-tools/src/opening.rs` lines 1-800 (I also read 800-879 for context). Every panic-prone spot in the window is guarded upstream, and the client-facing inputs are bounded or server-derived.

Checked and dropped:
- **Panics (`unwrap`, `BTreeMap` indexing, `counts[i]`):** `state.stages[&id]` (lines 277, 424, 454, 500, 556), `get_mut(...).unwrap()` (760) and `counts[i]` (841) are safe. `load` (lines 275-300) requires `counts.len() == objectives.len()` and the same stage-id set, and `validate_content` (317-406) guarantees every content stage has an entry.
- **Float handling:** `valid_position` (16-20) rejects NaN, infinity and values beyond 1e6, so `within` (22-24) cannot overflow. `on_position` (599) and `set_location_without_events` (611) validate before storing.
- **Counter overflow:** the objective increment (841-843) uses `saturating_add` and then `min(required)`.
- **Resource bounds:** the file read is capped (235-244). Collection sizes are capped in `validate_content` (320-363). Event quantities are range-checked (682, 688).
- **Atomicity:** `on_event` validates before it mutates, and the rewards are returned to the caller rather than applied inside the engine.
- **Client authority:** `Visit` positions come from `character.position` after movement validation (gameplay.rs:1817 says `gateway.rs` clamps the pose first). `ClassSelected` uses `profiles.active()` (gameplay.rs:4791-4797). `Defeat` comes from `encounter.defeated`. Craft quantity is derived from server-side grants (crafting.rs:370-379). Gather and Craft authorization requires a near actor with a matching trigger (703-720), and gather goes through the menu-choice gate (gameplay.rs:4513-4518).
- **Logic:** the `ordered` gate (779), the completion guard `!newly_accepted` (856), and the `earlier_complete` chain (292-293) all behave as their comments describe.

Two observations I did not turn into findings:
- Menu-driven Gather and Craft objectives advance by 1 per menu choice with no cooldown or material check. The code comment at gameplay.rs:4513-4514 and the module doc (lines 1-3) say this is a deliberate reconstruction. I could not prove it is unintended.
- Outside the window, `crafting.rs:386-389` calls `on_event(Craft { quantity })` after `consume_materials` and `grant_reward` have already run. If quantity were 0 (no 21785 grant), `on_event` would return `Err` at line 688, leaving the transaction half-applied. I checked the Miner transaction source and it comes from server-held smelting state, so I could not make this client-reachable.
