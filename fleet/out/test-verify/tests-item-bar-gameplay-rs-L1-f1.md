<!-- fleet job=test-verify id=tests-item-bar-gameplay-rs-L1-f1 status=done turns=6 usd=0.0063 tokens(read,write,in,out)=[59581, 20127, 14, 6277] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/item_bar_gameplay.rs:173

**Verdict:** `confirmed` (the core claim holds: the test cannot detect the route regression its name describes. Two secondary points in the claim are unverified or overstated, noted below.)

**Evidence:**

The test (`tests/item_bar_gameplay.rs:173-187`) has two assertions, and neither depends on which handler answered 42/16:

- `assert!(!out.changed);` (line 181)
- `assert!(!out.replies.iter().any(|r| r.starts_with(&[38, 0, 30, 0]) && r[24] == 1));` (lines 182-186)

Walk-through of regressions that still pass:

1. **Route dropped entirely.** Suppose the 42/16 handling is removed, so `handle_in_world_inner` returns `Outcome::default()` for that request. `changed` is false, so line 181 holds. `replies` is empty, so the `any` on line 183 is false and the negated assertion holds. The test passes. (`sync_tracked_target`, `sync_client_objectives` and the achievement settlement could add replies, but none of them is a 38/30 with `r[24] == 1`.)

2. **Misrouted to the Mystery Chest handler.** `mystery_chest_loot.rs:124-130` handles a Check for a non-chest id by returning `check_reply(id, false)` with `changed: false` and `pending = None`. That is a `38/30` whose byte 24 is 0 (`mystery_chest.rs:146-156`). The `r[24] == 1` guard is false, and `changed` is false, so the test passes.

3. **Misrouted to the item bar's own check.** `item_bar.rs:343-347` only emits the `38/30` success reply with byte 24 = 1 for a consumable. For a non-consumable, `handle` returns `Ok(None)` at `item_bar.rs:261-263`, so this path needs a regression that makes the item bar accept a non-consumable. That is the only way the test would fail, and it is the only regression the test does catch.

So the test catches "the item bar consumes or approves a non-consumable" and nothing about the 42/16 route itself. The name `other_inventory_requests_keep_their_routes` overclaims. The comment on lines 176-177 also states the expected routes, but no assertion checks them.

**Secondary points:**

- `r[24]` (line 185): the `&&` short-circuits, so `r[24]` is only evaluated when the reply starts with `38/0/30/0`. A short reply with that prefix would panic, which fails the test rather than passing it. This is not a vacuity problem.
- Instance 1 existence: I did not confirm this in the fixture (`lab/references/...` is outside the search roots). The claim's point is still valid either way. If instance 1 is absent, `item_bar` returns `None` and the request falls through, so the test is even weaker. The assertion `game.state().inventory.items.iter().any(|i| i.id == HAT_LIKE)` would close that gap.

**Minimal fix:** rename the test to `a_non_consumable_42_16_is_not_consumed_by_the_item_bar`, or add a canary that pins the expected route, for example `assert!(!out.replies.is_empty())` plus an exact-prefix check on the fall-through reply (or the chest's `38/30` with byte 24 = 0 when the chest package is loaded). Also add `assert!(game.state().inventory.items.iter().any(|i| i.id == HAT_LIKE))` before the request.
