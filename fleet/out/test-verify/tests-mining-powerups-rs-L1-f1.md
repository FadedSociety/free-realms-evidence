<!-- fleet job=test-verify id=tests-mining-powerups-rs-L1-f1 status=done turns=6 usd=0.0082 tokens(read,write,in,out)=[59904, 26697, 14, 8458] model=claude-haiku-5-5 -->
# high: tests/mining_powerups.rs:497

**Verdict:** `confirmed`, but the claim's own "destroys nothing" example is wrong. The real gap is a named-target-only regression.

**Evidence**

- The mutation that passes is: in `destruction()` (`src/mining.rs:1873-1887`), keep clearing the pressed cell (`run.board[points[0]] = TILE_EMPTY`), but skip or redirect the `run.board[...] = TILE_EMPTY` on the named `(4,3)` (or clear a blocker instead). `get_random_tile` still verifies that the picked tile is `(4,3)` and idle, so the handler still returns `Ok`.
- Walking the test (`tests/mining_powerups.rs:497-512`) against that mutation:
  - L505 `unwrap()`: passes, since the action is still accepted.
  - L506 no `OnActionMsg` reply: passes.
  - L509 `board_count(TILE_POWERUP_DESTRUCT) == 0`: passes, because the pressed cell is still cleared.
  - L510 `board_count(SELECTABLE) >= selectable_before - 1`: `(4,3)` is never removed, so the count is at least 1 before and after gravity. Passes.
  - L511 `board_at(4,10) != TILE_POWERUP_DESTRUCT`: passes, since the cell is not 952.
- No other test covers this. A grep for `TILE_POWERUP_DESTRUCT`, `952` and `destruct` across `tests/` finds only the lines above, plus `mining_powerups.rs:322` (an init message) and the atomicity/replay tests at 669, 772 and 804. The atomicity test (L801-819) only checks refusal and replay of the pressed tile. The queue-draw test (L754-798) only checks that exactly one draw is consumed. The short-list test (L653-691) only checks refusal. None of them inspects the state of `(4,3)` after a successful action.

**Where the claim is wrong**

- "Destroys nothing" is caught. If the handler removes no tile, the pressed `952` at `(3,3)` survives gravity, so `board_count(TILE_POWERUP_DESTRUCT) == 0` at L509 fails. The claim's first example is refuted by that line.
- The `>= before - 1` check on L510 is weak, as the claim says. It is not what catches "no tile removed".
- The claim's proposed fix needs a caveat. Gravity refills freed cells from the queue, and the fixture queue is not seeded in this test. So "(4,3) is not SELECTABLE" or "count drops by exactly one" could fail on a correct implementation if the refill draws a selectable value. Line 437 shows the pattern that makes the check deterministic: call `engine.seed_random_queue(&vec![0_u16; 70])` (a non-selectable value) before the action, then assert `board_at(4,3) != SELECTABLE` and/or the exact count.

**Minimal fix:** seed the queue with non-selectable values as at L438, then add `assert_ne!(board_at(&engine, 4, 3), SELECTABLE);` after the action. This catches the skip-named-removal and the wrong-tile mutations, and does not depend on the old `>=` bound.
