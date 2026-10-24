<!-- fleet job=test-audit id=tests-medic-level-five-chapter-rs-L1 status=done turns=9 usd=0.0113 tokens(read,write,in,out)=[199344, 37804, 20, 9236] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/medic_level_five_chapter.rs lines 1-1200 of 1236

Window reviewed: `tests/medic_level_five_chapter.rs` lines 1-1200 (helpers in `tests/support/npc_quest_chain.rs` and `medic_entry.rs` checked where the window depends on them). Most assertions are sound: the offer/refusal helpers compare full `GameplayState` and save bytes, the Surgical Precision record (3090008, giver Gordon, `enabled: false`) is genuinely reachable by the Gordon Talk path, the 425 XP total is an explicit 400 + `LEVEL_XP` (25), and the i32::MAX wallet cap matches `inventory.rs:855`. Two findings:

- **[medium] tests/medic_level_five_chapter.rs:816-832 refusals_and_reconnect_change_nothing - the comment says a duplicate Talk "only re-sends the held end screen", but nothing checks that a 49/13 end screen is re-sent.**
  - Why it cannot catch a regression: a change that makes the duplicate Talk drop the held end screen (no 49/13 in `duplicate.replies`) and still leaves state and save untouched would still pass; the test only asserts `!duplicate.changed`, the unchanged state and save, and the pending turn-in.
  - Fix: after `let duplicate = talk(...)`, assert `duplicate.replies.iter().any(|p| has_family(p, 49, 13, Some(PILLS)))`, and assert the re-sent end screen's actor and end text with the same checks `release_end_screen` uses (bytes 6..14 and 18..22).

- **[low] tests/medic_level_five_chapter.rs:1111-1115 and 1141-1145 a_failing_quest_event_for_one_player_does_not_stop_the_other - the wallet and profile refusals assert only `failed.is_err()`, not which error was raised.**
  - Why it cannot catch a regression: a turn-in that now fails for an unrelated reason (for example a missing end screen or a binding error on the patched state) still satisfies `is_err()`, so the test would pass without the cap being what refused it. The later state and save equality checks still hold in that case.
  - Fix: match the error text or variant for the wallet cap and the profile XP cap (or assert the same refusal on an unpatched control state) so each refusal is tied to its cap.

Not reported: the window's second-player completion assertions after line 1200 were not read, so the claim in `a_failing_quest_event_for_one_player_does_not_stop_the_other` that the other player completes is only partly checked here.
