<!-- fleet job=test-verify id=tests-login-rs-L1-f1 status=done turns=4 usd=0.0056 tokens(read,write,in,out)=[17204, 12165, 10, 7775] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/login.rs:632

**Verdict:** `refuted` (as a claim that the test cannot catch the regression it names). The vacuous assertion itself is real.

**Evidence:**

- The first-pass observation about line 632 is correct. `"old-head-long.adr"` is 17 bytes (o-l-d-`-`-h-e-a-d-`-`-l-o-n-g-`.`-a-d-r). `changed.windows(16)` yields 16-byte slices, and `&[u8] == &[u8; 17]` compares lengths, so `!changed.windows(16).any(|x| x == b"old-head-long.adr")` is always true. That line is dead and should be fixed (e.g. `windows(17)`).

- The test still catches the regression. Walk-through for the regression "patch_self keeps the old head bytes and does not drop the original head field" (the natural form: the old head string is copied through and the new one is written in front of it, or the old one is not skipped):
  - Line 620 `patch_self(&old, ...)` succeeds. The output is `[model][string("head.adr")][string("old-head-long.adr")][string("old-hair.adr")]...`.
  - Lines 621 to 628 (tail and both length prefixes) still pass, since the regression keeps the lengths consistent.
  - Line 630: `identity::patch_self(&changed, &sample()).unwrap()` is re-parsed. `src/identity.rs:364-368` reads head = "head.adr", then the second string = "old-head-long.adr", then `r.take(8)`, which consumes the `[12,0,0,0]` length of "old-hair.adr" plus `"old-"`. The next `r.string(512)` reads `"hair"` as an i32 of 0x72696168, which exceeds the bound of 512 and returns `Err("login string exceeds bound")`. The `.unwrap()` panics, so the test fails.
  - Line 631 `windows(8)` would also fail for the variant that drops the new head: `"head.adr"` never occurs in `"old-head-long.adr"`, `"old-hair.adr"`, or `sample()`'s other values.

- Remaining gap, which is a test-quality hole, not a refutation: a regression that injects a copy of the old head into the unowned 44-byte gap (`identity.rs:400`) would survive, because the parser ignores that gap, the tail check at 621 only covers the last 104 bytes, and line 632 is vacuous. That is contrived for the regression named, so I do not treat it as the claimed defect.

**Minimal fix** (recommended, not required for the verdict): change line 632 to `assert!(!changed.windows(b"old-head-long.adr".len()).any(|x| x == b"old-head-long.adr"));`, and optionally add `assert!(changed.len() + 0 == old.len() - (17 - 8))`-style length-delta check, since the head shrinks from 17 to 8 bytes.
