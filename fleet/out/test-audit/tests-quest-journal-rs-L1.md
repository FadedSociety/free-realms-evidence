<!-- fleet job=test-audit id=tests-quest-journal-rs-L1 status=done turns=5 usd=0.0062 tokens(read,write,in,out)=[49397, 22937, 12, 5745] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/quest_journal.rs lines 1-462 of 462

Window: `prototype/osfr-tools/tests/quest_journal.rs` lines 1-462. Read against `src/quest_journal.rs` (decode, handle, breadcrumb) and `src/quest_engine.rs` (select_quest 1540, offer 1573, offer_denial 1653, accept 1698). Two findings; the rest of the window checks real behaviour.

- **[medium] tests/quest_journal.rs:162-165 decodes_exact_native_widths - the "client's wire sizes 7, 4 and 10" assertions check the test's own packet builders, not the decoder.**
  - Why it cannot catch a regression: `select(1)`, `lock(1)` and `crumb(1)` are literal byte vectors built by helpers at lines 82-92 in this same file. Changing `decode` or the documented size of the packet cannot change their `.len()`, so these three asserts can never fail for a reason in the code under test.
  - Fix: assert the size against the decoder's contract, e.g. make a packet one byte longer or shorter than the documented size and assert `decode` returns `Err(Malformed)`. The existing trailing-byte cases at lines 194, 201 and 206 cover this partly. Alternatively, delete lines 162-165 and keep the comment as a note.

- **[low] tests/quest_journal.rs:352 breadcrumb_makes_the_normal_offer_and_never_completes_anything - the final `assert_no_award(&e, &outcome)` re-checks the outcome from the first breadcrumb (line 337), not the outcome of `e.accept(10)` at line 349.**
  - Why it cannot catch a regression: `accept`'s outcome is discarded. If accepting started emitting a `Reward` message or a reward grant, `assert_no_award` on the stale outcome still passes. The engine-state half of the check still runs against `e`, so only the outbound and rewards side of accept is unguarded.
  - Fix: `let accepted = e.accept(10); assert!(accepted.changed); assert_no_award(&e, &accepted);`, and use `accepted` in place of `outcome` at line 352.
