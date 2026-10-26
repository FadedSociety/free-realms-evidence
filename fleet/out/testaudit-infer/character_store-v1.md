<!-- fleet job=testaudit-infer id=character_store-v1 status=done turns=4 usd=0.0039 tokens(read,write,in,out)=[39415, 19130, 10, 2243] model=claude-haiku-5-5 -->
# tests/character_store.rs

{"file": "tests/character_store.rs",
 "tests": [
  {"name": "creates_a_save_and_ignores_a_new_default_on_load", "verdict": "keep", "covered_by": null, "reason": "Only test of single-character load_or_create create-then-ignore-default persistence and the schema_version 2 / no-legacy-version on-disk shape. Similar piece_095 tests cover a different multi-character store."},
  {"name": "a_fresh_process_restores_saved_coordinates", "verdict": "keep", "covered_by": null, "reason": "Restart persistence canary through a child process. piece_095::a_fresh_process_restores_every_character_and_the_active_selection uses the same pattern but on the multi-character store, not this module's file format, so it does not cover this path."},
  {"name": "successive_saves_replace_the_file_and_leave_no_temporary_files", "verdict": "keep", "covered_by": null, "reason": "Checks atomic replacement over repeated saves and that no temp files remain. No other test in the suite drives character_store::save directly for this."},
  {"name": "corrupt_and_unsupported_existing_files_are_not_reset", "verdict": "keep", "covered_by": null, "reason": "Refusal check: corrupt, unsupported-version, zero-guid, out-of-range and short-array files are rejected with InvalidData and left byte-identical. piece_095::corrupt_unsupported_or_oversized_stores_are_preserved is the same idea but for a different store format, so it is not an equivalent check."},
  {"name": "oversized_existing_save_is_bounded_and_preserved", "verdict": "keep", "covered_by": null, "reason": "Bound and preservation check for MAX_FILE_BYTES+1 with the 16 KiB message. Only direct test of this bound for character_store."},
  {"name": "invalid_updates_preserve_the_prior_valid_save", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal: NaN, infinities, out-of-range magnitudes and zero guid must not change the prior file. Security-relevant, no equal test elsewhere."},
  {"name": "transient_windows_reader_without_delete_sharing_allows_atomic_save_after_release", "verdict": "keep", "covered_by": null, "reason": "Windows-only (cfg(windows)) regression for the OS5 reader sharing case. Not run on other platforms, but no equivalent test exists; keep."},
  {"name": "failed_windows_replacement_preserves_the_previous_file", "verdict": "keep", "covered_by": null, "reason": "Windows-only refusal check: a locked file must make replacement fail without losing the previous save. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "All eight tests are the only direct checks of the character_store module in the suite (no other test calls character_store::save or load_or_create directly; other files use game_store, which wraps it). The similar files (piece_095, login, kart_service, housing, inventory) test their own stores with analogous shapes (restart child process, corrupt-file preservation, atomic save), so the overlap is by pattern, not by the same code path. Nothing was judged superseded or duplicate. The two cfg(windows) tests do not run on Linux CI. I did not compare game_store.rs's persistence tests in depth, so a partial overlap with game_store may exist that I did not verify."}
