<!-- fleet job=testaudit-infer id=piece_043-v1 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[25015, 15518, 8, 2185] model=claude-haiku-5-5 -->
# tests/piece_043.rs

{"file": "tests/piece_043.rs",
 "tests": [
  {"name": "recovered_job_ids_and_locale_rows", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the recovered Card Duelist job id 120, locale rows 2410/2411, Pet Trainer badge set 1785 and the null Pet Trainer profile id. No other file references piece_043 constants."},
  {"name": "milestone_rows_match_the_contiguous_locale_blocks", "verdict": "keep", "covered_by": null, "reason": "Sole check of the milestone locale blocks 34070-34074/34150-34154 and 34110-34114/34190-34194 for both jobs."},
  {"name": "level_up_presentation_rows_come_from_the_lua_table", "verdict": "keep", "covered_by": null, "reason": "Sole check of the badge set, movie name and sound id rows that mirror NotificationHandler:JobLevelUp."},
  {"name": "level_up_notification_requires_a_supported_badge_set", "verdict": "keep", "covered_by": null, "reason": "Refusal check: an unknown badge set must yield no notification. Nothing else exercises this gate."},
  {"name": "level_up_notification_uses_the_recovered_message_locale", "verdict": "keep", "covered_by": null, "reason": "Pins level-1 vs other-level message locale (919922/919923) and the sound id for a band level; no other coverage."},
  {"name": "level_up_notification_movie_is_not_gated_by_the_sound_bands", "verdict": "keep", "covered_by": null, "reason": "Documents a quirk (movie plays with no sound id off-band) that mirrors the Lua behaviour; unique to this file."},
  {"name": "ledger_grants_only_validated_completed_outcomes", "verdict": "keep", "covered_by": null, "reason": "Refusal check: lost and abandoned outcomes grant zero XP and leave level unchanged. Not covered elsewhere."},
  {"name": "ledger_rejects_a_replayed_instance", "verdict": "keep", "covered_by": null, "reason": "Replay-protection (security) check for DuplicateOutcome; no equivalent in other files."},
  {"name": "ledger_is_job_scoped_and_rejects_cross_job_outcomes", "verdict": "keep", "covered_by": null, "reason": "Refusal check for JobMismatch and per-job instance spaces; unique."},
  {"name": "ledger_refuses_a_zero_instance_id", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check for InvalidInstanceId; unique."},
  {"name": "ledger_unlocks_each_milestone_once_and_respects_the_cap", "verdict": "keep", "covered_by": null, "reason": "Covers milestone unlock-once and level cap at 20 over 25 outcomes; the only test of this path."},
  {"name": "non_member_cap_is_a_labelled_community_rule", "verdict": "keep", "covered_by": null, "reason": "Pins the non-member level-4 cap. It is a community-documented, reconstructed rule, so it is kept as a labelled canary rather than removed."},
  {"name": "snapshot_round_trip_validates_saved_progress", "verdict": "keep", "covered_by": null, "reason": "Persistence round-trip plus refusal of invalid level, zero level, non-member level and unknown milestone; unique."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file includes src/restoration/piece_043.rs via #[path], and no other test in the repo references piece_043 or its ProgressionLedger / level_up_notification APIs, so nothing is superseded or duplicated. The most similar files (piece_039 mining/farm ledger, kart_service, piece_086, housing_service, piece_040) share only structural naming (ledger, rank/milestone tables) and test different domains. I did not read the similar files' assertions in depth, so overlap is judged from names only. The file has no created_by/last_changed_by task, so no obsolescence by a later task could be confirmed. Every test is labelled keep under the conservative rule."}
