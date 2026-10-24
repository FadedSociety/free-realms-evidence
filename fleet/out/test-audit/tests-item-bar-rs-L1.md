<!-- fleet job=test-audit id=tests-item-bar-rs-L1 status=done turns=11 usd=0.0133 tokens(read,write,in,out)=[259799, 37498, 24, 12117] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/item_bar.rs lines 1-761 of 761

Window: `prototype/osfr-tools/tests/item_bar.rs` lines 1-761. Code under test read: `src/item_bar.rs` (handle, assign, check, confirm, activate, consume, usable, cooldown_left, slot_update, refresh, load) and `src/restoration/piece_048.rs` (ActionBarState::validate, ITEM_BAR_SLOTS = 4). No `#[ignore]`, no early-return skips, and no expected value derived from the code under test in this window. Most assertions are real: the recast boundary (1000/10000 blocks, 11000 ready), the backwards clock (`checked_sub` makes it ready), the pending-check/confirm pairing (the 42/15 replay needs a new check), and `bar == before` for refused assignments.

- **[low] tests/item_bar.rs:493-499 bar_use_refusals_spend_nothing_and_each_has_a_canary - the name and the header (line 3, "Every refusal has a canary") claim a canary per refusal, but there is one shared canary after the loop.**
  - Why it cannot catch a regression: a change that makes one refusal case succeed is still caught by `is_ability_failure` plus the potion/Medium counts in the loop, so no regression is missed here. The gap is that the name promises more than the body does. A refusal that is wrongly refused for a different reason (say, the ground-target parse) is covered only by the generic cast(0) canary, which does not share that request's shape.
  - Fix: either rename it (for example `bar_use_refusals_spend_nothing_and_the_plain_request_still_works`) or give each refusal a paired request that differs from it by only the one missing fact, asserting it heals.

- **[low] tests/item_bar.rs:589-590 the_bar_persists_and_runtime_state_does_not - the comment says "An empty bar adds nothing to be saved", but the body only asserts `is_empty()`.**
  - Why it cannot catch a regression: the serialized form of an empty bar (`{"bar":{"version":…,"bindings":[]}}`) is never compared, so a change that adds a field to the saved empty bar would still pass.
  - Fix: assert the serialized empty bar equals the expected empty-state JSON, or, if the claim is only about bindings, change the comment to say so.

Checked and not reported: the "five bindings" tamper case is rejected by the count check in `validate` (piece_048.rs:603) before the duplicate-slot check, so it does exercise the five-binding bound. The `ITEM_BAR_SLOTS == 4` assertion at line 759 is a legitimate pin to the recovered constant, not a tautology.
