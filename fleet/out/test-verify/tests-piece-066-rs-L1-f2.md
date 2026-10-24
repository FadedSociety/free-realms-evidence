<!-- fleet job=test-verify id=tests-piece-066-rs-L1-f2 status=done turns=7 usd=0.0065 tokens(read,write,in,out)=[80018, 22620, 16, 5741] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_066.rs:224

**Verdict:** `confirmed`. I could not refute it. The test does pin the truncated token, and it would fail on a correct data fix.

**Evidence:**

- The test asserts `"unresolved wiki prerequisite \"Quest:Learn\""` at `tests/piece_066.rs:224`. The validator formats `"unresolved wiki prerequisite \"{}\" on {}"` (`src/restoration/piece_066.rs:653-656`), so the warning exists today only because the stored prerequisite is the truncated `"Quest:Learn"`.
- The source data confirms the truncation. `notes/Research/original-quest-coverage.json:1401-1404` has `"prerequisites": ["Quest:Learn"]` on `Quest:Your First Weapon`, while `"previous"` on the same row is `"Quest:Learn to Mine & Smelt Ore"`. `CATALOGUE_RELATIVE_PATH` (`piece_066.rs:40`) points at this file.
- Walk-through of the fix. Extract the full prerequisite, so `prerequisites` becomes `"Quest:Learn to Mine & Smelt Ore"`. Then `prerequisite_links()` yields the full token. In `validate()`, `chain` includes `previous` values (`piece_066.rs:634-637`), so `chain.contains(...)` is true and no warning is pushed. The `joined.contains("unresolved wiki prerequisite \"Quest:Learn\"")` check at line 224 is then false, and the test fails. The `errors.is_empty()` check at line 212 is unaffected, which is why the failure is misattributed to a "gap" check.
- The first-pass review missed a second truncated pin. `tests/piece_066.rs:339-341` asserts `link.prerequisite == "Quest:Your"`, a truncation of `"Quest:Your First Weapon"`. That assertion also fails on a correct fix.
- The dispatch ledger already records this defect (`notes/Reviews/MMO Dispatch Ledger.json:181`: "catalogue wiki prerequisites truncated ('Quest:Learn' / 'Quest:Your') - file outside 066 paths, repair falls to lead").

**Minimal fix:** Pin the full tokens, not the warning. Replace line 224 with `assert!(links.iter().any(|l| l.page == "Quest:Your First Weapon" && l.prerequisite == "Quest:Learn to Mine & Smelt Ore"))`, and change line 340 to `"Quest:Your First Weapon"`. Remove the `Quest:Learn` entry from the expected-warning list. Note that the claim's suggested "warning set is empty" assertion would fail today, because `Quest:Learn` and `Quest:Your` both still warn. The suite will be red until the lead repairs the JSON, which is the correct signal for this defect.
