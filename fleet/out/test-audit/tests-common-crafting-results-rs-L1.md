<!-- fleet job=test-audit id=tests-common-crafting-results-rs-L1 status=nothing_found turns=4 usd=0.0020 tokens(read,write,in,out)=[12273, 8328, 10, 1647] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/crafting_results.rs lines 1-20 of 20

No findings in `prototype/osfr-tools/tests/common/crafting_results.rs` lines 1-20.

This window holds two helpers, not tests. It has no `#[test]` functions, no assertions, and no `#[ignore]` or early-return skips, so none of the five categories applies to the lines themselves.

- `vector(name)` (lines 1-13) loads `fixtures/native-crafting-results-community-vectors.json`. The fixture exists, and the `cooking_*`, `forging_*` and `smelting_*` keys that callers use are present (checked at lines 9-19 of the fixture). Expected bytes come from the captured fixture, not from the code under test, so they are not circular. A missing key panics through `unwrap()`, so it fails loudly rather than passing.
- `ack(id)` (lines 14-20) builds the expected 3-word ack frame in the test. It is an independent oracle, not a restatement of production code. Its callers are `cooking.rs:424`, `forging.rs:309` and `smelting.rs:142`, and those tests are outside this window.

One minor robustness point, which I do not rate as a finding: `chunks_exact(2)` silently drops a trailing odd hex nibble. A malformed fixture string would therefore be truncated, not rejected. No current fixture value is odd-length, so this cannot hide a failure today.
