<!-- fleet job=test-audit id=tests-kart-rewards-rs-L1 status=done turns=6 usd=0.0072 tokens(read,write,in,out)=[73693, 26987, 14, 6100] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_rewards.rs lines 1-642 of 642

Window reviewed: `prototype/osfr-tools/tests/kart_rewards.rs` lines 1-642, checked against `src/kart_rewards.rs` (validate, `claim_race_reward`, `reward_bundle_toast`) and `src/kart_racing.rs` (`claim_reward` / `RewardAlreadyClaimed`, `placement: None` at 602). Most tests are sound: the expected values are literals or registry constants that the production code does not compute from itself, the rollback tests compare live state, and the restart test is meaningful because the snapshot carries `reward_claimed`. The findings are below.

- **[medium] kart_rewards.rs:243 a_finished_registered_race_pays_once_with_real_coins_xp_and_the_recovered_toast - the name promises the recovered toast, but the body (lines 251-277) never inspects `payout.replies`.**
  - Why it cannot catch a regression: `claim_race_reward` could drop the `reward_bundle_toast` push at `src/kart_rewards.rs:328-331`, or emit a 50/0 instead of 50/1, and this test would still pass. Coins and XP are checked, but nothing about the reply packets is.
  - Fix: add `assert_eq!(payout.replies.len(), 3)` and `assert_eq!(&payout.replies.last().unwrap()[..3], &[50, 0, REWARD_SUBTYPE_BUNDLE])`, or rename the test to drop "the_recovered_toast". The toast detail is already covered by `the_payout_emits_the_recovered_38_and_50_replies` at line 589, so the rename is the cheaper option.

- **[low] kart_rewards.rs:276 a_finished_registered_race_pays_once_with_real_coins_xp_and_the_recovered_toast - `assert_eq!(result.placement, None)` pins a placeholder.**
  - Why it cannot catch a regression: it is not a regression check. `kart_racing.rs:426-427` and `:602` say placement is always `None` until server-wide state exists. The test therefore locks in the unimplemented behaviour, and the day placement is implemented this payout test fails for an unrelated reason.
  - Fix: remove the line, or move it into a racing-level test that is explicitly about the placeholder.

- **[low] kart_rewards.rs:557 the_starter_registration_is_reconstructed_complete_and_validated - `assert_eq!(registry.rows().count(), 5)` pins the table size.**
  - Why it cannot catch a regression: the test is about the rows being valid and labelled. Adding or removing a starter speedway, or a correct content-row swap, fails it with no bug present. The per-row checks at 558-566 already cover validity.
  - Fix: assert that every speedway in the recovered set (31, 32, 33, 34, 39) has a registration, using `registry.registration(id).is_some()`, instead of the count. Or drop the count.

No other findings in this window. Cases checked and passing: the `#[ignore]` and early-return skip checks found nothing; `serialized_restart` and `forged_or_unfinished` assert real state; the overflow rollback tests compare live inventory and profile state.
