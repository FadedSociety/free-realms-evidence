<!-- fleet job=test-audit id=tests-mining-powerups-rs-L1 status=done turns=6 usd=0.0110 tokens(read,write,in,out)=[101689, 33176, 14, 11703] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mining_powerups.rs lines 1-902 of 902

Window: `prototype/osfr-tools/tests/mining_powerups.rs` lines 1-902. Checked against `src/mining.rs` (`OnActionMsg` dispatch 776-800, `validate_powerup_definitions` 1076-1115, `shuffle_placements` 2034+). No `#[ignore]` or fixture-dependent early returns in the window.

- **[high] tests/mining_powerups.rs:497 destruct_action_clears_the_named_tiles - the only check on the named target (`SELECTABLE` at (4,3)) is `>= selectable_before - 1`, which passes if the action destroys nothing.**
  - Why it cannot catch a regression: a `952` handler that removes no tile, or removes the wrong tile, still leaves `SELECTABLE` count at or above `before - 1`. The `assert_ne!(board_at(4, 10), TILE_POWERUP_DESTRUCT)` on line 511 checks a cell the action never names (the named cells are (3,3) and (4,3)), and it is satisfied by any non-destruct value there.
  - Fix: assert the pressed cell is no longer `TILE_POWERUP_DESTRUCT`, and assert the named cell (3,3) and (4,3) are not `SELECTABLE` afterwards (or, with a seeded tile queue as in the shuffle tests, assert the exact `SELECTABLE` count drops by exactly one).

- **[high] tests/mining_powerups.rs:607 shuffle_placement_walk_matches_the_as2_targets - the value assertions (`distinct_result`, `equal_result`) are computed from literals and never read the code under test.**
  - Why it cannot catch a regression: line 618-621 and 627-632 map over indices with a hard-coded array and ignore the `distinct`/`equal` return values (the `equal` map uses `|(index, _)|`). A broken `shuffle_placements` that returns the wrong destinations still passes the value checks. Only the coordinate asserts at 617 and 626 exercise the function, and they cover just the two fixtures.
  - Fix: map the drawn values through the returned destinations (for each mover, its destination's slot gets `drawn[(index+n-1)%n]`, applied to a board of those positions) and assert the resulting value vector, or drop the tautological `*_result` blocks and keep the coordinate asserts with a third fixture (for example all-equal `[401,401,401]`).

- **[medium] tests/mining_powerups.rs:396 dynamite_shatters_the_recovered_neighbourhood - the name says the neighbourhood is destroyed, but only the pressed cell is checked.**
  - Why it cannot catch a regression: the seeded neighbour `(3,4)` is `SELECTABLE` and is never inspected. A handler that clears only the pressed cell and skips the BFS neighbour entirely still passes `board_count(TILE_POWERUP_DYNAMITE) == 0` and the no-reply check.
  - Fix: after the action, assert `board_at(3,4) != SELECTABLE` (or that the count of the seeded `SELECTABLE` drops by one) and that `(3,3)` is no longer dynamite. Rename to match the claim if the neighbour is not meant to be checked here.

- **[medium] tests/mining_powerups.rs:410 dynamite_neighbour_order_is_down_up_right_left - the "must fail" half can be refused for a reason other than order, and the comment's coordinates do not match the fixture.**
  - Why it cannot catch a regression: the bad list `3,4,4,4,3,4,3,5,4,4,` repeats the pressed tile `(3,4)` as an entry, which is a different defect from wrong order. An order check that is removed entirely still refuses that list, so the test passes. The comment on lines 411-413 names neighbours `(3,2)`, `(4,3)`, `(2,3)`, but the pool actually seeds `(3,5)`, `(3,3)`, `(4,4)` around the pressed `(3,4)`, and the duplicate `(4,4)` seed is silently removed by `retain`.
  - Fix: build a bad-order list that is otherwise identical to the valid one (same multiset, same length, no pressed repeat), e.g. `3,4,4,4,3,5,3,3,4,4,`, and assert it is refused with the board unchanged. Correct the comment to the real coordinates.

- **[medium] tests/mining_powerups.rs:381 malformed_definitions_are_refused - three of four cases assert only `is_err()`, so any unrelated load failure passes.**
  - Why it cannot catch a regression: `too_much_power` (950, power 4096), `duplicate` (951 twice) and `no_weight` (empty list at percent 100) check only that loading fails. A parse error or a missing-file error would satisfy them. The `wrong_value` case is the only one that checks its message.
  - Fix: match the error text for each case, for example `"invalid mining powerup power"`, `"duplicate mining powerup value"`, `"mining powerup spawn chance needs definitions"`, which are the exact messages in `validate_powerup_definitions` (mining.rs 1085, 1098-1115).

- **[low] tests/mining_powerups.rs:515 shuffle_action_rotates_tiles_and_stays_in_bounds - the name promises rotation and bounds, but the body checks counts plus a gravity-dependent cell `(4,10)`.**
  - Why it cannot catch a regression: no rotation is asserted (only one `SELECTABLE` is in play and it is not checked at the pressed slot (3,3)), and "stays in bounds" is never checked. The `(4,10)` value depends on gravity from the named (4,3) tile, so an unrelated gravity or refill change moves it and the test churns, while a wrong-slot placement that happens to keep one `SELECTABLE` on the column still passes.
  - Fix: rename to what it checks, or assert the pressed slot value after the action (`board_at(3,3) == TILE_WILDCARD`) and the exact destination of the picked tile. Use the seeded tile queue (as the runtime shuffle tests do) so the destination is deterministic.
