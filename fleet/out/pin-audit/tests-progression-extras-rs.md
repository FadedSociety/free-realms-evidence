<!-- fleet job=pin-audit id=tests-progression-extras-rs status=nothing_found turns=3 usd=0.0011 tokens(read,write,in,out)=[6561, 5147, 8, 861] model=claude-haiku-5-5 -->
# tests/progression_extras.rs

No findings in `prototype/osfr-tools/tests/progression_extras.rs`. All three screened lines are fixture-driven, not data-driven:

- **Line 226 (`add_entry_body_matches_client_reader_8d8570`):** `packet[20..24]` checks `collection_id: 10`, which the test sets itself in the `CollectionEntryUpdate` literal (line 210). It is a wire-layout check, not a tuned value.
- **Lines 332 and 355 (`collection_completes_and_grants_once_across_gameplay_sources`):** the `5` comes from `coin_grant(5)` (defined at line 148, passed as `reward` at line 290). The test builds that grant itself, so the expected coin total is the fixture's own amount, not a value from a data file. Nothing in `data/content` feeds this path.
