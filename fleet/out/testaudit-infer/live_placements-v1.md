<!-- fleet job=testaudit-infer id=live_placements-v1 status=done turns=4 usd=0.0043 tokens(read,write,in,out)=[49720, 21443, 10, 2287] model=claude-haiku-5-5 -->
# tests/live_placements.rs

{"file": "tests/live_placements.rs",
 "tests": [
  {"name": "another_session_sees_a_new_placement_without_reload", "verdict": "keep", "covered_by": null, "reason": "Only test of the cross-session add path (other session's tick sends one AddNpc with the row's actor/model/name/transform, no duplicate, and reconnect loads the file). Unique to live placement watch."},
  {"name": "unplace_removes_it_from_other_sessions", "verdict": "keep", "covered_by": null, "reason": "Only test that an unplace reaches other sessions as 35/3 once and then goes quiet; no equivalent elsewhere in the suite."},
  {"name": "far_away_placement_is_sent_only_when_in_range", "verdict": "keep", "covered_by": null, "reason": "Range-gated add/remove for a live placement; the distance boundary is only checked here for placements (players.rs covers radius for players, a different path)."},
  {"name": "malformed_file_keeps_the_previous_view", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a truncated table publishes nothing and keeps revision and state; a later valid write is applied. Security/refusal-style, no equal test found."},
  {"name": "poll_is_rate_limited_and_does_not_duplicate", "verdict": "keep", "covered_by": null, "reason": "Pins the one-second poll rate limit and no-duplicate-on-same-mtime behaviour for live placements; not clearly covered elsewhere."},
  {"name": "two_admins_converge_to_the_final_rows", "verdict": "keep", "covered_by": null, "reason": "Multi-writer convergence with unique GUIDs and no duplicate adds; distinct from single-writer tests in this file and no equivalent found."},
  {"name": "sessions_in_another_zone_do_not_see_it", "verdict": "keep", "covered_by": null, "reason": "Zone isolation for live placements, then one add on zone transfer. Only zone check for this feature; the fixture's comment notes instance membership is covered elsewhere (shared_world_membership), not this zone check."},
  {"name": "a_same_guid_edit_replaces_the_actor_for_the_writer_and_a_poller", "verdict": "keep", "covered_by": null, "reason": "Regression-style canary for same-GUID edits being skipped by both the poller and the writer; unique and specific."},
  {"name": "an_unreadable_table_refuses_the_commands_without_changing_anything", "verdict": "keep", "covered_by": null, "reason": "Refusal check across three commands plus oversized-file refusal; no save, no view change, no rewrite. Must keep under the refusal rule."},
  {"name": "shared_view_sends_the_new_placement_once_through_the_revision", "verdict": "keep", "covered_by": null, "reason": "Covers the revision-driven shared_npc_view path (gateway 20 Hz loop) for placements, not exercised by the other tests in this file. Other shared_npc_view users (brawler_*, collection_coin_pickup, field_camps_high_band) test different actors/flows."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Checked the file's tests and grepped for realm place, set_world_dir, shared_npc_view and the refusal message across tests/. No test in another file drives the same placement-watch path with the same assertions. I did not read live_events.rs or shared_field_interest.rs in depth; they use set_world_dir and npc_placements.json and are the closest neighbours to check if the confidence needs raising. The similar-file list in the pack (power_up_drops, housing_service, player_trade, coin_store_siblings, players) is not about placement watch, so it gave no overlap. Verdicts are conservative; I found no candidates for removal."}
