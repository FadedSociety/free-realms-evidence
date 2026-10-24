<!-- fleet job=test-audit id=tests-brawler-job-chain-rs-L1201 status=done turns=14 usd=0.0190 tokens(read,write,in,out)=[411005, 51179, 30, 17011] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/brawler_job_chain.rs lines 1201-2139 of 2139

Reviewed `prototype/osfr-tools/tests/brawler_job_chain.rs` lines 1201-2139 in full, plus the helpers they call (lines 46-800) and `tests/support/terrain.rs`. Most of the window is sound: the refusal tests compare the full `saved()` state, the replay and reload checks are real, and `talk`/`interact_npc` panic when the menu or dialogue is missing, so the `let _ =` calls are guarded. Two findings:

- **[medium] prototype/osfr-tools/tests/brawler_job_chain.rs:1612 the_reward_goes_to_profile_43_after_a_job_switch - the name says the reward is paid after a job switch, but the body never performs one.**
  - Why it cannot catch a regression: the body calls `with_active_job` (line 1620), which seeds the saved active profile to Adventurer through `seed_active_profile`. No 26/13 switch packet is sent, and the helper comment at 1618 says so. A regression in the real job-switch path (26/13 handling, or the switch resetting or rebinding the reward profile) would still pass this test.
  - Fix: either rename it to something like `the_reward_goes_to_profile_43_when_the_active_profile_is_adventurer`, or drive a real 26/13 switch to Adventurer, which needs an outfit that the captured opening inventory lacks, and assert that the 26/13 reply and the active-profile change happen before the turn-in. Then keep the XP asserts at lines 1628-1637.

- **[low] prototype/osfr-tools/tests/brawler_job_chain.rs:2083 the_spawn_and_content_are_reachable - the `disc.len() == 105` assert checks the shared support helper's own sample count, not anything about Petra's spawn ground.**
  - Why it cannot catch a regression: a change to Petra's spawn position, terrain, or slope would not move this count. The count only changes if `tests/support/terrain.rs::disc_points` changes, and that case is already the helper's own concern. The ring loop at lines 2093-2103 also repeats the 5 m ring samples that `disc` already includes (lines 2085-2089).
  - Fix: drop the exact count, or keep only the slope and ground checks on the spawn disc (lines 2084-2092) and the ring-ground check, and add a separate assertion that the slope maximum is the value the spawn actually produces.

Nothing else in the window met the criteria. I found no `#[ignore]`, no early return on a missing fixture, and no unused snapshot (the `before_second` capture at line 1484 is compared at line 1496).
