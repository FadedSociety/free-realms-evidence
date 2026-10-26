<!-- fleet job=testaudit-infer id=piece_031-v1 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[23624, 14443, 8, 1871] model=claude-haiku-5-5 -->
# tests/piece_031.rs

{"file": "tests/piece_031.rs",
 "tests": [
  {"name": "catalogue_holds_the_sixteen_captured_profiles_plus_the_two_staff_rows", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the 18-row catalogue split between captured payloads and community rows; no other file drives piece_031's jobs()."},
  {"name": "every_row_keeps_a_distinct_recovered_name_string_id", "verdict": "keep", "covered_by": null, "reason": "Uniqueness and non-zero string-id check on piece_031's own catalogue; not repeated elsewhere."},
  {"name": "localization_validation_uses_the_name_string_ids", "verdict": "keep", "covered_by": null, "reason": "Exercises piece_031::validate_locale drift and missing-string errors. piece_042 has a similar locale test but calls a different module's validate_locale with different error types, so it is not the same path."},
  {"name": "combat_rows_are_exactly_the_recovered_type_two_jobs", "verdict": "keep", "covered_by": null, "reason": "Pins the combat id set and cross-checks profile type against classification; unique to this file."},
  {"name": "classifications_match_the_wiki_roster_split", "verdict": "keep", "covered_by": null, "reason": "Pins per-class counts and specific crafting/freestyle ids from the wiki roster split; no equivalent found."},
  {"name": "coverage_reports_captured_community_only_and_removed_rows", "verdict": "keep", "covered_by": null, "reason": "Checks Coverage::recovered and the Pet Trainer removal record (17419, 2009-12-14); piece_043 only mentions Pet Trainer in comments and asserts it as a gap, so it does not cover this."},
  {"name": "client_profile_datasource_columns_keep_the_recovered_order", "verdict": "keep", "covered_by": null, "reason": "Pins the 16 Profile_DS column order from the decompiled client; no other test in the similar set checks PROFILE_DS_COLUMNS."},
  {"name": "unlock_evidence_stays_client_side_and_names_the_captured_state", "verdict": "keep", "covered_by": null, "reason": "Pins the activity-finder column indices, captured active/unlocked ids, and the explicit no-quest-ids-recovered claim. This is a refusal-style boundary check and has no equivalent elsewhere."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "All eight tests exercise piece_031's own catalogue module and none has a same-path, same-assertion twin in the five similar files. piece_032 (Brawler progression) and piece_042 (validate_locale for a different progression module) overlap only in topic. The file's header claims it is a #[path] include, so it is not a crate-level test. Nothing is removable; if the suite's time budget matters, the only candidate for consolidation is the two-line-per-row string checks inside every_row_keeps_a_distinct_recovered_name_string_id, which are not worth removing."}
