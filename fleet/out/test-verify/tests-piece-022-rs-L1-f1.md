<!-- fleet job=test-verify id=tests-piece-022-rs-L1-f1 status=done turns=3 usd=0.0038 tokens(read,write,in,out)=[9969, 12833, 8, 4091] model=claude-haiku-5-5 -->
# high: tests/piece_022.rs:333

**Verdict:** `confirmed`, with one factual correction to the claim's reasoning.

**Evidence:**

- **Correction:** the claim says the body "depends only on" test-local constants. That is wrong. Line 336 `assert_eq!(HOUSING_FIXTURE_UPDATE, 40);` compares against the code-under-test constant imported at line 31 from `src/restoration/piece_022.rs:59`. So a change to that constant would fail this test. That is the only code under test the body touches.
- **The rest of the body is test-local.** Lines 337-342 slice `VEC_FIXTURE_UPDATE_PREFIX` and compare it with `FIXTURE_GUID` and `HOUSE_GUID`, which are constants in the test file (lines 63, 75). I checked the bytes by hand. `prefix[4..12]` is `01 c0 f5 7b a1 4c f5 07`, which is `0x07f54ca17bf5c001`, and `prefix[12..20]` is `da 10 2d b8 69 31 f5 07`, which is `573418857690894554`. The fixture-prefix layout matches the captured bytes.
- **No code path is exercised.** A grep for `fixture_update|FixtureUpdate|HOUSING_FIXTURE_UPDATE` in `src/restoration/piece_022.rs` finds only the constant at line 59. There is no encoder, decoder, or router code there that handles fixtures. The test never constructs `HousingEntranceRouter`, never calls `register_house`, `enter`, or `decode_enter_request`, and never reads the stored house record.
- **Named regression passes.** If the router stopped binding fixtures to the entered house, or the enter path stored a different guid, every assertion here still holds. Only a change to the constant `40` or to the test's own hex/constants would fail it. Neither is the regression named in the test name. So the central claim holds: the test cannot catch a fixture-to-house binding regression.
- The function name and the header comment on lines 334-335 ("the house guid is the same instance identity the enter request named") overstate what is checked. The body only checks a captured byte layout.

**Minimal fix:** either rename the test to `captured_fixture_update_prefix_layout` and drop the "bind" wording, or add a real check. For the real check, call the router's enter path after `register_house(captured_house())`, then assert the stored house guid equals `HOUSE_GUID` and that the fixture update carries that same guid. For example: `assert_eq!(router.enter(...).house_guid, u64::from_le_bytes(prefix[12..20].try_into().unwrap()))`. Exact method names should be checked against the router API before use.
