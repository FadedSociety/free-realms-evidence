<!-- fleet job=test-audit id=tests-power-up-group-heal-rs-L1 status=done turns=4 usd=0.0024 tokens(read,write,in,out)=[10117, 5466, 10, 3230] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/power_up_group_heal.rs lines 1-83 of 83

Window: `prototype/osfr-tools/tests/power_up_group_heal.rs` lines 1-83. Code under test read: `prototype/osfr-tools/src/world.rs:875-886` (`claim_group_heal`) and the field at `world.rs:843`.

- **[medium] prototype/osfr-tools/tests/power_up_group_heal.rs:58-68 `a_picker_without_a_committed_place_claims_nothing` and :70-83 `the_memory_is_bounded` (with :13-32 `a_kill_gives_its_group_heal_once`) - nothing pins the documented 256-claim memory depth; the file passes with a 1-entry memory.**
  - Why it cannot catch a regression: `world.rs:881` could change from `>= 256` to `>= 1` (memory of one claim). Trace the file with that cap: in `a_kill_gives_its_group_heal_once`, (7,9) is stored, the repeat (7,9) is still refused, then (7,10) evicts it and (8,9) is accepted, so every assertion holds. In `the_same_kill_id_in_two_instances...`, the duplicate in the child is still refused because it is the immediately preceding claim. In `the_memory_is_bounded`, the 300 filler claims evict (7,9), so the final `Some(0)` still holds. The doc comment at `world.rs:874` ("The last 256 claims are remembered") is therefore unverified by any test.
  - Fix: add a test that performs 255 distinct claims after `(7,9)` and asserts `claim_group_heal(101, (7, 9))` is still `None` (remembered), then one more distinct claim (256 total after it) and asserts `Some(0)` (forgotten). This pins both edges of the window, so a cap of 1, 10, or 512 fails.

- **[low] prototype/osfr-tools/tests/power_up_group_heal.rs:75 `the_memory_is_bounded` - the filler count 300 is an unexplained magic number tied to the hidden 256 cap.**
  - Why it is churn-prone: the test only needs "more than the cap" filler, but it does not say so. Raising the cap above 300 makes it fail for a reason the name does not suggest, and lowering it changes nothing.
  - Fix: name the cap as a shared constant exposed by `world.rs` (or state in a comment that 300 must exceed it) and derive the filler count from it, e.g. `CAP + 1`, together with the edge test above.

No `#[ignore]`, early-return skips, or `is_ok()`-only assertions were found in this window. The `join` helper and the other assertions read the state they name, and the child-instance test does exercise a different instance from the one where the first claim was made.
