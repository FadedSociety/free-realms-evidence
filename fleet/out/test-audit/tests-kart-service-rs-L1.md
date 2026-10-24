<!-- fleet job=test-audit id=tests-kart-service-rs-L1 status=done turns=7 usd=0.0082 tokens(read,write,in,out)=[114560, 31227, 16, 6387] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_service.rs lines 1-1200 of 4095

Window reviewed: `prototype/osfr-tools/tests/kart_service.rs` lines 1-1200. No test in this window is tautological (no assertion compares a value against the same function's output, and no constant is compared with itself), and I found no `#[ignore]` or early-return skips. The findings below are weaker-than-claimed assertions and one name/doc overclaim.

- **[medium] prototype/osfr-tools/tests/kart_service.rs:368 and :371 `weapon_state_is_content_bound_and_cannot_resume_foreign_actors` - the two refusal checks use `KartService::restore(...).is_err()`, which passes on any error.**
  - Why it cannot catch a regression: if the disabled-content restore (368) or the foreign-owner restore (371) starts failing for an unrelated reason, such as a content-validation or other corrupt-field error, the test still passes. The weapon-binding rule could be deleted and the test would still pass whenever some other check happened to fail.
  - Fix: match the specific error the way lines 344-347 already do, e.g. `Err(ServiceError::CorruptSnapshot { field: "weapons" })` for both cases (or the field the foreign-owner check actually reports, after confirming it in `kart_service.rs`).

- **[medium] prototype/osfr-tools/tests/kart_service.rs:1118 `pickup_claims_without_content_refuse_and_move_nothing` - the doc says foreign, malformed and over-budget claims "refuse without touching the queue, the session or a save", but the foreign claim (1138-1143) and the malformed claim (1146-1153) have no snapshot comparison.**
  - Why it cannot catch a regression: a change that mutates the queue, session or pickup state on a foreign or malformed claim still passes, because only the refusal variant or the error variant is checked. Only the over-budget case (1166-1171) compares state. Also, the code spends an observation before the foreign check (`kart_service.rs:1907`), so the doc's "without touching a save" wording is not fully accurate for foreign claims.
  - Fix: take `let before = service.snapshot()` before each refused claim and assert it equals `spending(before, 1)` for the foreign claim (which spends one slot per the code), and `before` for the malformed claim (which returns before the observation count). Correct the doc to match.

- **[low] prototype/osfr-tools/tests/kart_service.rs:1113-1134 `pickup_claims_without_content_refuse_and_move_nothing` - the name says it "move[s] nothing", but the body asserts the snapshot changes by one observation slot.**
  - Why it cannot catch a regression: this is a naming issue rather than a hole, but the name misleads a reviewer about the test's real contract, so a change to observation accounting could be read as allowed or as a breach depending on who reads it.
  - Fix: rename to something like `pickup_claims_without_content_refuse_and_spend_only_the_observation_slot`, or keep the name and drop the "move nothing" wording from the doc.

- **[low] prototype/osfr-tools/tests/kart_service.rs:524 and :529 `native_boost_award_is_owned_persistent_and_queue_bounded` - the malformed-payload checks use `.is_err()` instead of the typed `PayloadLength` error.**
  - Why it cannot catch a regression: a change that accepts a 7- or 9-byte payload and refuses it for some other reason would still pass. The test would also pass if the handler returned any error for an unrelated reason. The sibling test `use_item_refusals_are_typed_and_move_nothing` (lines 847-857) already pins `PayloadLength { subtype, expected, actual }`.
  - Fix: assert `Err(ServiceError::PayloadLength { subtype: BOOST_REQUEST_SUBTYPE, expected: OWNED_ID_PAYLOAD_LEN, actual: 7 })` and the same for 9.

- **[low] prototype/osfr-tools/tests/kart_service.rs:1181 `preparation_loads_vehicle_but_waits_for_go_and_survives_restore` - `setup.replies().len() == 4` pins an exact frame count that is incidental to what the test is about (no early Go, state preserved across restore).**
  - Why it cannot catch a regression: it is not a hole, but any unrelated addition or removal of a setup frame breaks this test without touching the preparation-versus-Go behaviour it is named for.
  - Fix: assert the specific frames that matter (for example, that no `33/10` frame and no `GAME_STATE` frame appears before Go, which lines 1182 already partly does) and drop the exact count, or keep the count with a comment tying it to the recovered setup sequence.
