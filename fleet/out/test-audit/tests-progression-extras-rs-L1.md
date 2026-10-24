<!-- fleet job=test-audit id=tests-progression-extras-rs-L1 status=done turns=7 usd=0.0074 tokens(read,write,in,out)=[92113, 28679, 16, 5705] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/progression_extras.rs lines 1-679 of 679

Window: `prototype/osfr-tools/tests/progression_extras.rs` lines 1-679 (whole file). Four findings; the rest of the window checks what its name claims.

- **[medium] prototype/osfr-tools/tests/progression_extras.rs:667 shipped_achievement_rules_join_every_title_by_name - the name says every title is joined by name, but the body only checks counts (90 rules, 17 title bindings, no claim bindings, one job slug).**
  - Why it cannot catch a regression: `AchievementBindings::load` (src/progression_extras.rs:297-304) silently drops any `title_names` entry that has no match in `title_by_name`. If a title name is misspelled, or a binding is dropped, the count only changes if the total crosses 17. Swapping which achievement a title binds to, or binding the wrong title id, leaves the count at 17 and the test passes. Nothing checks that each `title_names` entry resolves.
  - Fix: iterate `achievements.json` rules that list `title_names` and assert that every name exists in `titles.json`. Also assert that each `title_bindings()` entry's `title` id equals `title_by_name` for that name, and that the set of bound keys equals the expected set. Or rename the test to say it counts bindings.

- **[medium] prototype/osfr-tools/tests/progression_extras.rs:458 claim_batch_cannot_grow_saved_history_past_its_load_bound - the name says it checks the load bound, but the body only goes through `handle_claim_request`.**
  - Why it cannot catch a regression: the saved-state bound is enforced in `from_saved` (src/progression_extras.rs:1135 and 1176, the `MAX_CLAIM_HISTORY` checks). `with_claimed_ids` does no validation, and the test never calls `from_saved` or the ledger load path. Removing or raising the load-time check still passes. The test only exercises the request-time guard at src/progression_extras.rs:1242.
  - Fix: either rename it to something like `claim_batch_rejected_when_it_would_exceed_history_bound`, or add a load assertion: build a saved state with 4096 claimed ids plus one pending entry and assert the restore call returns an error, and that a 4095-id state restores.

- **[low] prototype/osfr-tools/tests/progression_extras.rs:412 claim_tracker_grants_only_queued_server_reward_once - the definitions reply is checked only as "price > 0".**
  - Why it cannot catch a regression: the blob at bytes 9..13 could carry the wrong definition's price, a stale inventory price, or any positive number, and the test still passes. The definition id and the rest of the record are not checked either.
  - Fix: assert the exact encoded value for definition 100 from the fixture (`100i32` and the fixture's default data), or at least check that the returned definition id matches 100.

- **[low] prototype/osfr-tools/tests/progression_extras.rs:600-610 source_content_ids_are_unique_and_locale_backed - exact `name_id`/`description_id` field counts (238, 187, 226, 90, 1) pin shipped content totals that change whenever content is added or re-curated.**
  - Why it cannot catch a regression: these counts do not test the locale resolution or the uniqueness claim the test name makes. Adding one localized row, or a row that changes its ids, breaks the test for reasons unrelated to what its name claims.
  - Fix: keep the locale-resolution check (`assert_locale_ids_resolve`) and the uniqueness check, and drop the exact field-count pins. If they must stay, move them to a separate content-inventory test.
