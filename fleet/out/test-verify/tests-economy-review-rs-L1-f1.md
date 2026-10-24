<!-- fleet job=test-verify id=tests-economy-review-rs-L1-f1 status=done turns=4 usd=0.0041 tokens(read,write,in,out)=[21252, 16288, 10, 3756] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/economy_review.rs:286

**Verdict:** `refuted`

**Evidence:**

The claim names two regressions. The first is a change that stops persisting before the hand-out. The test catches that. The second is a rollback when the caller reports failure. No such path exists, and the claim's own reasoning does not show it is reachable.

1. **Stop-persisting regression is caught.** The test body (`tests/economy_review.rs:290-295`) is:
   ```rust
   let mut counter = InstanceCounter::open(&path, &[]).unwrap();
   let burned = counter.allocate().unwrap();
   assert_eq!(burned, 1);
   let mut reopened = InstanceCounter::open(&path, &[]).unwrap();
   assert_eq!(reopened.allocate().unwrap(), 2);
   ```
   `open` reads the document from disk (`piece_081.rs:106`). If `allocate` returned before writing, the file would not exist. `open` would then yield `FIRST_INSTANCE_ID = 1` (`piece_081.rs:108`, `:118`), and line 295 would fail with `1 != 2`. The reopen step is a durability check that runs before any grant, so the claim's requested "on-disk reads 6 before the grant" assertion adds nothing for this arm.

2. **Rollback-on-caller-failure is not a reachable regression in this code.** `allocate` (`piece_081.rs:140-146`) takes no grant result and returns only `Result<i32, CounterError>`. `grep` for `InstanceCounter`, `allocate_from_snapshot` and rollback/release across `prototype/osfr-tools` finds no caller that reports a grant failure back to the counter. The only production caller is `inventory.rs:1014`, and it uses `allocate_from_snapshot`, a different pure function. For a rollback to happen, someone would have to add a new method or change `allocate`'s signature. A signature change breaks the test's `assert_eq!(burned, 1)` at compile time. A new, separate method would be a new API that this test does not call, so the test would not catch it. That is a coverage gap for hypothetical code, not a defect in the code under review.

3. **Test name overstates coverage (non-blocking).** The name and comment at line 293 say "when the grant never lands", but the body does not model a failure. It only shows that an allocation followed by a reopen does not reuse the id. A rename, for example to `candidate_counter_burns_an_id_across_reopen`, or a comment noting that the grant is not simulated, would make the intent accurate. This does not make the claimed regression uncatchable.

The claim's specific code-change scenario (stop persisting before return) fails this test at line 295. The rollback scenario needs an API that does not exist. The claim is therefore refuted.
