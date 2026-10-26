<!-- fleet job=testaudit-infer id=bandit_hideout_dungeon-v1 status=done turns=3 usd=0.0041 tokens(read,write,in,out)=[24805, 17368, 8, 3447] model=claude-haiku-5-5 -->
# tests/bandit_hideout_dungeon.rs

{"file": "tests/bandit_hideout_dungeon.rs",
 "tests": [
  {"name": "level_eight_is_refused_and_keeps_the_pending_screen", "verdict": "keep", "covered_by": null, "reason": "Level-floor refusal with state-unchanged and pending-screen reuse; a refusal check for the new row's gate. Not verified as duplicated elsewhere."},
  {"name": "level_nine_starts_the_battle", "verdict": "keep", "covered_by": null, "reason": "Only check of the row's level-9 start, the difficulty-4 arena scaling and the explicit 41/109 exit for this row."},
  {"name": "the_start_screen_carries_the_instance_and_roster_count", "verdict": "duplicate", "covered_by": "tests/bixie_hive_dungeon.rs::the_start_screen_carries_the_instance_and_roster_count", "reason": "Same 41/114 path and same instance/roster/prize-preview assertions on a sibling row; bixie's version checks the full DETAILS_LEN and id as well. Only the row constant differs. Low-confidence: may be kept as a per-row content regression."},
  {"name": "the_full_route_pays_sixty_coins_and_one_prize", "verdict": "keep", "covered_by": null, "reason": "End-to-end payout check (60 coins, one prize, 50 job XP once, replay pays nothing) for this row; the only full-route test for battle 12360."},
  {"name": "the_portal_row_applies_the_same_level_and_prize_gates", "verdict": "keep", "covered_by": null, "reason": "Portal publication and gate parity for the new row; a refusal/gate check."},
  {"name": "refusals_leave_state_and_pending_battle_unchanged", "verdict": "keep", "covered_by": null, "reason": "Refusal check (forged, out-of-range, knocked-out, full bag, consumed) changing no saved state; never removable without an equal test."},
  {"name": "a_second_player_runs_its_own_instance_and_is_paid_once", "verdict": "keep", "covered_by": null, "reason": "Isolation and single-payment check across two sessions; security-adjacent, kept."},
  {"name": "the_win_and_the_mid_fight_return_survive_a_reload", "verdict": "keep", "covered_by": null, "reason": "Persistence check: reload mid-fight drops run without payout; won reload cannot pay again. Persistence tests are kept."},
  {"name": "every_previewed_prize_resolves_for_the_shipped_catalogue", "verdict": "keep", "covered_by": null, "reason": "Catalogue resolution and stack-fit check for this row's prizes; bixie's analogue checks a different row's prizes."},
  {"name": "guids_are_unique_across_the_shipped_content", "verdict": "duplicate", "covered_by": "tests/bixie_hive_dungeon.rs::guids_are_unique_across_shipped_content", "reason": "Same GUID-uniqueness walk over all battles; this version additionally checks field_enemies.json and encounter actors, so it is not strictly a subset. Partial duplicate; keep the stronger one in whichever file, or retain here for the field/encounter check."},
  {"name": "a_live_mining_movie_refuses_the_battle", "verdict": "keep", "covered_by": null, "reason": "Busy-table refusal check that changes nothing; refusal test kept."},
  {"name": "a_second_session_sees_the_marker_not_the_arena", "verdict": "keep", "covered_by": null, "reason": "Visibility/privacy check (arena actors hidden from other sessions); kept."},
  {"name": "a_live_change_before_the_close_survives_the_payout", "verdict": "keep", "covered_by": null, "reason": "Payout-from-live-state check; only test for dev-grant survival in this row's route."},
  {"name": "a_failing_start_or_payout_does_not_stop_the_other_session", "verdict": "keep", "covered_by": null, "reason": "Error-isolation check across sessions; refusal/robustness, kept."},
  {"name": "the_marker_is_on_the_ground_and_clear", "verdict": "keep", "covered_by": null, "reason": "Placement check for the new marker (terrain height, clearance from spawns/markers); unique to this row. Sibling thugamug_battle has a same-named test for a different marker."},
  {"name": "the_shipped_rows_are_unchanged_and_the_new_row_is_appended", "verdict": "keep", "covered_by": null, "reason": "Regression canary that earlier rows keep title/difficulty/level/payout and the new row is the only addition; canary, kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The file is a per-row clone of tests/bixie_hive_dungeon.rs (same fixture, route and structure, T354 vs T353). Two tests (start screen, GUID uniqueness) are near-duplicates of bixie equivalents; the rest pin this row's own marker, prizes, route and canary checks and are kept. Review was partial (read the start-screen, GUID and full-route openings, plus the bixie equivalents); assertion-level comparison of the route, refusal, reload and multi-session tests against bixie and thugamug_battle was not done, so their keep verdicts are conservative. Consider a shared parametrised helper rather than deleting tests."}
