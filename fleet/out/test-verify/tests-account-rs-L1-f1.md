<!-- fleet job=test-verify id=tests-account-rs-L1-f1 status=done turns=8 usd=0.0042 tokens(read,write,in,out)=[53221, 13859, 18, 3878] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/account.rs:377

**Verdict:** `confirmed`

**Evidence:** I tried to refute the claim by walking the test against the regression it names: `remove_character` removes the row before the owner check and then returns false.

- `tests/account.rs:427-432` checks only the reply: `rejected_delete.status == NotOwnedOrMissing` and `message_bytes[0] == 10`. Nothing reads the store for `foreign.guid` after the rejected call.
- `foreign` is used again only at line 451, `assert!(next.guid > foreign.guid)`. That compares a plain number taken from the earlier create reply, not store state. Guids come from a counter (`account_store.rs:334-344`, `next_character_guid`), not from the max existing guid, so removing the foreign row would not change `next.guid` and this assertion would still pass.
- Line 443, `store.character(owned.guid).is_none()`, covers only the owner's own delete.
- `session.selected_character()` and `session.account_id()` (lines 408-409, 422) do not depend on the foreign row.
- No other assertion in the test reads `store.character(foreign.guid)` or `store.account(owner_b)`. Nothing in the test checks `owner_b`'s `character_guids` either.

So the mutated `remove_character` (delete row, then return false on owner mismatch) passes every assertion in this test. The regression is visible through this test's own API, because `delete_character` is called directly on the `AccountStore` with no staging.

**Mitigating context (does not refute the test gap):** the production login path at `src/login.rs:463-468` runs the delete on `store.clone()` and commits only when the status is `Deleted`. So in the live gateway path, a non-`Deleted` result discards the mutated clone. The regression would still be real for the store API, and the test is the only one that exercises the non-owner delete directly. `tests/login.rs:344-357` only deletes the owner's own character (guid 2), so it does not catch this either.

**Minimal fix:** after line 432, add
`assert!(store.character(foreign.guid).is_some());`
`assert!(store.account(owner_b).unwrap().character_guids.contains(&foreign.guid));`
</result>
