<!-- fleet job=bug-hunt id=src-mining-rs-L1601 status=done turns=14 usd=0.0203 tokens(read,write,in,out)=[435342, 52004, 30, 18920] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/mining.rs lines 1601-2400 of 2434

One finding in my window (lines 1601-2400). I read the whole window and the callers that matter (the `OnActionMsg` handler at mining.rs:776-800, the clone-then-commit at 619/921, `validate_powerup_definitions` at 1076-1100, and the gateway `contain` boundary at osfr-gateway.rs:3735-3754).

- **[medium] prototype/osfr-tools/src/mining.rs:2039 - `shuffle_placements` indexes `positions[0]` before its own `n == 0` guard, so an empty placement list panics.** `vec![positions[0]; n]` is evaluated even when `n == 0`, so `positions[0]` panics on an empty slice. The `if n == 0 { return ... }` guard at 2040 is never reached in that case.

  **Failure scenario:** a player is on a Playing run whose board has a shuffle powerup (`953`) and no other idle tile with value `>= 200` other than blockers and dropzones, so `candidates` is empty after `retain` (1910). The player sends `OnActionMsg\t953\t<x>,<y>,` with only the pressed tile. Then:
  1. `apply_powerup_action` passes the pressed-tile check (1795-1800).
  2. `shuffle_tiles` computes `cap = min(power-1, 0) = 0` (1916), and `points.len() == cap+1 == 1` passes (1920).
  3. `placements` stays empty, so `n = 0`, and `shuffle_placements(&[], &[])` is called (1940).
  4. `positions[0]` panics on the empty slice (2039).

  The same happens for any shuffle press when the content sets `power == 1`. `validate_powerup_definitions` only requires `power >= 1` (mining.rs:1100), and the real power values are not recovered (comment at 110-111), so this depends on the content table.

  **Reach:** `OnActionMsg` (mining.rs:776-798) → `apply_powerup_action` (1773) → `shuffle_tiles` (1894) → `shuffle_placements` (2034). Nothing upstream rejects a one-point list. `powerup_points` only requires two values (2273-2275) and `shuffle_tiles` only checks the count, which is 1 here. The panic happens before the `next` state is committed (921), so the session's saved state is unchanged. The gateway's `contain` (osfr-gateway.rs:3735-3754) catches it and ends only that player's session with `internal_error`. The server process survives, so I rate this medium, not high.

  **Fix:** return early when `positions` is empty, before the index, e.g. `if drawn_values.is_empty() { return Vec::new(); }` at the top of `shuffle_placements`, or reject `n == 0` in `shuffle_tiles` with `invalid("mining shuffle needs a tile")`. Either way the `vec![positions[0]; n]` line must not run on an empty slice.

Checked and not reported: `apply_powerup_action` and the other powerup handlers mutate `run` before returning `Err`, but the handler works on a clone and only commits at 921, so those partial writes are discarded. `coordinate_list`/`number_list`/`decode_payload` lengths and indices are guarded. `reward_transaction` cannot divide by zero, because `validate_spec` rejects `per_reward == 0` (mining.rs:1162). `shatter` can re-explode a stale array2 entry (no `board != EMPTY` check), but I could not show it diverges from the original, so I left it out.</result>
