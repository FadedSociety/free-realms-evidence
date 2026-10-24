<!-- fleet job=test-verify id=tests-item-categories-rs-L1-f1 status=done turns=3 usd=0.0038 tokens(read,write,in,out)=[9667, 13299, 8, 4128] model=claude-haiku-5-5 -->
# high: tests/item_categories.rs:87

**Verdict:** `confirmed` (the regression-catching claim holds, but the claim's description of the current rejection path is inaccurate; see below).

**Evidence:**

- The test loop at `tests/item_categories.rs:88-101` asserts only `assert!(ItemCategories::load(&fixture.directory).is_err())`. It never inspects the error text, so any `Err` passes.
- `Fixture::new()` (lines 49-53) computes `packet_sha256` once over the original packet. `fixture.write()` (line 99) only rewrites the content, so the stale hash is kept for mutations 0-3 and 6.
- Walk-through with the named checks deleted from `src/item_categories.rs`:
  - Mutation 0 (`categories[1].id = 10`): with `!ids.insert(...)` removed (line 82), the duplicate row is serialized. The packet bytes differ from the original, so the check at line 125 (`differs from prepared proof`) returns `Err`. Test passes.
  - Mutation 1 (`groups[2].category_id = 10`): the `!pairs.insert` check (line 108) removed means an extra (8,10) row is emitted. The packet differs, so line 125 fires. Test passes.
  - Mutation 2 (`display = -1`): the `display < 0` check (line 81) removed. The serialized `-1` changes the packet, so line 125 fires. Test passes.
  - Mutation 3 (`groups[0].id = 0`): the `id <= 0` check (line 106) removed. The packet changes, so line 125 fires. Test passes.
  - Mutation 6 (`categories = []`): the `categories.is_empty()` check (line 67) removed. Group rows still reference categories, so the packet changes and line 125 fires. Test passes.
- So the row-validation checks at lines 66-111 are not exercised in any way that can fail this test. The claim's core point stands.
- Refutation attempts that failed: mutation 4 (proof-only) and mutation 5 (`schema_version = 2`, which the check at line 66 rejects, and which would otherwise pack an identical packet) are caught by the test as stated. Removing the hash check at line 125 would make mutations 0-3 and 6 return `Ok` and fail the test, so the hash-removal regression is caught. Nothing else in `repo` tests `ItemCategories::load` validation (grep of `ItemCategories|item_categories|invalid or duplicate|unsupported item category|differs from prepared proof`). The only other test in that file (the `#[ignore]`d oracle test) requires private content, so it cannot serve as a backstop.

**Inaccuracy in the claim:** The claim says mutations 0-3 and 6 are "rejected only by the stale `packet_sha256`". In the current code they are rejected earlier, by the validation checks (lines 84, 110 and 71/67). The hash is only the fallback that rejects once those checks are deleted. The conclusion is still correct, but the mechanism should be stated as "rejected by validation first; the hash masks the validation being removed."

**Minimal fix:** For mutations 0-3, assert `err.to_string().contains("invalid or duplicate item category")`. This also matches the group message at line 110, which contains that substring. For mutation 6, assert `contains("unsupported item category content")`. Keep mutation 4 asserting `contains("differs from prepared proof")`.
