<!-- fleet job=test-audit id=tests-fishing-service-rs-L1 status=done turns=10 usd=0.0070 tokens(read,write,in,out)=[139491, 23625, 22, 5391] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/fishing_service.rs lines 1-332 of 332

Window reviewed: `prototype/osfr-tools/tests/fishing_service.rs` lines 1-332 (plus `tests/support/fishing_packets.rs`, `src/fishing_service.rs` 160-400 and 684-800, `src/fishing.rs` 284-335).

- **[high] prototype/osfr-tools/tests/fishing_service.rs:264 client_cannot_claim_a_catch_without_a_server_bite - the forged catch is rejected for an unrelated decode reason, so the "no server bite" guard is never exercised.**
  - Why it cannot catch a regression: `request(14, ...)` builds a sub-14 packet, and sub 14 is `Sub::Result`, a server-to-client packet. `ClientRequest::decode` (`src/fishing.rs:322`) hits `other => Err(Error::UnknownSub(14))` before `handle` reaches any bite/phase check. The `is_err()` therefore passes on any code that rejects sub 14, including a server that drops the bite check entirely. Only the reward-inventory check is left, and it is trivially true because no catch ever happened in this test.
  - Fix: send a well-formed reel (`reel_request()`, sub 7, flag 1) at a time before the bite (e.g. right after the cast at T0+1, with no `tick` to T0+1510). Assert the error is specifically `Error::OutOfOrder` (or whatever the no-bite guard returns). Also assert `service.phase(PLAYER)` and `service.run_state` are unchanged, and that a later legitimate bite/reel still works so the rejection is shown to be state-preserving.

- **[medium] prototype/osfr-tools/tests/fishing_service.rs:295 leave_despawns_schools_and_drops_attempt_without_reward - the name claims the attempt is dropped and no reward is granted, but the body checks neither.**
  - Why it cannot catch a regression: nothing asserts that the attempt was cleared (no `service.phase`/attempt check, no `run_state`), and the reward inventory is never read. `quest_events.is_empty()` and `len()==0` would still pass if `leave` granted an item into `RewardState` without emitting a quest event, or if the attempt survived in a separate map.
  - Fix: after `leave`, assert `service.reward_state(PLAYER)` is `None` or its inventory `items` is still empty, and assert the attempt is gone (for example, a second `handle(&cast_request(), ...)` returns `Err(OutOfOrder)` or `instance_id(PLAYER)` is `None`). Also assert the returned despawn replies carry the expected school ids, not just the count of `(138,12)`.

- **[low] prototype/osfr-tools/tests/fishing_service.rs:307 minigame_cancel_despawns_schools_and_drops_attempt_without_reward - same overclaim as above.**
  - Why: it never reads reward state or checks that a later cast/reel is refused, so a grant-on-cancel regression that emits no quest event passes.
  - Fix: add the same reward-inventory-empty check and a post-cancel `handle` rejection assertion.

- **[low] prototype/osfr-tools/tests/fishing_service.rs:282 disconnect_mid_fight_clears_ephemeral_state_without_grant - "without grant" is checked only via empty `quest_events`.**
  - Why: `src/fishing_service.rs:368` `disconnect` discards `runs.disconnect()` output and never touches rewards, so a regression that grants an item on disconnect would still pass this test unless it also emits quest events.
  - Fix: assert `service.reward_state(PLAYER)` is `None` (session gone) or that the inventory item list is unchanged after reconnect.

- **[low] prototype/osfr-tools/tests/fishing_service.rs:323 content_covers_six_areas_with_client_name_ids_and_reconstructed_tuning - over-pinned counts (`lures.len() == 13`, `sizes.len() == 4`) and a weak `contains("R:")` check on the timing source.**
  - Why: adding or correcting a lure row, which is unrelated content churn, breaks this test even though the test is about area count and client ids. `contains("R:")` is also satisfied by any string containing that substring.
  - Fix: drop the exact lure count (or assert `lures` is non-empty and every lure's `fish` keys resolve). Keep `validate_content()` and `area_count()==6`, and check the `timing.source` tag against the exact provenance value the content file uses.
