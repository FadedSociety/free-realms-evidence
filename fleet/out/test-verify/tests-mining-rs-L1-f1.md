<!-- fleet job=test-verify id=tests-mining-rs-L1-f1 status=done turns=9 usd=0.0085 tokens(read,write,in,out)=[114238, 28528, 20, 7584] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/mining.rs:569

**Verdict:** `confirmed`

**Evidence:** I could not refute the claim. Walking the test with the guard deleted (`mining.rs:1565`, `if !in_board(x, y, bounds) || y != bottom`):

- `tests/mining.rs:579-582`: `OnLevelEventMsg 50 (LEFT, TOP)` targets `rows[0][0]`. `empty_rows()` (line 75) is all `1`s, so the cell is shape code `1`. `mining.rs:1344-1345` shows code `1` is filled by `random_tile(run, spec, false, ...)`, which excludes collectables. The cell is therefore never ORE. With the guard gone, it reaches the goal lookup at `mining.rs:1586` (`spec.goals` has only ORE=601), which returns `Err`. The `.is_err()` assertion still passes.
- `tests/mining.rs:585-588`: `(LEFT+1, TOP+7)` is `rows[7][1]`, a plain value-1 cell on the bottom row. It also fails the goal lookup and returns `Err`. The second `.is_err()` still passes.
- The test has no other assertions, and it never checks `engine.state()`. So the mutant survives.
- The only collectable, `rows[7][0] = -ORE` (line 571), sits at `(LEFT, TOP+7)`, and neither call targets it. Its only off-row path is never exercised.
- The dispatch at `mining.rs:830-843` does no bounds or row check of its own, so `collect_fall` is the only place the bottom-row guard lives.

The suggested fix also holds up. With `rows[6][1] = -ORE` and a fall at `(LEFT+1, TOP+6)`, the board value is 601, which matches goal index 0. With the guard deleted, the call would succeed and `is_err()` would fail. With the guard in place, `y=9 != bottom=10`, so it returns `Err`. The sign convention matches the existing win test at line 594, where `-ORE` falls successfully.

Minor additions: the `rows[0][1] = 403` setup at line 572 is never targeted, so it is dead setup. Out-of-board coordinates are also untested, so deleting the `!in_board` half would not be caught by this test either.

**Minimal fix:** Set `rows[6][1] = -i32::from(ORE)` and send `OnLevelEventMsg\t50\t{LEFT+1}\t{TOP+6}`. Assert `is_err()` and that `engine.state()` is unchanged before and after. Keep the bottom-row non-goal call as a separate assertion.
