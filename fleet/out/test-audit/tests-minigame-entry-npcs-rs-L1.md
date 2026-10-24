<!-- fleet job=test-audit id=tests-minigame-entry-npcs-rs-L1 status=done turns=7 usd=0.0088 tokens(read,write,in,out)=[120311, 28263, 16, 8086] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/minigame_entry_npcs.rs lines 1-793 of 793

Window reviewed: `prototype/osfr-tools/tests/minigame_entry_npcs.rs` lines 1-793. Most tests are sound: the gateway tests drive the real 26/8 -> 26/10 path, the dormant derby test (732) checks loader outcomes and save bytes, and the kart/derby drawable checks compare against emitted `NpcVisibility` actors. The findings below are the weaker spots.

- **[medium] tests/minigame_entry_npcs.rs:486 the_race_choice_shares_the_account_action_budget - the name claims a shared account budget, but the body only exercises one `ActionBudgets` bucket with one 26/10 payload.**
  - Why it cannot catch a regression: `ActionBudgets` is keyed by account and checked per family. If 26/10 were given its own bucket, or if other budgeted families stopped drawing from the shared one, this test would still see 10 allowed and then a refusal. It never mixes in another family and never goes through `Gateway`.
  - Fix: on the same `PLAYER`, interleave a different budgeted request (for example a 15/1 chat or 40/x packet from the `src/social_chat.rs:68-78` list) after some 26/10 calls. Assert it is refused once the shared allowance is spent. Ideally also run the 26/10 choice through `Gateway`, as `gateway.rs:1577-1585` does.

- **[medium] tests/minigame_entry_npcs.rs:448 the_shipped_package_offers_from_every_gate - the name says every driver's menu offers the derby, but no driver is clicked and no 26/9 menu is read.**
  - Why it cannot catch a regression: the test only checks `DerbyGateway::load` output and `set_derby_gates(...).is_empty()`. Both are already covered by 414. If the menu builder dropped MAD_JACK, CRASH, BURT or RIP, or never published 3053, this test would still pass. The only real-gateway derby offer check (683) uses MAD_JACK alone.
  - Fix: loop over `[MAD_JACK, CRASH, BURT, RIP]`, create a gateway at `npc_position(driver)` with the derby package written, call `click`, and assert `menu_option(&menu, 3053).is_some()`. Optionally follow with a `choose` and assert a 39/16 reply.

- **[low] tests/minigame_entry_npcs.rs:683 the_derby_driver_offers_the_derby_when_a_package_exists - "a live derby is not entered twice" never checks that a derby is live before the second selection.**
  - Why it cannot catch a regression: after the first `choose`, the test checks only `gameplay_changed` and a 39/16 packet. The second `handle_at` is compared with the saved bytes. If the first start left no derby state, or if the menu was simply closed, the second attempt would still leave the save unchanged, so the "not entered twice" claim goes untested.
  - Fix: after the first start, assert `gameplay.derby.is_some()` (or the derby's active/entry flag). Then assert that the replayed 26/10 returns no change and no second 39/16 offer, so both the live state and the refusal are checked.

- **[low] tests/minigame_entry_npcs.rs:564-570 the_wildwood_driver_offers_and_starts_the_kart_race_for_two_players - the close assertion is an OR that is almost always true.**
  - Why it cannot catch a regression: `closed.state_changed || !closed.replies.is_empty()` passes if any reply comes back, even one that does not close the race. The later `active.is_none()` check does catch a missed close, but this line adds little and its message ("must be accepted") does not match what is checked.
  - Fix: assert the specific outcome, for example `closed.state_changed` together with `after.kart_entry.active.is_none()`, or the expected 39/ or 41/ close reply, and drop the `||`.

- **[low] tests/minigame_entry_npcs.rs:640, 652, 720 - `let _ = gateway.handle_at(...)` discards errors on the refused and forged paths.**
  - Why it cannot catch a regression: a forged or ineligible choice that starts returning `Err` (for example a disconnect or a parser failure) passes silently, as long as the save bytes are unchanged. The refused paths in 774-776 use `choose(...).unwrap()` and so do not have this gap.
  - Fix: use `choose(...)` (which unwraps) or `.expect("refusal is reported, not an error")` in these three places, so an unexpected error fails the test.
