<!-- fleet job=bug-hunt id=src-gameplay-w95-vendor-coin-store-regressions-rs-L1 status=nothing_found turns=5 usd=0.0024 tokens(read,write,in,out)=[25063, 10270, 12, 1647] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/w95_vendor_coin_store_regressions.rs lines 1-175 of 175

No defects in `prototype/osfr-tools/src/gameplay/w95_vendor_coin_store_regressions.rs` lines 1-175.

Why nothing is reported:

- **The whole window is test-only code.** `prototype/osfr-tools/src/gameplay.rs:5459-5460` declares it as `#[cfg(test)] mod w95_vendor_coin_store_regressions;`. The only function is a `#[test]` marked `#[ignore]`, and the helpers (`reference`, `bundled_content`, `count_definition`) exist only for it. The task excludes `#[cfg(test)]` code, so none of the five defect classes apply.
- **Nothing in the window is reachable from a client packet or a save.** The `expect`/`unwrap` calls (lines 9, 27, 43-50, 54, 82, 141, 172-174) and the `price as u32` cast (line 74) act on local fixture files, a test-built `GameplayState`, or fixed-length slices. The client-shaped byte vectors (lines 93-107, 123-130, 151-158) are hand-built inputs to the production handlers, so they are the test's own inputs, not production trust issues.
- **The assertions match the code they test.** The coin and count arithmetic at lines 119-121, 142-143 and 172-174 is consistent with the purchase flow. The refusal path at lines 159-167 checks that state is unchanged, and that check is the regression guard it names. I found no assertion that contradicts its test name.

I did not read the production handlers (`Gameplay::handle_in_world`, `npc_interaction` buy/select, `inventory.grant`). They are outside this window, and the flagged risks would have to be found there, not in this file.
