<!-- fleet job=test-audit id=tests-titles-claims-rs-L1 status=done turns=6 usd=0.0095 tokens(read,write,in,out)=[92434, 30226, 14, 9562] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/titles_claims.rs lines 1-942 of 942

Window reviewed: `prototype/osfr-tools/tests/titles_claims.rs` lines 1-942 (read in full). Code under test checked: `progression_extras.rs` (`definition_blob` at 1342-1362, claim/definitions path at 1300-1340, `MAX_CLAIM_ITEMS` at 30). No `#[ignore]` or silent early `return` exists in the file. `Fixture::new` asserts loudly if the `lab/` content fixture is missing (the `lab/` directory is absent from this checkout, so these tests will panic here rather than pass). That is a loud failure, not a silent skip, so it is not reported.

- **[medium] tests/titles_claims.rs:576 definitions_before_claim_use_pending_contents_without_consuming_them - the comment at 567-568 says each path "must receive its own complete definitions response", but the body is only checked as a 9-byte header prefix; the blob is never decoded.**
  - Why it cannot catch a regression: the server can return a truncated, empty, or wrong-length 108/6 body (wrong declared length, missing or extra definition rows, trailing bytes) after the first nine bytes, and this test still passes. It also never checks which definition ids are described. The sibling test at line 633 does decode the whole body, so this is a gap, not a design choice.
  - Fix: after the header check in the loop, call `decode_definitions_response(&response, tracker, &inventory)` and assert it equals `[8]`, the same as lines 632-635.

- **[medium] tests/titles_claims.rs:281 decode_definitions_response - for every id other than 8 the "reader-derived" expected row is `inventory.definition_record(id)`, which is the same accessor the server uses. The doc at 248-253 claims each row is checked against the reader-derived fixture, which overstates it.**
  - Why it cannot catch a regression: `definition_blob` (progression_extras.rs:1349-1359) copies `definition_record(id)` verbatim. Any change to how that record is serialized, or to its layout for non-8 ids, changes both sides equally, so the comparison still passes. Only id 8 is checked against an independent pinned layout (`DEFINITION_8_ROW`). The `ids` return value only confirms the leading id dword.
  - Fix: for every row, also run `decode_definition_header` and assert the decoded name/icon/tint/model/texture/gender/kind against a pinned table for each requested id. Or narrow the doc comment to say that only id 8 is pinned to the client layout.

- **[low] tests/titles_claims.rs:698-717 claim_payout_uses_live_coins_after_queueing - the name says the payout "uses live coins", but `item_grant()` (line 300) has `coins: 0`, so the claim's coin payout is never exercised.**
  - Why it cannot catch a regression: a claim that ignores `grant.coins` entirely, or that adds the grant's coins to a wrong base, still leaves coins at 7 and passes. The test only shows that a claim does not reset the wallet to an earlier snapshot.
  - Fix: build a grant with nonzero coins (e.g. 5) in this test and assert the post-claim coins are 12 (live 7 plus grant 5). That exercises the payout and the live-wallet read together.

- **[low] tests/titles_claims.rs:429 achievement_title_selects_and_persists_while_forged_id_changes_nothing - the reply offset `replies[0][6..10] == 24` is an unexplained literal, and it is not tied to anything the test name claims.**
  - Why it cannot catch a regression: it is an incidental wire value (probably a length or count). Unrelated layout or content changes will break it with no link to title selection or persistence, which causes churn rather than catching the bug the name describes.
  - Fix: name the field in a helper and check it against the value the code computes for that field (or drop the assertion). The title-id check at line 435 is the one that matters here.
