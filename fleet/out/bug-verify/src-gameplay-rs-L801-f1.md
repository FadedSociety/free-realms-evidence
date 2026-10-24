<!-- fleet job=bug-verify id=src-gameplay-rs-L801-f1 status=done turns=11 usd=0.0148 tokens(read,write,in,out)=[290956, 48613, 24, 11577] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/gameplay.rs:1479

**Verdict:** confirmed, with a corrected mechanism and fix. The symptom is real; the proposed fix is wrong.

**Severity if confirmed:** low. Pattern use is a missing feature, not a regression in a wired path. No crash, save corruption, or item/coin gain is involved. The reviewer's "medium" overstates it.

**Evidence (what holds):**
- Module tree: `src/lib.rs:26` has `pub mod gameplay;`, so `gameplay.rs` is live. `item_bar.rs` is also live (`lib.rs:38`).
- Live entry: `handle_in_world_inner` (`gameplay.rs:2216`) calls `self.handle(...)` at `:2333` when `self.opening.is_none()`. That reaches the 42 branch at `gameplay.rs:5337-5353`, which calls `learn_consumed_patterns(&before)` at `:5353`.
- The only call site of `learn_consumed_patterns` is `:5353`. The only call to `learn_recipe` is `:1500`. Repo-wide, the only other writers to `learned_recipes` are the opening seed at `:867` and test fixtures (`tests/chess_route.rs:60`, `tests/recipe_book_route.rs:153`). So no live path can add a learned recipe from a pattern.
- `inventory.rs:1145-1212` (`route`): opcode 2 sets `item_id = 0` (no count change), 3/8 call `equip` (sets `entry.item_id`, no count change), and `_ => Ok(default)`. Family 35/34 returns replies only. Nothing in the 42 branch decrements a count, so `before` and after are equal.
- Count decrements exist only in `Inventory::consume` (`inventory.rs:1062`), and its callers are item_bar, pets, coin_shop, mystery chest, crafting `consume_materials` (`gameplay/crafting.rs:508`), housing and trade (`trade.rs:1321` decrements `owned.count` directly). None of these spends a recipe pattern in a live path.

**Evidence (what is wrong):**
- The proposed item-bar fix cannot work. `item_bar.rs:22-23` says only the Small Health Potion rows (2173, 11002) are usable. `Effects::default()` (`item_bar.rs:76-88`) is that table, and `consume` (`item_bar.rs:423-442`) refuses any definition without an effect row (`:438`) before calling `inventory.consume`. A pattern can never reach `inventory.consume` through the bar.
- Pattern use (the 42/15 "use a pattern" action, if the native client sends it that way) is simply not implemented. `route` drops it as a no-op, so there is nothing to wire `learn_consumed_patterns` to.
- Caution on the reviewer's "common dispatcher" option: a before/after count diff is not a consumption signal. Any decrement would fire it, including trade (`trade.rs:1321`) or a sale. Handing out a recipe for giving an item away would be a gain bug.

**Corrected fix:** implement an explicit server-side pattern-use action. Validate that the instance is a pattern with `recipe_item_definition_id` (`recipes.rs:131`), call `inventory.consume(id, 1)`, then call `learn_recipe(recipe_id)` and send its packet. Do this in one place so a refused use changes nothing. Do not route it through `item_bar`. Add a test that uses a pattern (for example definition 2506) and asserts the 0x3f/op1 recipe-add packet, plus a test that a refused or duplicate use leaves the count and `learned_recipes` unchanged.
