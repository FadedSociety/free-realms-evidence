<!-- fleet job=bug-verify id=src-restoration-piece-083-rs-L1-f1 status=done turns=5 usd=0.0040 tokens(read,write,in,out)=[44103, 17697, 12, 2617] model=claude-haiku-5-5 -->
# medium: piece_083.rs:475-478

**Verdict:** refuted

**Severity if confirmed:** n/a

**Evidence:**

1. **Not in the real server.** `prototype/osfr-tools/src/restoration/piece_083.rs` is not in the module tree. `src/lib.rs` has no `restoration` or `piece_083` reference (search returned no matches). No `#[path]` in `src/` points at it; the only `#[path]` include is `tests/piece_083.rs:35-37` (`#[path = "../src/restoration/piece_083.rs"] mod piece_083;`). A search of `prototype/osfr-tools` for `piece_083` finds only that test include and comments inside the file itself. `ShopLedger`, `ShopCatalogue`, `PurchaseRequest` and `member_unit_price` appear nowhere else in `src/`. The defect is therefore test-only, and the production coin-store path does not use this code.

2. **The live path is a different function.** The live coin store is `src/coin_shop.rs` (`handle_coin_store` at line 402, reached from `npc_interaction.rs:574-605`). Its price code is at `coin_shop.rs:533-543`, which is a separate implementation. The claimed line numbers (475-478) do exist in piece_083.rs, but that file is not compiled into the server.

3. **Claimed mechanics checked.** The `checked_mul` → `InvalidQuantity` mapping at piece_083.rs:475-478 matches the claim. The reach argument is also accurate on its own terms: `parse` (line 120) takes `quantity` with no upper bound beyond `>= 1` (line 438). This does not rescue the finding, because the code it describes is not in the server.

Side note, not a confirmation: the live `coin_shop.rs:533-542` has the same shape. `checked_mul` failure returns `RESULT_INVALID_QUANTITY` rather than a balance refusal. A separate report against `coin_shop.rs` would need its own evidence, including whether `unit_price` can actually overflow on that path. The claimed defect as written, at piece_083.rs:475-478, should be dropped.</result>
