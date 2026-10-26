<!-- fleet job=testaudit-infer id=piece_074-v1 status=done turns=2 usd=0.0033 tokens(read,write,in,out)=[10797, 18602, 6, 1727] model=claude-haiku-5-5 -->
# tests/piece_074.rs

{"file": "tests/piece_074.rs",
 "tests": [
  {"name": "category_table_is_the_ten_recovered_client_rows", "verdict": "keep", "covered_by": null, "reason": "Pins the 10-row COLLECTION_CATEGORIES table and its first/last rows against the client CollectionCategories.txt; the only such check. piece_038 only checks category column names, not the row table."},
  {"name": "category_bucket_is_the_recovered_modulo", "verdict": "keep", "covered_by": null, "reason": "Checks the % 10 bucket and that category 0 is refused; no equivalent bucket test found in the similar files."},
  {"name": "collecting_every_entry_completes_the_collection_once", "verdict": "keep", "covered_by": null, "reason": "Exactly-once completion on the piece_074 CollectionLedger path. piece_038::a_collection_completes_once_when_its_last_entry_arrives exercises the same idea but on a different module (piece_038 ProfileCollections), so it is not the same path."},
  {"name": "replaying_a_collected_entry_does_not_re_emit_a_completion", "verdict": "keep", "covered_by": null, "reason": "Replay-idempotence check (reward granted twice guard) on piece_074's ledger. Similar in spirit to piece_038::a_replayed_add_entry_is_ignored_and_never_re_completes but a different implementation; not the same path, so kept."},
  {"name": "restart_preserves_progress_and_the_completion_marker", "verdict": "keep", "covered_by": null, "reason": "Persistence round-trip (to_bytes/from_bytes) of progress and completion markers; persistence check, no equivalent elsewhere."},
  {"name": "malformed_definitions_and_entries_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal test (unknown category, empty, duplicate entry, duplicate collection, unknown entry); hostile/refusal input must be kept."},
  {"name": "a_corrupt_or_unsupported_ledger_is_refused", "verdict": "keep", "covered_by": null, "reason": "Corrupt/unsupported/oversized persisted-ledger refusal check; security-relevant parsing refusal, kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "All seven tests are kept. The most similar file, tests/piece_038.rs, has overlapping names (once-only completion, replay ignored) but tests a different module (piece_038::ProfileCollections, not piece_074::CollectionLedger), so it does not drive the same path and is not named as a duplicate. The piece_074 tests have no doc lines and no crate module imports; the file pulls its source via #[path] include, which is a lead-owned integration step, not a redundancy issue. Other similar files (housing_service, soccer_service, piece_060, player_trade) are unrelated domains."}
