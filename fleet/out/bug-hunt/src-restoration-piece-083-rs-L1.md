<!-- fleet job=bug-hunt id=src-restoration-piece-083-rs-L1 status=done turns=5 usd=0.0107 tokens(read,write,in,out)=[54892, 28648, 12, 13228] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_083.rs lines 1-549 of 549

Window `prototype/osfr-tools/src/restoration/piece_083.rs` 1-549 read in full. The parse path (120-139) is bounds-safe, the staged-commit path (495-539) is atomic (persist failure leaves `self` untouched, and every early return happens before `*self = staged`), and the quantity/stock/tint/member checks are ordered as documented. The findings below are the ones I could tie to lines. There is no production caller of `ShopLedger::purchase` in `src/` yet (only `tests/piece_083.rs`), so reach is stated as the intended client path.

- **[medium] piece_083.rs:475-478 - A total price that overflows `u32` is refused as result 4 (invalid quantity) instead of result 7 (balance not enough).**
  - Failure scenario: a catalogue row has `cost = 2_000_000_000` (accepted by `from_json`, which only rejects `cost > i32::MAX`), `max_per_order` unset, and no stock limit. The client requests quantity 3. `unit_price.checked_mul(3)` returns `None`, so the code returns `Refusal::InvalidQuantity`, which maps to result 4. The character cannot afford 6e9 coins, so the correct answer is 7. The comment at line 469 says "7 when short". The client gets the wrong refusal and message.
  - Reach: `PurchaseRequest::parse` (piece_083.rs:120) takes `quantity` from the packet with no upper bound beyond `>= 1`. The catalogue row comes from the server's own JSON via `from_json` (190-227). Nothing upstream prevents the overflow.
  - Fix: on `checked_mul` `None`, return `refused(Refusal::BalanceNotEnough { required: u32::MAX, available: balance })`, or compute the total as `u64` and compare it with `balance` before narrowing.

- **[medium] piece_083.rs:375-386 (called from 463-466) - `owned()` sums stack counts in `u32` with unchecked `.sum()`, so it panics in debug builds and wraps in release builds.**
  - Failure scenario: stacks are per (definition, tint) and `owned()` sums across all tints and all merchants. The client buys one definition from an uncapped row (`owned_limit` unset, `max_per_order` unset, unlimited stock, cost 0 or cheap) with quantity 2_147_483_647 and tint 0, then again with tint 1, then with tint 2. The per-stack counts are each valid `u32`, and their sum exceeds `u32::MAX`. The next purchase of that definition from a row with `owned_limit = Some(_)` calls `owned()` at line 464. In debug that panics on a client-controlled request. In release the sum wraps to a small value, so the cap check at 465 passes and the client gains units past the cap.
  - Reach: `parse` (120-139) → `purchase` step 6 (463-464). The only checks on quantity are `max_per_order` and stock, and both are absent on the uncapped row. Nothing bounds the sum.
  - Fix: accumulate with `u64` (`.map(|s| u64::from(s.count)).sum::<u64>()`) and compare that against `u64::from(limit)`, or use `checked_add` and treat overflow as a refusal.

- **[low] piece_083.rs:453 and 498-537 - A tintable row accepts any non-negative tint, and every new tint creates a new stack and transaction record with no cap, so a zero-cost tintable row lets one client grow the ledger without limit.**
  - Failure scenario: `from_json` (211-214) does not reject `cost == 0`. For a tintable row with cost 0, the client sends purchases with tint 0, 1, 2, … each for quantity 1. Each one passes the balance check (0 >= 0), pushes a new `OwnedStack` (506-510) and a `TransactionRecord` (523-537), and the whole ledger is cloned (495) and persisted (538). Memory and save size grow with every packet, and the cost of each request grows with the ledger. Only the i32 id ceiling (486-491) stops it, after about 2^31 records.
  - Reach: `parse` → `purchase` step 4 (453). Tint is checked only for `>= 0` on tintable rows. Nothing caps distinct stacks or per-character transactions.
  - Fix: reject `cost == 0` for purchasable rows in `from_json`, and/or cap the number of distinct stacks and the transaction log per character before the commit.

- **[low] piece_083.rs:367-369 - `ShopLedger::credit` overwrites the coin balance instead of adding to it.**
  - Failure scenario: a caller in the lead-owned economy layer that grants 500 coins to a character holding 1000 leaves them with 500. The name and the "lead-owned economy layer" comment both suggest additive semantics. The tests at 240, 269, 285 and 321 use it as a set, so this may be intentional. There is no production caller, so the impact is latent.
  - Reach: none in `src/` today. The API is `pub`.
  - Fix: either rename to `set_coins`, or make it `saturating_add` / `checked_add` if the intent is a grant.
