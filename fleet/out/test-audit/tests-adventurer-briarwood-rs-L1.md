<!-- fleet job=test-audit id=tests-adventurer-briarwood-rs-L1 status=done turns=6 usd=0.0084 tokens(read,write,in,out)=[84114, 30865, 14, 7357] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/adventurer_briarwood.rs lines 1-963 of 963

Window reviewed: `prototype/osfr-tools/tests/adventurer_briarwood.rs` lines 1-963. Most of the chain is well pinned: the record fields are checked against the authored JSON rather than against the code's output, the save/reload and "replayed 49/14 pays nothing" checks compare full serialized state and bytes, and the overflow refusal checks coins, XP, items and status. The findings below are the weak spots.

- **[medium] tests/adventurer_briarwood.rs:911 the_chapter_uses_no_dev_commands_and_leaves_the_character_free - the name claims "no dev commands", but the only check is that no reply starts with the teleport prefix `[38, 0, 12, 0]`.**
  - Why it cannot catch a regression: the test never sends a chat or dev command, and `complete_rumors` only drives the production quest and menu packets. A change that routes the chapter through a realm-coins or realm-level handler (the `realm coins` / `realm level` commands named in the comment at 921-922) would still pass, as long as the coin and XP totals come out the same and no reply has the teleport prefix.
  - Fix: either rename the test to "the chapter sends no teleport packet", or assert that no dev-command path is reached, for example by checking that the chapter's replies contain only 49/x, 26/x and 45/x families, and that profile and coin totals match the content reward exactly.

- **[medium] tests/adventurer_briarwood.rs:848 the_briarwood_scout_... / a_wrong_position_or_npc_or_forged_turn_in_changes_nothing (near-cap block) - `let _ = capped.handle_in_world(...)` discards the `io::Result` from `handle_in_world` (src/gameplay.rs:2169).**
  - Why it cannot catch a regression: a change that makes the overflowing turn-in return `Err` (an io error that the server would surface as a failure) instead of a clean refusal still passes. The state assertions at 849-866 would also pass, because an error that leaves state untouched looks the same as a refusal. The test cannot tell "refused cleanly" from "errored".
  - Fix: bind the result and assert it is `Ok`, then assert that the outcome has no 49/3 or 49/4 completion reply and no 49/14 success reply. Then keep the existing state checks.

- **[medium] tests/adventurer_briarwood.rs:875-907 two_players_each_own_the_chain - B is created with `completed(OTHER, &[])`, so the negative check at 898-905 is blocked by B's missing E4 prerequisite, not by isolation between players.**
  - Why it cannot catch a regression: if A's quest state leaked into B's save, B would still not be offered E5, because B lacks E4. The test also never checks that B's own first offer (MISSING_SISTERS at 898) produces a 49/1, so it does not show that B has a working chain at all. The `assert_unchanged(&b, &b_before)` at 883 is the only check that can catch leakage.
  - Fix: give B `chapter_prerequisites(OTHER)` and run the chain, or at least assert that B's own offer packet for MISSING_SISTERS is present. Then assert that E5 is offered to B only after B completes E4, and that B's payout is separate from A's.

- **[low] tests/adventurer_briarwood.rs:368-384 rumors_of_briarwood_is_offered_after_thugamugs_thievery - the comment says "Geoffrey's next tell is E4 itself", but the body only asserts that RUMORS is absent.**
  - Why it cannot catch a regression: a change that makes Geoffrey tell nothing, or tell something else, still passes.
  - Fix: assert that `offered.replies` contains a 49/1 for `THIEVERY` (`has_family(packet, 49, 1, Some(THIEVERY))`), so the comment matches a checked fact.
