<!-- fleet job=test-audit id=tests-harvesting-runtime-border-rs-L1 status=done turns=10 usd=0.0092 tokens(read,write,in,out)=[123665, 27786, 22, 8979] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/harvesting_runtime_border.rs lines 1-205 of 205

Window reviewed: `prototype/osfr-tools/tests/harvesting_runtime_border.rs` 1-205. The three refusal cases are sound: I checked them against `validate_border` (harvesting.rs:1300-1320) and the call site (gameplay.rs:1011-1014). Each case has a playable code 1 on an edge axis (index 0, row 0, or column 0), so the gate refuses them and they fail if the gate is removed or narrowed to index 0 only. The padded, legacy and mining cases are real load assertions, not skips. The findings below are the gaps I could confirm.

- **[medium] harvesting_runtime_border.rs:107-109 / 145-180 `unpadded_eight_kind_export_is_refused_without_mutation` - the edge-axis dropzone exemption (`code != SHAPE_DROPZONE` in harvesting.rs:1312) is never tested in isolation.**
  - Why it cannot catch a regression: a change that rejects code 4 on row 0 or column 0 still passes. Case 1 is refused anyway because of its row-0 `1`s (index 0 is `1`). Case 2 and case 3 contain only `0` and `1` on their edges. The padded writer output puts its dropzone at row `border+playable_rows` and columns `border..`, so it never sits on an edge (x=0 or y=0) and the padded test does not exercise the exemption either.
  - Fix: add a case with a valid border shape whose edge cell is `4` (for example, the padded document with a dropzone code written at column 0 or row 0, with no `1` on that edge), and assert it loads. Alternatively, assert `validate_border` directly on a shape whose only edge code is `4`.

- **[low] harvesting_runtime_border.rs:15 and 118-132 `expect_refused` - the "byte-identical tree" claim covers only top-level files.**
  - `tree_fingerprint` (lines 52-66) skips every directory (`continue` at line 57), so any write a refused `Gameplay::load` makes into a subdirectory is invisible to the fingerprint. The doc comment says "a refusal must leave the tree byte-identical", and line 130 asserts "must not mutate the save or content", which overclaims for nested paths. I did not verify whether `Gameplay::load` writes into subdirectories.
  - Why it cannot catch a regression: a refusal that writes a repair or quarantine file under a subdirectory passes.
  - Fix: recurse into subdirectories in `tree_fingerprint` (keyed by relative path) so nested writes change the fingerprint.

- **[low] harvesting_runtime_border.rs:118-126 `expect_refused` - the refusal match is a bare substring `"border"`.**
  - The check `error.to_string().contains("border")` would accept any error whose text includes "border", not only the `harvesting border gate:` prefix from gameplay.rs:1014. It does not check which cell or which gate refused.
  - Why it cannot catch a regression: a different error that happens to mention "border" passes, and so does a refusal of the right kind that comes from another gate with that word in it.
  - Fix: match the full prefix `"harvesting border gate:"` and, for each case, the cell coordinate the validator reports (for example `(x 0, y 0)`, `(x 1, y 0)`, `(x 0, y 1)`).

- **[low] harvesting_runtime_border.rs:135 `unpadded_eight_kind_export_is_refused_without_mutation` - the name overclaims.**
  - Only the first block is an eight-kind export. The row-0 and column-0 blocks (lines 145-180) use only codes 0 and 1 and do not test eight kinds.
  - Why it cannot catch a regression: a reader relying on the name would believe the eight-kind tile set is covered on the border path, but nothing in the other two blocks checks it.
  - Fix: split into separate tests with names that match their bodies (for example `unpadded_eight_kind_export_is_refused`, `row_zero_playable_is_refused`, `column_zero_playable_is_refused`), or rename this one to describe all three cases.
