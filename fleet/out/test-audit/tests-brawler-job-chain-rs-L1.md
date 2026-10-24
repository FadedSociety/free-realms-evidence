<!-- fleet job=test-audit id=tests-brawler-job-chain-rs-L1 status=done turns=10 usd=0.0167 tokens(read,write,in,out)=[275859, 44746, 22, 16609] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/brawler_job_chain.rs lines 1-1200 of 2139

Window reviewed: `brawler_job_chain.rs` lines 1-1200. Two findings. Most of the window is sound: the fixtures exist, the gating helpers are real, and the shared-view replay test (1092-1148) is valid because `append_pending_turnin_screen` only replays when the batch carries the actor's 35/2.

- **[medium] prototype/osfr-tools/tests/brawler_job_chain.rs:223-236 assert_refusal_changes_nothing - the helper checks only `outcome.changed` and the serialized state, never the refusal's replies or outbound packets, so a refused turn-in that still re-sends a 49/4 completion or a 49/13 end screen passes.**
  - Why it cannot catch a regression: a change that keeps `changed == false` and the state equal but still emits `[49,0,4,0]` or a 49/13 for an already-completed or wrong-actor turn-in would pass every call site: "duplicate C3 turn-in" (870-876), "wrong pending turn-in" (957-963), "duplicate reward before reload" (981-987) and "duplicate reward after reload" (994-1000). The client would still see a second completion screen.
  - Fix: in the helper, assert that `outcome.replies` contains no `[49,0,4,0]` and no `[49,0,13,0]` (or that the outbound set is empty), in the same way the 1151 test already checks `refused.outbound.is_empty()`.

- **[low] prototype/osfr-tools/tests/brawler_job_chain.rs:1194-1200 carlos_to_jones_to_blackspore_completes_in_order - the name claims the order is enforced, but the body only checks final coins and statuses after `complete_chapter`, which runs the steps in a fixed sequence by construction (758-785).**
  - Why it cannot catch a regression: if the engine let C5 (`SEARCH_BLACKSPORE`) or C4 be offered before its prerequisite completed, the test's own fixed sequence would still reach the same end state and pass. Prerequisite denial is only tested for C6 and 3_030_005 in the separate 1151 test.
  - Fix: either rename the test to drop "in order", or add a refusal before each step (for example, `offer(SEARCH_BLACKSPORE, SABASTIAN)` before C4 completes must return `QuestDenial::Prerequisite` with no state change), so the ordering is actually exercised.
