<!-- fleet job=test-audit id=tests-support-wizard-entry-rs-L1 status=nothing_found turns=8 usd=0.0054 tokens(read,write,in,out)=[78733, 17540, 18, 4747] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/support/wizard_entry.rs lines 1-174 of 174

Reviewed `prototype/osfr-tools/tests/support/wizard_entry.rs` lines 1-174. No finding meets the five categories.

What I checked:
- **Byte offsets in `assert_reward_rows` (147-174) and the reward-bundle layout.** I read `encode_quest_reward_bundle` (`src/quest_engine.rs:2940-2984`) and `quest_end_packet` (`src/quest_engine.rs:1278-1300`). Success byte at 26, coins at 27..31, stars at 31..35, reward display source GUID at 63..71, player GUID at 71..79, and name id at 83..87 all match the production writer. The expected quest title comes from the hand-written `quest_title` map (109-116), not from the code under test.
- **Expected values.** `REWARD_COINS` (5), `REWARD_XP` (25), `FIZZLESTICKS`, and the per-quest title IDs are literals, so the reward assertions are not derived from production output.
- **`release_wizard_end_screen` (121-143).** It delegates the actor and end-text checks to the shared `release_end_screen` (`tests/support/npc_quest_chain.rs:483-509`), which asserts them against literal expectations. It adds the animation-dword and reward-row checks itself, so it does assert something.
- **`offered_card` (91-107).** It asserts the decoded quest id against the requested id. The redundant check against `offer`'s own assertion is harmless.
- **Fixtures and skips.** There are no `#[ignore]` attributes, no early returns, and no missing-fixture passes in this window.

Non-blocking note (not reported as a finding): the doc comment on `wizard_state` (line 59) says only profile 12 is unlocked, but the body also unlocks `BRAWLER`. This is a comment-accuracy issue and cannot cause a false pass.
