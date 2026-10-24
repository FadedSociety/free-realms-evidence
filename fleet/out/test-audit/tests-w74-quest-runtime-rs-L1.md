<!-- fleet job=test-audit id=tests-w74-quest-runtime-rs-L1 status=done turns=5 usd=0.0038 tokens(read,write,in,out)=[29554, 14057, 12, 3427] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/w74_quest_runtime.rs lines 1-175 of 175

Window reviewed: `prototype/osfr-tools/tests/w74_quest_runtime.rs` lines 1-175. Two findings, both in the final stretch of the one test.

- **[medium] prototype/osfr-tools/tests/w74_quest_runtime.rs:174 saved_regional_quest_syncs_on_world_entry_and_bad_application_messages_are_dropped - the last assertion is a bare `is_ok()` on an unrelated npc_interaction message (26/4), with no check on the reply or state.**
  - Why it cannot catch a regression: the gateway routes 26/4 to `npc_interaction` (src/gateway.rs:494), so any change to that handler, or any change that makes `handle` return `Ok` with a rejected/empty outcome, still passes. The line also passes the raw `[26, 0, 4, 0]` without the `application(...)` framing that every other message in the test uses (lines 117, 127, 150), so the call may be rejected for framing reasons rather than exercising the handler. Either way it asserts nothing about quests or about the test's name.
  - Fix: either delete the line, or replace it with a check that the outcome is what you intend, e.g. wrap the body with `application(...)`, then assert the returned outcome has no gameplay change (`!outcome.gameplay_changed`) and that `snapshot().gameplay.npc_quests` is unchanged from the value at line 172. If the intent was "npc_interaction still answers", assert a specific reply family/subtype instead of `is_ok()`.

- **[low] prototype/osfr-tools/tests/w74_quest_runtime.rs:117-124 saved_regional_quest_syncs_on_world_entry_and_bad_application_messages_are_dropped - the malformed 49/2 case checks only the trace entry, not that the message produced no replies or changed no state.**
  - Why it cannot catch a regression: the `trace.iter().any(...)` check passes if a rejection trace is recorded even when the gateway also emits a reply packet or mutates quest state. Only the unknown-subtype case (lines 135-146) checks `pending_turnin`, and neither case checks the reply list. The test name says bad messages are "dropped", which implies no effect.
  - Fix: after each rejected `handle`, assert `rejected.replies.is_empty()` (or that it has no quest-family reply) and compare `snapshot().gameplay.npc_quests` against the pre-message state, not only `pending_turnin`.

Not reported: the `#[ignore]` at line 55 has a reason, and the test does not early-return on a missing fixture. The private `lab/references` paths resolve outside the repo, so the test is skipped on the integrator by design; that is a coverage gap for the gate, not a silent pass.
