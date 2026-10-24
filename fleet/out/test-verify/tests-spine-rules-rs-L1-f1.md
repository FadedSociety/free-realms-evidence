<!-- fleet job=test-verify id=tests-spine-rules-rs-L1-f1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[20963, 14728, 10, 2962] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/spine_rules.rs:130

**Verdict:** `confirmed`

**Evidence:** I could not refute the claim. The test reads the ceilings only from the working-tree file and never compares them to any baseline.

- `tests/spine_rules.rs:130-139` reads `tests/spine_rules.ceilings` straight from disk into `ceilings`. Nothing is compared to `git show HEAD:...`, a checked-in copy, or a pinned hash.
- `:141-145` checks only that the key sets match. `:149-158` fails only if `values[key] > ceilings[key]`. Both checks take the ceiling as given, so raising a ceiling passes.
- Walk-through of the claimed change: set `hub:src/gameplay.rs 5700` in `spine_rules.ceilings` (current value 5515, `ceilings:7`), and add about 100 lines so the measured value is about 5615. The key sets still match, `5615 > 5700` is false, the `over` list is empty, and the test passes.
- The only other write path is `:159-176`, which runs only when `SPINE_RATCHET_LOWER` is set. It lowers values and never checks for upward edits, so it cannot block a raise.
- The "builders may not edit this file" rule appears only as a comment (`spine_rules.ceilings:2`) and in the notes. I found no check for it in `repo` outside `notes/`. `integrate.sh` is not in `repo`, so I could not verify any enforcement there.
- The test's name, `spine_rules_only_ratchet_down`, and its doc comment (`:1-2`) overstate what it checks. It enforces "values ≤ file", not "ceilings only go down".

**Minimal fix:** add a baseline check in `spine_rules_only_ratchet_down`, for example: `let base = git show HEAD:prototype/osfr-tools/tests/spine_rules.ceilings` (skipping 999999 entries), then `assert!(ceilings[k] <= base[k])` for each key. Alternatively, pin `sha256(spine_rules.ceilings)` in the test so any edit forces a deliberate update. Either way, rename the test if this is not added.
