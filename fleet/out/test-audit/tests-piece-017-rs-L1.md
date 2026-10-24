<!-- fleet job=test-audit id=tests-piece-017-rs-L1 status=done turns=4 usd=0.0050 tokens(read,write,in,out)=[18162, 12109, 10, 6635] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_017.rs lines 1-230 of 230

Window: `prototype/osfr-tools/tests/piece_017.rs` lines 1-230. I read the code under test (`src/restoration/piece_017.rs`, all 207 lines). Most tests are sound: `audit_recovery` runs `reject_active_runs` before `audit_conservation`, so the rejection tests fail for the reason their names give. Each in-window test was checked against that code. The findings below are the ones that survived that check.

- **[medium] prototype/osfr-tools/tests/piece_017.rs:184-210 private_forging_abandon_restart_pair_conserves_materials - the comment says the test stops "a rewritten evidence file" from passing silently, but it is `#[ignore]`d and its fixture directory is absent.** `lab()` resolves to `<repo>/lab`, and `list` on that path returns "not a directory". The default gate never runs this test, and `--ignored` runs panic on `unwrap` rather than checking anything. The ignore reason is present, so this is a skip the gate cannot see, not a silent pass.
  - Why it cannot catch a regression: nothing runs it in the merge gate. A change to the forging recovery logic, or a rewritten capture, goes unnoticed unless someone runs the ignored tests by hand, and those runs fail for lack of files.
  - Fix: add a committed, non-ignored fixture pair under `tests/` that is derived from the same JSON shape (the `state()` helper already builds it), and assert `audit_recovery` plus the `expected["gameplay"] == after["gameplay"]` comparison on it. Keep the private lab test only as an optional extra.

- **[low] prototype/osfr-tools/tests/piece_017.rs:180 conservation_accepts_a_fresh_attempt_replacing_a_stale_offer - the recovery half uses only `is_err()`, so it passes for any error.** `audit_recovery` fails here because `reject_active_runs` finds the surviving run 46000002. A regression that makes it fail for an unrelated reason (for example, a quest or counter check) would still pass.
  - Why it cannot catch a regression: `is_err()` does not identify which check fired.
  - Fix: `assert!(audit_recovery(&before, &after).unwrap_err().contains("cooking run 46000002 (Playing) survived"));`

- **[low] prototype/osfr-tools/tests/piece_017.rs:99 and :112 conservation_rejects_lost_materials / conservation_rejects_a_cancel_reward - the checks are substring matches on bare numbers ("2862", "35").** The code's messages are `definition {} tint {} count {} -> {}`, so the match happens to hit the definition id. A short id like "35" would match in many messages if one were ever added.
  - Why it cannot catch a regression: the match ignores whether the error names the right item and direction, so a message that merely includes those digits still passes.
  - Fix: assert the full message, for example `contains("definition 2862 tint 229 count 4 -> 3")` and `contains("definition 35 tint 229 count 0 -> 1")`.

- **[low] prototype/osfr-tools/tests/piece_017.rs:229 private_cooking_native_midround_disconnect_conserves_materials - the coins value 110 is hard-coded from the fixture.** The `audit_conservation` call already requires before and after coins to match, so this line only restates a fixture constant.
  - Why it cannot catch a regression: it adds no check beyond the audit, and it breaks on any legitimate fixture refresh.
  - Fix: compare `after` coins to `before` coins, or drop the line.

No `cannot fail` findings. Every in-window test has an assertion that a plausible code change would break.
