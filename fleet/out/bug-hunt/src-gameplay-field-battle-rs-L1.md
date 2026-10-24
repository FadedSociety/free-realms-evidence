<!-- fleet job=bug-hunt id=src-gameplay-field-battle-rs-L1 status=nothing_found turns=21 usd=0.0161 tokens(read,write,in,out)=[422811, 36460, 44, 14614] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/field_battle.rs lines 1-135 of 135

No reachable defect in `gameplay/field_battle.rs` lines 1-135.

What I checked:

- **Unwraps (lines 74, 96, 111, 131):** `profiles`, `abilities` and `encounter` are all `Option`s, but they are loaded and replaced together. `abilities` and `encounter` are set together at `gameplay.rs:681-697` (both need `opening.json`), and `content_reload.rs:24-25` swaps them as a pair. `profiles` is already unwrapped at `gameplay.rs:4619`, before the `handle_battle_go` call at `gameplay.rs:4738`, so line 74 adds no new crash. Line 111 is guarded by the `take_pending_battle` returning `Some`, which requires an encounter. Line 131 runs only after that same path, so it is safe.
- **Prize gate (lines 27-39):** `encounter/field.rs:411-421` uses `all()`, which short-circuits, so the bundle only matters when every row passed. `inventory.rs:513-534` rejects zero quantity and any row over one stack, and bounds the bundle length. Empty bundles pass. The gate runs before any mutation in both `begin_field_battle` (line 49) and `handle_battle_go` (line 92).
- **Consume-then-refuse (lines 85-95, 107-121):** `take_pending_battle` consumes the screen, but every refusal path goes through `refuse_battle`, which reopens it through `reopen_battle_screen` (`field.rs:511-536`). `begin` mutates nothing before its refusals; `pending_battle` is cleared only after the checks pass (`encounter.rs:1356-1386`).
- **Level comparison (`field.rs:33-35`):** `level < required` is correct and matches its doc.
- **Proximity (`field.rs:566-573`):** the distance check uses the client-reported position. That is inherent to the game and gates only the screen, not a grant.
- **`apply_encounter` `?` after `begin` (line 58):** `begin` returns no rewards, so nothing is left half-applied.

Not reportable: the `unwrap` at line 74 and the `unwrap` at line 96 are guarded by upstream code that already panics first or keeps the two options in step; the reward-selection path (`encounter.rs:2002`) lies outside this window and grants one prize, which the all-prizes preflight covers.
