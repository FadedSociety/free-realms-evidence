<!-- fleet job=test-audit id=tests-miner-first-ore-rs-L1201 status=done turns=8 usd=0.0101 tokens(read,write,in,out)=[145925, 36972, 18, 8116] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/miner_first_ore.rs lines 1201-2296 of 2296

Window: `prototype/osfr-tools/tests/miner_first_ore.rs` lines 1201-2296. Most tests here are sound: the refusal and replay checks go through `assert_packet_changes_nothing` / `assert_inert` (support/npc_quest_chain.rs:702, miner_first_ore.rs:194), which compare serialized state and save bytes, and the payouts are checked against literal values. The findings below are the ones I could confirm.

- **[medium] prototype/osfr-tools/tests/miner_first_ore.rs:2255 `the_chapter_uses_no_dev_commands` - the name and doc claim "no realm chat command is sent", but the body never checks chat; the only forbidden-packet check is the 38/12 teleport prefix.**
  - Why it cannot catch a regression: a change that sends a chat or dev command on any step would still pass, because nothing inspects for it. The teleport check at 2278-2283 also covers only the `replies` vector, and line 2268 (`gather_copper(...)`) discards its replies, so a teleport sent during the gather would also pass.
  - Fix: either drop "no realm chat command" from the name and doc, or scan every reply (including the gather's) for the chat family and assert none is present. Assert the 38/12 check over all collected replies.

- **[medium] prototype/osfr-tools/tests/miner_first_ore.rs:2058 `the_objective_is_produced_by_the_shipped_mining_board` - the "one shipped win pays at least RUSH_ORE" check recomputes the payout with a formula copied from the code and never runs a win.**
  - The expected yield is `goal.quota / goal.per_reward * output.cluster_quantity` (lines 2140-2145), using the full quota. The engine (src/mining.rs:1686-1707, `reward_transaction`) pays `collected / per_reward * cluster_quantity` for the tiles actually collected. The test therefore checks a spec-derived number, not the engine's payout. Breaking the engine's reward path (a wrong `collected`, a dropped per-reward division) leaves this test green. The doc's "produces its gather target" is also only checked as "has a COPPER_ORE output", not as the gather objective's value.
  - Why it cannot catch a regression: the expected number comes from the same formula as the code under test, and no reward is produced through the engine.
  - Fix: run the shipped board to a won state through `Type8Engine` and assert the paid Copper Ore equals `RUSH_ORE` or more, or assert the engine's `reward_transaction` output for a full-quota run against a hard-coded per-output count taken from the shipped JSON. The gameplay test at 1862-1866 already covers the live payout, so this test should assert the shipped row values as literals.

- **[low] prototype/osfr-tools/tests/miner_first_ore.rs:1755 `a_near_cap_coin_balance_refuses_the_turn_in_without_paying_xp_or_item` - the doc says "spending the overflow frees the same held end screen", but the body sets `state.inventory.coins = 0` directly.**
  - Why it cannot catch a regression: the spend path (whatever the production code does to spend coins) is never exercised, so a bug there would not be seen. The assertion at 1759 only checks that the balance is 5 after the turn-in.
  - Fix: spend the overflow through the production path (or assert the balance drops by a specific amount through a real purchase), then assert the retry pays exactly 5.

- **[low] prototype/osfr-tools/tests/miner_first_ore.rs:1661 `the_record_and_both_npcs_resolve` - the loop over Trixi's `quest_ids_given` checks each record's enabled state, but passes vacuously if the array is empty.**
  - Why it cannot catch a regression: if Trixi's `quest_ids_given` were emptied, the loop would not run and the "only Rush Order is live" rule would not be checked.
  - Fix: assert `quest_ids_given` is non-empty and contains `RUSH_ORDER` before the loop.
