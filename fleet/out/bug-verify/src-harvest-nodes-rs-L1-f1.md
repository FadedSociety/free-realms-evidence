<!-- fleet job=bug-verify id=src-harvest-nodes-rs-L1-f1 status=done turns=9 usd=0.0087 tokens(read,write,in,out)=[119132, 25531, 20, 8631] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/harvest_nodes.rs:371-384

**Verdict:** confirmed (the mechanism is real), with the severity lowered to low-medium. The cited lines and the code path check out. The overshoot is reachable from a client move. The harm is a stranded, recoverable win, not loss or gain of items.

**Severity if confirmed:** medium. It is not high: nothing crashes, no save is corrupted, and no items or coins are gained. The run is held in `LevelComplete` and the reward is not lost. The player can pay it out once they make room in the bag. The stranding is self-inflicted.

**Evidence (all paths under `prototype/osfr-tools/src`):**

- *Module tree:* `lib.rs:37` has `pub mod harvest_nodes;`, `lib.rs:54` has `pub mod mining;`, and `gameplay.rs:45` has `mod crafting;`. `gameplay.rs:2495` imports `payout_fits` from `harvest_nodes`. So this is production code, not test-only.
- *Gate:* `harvest_nodes.rs:377` sets `clusters = (goal.quota / goal.per_reward.max(1)).max(1)`. It is quota-based, and `payout_fits` (lines 371-384) runs `grant_bundle` on a clone. It is called once, at `gameplay.rs:2528`, in the 26/8 handler before `begin_gather`. Nothing re-checks it later.
- *Payout:* `mining.rs:1705` sets `clusters = run.collected[goal_index] / goal.per_reward`, which is collected-based.
- *Overshoot:* `mining.rs:1588` (fall path) and `mining.rs:1638` (`collect_chain_goals`) each add 1 to `collected` per goal tile, with no cap at quota. A chain of several goal-valued tiles (`mining.rs:706-716`, `751-757`) can push `collected` past quota in one move. Gravity (`mining.rs:758-765`, `1612`) can add more. `settle_after_collect` (`mining.rs:1664-1671`) only checks `collected >= quota`, so the win fires with the overshoot kept.
- *Failure:* on `OnNextLevelMsg` (`mining.rs:870-879`), `reward_transaction` runs with the larger count. `apply_type8` (`crafting.rs:443-464`) then calls `grant_reward`. `grant_bundle` (`inventory.rs:1045-1059`) is all-or-nothing, and `grant_with_tint` (`inventory.rs:1009-1010`) returns "inventory is full" when `MAX_ITEMS` is reached. It also rejects a quantity above one stack (`inventory.rs:982-983`). Either error propagates, so the staged change is not kept.
- *Example:* quota 10, per_reward 5. The gate reserves 2 clusters. A 5-tile chain of that goal gives `collected` 15, which pays 3 clusters. A bag with room for exactly 2 clusters then fails the grant.

**Caveats:**

- Each retry is assumed to fail the same way while the bag stays full. I did not trace the session/error handling after the `Err`. The claim also says the phase stays `LevelComplete`. I did not confirm that by reading the error path, but the staged-clone structure supports it.
- The scenario needs the bag to be nearly full at run start. That is narrow, but a player can produce it.

**Corrected fix:** The suggested `quota.saturating_add(max_chain_size)` in `payout_fits` is sound only if the bound also covers gravity-driven overshoot. A safer bound is `(quota + board_tiles) / per_reward`, where `board_tiles = width * height`. The option of capping `collected` at `quota` in both increment sites works too. It makes the gate and the payout agree exactly. It does change the quota-update messages and drops overshoot tiles, so it should be a deliberate design choice.</result>
</invoke>
