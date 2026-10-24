<!-- fleet job=test-audit id=tests-scavenger-hunt-quest-rs-L1 status=done turns=10 usd=0.0129 tokens(read,write,in,out)=[244314, 50039, 22, 8365] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/scavenger_hunt_quest.rs lines 1-1200 of 1257

Reviewed `prototype/osfr-tools/tests/scavenger_hunt_quest.rs` lines 1-1200 (read through 1257 for the helpers' tail). Most tests here are sound: payouts compare whole state and save bytes, refusals snapshot state and bytes, and the content tests read the real JSON. I found three issues.

- **[medium] prototype/osfr-tools/tests/scavenger_hunt_quest.rs:915 the_hunt_identity_and_admin_script_are_recorded - the name says the admin script is recorded, but the body checks no script; the comment at 1074-1077 says it deliberately does not read it.**
  - Why it cannot catch a regression: the test passes if the operator broadcast script is deleted, changed, or never written. Its checks cover quest ids, the giver, the Adventurer job reference, the objective positions and provenance, and the reward. None of them touch a script.
  - Fix: rename it to match what it checks (for example `the_hunt_content_identity_is_recorded`). If the script is meant to be guarded, add an assertion on a content-side field rather than on note prose. Otherwise drop the name claim.

- **[medium] prototype/osfr-tools/tests/scavenger_hunt_quest.rs:841-845 and 868-872 an_over_cap_reward_is_refused_for_that_player_only - the over-cap refusal is checked only with `handle_in_world(...).is_err()`, so the test does not establish that the 50-coin cap is what refused it.**
  - Why it cannot catch a regression: any error on the 49/14 path passes these checks, including a missing pending turnin, a lost actor, or a broken reward lookup. The state and bytes comparisons and `pending_turnin == Some(QUEST)` would still hold, because nothing mutated. Removing the cap check alone would still fail, since the coin total would then exceed the cap and the call would succeed. But the test cannot tell cap refusals from any other refusal.
  - Fix: assert the error kind or message that the cap path produces (for example, that the error mentions the coin cap or is the specific reward-capacity error), and confirm the same error on the retry at 868-872. Alternatively, add a control turn-in for B at the same state that succeeds, so the failure is shown to be the cap.

- **[low] prototype/osfr-tools/tests/scavenger_hunt_quest.rs:258 the_four_stops_complete_and_pay_once - `assert_eq!(screen.len(), 99)` pins the exact byte length of the 49/13 end-screen packet, which the test is not about.**
  - Why it is churn, not a missed bug: the test is about the payout and the turn-in gate. Any unrelated change to the end-screen layout (for example, an added trailing field the client ignores) fails this line even though the payout is correct.
  - Fix: keep the two reward-value checks at 259-260, which are what the test is about, and check the packet's own shape with a per-field read under its reader (or assert the length only in the packet-shape test that owns it).
