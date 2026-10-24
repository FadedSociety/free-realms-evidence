<!-- fleet job=test-audit id=tests-blacksmith-first-order-rs-L1 status=done turns=10 usd=0.0131 tokens(read,write,in,out)=[264721, 41057, 22, 10537] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/blacksmith_first_order.rs lines 1-886 of 886

Window reviewed: `blacksmith_first_order.rs` lines 1-886 (with `support/npc_quest_chain.rs` helpers 385-684 and `common/gateway_vendor.rs` 85-125 read to confirm what the assertions check). No `#[ignore]`, no early-return skips (the fixture panics when reference content is missing, so it cannot pass silently). The refusal tests do compare full `GameplayState` before and after, and the buy/reward asserts use literal expected values, so I found no "cannot fail" tautologies in this window.

- **[medium] `prototype/osfr-tools/tests/blacksmith_first_order.rs:625` `refusals_and_reconnect_change_nothing` (reconnect section, 625-654) - the "reconnect" is an in-memory `game_as(CHARACTER + 7, Some(reconnect.state()))`, not a serialized save/load, and the comment's "still pays exactly once after the reload" is not checked by a replay.**
  - Why it cannot catch a regression: a change that drops a `#[serde(skip)]`-style field, or a pending offer/turn-in field, from `GameplayState` serialization would still pass, because the test never serializes. Likewise, a double payment on reload would not be caught, since the reward is asserted once and never replayed.
  - Fix: reconnect through `fixture.reload_serialized(&reconnect)` (the helper exists in `support/npc_quest_chain.rs:186`), then assert `counts`, inventory, and `pending_turnin`, and send `quest_end_reply(MERCHANDISE)` again via `assert_packet_refused_without_change` to pin "pays exactly once".

- **[medium] `prototype/osfr-tools/tests/blacksmith_first_order.rs:337-338` `the_supply_visit_and_the_vendor_purchase_pay_once` - the comment says "A locked profile is refused by the reward path", but the body only switches to Brawler (which is unlocked in the fixture, line 82) and never exercises a locked-profile refusal.**
  - Why it cannot catch a regression: if the reward path stopped checking the unlock for profile 16, or refused it, nothing here would notice; the test passes for either behaviour as long as the Brawler switch succeeds and XP lands on 16.
  - Fix: either delete the "locked profile is refused" claim from the comment, or add a case that makes profile 16 locked before turn-in and asserts the 49/13 reward is refused with coins and profile XP unchanged.

- **[low] `prototype/osfr-tools/tests/blacksmith_first_order.rs:257` `smitty_offers_the_merchandise_lesson_only_to_blacksmiths` - `menu_option(&menu, LEARN_BLACKSMITH_LABEL);` discards its result, so the line is only a panic-on-absent presence check with no comment saying what it asserts.**
  - Why it cannot catch a regression: a change that re-labels or removes the Blacksmith option would either panic with an unclear message or, if the label is silently present on the Adventurer menu, pass with no assertion about the option's offer state.
  - Fix: bind it and assert the intent explicitly, e.g. `assert!(menu_option_bytes_exists(...))` with a message "Adventurer sees the Learn Blacksmith option", or drop the line and keep only the 49/1 absence check at 258-264.

- **[low] `prototype/osfr-tools/tests/blacksmith_first_order.rs:331` `bruno_sells_exactly_the_three_recovered_components` (and the 66/42 list check at 332-335) - exact ordered `vec![WOODEN_PLANKS, THORNY_FASTENERS, SINGING_COAL]` and `json!([55, 56, 879])` pin the row order, which is incidental to the requirement "exactly these three components".**
  - Why it cannot catch a regression: nothing about the sale is broken by a reorder, so this only causes churn when the vendor list is re-sorted; conversely, it does not check the set beyond what the BTreeSet check at line 757 already does.
  - Fix: compare as sets (`BTreeSet`, as at line 756) for the "exactly three" claim, and keep one ordered check only where the client reader order is the thing under test.</result>
</invoke>
