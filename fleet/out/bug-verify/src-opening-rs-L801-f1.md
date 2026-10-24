<!-- fleet job=bug-verify id=src-opening-rs-L801-f1 status=done turns=21 usd=0.0219 tokens(read,write,in,out)=[754005, 59980, 44, 13806] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/gameplay/crafting.rs:366-389

**Verdict:** confirmed (the mechanism is real), but I would downgrade severity to **low**. The claim's own caveat is right that the impact is mostly a dropped completion and a forced disconnect, not a gain.

**Severity if confirmed:** low. Items are not duplicated or lost: the ore is consumed and the silver bar is granted together. No crash and no save corruption were found.

**Evidence (all paths verified):**

1. **Module tree.** `src/lib.rs` has `pub mod gameplay;`, and `src/gameplay.rs:45` has `mod crafting;`. `crafting.rs` is live code, not test-only. `smelting.rs` is `pub mod smelting` (lib.rs:80).
2. **Reach.** The 39/x frame during a running smelt goes `gameplay.rs:4284-4285` → `route_movie` → `crafting.rs:70-72` (`smelting.handle(inner)?` then `apply_craft(CraftingJob::Miner, …)`). The recipe-book start path goes through `gameplay.rs:4428-4429`. Both propagate with `?`.
3. **Recipe key.** `smelting.rs:265-293` (`begin_recipe`) checks only `learned`, the rank and the ingredients, then stores `active_recipe_key`. `recipes.json` has non-copper Miner recipes with `minigame_type_id: 9`, e.g. `miner.silver_bar` (recipe_id 7, output 21788×1, lines 3863-3886). `smelting.rs:511-516` builds the grant from `selected_recipe()`. So a learned silver recipe yields `quantity = 0` at `crafting.rs:370-379`.
4. **Early error.** `opening.rs:685-689`: `OpeningEvent::Craft { quantity } if recipe_id == 0 || !(1..=10_000).contains(&quantity)` returns `invalid("invalid opening craft event")`. This check runs before the authorization block at 703-720, so it fires for any quantity 0 event.
5. **Mutations before the error.** `crafting.rs:366-367` runs `consume_materials` and `grant_reward` before the event (`:386-389`). The engine's own `smelting.rs:497-507` has already set `phase = Won` and incremented `completed` before `apply_craft` runs. The `?` at 389 skips `apply_opening`, `npc_quest_event` (402-408), `npc_minigame_win` (409), and `out.replies.extend(result.replies)` (412). That last one drops the OnGameWon and results packets, and the inventory `out.replies` from consume and grant are dropped as well.
6. **Caller.** No rollback exists. A grep for rollback/snapshot found none in gameplay. `gateway.rs` `end_session` (around lines 4429-4433) saves `session.gateway.snapshot()` after an error, so the mutated state persists. I did not fully trace how `dispatch_message`'s `?` error is contained in the gateway, so whether the session drops or only the packet is lost is unconfirmed.
7. **Reachability caveat.** The silver recipe must be in `learned_recipes`. `learn_recipe` (`gameplay.rs:1424-1449`) has no inventory check of its own, so this depends on the caller that grants pattern items. The gate `opening_craft_pending(2002)` is also needed, i.e. the Miner tutorial craft must be pending. Both are plausible but narrow.

**What the claim got right:** the line numbers cited are accurate (crafting.rs 366-389, 402-409; opening.rs 688-689; smelting.rs 270-293, 511-516; opening_craft_pending at 215-231).

**Corrected fix:** the claimed fix is sound. Skip the opening event when quantity is 0: `if quantity > 0 && self.opening_craft_pending(opening_recipe)`. A stronger fix is to keep the event from failing after the mutations, because the failure also drops the completion replies and the consume/grant inventory packets. Either validate that the transaction grants 21785 before mutating, or make the event non-fallible at this point.
