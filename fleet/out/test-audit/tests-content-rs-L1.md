<!-- fleet job=test-audit id=tests-content-rs-L1 status=done turns=10 usd=0.0075 tokens(read,write,in,out)=[132896, 25428, 22, 6000] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/content.rs lines 1-195 of 195

Reviewed `prototype/osfr-tools/tests/content.rs` lines 1-195 against `src/content.rs` (`read_records`, `validate`, `validate_reward`, `reference`, `unique_ids`, `check_sources`, `Display` for `ContentError`) and the fixtures under `tests/fixtures/content/`. Each test loads a real fixture (or a copy with one JSON edit) and asserts on the concrete error variant plus its fields. The expected values (`"quest 101"`, `"npc 2732686529148769137"`, `"999999"`, `"-999"`, `"zone" / "7"`, `"items.json"` at index 0, schema 2 vs 1) come from the fixture data or the constants, not from re-running the loader. Each mutation is reached by the loader before any other failure, so no test passes by accident. No `#[ignore]`, no early returns, and all listed fixture files exist.

- **[low] tests/content.rs:124 missing_zone_references_fail_with_the_owner_field_and_target - the name says "zone references" (plural), but only the NPC `zone_id` edge is exercised.**
- **Why it cannot catch a regression:** the loader also checks `poi.zone_id` (`content.rs` ~line 727) and `dungeon.zone_id` (~line 791). Removing or breaking either of those checks would still pass this test, and nothing else in the window covers them. The name suggests broader coverage than the body provides.
- **Fix:** rename it to something like `missing_npc_zone_fails_with_the_owner_field_and_target`, or add parallel cases that set `pois.json` `zone_id` to 999 and assert `poi 3` / `zone_id` / `999`, plus a dungeon case if the fixture has `zone_id` set.

No findings in the other categories (cannot-fail, asserts-nothing, skipped, or over-pinned) for this window.
