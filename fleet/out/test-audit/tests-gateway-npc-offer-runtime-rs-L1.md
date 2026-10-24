<!-- fleet job=test-audit id=tests-gateway-npc-offer-runtime-rs-L1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[17632, 13659, 10, 3146] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/gateway_npc_offer_runtime.rs lines 1-324 of 324

Window reviewed: `prototype/osfr-tools/tests/gateway_npc_offer_runtime.rs` lines 1-324. The test is `#[ignore]`d with a reason, and a missing fixture panics rather than returning early, so it is not a silent skip. The final assertion does touch the claimed behaviour, so the findings below are about how much of the claim it actually checks.

- **[medium] tests/gateway_npc_offer_runtime.rs:320 account_store_gateway_talk_to_samantha_sends_quest_offer - the test only checks that some 49/1 family packet arrived; it never checks which quest is offered.**
  - Why it cannot catch a regression: the server could send a 49/1 offer for the wrong quest id, a stale quest, or a placeholder offer body, and `families.contains(&(49, 1))` still passes. Only the 2-byte family header of each reply is inspected (`family()` at line 103), so the offer payload is never looked at.
  - Fix: decode the 49/1 body with `npc_interaction::decode_quest_offer_49_1` (src/npc_interaction.rs:1263), which the sibling test `native_save_samantha_uses_localized_quest_offer_and_reply_state` in src/gameplay/w64_regional_quest_tests.rs:1169 already does, and assert the quest id and intro fields match the fixture's expected Samantha quest.

- **[medium] tests/gateway_npc_offer_runtime.rs:298-302 account_store_gateway_talk_to_samantha_sends_quest_offer - the "sole Talk choice" is checked only by the option count, not by what the option is.**
  - Why it cannot catch a regression: a menu with one option of any type or label passes `option_count == 1`. The test then sends `npc_select(SAMANTHA_GUID, 1)` (line 312) without checking that option id 1 is the Talk entry. If the server changed the option id to 0 or 2, the failure would only show up as a missing 49/1, not as the menu change that caused it, and a single non-Talk option would still pass the menu assertion.
  - Fix: parse the 26/9 option entries (the option id and label/type fields that follow the count at byte 13) and assert that the sole entry is the Talk option with the id the test then selects, so the select value comes from the menu rather than being hard-coded.

- **[low] tests/gateway_npc_offer_runtime.rs:139 send_application - `let _ = sender.acknowledge(&packet);` discards the error from acknowledging the server's ACKs.**
  - Why it cannot catch a regression: if the reliable-layer ACK handling starts failing, the send path keeps going, the window stays full, and the test sees only the missing replies later, or none, with no pointer to the ACK failure.
  - Fix: `sender.acknowledge(&packet).unwrap()`, or assert on its result, so an ACK failure fails the test at the point it happens.
