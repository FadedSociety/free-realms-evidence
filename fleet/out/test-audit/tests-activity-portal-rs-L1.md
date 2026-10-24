<!-- fleet job=test-audit id=tests-activity-portal-rs-L1 status=done turns=6 usd=0.0080 tokens(read,write,in,out)=[69705, 27172, 14, 7737] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/activity_portal.rs lines 1-445 of 445

Window: `prototype/osfr-tools/tests/activity_portal.rs` lines 1-445. Read against `src/activity_portal.rs` (parse 361-374, admit 274-305, list_packet 308-356, load 214-238, with_chess_rows 251-271). The fixture `data/content/field_battles.json` exists, so nothing is silently skipped. Most tests are sound: the wire-layout byte literals (lines 148, 130, 414) match the writer, the malformed-length and refresh/play tests exercise the real length checks, and the chess/battle admission assertions match the code.

- **[medium] tests/activity_portal.rs:371 shipped_battle_content_publishes_every_battle - the name says every battle is published, but the only content check is that id 96 is present and the row count equals the count of ids that `load` itself returned.**
  - Why it cannot catch a regression: `Catalogue::load` could silently drop any battle except one (for example a filter on `required_combat_level` or a `take(1)`) and the test still passes, because `ids` is taken from the same code under test. The shipped file actually holds 10 battles (ids 96, 12370, 12340, 12301, 12302, 12303, 12350, 12310, 12311, 12400), and the test never looks at 9 of them.
  - Fix: hard-code the expected id list (or count the `battles` array in the raw JSON via `serde_json::Value`, independent of `Catalogue::load`) and assert `ids` equals it exactly.

- **[medium] tests/activity_portal.rs:249 admission_follows_the_rules_in_order - the name promises refusal precedence, but the body never checks that Busy wins over NotCombatJob or LevelTooLow.**
  - Why it cannot catch a regression: `admit` (src/activity_portal.rs:280-291) checks Busy before the job and level gates, and the code comment says "Order matters". Moving the `busy` check below the job/level checks would still pass every assertion here, because each refusal is only tested with the other conditions satisfied.
  - Fix: add `assert_eq!(catalogue.admit(96, non_combat_viewer, true), Err(Refusal::Busy))` and `assert_eq!(catalogue.admit(12302, FIGHTER, true), Err(Refusal::Busy))`, so each lower-ranked refusal is shown to lose to Busy.

- **[low] tests/activity_portal.rs:230 every_short_or_garbled_input_is_handled - there is no assertion at all; the test only checks that `parse` does not panic.**
  - Why it cannot catch a regression: a change that accepts a 13-byte or 7-byte forged Play, or that returns `Ok(Some(Play))` for garbage, passes. Only a panic fails it.
  - Fix: for each `forged` input assert `parse(&forged).is_ok_and(|r| r.is_some()) == (forged.len() == 12)`, and for each `bytes` input assert that a non-Play/Refresh prefix yields `Ok(None)`.

- **[low] tests/activity_portal.rs:121 list_matches_the_client_reader_for_every_row - the name says every row is checked, but only row 0 is compared in full; row 1 gets two dword checks and no check of its name, icon, category or can-join flag.**
  - Why it cannot catch a regression: a writer change that corrupts row 1's category, icon, name/description ids or the per-row `CanPlayerJoin` (for example, flipping it to 1 for level 9 at level 5) still passes. Row 1's join flag is not asserted anywhere in this test (the flag check at line 138 only covers members-only).
  - Fix: assert `list.rows[1]` in full (`[12302, 0, 10, 4_802, 2, 54_402, 55_402, 54_402, 55_402, 1]`, with its tail) and assert `list.flags == [(1, 0), (0, 0)]`.
