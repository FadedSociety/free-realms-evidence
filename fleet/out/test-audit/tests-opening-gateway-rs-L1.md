<!-- fleet job=test-audit id=tests-opening-gateway-rs-L1 status=done turns=9 usd=0.0079 tokens(read,write,in,out)=[119415, 25945, 20, 6885] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/opening_gateway.rs lines 1-372 of 372

Window reviewed: `prototype/osfr-tools/tests/opening_gateway.rs` lines 1-372. The single test (`private_all_opening_actions_dungeon_return_and_restarts`, line 112) is `#[ignore]`d with a stated reason, so it is not a silent skip. Its helpers and most assertions do check real state: snapshot equality after refused remote interactions (138, 214), phase "won" (174-190), stage completion (356-360), and no double-credit of discoveries via the final snapshot comparison (363-371, which holds because `opening.rs:729` only credits on `insert`). Those are sound. Three weaker spots:

- **[medium] tests/opening_gateway.rs:197-198 private_all_opening_actions_dungeon_return_and_restarts - the magic-door check `assert_eq!(g.state().zone_id, 0)` has no pre-door assertion that the player is somewhere other than zone 0.**
  - Why it cannot catch a regression: if the restart (line 192) already leaves the character in zone 0, or if the `[26, 0, 42, 0]` packet is ignored, the zone is 0 either way and the assertion passes. `gateway.rs:509` shows the packet is matched on `(26, 42)`, but nothing in the test proves the door changes anything.
  - Fix: assert `zone_id != 0` (or the dungeon zone id) immediately after `restart` and before the door packet at line 197. Then assert the door moves it to 0.

- **[medium] tests/opening_gateway.rs:191-196 and 208-221 private_all_opening_actions_dungeon_return_and_restarts - coin checks compare two balances without proving a reward was ever paid.**
  - Why it cannot catch a regression: `coins` is read before and after `restart` and compared, and again around the return. If the dungeon reward and the shop path never credit coins, the balance stays at its starting value and every equality still holds. Coin persistence is therefore never shown to be exercised.
  - Fix: after the win (line 189), assert that coins increased by the dungeon's expected reward from `encounters.json` (or from the reward table in content). Then assert that value survives `restart` (line 193-196).

- **[low] tests/opening_gateway.rs:131 private_all_opening_actions_dungeon_return_and_restarts - the starting inventory is pinned to an exact count of 7.**
  - Why it cannot catch a regression: this is about login and the starting inventory, not the opening flow. Any unrelated change to starting items fails here, which causes churn without testing the behaviour the test is named for.
  - Fix: assert the specific starting item(s) this flow depends on (by definition id from the content), or drop the count and rely on the later checks.
