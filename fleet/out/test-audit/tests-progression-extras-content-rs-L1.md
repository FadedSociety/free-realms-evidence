<!-- fleet job=test-audit id=tests-progression-extras-content-rs-L1 status=done turns=4 usd=0.0041 tokens(read,write,in,out)=[16911, 14625, 10, 4194] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/progression_extras_content.rs lines 1-150 of 150

Window: `prototype/osfr-tools/tests/progression_extras_content.rs` lines 1-150. Read against `src/progression_extras.rs:97-220` (structs and `parse_*` are plain serde deserializers, no validation) and `data/content/titles.json:37-62`.

- **[medium] prototype/osfr-tools/tests/progression_extras_content.rs:61 title_and_collection_ids_resolve_to_client_data - the name says client ids resolve to client data, but no title or collection `client_id` is ever looked up in client data; the only checks are uniqueness (lines 77, 99).**
  - Why it cannot catch a regression: if `client_id` values were wrong or fabricated (e.g. a title id of 88 that the client does not know), the test still passes as long as they are unique and non-null (`unwrap()` at lines 75 and 97 only catches None). The resolution checks that do run cover name_id, description_id, image_id, and entry item/icon ids, not the client id.
  - Fix: resolve each `client_id` against a client-side table (the same kind of lab reference the test already loads for images/items), or rename the test to something like `title_and_collection_locale_and_image_ids_resolve` so the name matches the body.

- **[medium] prototype/osfr-tools/tests/progression_extras_content.rs:90 title_and_collection_ids_resolve_to_client_data - `assert!(title.source_tags.contains_key("client_id"))` passes on the provenance marker itself, which is explicitly unverified.**
  - Why it cannot catch a regression: `titles.json:52` (and every title, lines 52/77/102/127/152/177/...) sets `source_tags.client_id` to `"legacy_reference_candidate_unverified_by_family_152_capture"`. A change that leaves the key present but still unverified passes, and a regression that drops the value to an empty string also passes. The assertion checks the key's presence, not what it says.
  - Fix: assert the value is not the `legacy_reference_candidate_unverified...` marker (or is a verified tag), e.g. `assert_ne!(title.source_tags["client_id"], "legacy_reference_candidate_unverified_by_family_152_capture")`, or drop the line if the gate is not meant to enforce provenance.

- **[low] prototype/osfr-tools/tests/progression_extras_content.rs:71 title_and_collection_ids_resolve_to_client_data - exact counts `90` (line 71), `241` (line 93) and `8` entries (line 143) are pinned to the current shipped data, which is unrelated to id resolution.**
  - Why it is churn, not a missed bug: adding or removing a legacy title or a collection entry breaks this test even when every id still resolves, which is what the test is about.
  - Fix: assert `!definitions.is_empty()` for the resolution loops, and keep a single count check in a dedicated content-count test, or assert the Briarwood-specific values only.

- **[low] prototype/osfr-tools/tests/progression_extras_content.rs:81-83 and 84-89 (and 110-115, 129-131) - `if let Some(...)` silently skips the locale/image check whenever the field is None.**
  - Why it matters: the shipped titles have `description_id: null` and `image_id: null` (e.g. `titles.json:46-47`), so for most titles the description and image resolution checks never run and the test passes without checking them. This is probably intended for optional fields, but nothing asserts the count of checked ids, so a regression that nulls them all would pass silently.
  - Fix: count the checked ids and assert the count is above zero, or assert that `image_id` and `description_id` are non-null for the titles that the content build marks as having them.

Not a finding: the fixture path `lab/...` (line 26) lives outside `repo`, so a missing fixture makes the test panic on `unwrap()` rather than pass silently; no early return or `#[ignore]` is present in this window.
