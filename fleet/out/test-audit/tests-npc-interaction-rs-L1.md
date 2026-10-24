<!-- fleet job=test-audit id=tests-npc-interaction-rs-L1 status=done turns=6 usd=0.0083 tokens(read,write,in,out)=[99986, 31051, 14, 6877] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/npc_interaction.rs lines 1-1200 of 1213

Window: `prototype/osfr-tools/tests/npc_interaction.rs` lines 1-1200. I read the whole window, plus `tests/support/npc_quest_chain.rs` (the `accept`, `offer`, `talk`, `interact` helpers) and the `RESULT_SUCCESS` definition in `src/coin_shop.rs`. No test is outright unfailable: the expected values are literals or wire layouts, not outputs of the code under test. The findings below are the weak spots.

- **[medium] tests/npc_interaction.rs:1156 vendor_165_4_and_66_43_still_route - the refused 66/43 buy is checked only with `assert_ne!(status_dword, 1)`, which accepts any non-success code.**
  - Why it cannot catch a regression: the refusal could start reporting a different non-success status (for example a code meaning "sold out" or "unknown error") and the test would still pass. Nothing pins what a refusal reports. The comment on line 1140 says the status dword at offset 48 is `0`, but the code never checks that.
  - Fix: assert the exact refusal code the 66/44 writer emits for a non-stock item (the value at offset 48 is `0` per the comment), e.g. `assert_eq!(u32::from_le_bytes(status[48..52].try_into().unwrap()), 0)`, and compare it to the named constant if one exists.

- **[low] tests/npc_interaction.rs:1140-1155 vendor_165_4_and_66_43_still_route - "answers one 66/44 refusal" is checked on `.last()` only, so the test never counts replies.**
  - Why it cannot catch a regression: a change that sends an extra 66/44 (or a stray 66/x packet) before the refusal still passes, because only the last reply is inspected. The doc comment says "answers one 66/44 refusal", which this does not establish.
  - Fix: assert `refused.replies.len() == 1` (or count the packets starting with `[66, 0, 44, 0]` and assert the count is 1).

- **[low] tests/npc_interaction.rs:296-307 interaction_rejects_out_of_range_npc - only the just-out-of-range case is checked, with no in-range control in the same test.**
  - Why it cannot catch a regression: if `interact` returned `OutOfRange` for every position, this test would still pass. The same test has no proof that the boundary is at 12.0 rather than, say, 0 or 100.
  - Fix: add `assert!(service.interact(VENDOR_ID, zone, [position[0] + 11.99, position[1], position[2]], None).is_ok());` (and/or the exact position) before the 12.01 refusal, so the test pins the boundary from both sides.

- **[low] tests/npc_interaction.rs:136 vendor_menu_shop_buy_sell_and_close_use_coin_shop_validation - `window.items.len() == 1` pins the whole shipped stock count to a single item.**
  - Why it matters: this is incidental to the shop-path behavior the test is about (buy/sell/close validation). Adding a second stocked item to the vendor's content or to the `set_vendor_stock_items` mapping would break this test even though the buy/sell logic is unchanged. That is churn, not a missed bug.
  - Fix: assert that item 8 is present with the expected price (already on line 141), and drop the exact `len() == 1`, or assert `len() >= 1`.
