<!-- fleet job=test-audit id=tests-investigate-the-wolves-rs-L1 status=done turns=7 usd=0.0104 tokens(read,write,in,out)=[125706, 37883, 16, 8732] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/investigate_the_wolves.rs lines 1-1200 of 1379

Window reviewed: `prototype/osfr-tools/tests/investigate_the_wolves.rs` lines 1-1200. Most tests here compare saved state before and after, or check against authored content, so they can fail. The findings below are the ones that hold up.

- **[medium] prototype/osfr-tools/tests/investigate_the_wolves.rs:439 anne_offers_investigate_the_wolves_and_accepts_it - the doc says the quest has "no prerequisite and no job gate", but the body never checks either.**
  - Why it cannot catch a regression: the body only runs `accept_at_anne` (49/1 ids, Active, objective 0) and a no-offer Talk. A change that adds a `prerequisite_quest_ids` entry or a `job` key to the quest record would still pass, because nothing in this test reads the record. The record-level checks sit in a different test (around lines 1216-1220, outside this window).
  - Fix: in this test, load `data/content/quests/adventurer.json`, find record 3000061, and assert `prerequisite_quest_ids == []` and `record.get("job").is_none()`. Alternatively, drop "no prerequisite and no job gate" from the doc and point it at the record test.

- **[low] prototype/osfr-tools/tests/investigate_the_wolves.rs:1137 a_mining_movie_refuses_the_talk_until_it_closes - the doc says the busy rules are "mutual", but the body only checks one direction.**
  - Why it cannot catch a regression: the test shows that a Talk is refused while the mining movie is active. It never checks that the quest Talk, or any other interaction, blocks the start of a mining movie. A change that lets `realm mine` start during a dialogue or turn-in would still pass.
  - Fix: either narrow the doc to "a Talk is refused while the mining movie is active", or add the reverse check: while the Anne end screen is pending, `realm mine` must be refused with no state change.

- **[low] prototype/osfr-tools/tests/investigate_the_wolves.rs:408 open_end_screen - `end.len() == 99` pins the whole 49/13 bundle size, which is a byte count that is incidental to what the helper is for.**
  - Why it cannot catch a regression: it is not wrong for the client layout, but the helper is shared by six tests about turn-in, reload and refusal. A field that is added after the coins (for example a trailing float) would fail all of them even though none of them is about the layout. That is churn, not a missed bug.
  - Fix: keep the field-level checks at 14, 18 and `end_screen_reward`. Move the exact length to the one reader test that owns the 49/13 layout, or assert `end.len() >= 35` with the field offsets above.
