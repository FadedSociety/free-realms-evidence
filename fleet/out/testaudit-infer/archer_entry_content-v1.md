<!-- fleet job=testaudit-infer id=archer_entry_content-v1 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[4680, 5094, 6, 1021] model=claude-haiku-5-5 -->
# tests/archer_entry_content.rs

{"file": "tests/archer_entry_content.rs",
 "tests": [{"name": "enabled_archer_chapter_records_are_complete_and_others_stay_disabled", "verdict": "duplicate", "covered_by": "tests/archer_entry_chain.rs::enabled_archer_chapter_records_are_complete_and_others_stay_disabled", "reason": "The test body only calls support/archer_entry.rs::assert_enabled_archer_chapter_records(). archer_entry_chain.rs has a test with the same name that calls the same helper (line ~596), so the same path with the same assertions runs twice. The file's own doc says it is a focused target for the same checks, so it adds no coverage."}],
 "whole_file_removable": true,
 "confidence": 0.8,
 "notes": "The whole file is a one-line wrapper around a shared helper that archer_entry_chain.rs already runs. The only reason to keep it is a focused run target; if that is wanted for workflow reasons, keep it, but it is not a coverage test. The sibling medic_entry_content.rs follows the same pattern and would be assessed the same way. The support module itself is not part of this file and was not reviewed for removal."}
