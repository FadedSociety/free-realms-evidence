<!-- fleet job=testaudit-infer id=quest_engine-v1 status=done turns=4 usd=0.0051 tokens(read,write,in,out)=[52131, 25643, 10, 2774] model=claude-haiku-5-5 -->
# tests/quest_engine.rs

{"file": "tests/quest_engine.rs",
 "tests": [
  {"name": "content_db_definitions_drive_accept_progress_and_turnin_packets", "verdict": "keep", "covered_by": null, "reason": "End-to-end accept, progress, turn-in and reward packet sequence from the content DB; the only check of this full path in the pack's similar files."},
  {"name": "empty_objective_quest_cannot_be_offered_or_turned_in", "verdict": "keep", "covered_by": null, "reason": "Refusal check: an empty-objective quest must not offer, accept or turn in. Keep as a refusal guard."},
  {"name": "all_six_requested_objective_kinds_increment_counters", "verdict": "keep", "covered_by": null, "reason": "Only test in the pack driving all six ObjectiveKind variants through on_event together; not clearly covered by another file."},
  {"name": "prerequisite_level_job_member_and_limit_gates_are_server_owned", "verdict": "keep", "covered_by": null, "reason": "Server-owned gate refusals (prerequisite, limit 47/15, level, job, membership) are security/refusal checks; keep."},
  {"name": "decline_abandon_and_reload_preserve_only_valid_progress", "verdict": "keep", "covered_by": null, "reason": "Persistence and reload round-trip of progress, selection and abandon; persistence check, keep."},
  {"name": "duplicate_turnin_retry_uses_the_character_quest_grant_key_once", "verdict": "keep", "covered_by": null, "reason": "Idempotency canary for reward grants keyed by character and quest; keep."},
  {"name": "source_tagged_opening_fixture_matches_the_existing_seventeen_stage_engine", "verdict": "keep", "covered_by": null, "reason": "Differential check of the new engine against the legacy opening engine over 17 stages; strong cross-engine canary, keep."},
  {"name": "protocol_message_builders_leave_contextual_quest_end_unencoded", "verdict": "keep", "covered_by": null, "reason": "Opcode and encode_exact-None checks on the builders. Partly overlaps the first test's encode_exact assertions, but it is a direct unit check of the builder contract; kept conservatively. Low-value candidate for later pruning."},
  {"name": "login_journal_builder_orders_209_1_before_209_2", "verdict": "keep", "covered_by": null, "reason": "Pins the login journal packet order (209/1 before 209/2). Not checked against the similar files in the pack; kept conservatively. Confirm against startup_world or opening_journal tests before removal."},
  {"name": "split_regional_quest_catalogue_accepts_and_restores_an_npc_offer", "verdict": "keep", "covered_by": null, "reason": "Loads the real split catalogue, offers from an NPC root and restores after save; real-data persistence check, keep."},
  {"name": "enabled_split_quests_send_their_goal_text_and_live_keys", "verdict": "keep", "covered_by": null, "reason": "Covers every enabled split quest's goal text and 49/8 live keys against the locale export; regression for T403, keep."},
  {"name": "a_zero_goal_text_id_is_a_load_error", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a zero goal text id must fail the loader. Keep."},
  {"name": "split_quest_locale_ids_resolve_to_exported_rows", "verdict": "keep", "covered_by": null, "reason": "Data-integrity check that every title/intro/description locale id exists in the export, plus fixed ids for two named quests. Not clearly covered by the enabled-goal test, which only checks goal text; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Conservative pass. I read lines 250-1039 in full and only the test names and doc lines for the rest (lines 1-250 and 550-655 are helpers and the start of the duplicate-turnin test). I did not read the similar files' test bodies, so I found no verified superseded or duplicate pairs. Most plausible overlaps for a later pass: protocol_message_builders_leave_contextual_quest_end_unencoded vs. the encode_exact assertions in content_db_definitions_drive_accept_progress_and_turnin_packets, and login_journal_builder_orders_209_1_before_209_2 vs. startup_world or opening_journal tests. None is removable on the current evidence. The file has no shared crate modules or helpers beyond the local fixtures."}
]}
