<!-- fleet job=test-audit id=tests-derby-route-rs-L1 status=done turns=7 usd=0.0091 tokens(read,write,in,out)=[129214, 35018, 16, 6773] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/derby_route.rs lines 1-1200 of 1651

Window reviewed: `prototype/osfr-tools/tests/derby_route.rs` lines 1-1200. Read the test bodies in full, plus `derby_gateway.rs` (cancel, close, take_completion, completion_grant) to confirm behaviour. The fixture-skip paths are fine: `GameplayFixture::build` asserts the content directory exists rather than returning early, and no `#[ignore]` appears in the window. The `[50, 0, 1]` reward-bundle check at line 1109 matches the opcode family documented in `kart_rewards.rs`, so it is not vacuous.

- **[medium] prototype/osfr-tools/tests/derby_route.rs:653 offer_cancel_and_running_quit_retire_without_rewards_and_stale_quit_is_inert - the name promises "without rewards", but the body never checks a reward, ledger, or completion value.**
  - Why it cannot catch a regression: the test only checks the `[39,0,19]` packets, `active()`, `phase()`, and `close()`. It never calls `take_completion()` or inspects `paid_matches`/`saved_state()`. A change that let a cancelled or quit match reach `take_completion() == Some(instance)` (for example, by leaving the service in `Results` on quit, or by not removing it on cancel) would still pass, because `derby_gateway.rs:448` is only consulted by code this test never calls.
  - Fix: after the cancel and quit paths, assert `gateway.take_completion().is_none()` and `gateway.saved_state().is_none()`. Also keep the existing packet checks.

- **[medium] prototype/osfr-tools/tests/derby_route.rs:1063 gameplay_routes_the_npc_offer_and_closes_a_fabricated_contact_without_paying - the doc says the fabricated contact "damages the NPC", but the body only asserts `!contact.replies.is_empty()`.**
  - Why it cannot catch a regression: any packet in the reply, such as an unrelated ack, satisfies the check. The contact could be dropped with no damage applied and the test still passes. The coin, derby, and reward checks only prove that no payout happened.
  - Fix: decode the `contact.replies` (or read the match state through the existing derby accessors) and assert that the NPC's health dropped by the expected contact damage (`contact_damage_per_unit * impact`, with the 5.0 impact used here). Alternatively, delete "damages the NPC" from the doc.

- **[low] prototype/osfr-tools/tests/derby_route.rs:862 a_t023_save_keeps_the_temporary_job_when_the_previous_job_is_locked - the doc says the load "logs the skip", and nothing checks that.**
  - Why it cannot catch a regression: the logging claim has no assertion, so a change that drops the log line passes. The last assertion (line 904, `any(job != DEMO_DERBY_DRIVER_PROFILE)`) is satisfied by any unlocked job, including the job that was active before the match, so it does not check the repair.
  - Fix: either remove "logs the skip" from the doc, or capture the log output and assert on it. Tighten line 904 to name the expected unlocked job (the pre-match active profile) rather than "any non-demo job".

- **[low] prototype/osfr-tools/tests/derby_route.rs:1159 gameplay_routes_the_offer_pays_one_completion_and_ignores_replays (entry-outfit check) - the expected bytes are cut with a hard-coded trailer length, `entry_switch[12..entry_switch.len() - 4]`.**
  - Why it cannot catch a regression: this is not a logic hole, but it pins an incidental trailer width. Any unrelated change to the 35/0/7 packet's trailing fields breaks the test without touching the outfit behaviour. It also compares against `profile_attachments`, the same source the packet is built from.
  - Fix: locate the outfit by its prefix and length (for example, `entry_switch[12..12 + driver_outfit.len()] == driver_outfit`), and assert the packet's total length against a named constant rather than deriving it from the slice end.
