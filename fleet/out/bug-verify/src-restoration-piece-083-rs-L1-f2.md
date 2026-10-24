<!-- fleet job=bug-verify id=src-restoration-piece-083-rs-L1-f2 status=done turns=5 usd=0.0051 tokens(read,write,in,out)=[54146, 26953, 12, 2387] model=claude-haiku-5-5 -->
# medium: piece_083.rs:375-386

**Verdict:** refuted

**Severity if confirmed:** n/a (the code is not in the shipped server)

**Evidence:**

1. **Module tree (decisive).** `piece_083.rs` is not declared by any `mod` in `src/lib.rs`, `src/bin/*.rs` or any `mod.rs`. The only file that includes it is the test target: `prototype/osfr-tools/tests/piece_083.rs:35-37` (`#[path = "../src/restoration/piece_083.rs"] mod piece_083;`). A repo-wide search for `piece_083`, `ShopLedger`, `PurchaseRequest` and `purchase(` finds no use outside that test and the file itself (plus a comment in `piece_084.rs`). `piece_084` has its own `record_purchase`, not this code. So `owned()` (375-386) and `purchase()` (415-548) are test-only and cannot be reached by a remote client.

2. **The live coin-store path is different.** `src/coin_shop.rs:402-413` dispatches family 165 sub-opcode 4 (length 28) to `buy_with_merchant(...)`, not to `ShopLedger::purchase`. The live path does not call `parse` at 120-139 or `owned()` at 375. (I did not audit the live path's own cap logic; that is outside this claim.)

3. **The claimed reach also misreads the code.** The per-stack write at 502 already uses `checked_add` and refuses on overflow, and the cap check at 465 already uses `u64` arithmetic (`u64::from(owned) + u64::from(quantity) > u64::from(limit)`). The only unchecked sum is inside `owned()`, which is a real but test-only concern. The claim's "panics in debug / wraps in release" describes the test-only helper, not server behaviour.

Conclusion: the defect does not exist in the real server. At most it is a latent arithmetic hygiene issue in a test-included reference module, which is not a defect a remote player can trigger.
