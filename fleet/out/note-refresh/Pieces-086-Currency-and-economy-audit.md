<!-- fleet job=note-refresh id=Pieces-086-Currency-and-economy-audit status=done turns=15 usd=0.0188 tokens(read,write,in,out)=[378699, 50436, 32, 17430] model=claude-haiku-5-5 -->
# notes/Research/Pieces/086 Currency and economy audit.md

**Verdict:** badly stale. The file:line citations for the coin sites have moved, and most of the "open findings" status table is now false. The sinks (revive, Coin Shop buy, trade), the quest-reward atomicity gap and the kart integration have all landed since the audit. The recovered-client facts (currency rows, packet IDs, the recorded profile) were not checked and are outside this pass.

**Corrections:**

1. `old:` `paid-revive-sink` | proposal-only | revive cost and wallet gate recovered (piece 037); nothing debits coins
   `new:` `paid-revive-sink` | wired | revive cost and wallet gate recovered (piece 037); the paid revive debits the engine's price with `Inventory::spend_coins` in the same staged `Gameplay` (`gameplay/knockout.rs:43-44`)
   `why:` repo:prototype/osfr-tools/src/gameplay/knockout.rs:43-44 (`engine.paid_revive(...)` then `self.inventory.spend_coins(price)`); repo:prototype/osfr-tools/src/inventory.rs:877-886

2. `old:` Queued (items 083, 084) | recovered coin sink, not implemented; coins can currently only increase
   `new:` Partly implemented | Coin Shop buy debits the balance before the grant (`coin_shop.rs:544-556`, `next_state.coins -= total_price`); coins can decrease
   `why:` repo:prototype/osfr-tools/src/coin_shop.rs:544-556 (insufficient-coins check, then debit and `grant`); the Coin Shop sell path is at coin_shop.rs:703

3. `old:` Queued (item 085) | recovered coin trade, not implemented
   `new:` Implemented in `trade.rs` | coins move between the two staged inventories on commit
   `why:` repo:prototype/osfr-tools/src/trade.rs:1303 (`staged[source].state.coins -= session.coins[source]`) and trade.rs:1340 (`staged[target].state.coins = total`)

4. `old:` `Inventory::grant_coins` (the only balance mutation) | `prototype/osfr-tools/src/inventory.rs:427`
   `new:` `Inventory::grant_coins` (the credit site; debits are `Inventory::spend_coins`, `inventory.rs:877`, and the Coin Shop and trade debits above) | `prototype/osfr-tools/src/inventory.rs:859`
   `why:` repo:prototype/osfr-tools/src/inventory.rs:859-866 (`grant_coins`, `self.state.coins += amount`); the function is no longer at line 427, and `grant_coins` is not the only mutation (inventory.rs:886; coin_shop.rs:556; trade.rs:1303, 1340)

5. `old:` exactly one coin
   balance assignment site
   `new:` one coin credit site and several debit sites (see the inventory table above)
   `why:` the same assignment sites as correction 4 (repo:prototype/osfr-tools/src/inventory.rs:866, 886; coin_shop.rs:556; trade.rs:1303, 1340; gameplay/knockout.rs:44). Note: this old text spans lines 102-103 of the note; apply it as one replacement.

6. `old:` coins-before-items
   `new:` fixed (coins and items commit together)
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:5413-5424 (`apply_quest` calls `inventory.grant_bundle(reward.coins, &reward.items)` on a clone, then `quests.acknowledge_reward` only on success); repo:prototype/osfr-tools/src/inventory.rs:1044-1059 (`grant_bundle` stages coins and items, commits both or neither)

7. `old:` `gameplay::apply_quest` credits coins, then grants items after the quest is already marked rewarded; an item failure leaves a partial reward
   `new:` `gameplay::apply_quest` stages coins and items together through `Inventory::grant_bundle` and acknowledges the quest only after that commit; an item failure leaves the quest pending, with no partial reward
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:5413-5437 (the `Err` arm reports "Quest reward remains pending" and does not acknowledge). Also repo:notes/Reviews/Economy Independent Review.md:109-110 records the same fix.

8. `old:` not_registered | kart payouts exist as a proposal only
   `new:` wired | kart race payouts are granted into the live inventory through `KartGateway::claim_reward_with_event` (`gameplay.rs:1940-1941`)
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:1940-1941 (`kart.claim_reward_with_event(&mut staged.inventory, profiles)`); repo:prototype/osfr-tools/src/kart_gateway.rs:724-760 (commits the staged inventory and profiles)

9. `old:` `kart_race` is a proposal that the lead has not registered in `src/lib.rs`.
   `new:` `kart_racing` is registered in `src/lib.rs` (`pub mod kart_racing;`) and its reward claim runs in the live gameplay path; the `KartRace` producer label in `piece_086.rs` is checker-only.
   `why:` repo:prototype/osfr-tools/src/lib.rs:46; repo:prototype/osfr-tools/src/gameplay.rs:1940-1941; repo:prototype/osfr-tools/src/restoration/piece_086.rs:162-163

10. `old:` `prototype/osfr-tools/src/encounter.rs:133`
    `new:` `prototype/osfr-tools/src/encounter.rs:637`
    `why:` repo:prototype/osfr-tools/src/encounter.rs:133 is the `distance` helper now; `pub struct EncounterReward { pub coins: u32, ... }` is at encounter.rs:636-637

11. `old:` `prototype/osfr-tools/src/quests.rs:67`
    `new:` `prototype/osfr-tools/src/quests.rs:70`
    `why:` repo:prototype/osfr-tools/src/quests.rs:67-70 (`QuestReward` now begins at 68, `pub coins` at 70). The `Trial.reward_coins` cite `quests.rs:119` is now line 126 (quests.rs:126); the `OpeningReward.coins` cite `opening.rs:46` is now line 48 (opening.rs:46-48).

**Unsure:**
- The "Implemented sources in the live gameplay path" list (`quest_reward`, `checkpoint_trial`, `encounter_clear`, `opening_stage`, `opening_discovery`) omits the kart claim (see correction 9). I did not check whether the trade and Coin Shop debits are the intended "checked sinks" the Lead paragraph asks for, so I left that sentence alone.
- The test counts (10 Rust tests in `tests/piece_086.rs`, matching "10 passed") check out. I did not count the 16 Python tests exactly; `tests/pieces/test_piece_086.py` has about that many test methods.
- The `check_invariants` "0 violations" result and the lab bundle paths were not re-run, so I could not confirm them.
- The "Open findings" rows for `station-cash-source-external` and `coin-payout-numbers-unrecovered` are not contradicted by anything I read, but I did not check for SC credit sites beyond `coin_shop.rs`'s wallet code.
