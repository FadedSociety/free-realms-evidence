<!-- fleet job=test-verify id=tests-s6-characterization-rs-L1-f1 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[19428, 12193, 10, 2896] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/s6_characterization.rs:635

**Verdict:** `confirmed`

**Evidence:**
- `tests/s6_characterization.rs:635-660` (`reward_count_excludes_rented_items`) builds an `InventoryState` by hand (one owned stack, count 5; one rented stack, count 3) and asserts only `assert_eq!(count_definition_owned(&state, 21785), 5);` (line 659).
- `count_definition_owned` is the file-local helper at lines 40-47. It is the only thing called. It filters `item.rental.is_none()` and sums counts. No `osfr_tools` production function is invoked: the file's only `osfr_tools` imports are `account_store::AccountRole`, `gateway::{Gateway, GatewayOutcome}`, and `inventory::{InventoryItem, InventoryState, RentalState}` (lines 26-30), and none of them is called by this test.
- The production filters the claim names exist: `src/gameplay/crafting.rs:329` (`material_count`) and `:500` (`consume_materials`), both `item.rental.is_none()`. Also `src/gameplay.rs:1471` and `src/coin_shop.rs:770`. Changing any of them to count rented stacks would leave this test green, because nothing in the test reads them.
- I grepped `#[test]` and `#[ignore` in the file. Line 634 is the only non-ignored test, so the claim's "only test that runs on the integrator" is also accurate.
- No assertion in the test would fail under a production regression. The test is a tautology against a copy of the rule. The claim holds.

**Minimal fix:** Replace the local helper with a production call and assert on it. `material_count` (`crafting.rs:324`) is `pub(super)`, so an integration test in `tests/` cannot reach it. The canary therefore has to live in-crate: a `#[cfg(test)]` unit test next to `crafting.rs` that builds a `Gameplay` with one owned and one rented stack of 21785 and asserts `material_count(21785) == 5`. I did not verify that `Gameplay` can be constructed without the private content. If it cannot, the fallback is to delete the test, since the ignored packet-path tests are the only real coverage. The claim's suggested route through `gathering_payout.rs` was not checked for visibility.
