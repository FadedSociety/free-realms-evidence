<!-- fleet job=test-verify id=tests-brawler-mongo-chain-rs-L1201-f1 status=done turns=6 usd=0.0035 tokens(read,write,in,out)=[35695, 11429, 14, 3469] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/brawler_mongo_chain.rs:1609

**Verdict:** `confirmed`

**Evidence:** The claim holds. Nothing in the test snapshots B's wallet before A's turn-in, and the only assertion on it compares B's value with itself.

- `brawler_mongo_chain.rs:1609-1613`: `assert_eq!(b.state().inventory.coins, coins(&b), "B's wallet is untouched by A's payouts")`. `coins` is `game.state().inventory.coins` (`support/npc_quest_chain.rs:583-585`), so both sides read the same field of the same session at the same moment. This assertion passes no matter what B's wallet does.
- No B snapshot exists. The only pre-payout read is `let before = economy(&a);` at line 1597, which reads A's session. A search of the test file finds no `saved(&b)`, `coins(&b)` or `economy(&b)` before line 1609. Nothing in the test before line 1609 captures B's wallet.
- No later assertion covers it. Lines 1615-1622 check B's gate, fight phase and Mongo health, and A's encounter. None of them checks coins.
- `finish_quest` (`support/npc_quest_chain.rs:529-557`) only checks A's `coins_before`/`coins(game)` and the XP on the session it is given (`a`). It never reads B.

Walk-through of the regression: a change that credits B's wallet on A's turn-in leaves B's `inventory.coins` changed. Both sides of line 1609 still read the same post-change value, so the assertion passes. The claimed defect stands.

**Minimal fix:** Before `finish_quest` (line 1599) add `let b_before = saved(&b);`. After line 1608 add `assert_eq!(saved(&b), b_before, "B's wallet is untouched by A's payouts");`. `saved` is already imported and serializes the whole `GameplayState`, so this also catches non-coin changes to B. Nothing ticks or acts on B between the snapshot and the assertion, so the equality is safe. A coins-only check, `assert_eq!(coins(&b), b_before_coins)`, also works but is weaker.
