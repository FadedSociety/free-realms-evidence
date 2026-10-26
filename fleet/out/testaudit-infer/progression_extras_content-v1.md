<!-- fleet job=testaudit-infer id=progression_extras_content-v1 status=done turns=5 usd=0.0031 tokens(read,write,in,out)=[42256, 14761, 12, 1732] model=claude-haiku-5-5 -->
# tests/progression_extras_content.rs

{"file": "tests/progression_extras_content.rs",
 "tests": [{"name": "title_and_collection_ids_resolve_to_client_data", "verdict": "keep", "covered_by": null, "reason": "Only test that checks title/collection image ids against the client Images.txt, collection entry item_definition_id against ClientItemDefinitions.json, and the Briarwood collection's category/wiki-category/description/entry shape. The overlapping parts (count of 90 titles and 241 collections, client_id uniqueness, locale ids non-empty) are also asserted in tests/progression_extras.rs::source_content_ids_are_unique_and_locale_backed, but that test does not check images or item definitions, so this one is not clearly covered elsewhere."}],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Single-test file. Partial overlap with progression_extras.rs::source_content_ids_are_unique_and_locale_backed (counts, id uniqueness, locale resolution via assert_locale_ids_resolve) and with progression_extras.rs::shipped_achievement_rules_join_every_title_by_name (title count 90). Its unique value is the client-data cross-check (images, item definitions) and the Briarwood fixture. Could trim the duplicated count/locale asserts if the suite cost matters, but the file as a whole should stay. Reads lab/ reference files, so it depends on the lab checkout being present."}
