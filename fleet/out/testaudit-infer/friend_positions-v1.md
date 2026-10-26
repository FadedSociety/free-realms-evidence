<!-- fleet job=testaudit-infer id=friend_positions-v1 status=done turns=4 usd=0.0049 tokens(read,write,in,out)=[54693, 23459, 10, 2933] model=claude-haiku-5-5 -->
# tests/friend_positions.rs

{"file": "tests/friend_positions.rs",
 "tests": [
  {"name": "parser_accepts_exact_client_shapes_and_nothing_else", "verdict": "keep", "covered_by": null, "reason": "Only test of parse_location_request for 26/21, 40/14 and 40/16 (no other test file references these symbols). Covers truncation, trailing bytes, bad booleans and out-of-range coordinates, which are refusal checks."},
  {"name": "positions_packet_matches_recovered_reader_layout", "verdict": "keep", "covered_by": null, "reason": "Only byte-level check of the 74/5 encoder against the recovered reader layout, plus NaN, infinity and over-cap refusals. No other test covers encode_friend_positions."},
  {"name": "mutual_online_friends_in_the_same_scope_get_real_coordinates", "verdict": "keep", "covered_by": null, "reason": "Positive visibility rule and out-of-scope canary for the friend-position feature; not exercised elsewhere."},
  {"name": "other_zone_instance_and_battle_friends_are_hidden_without_coordinates", "verdict": "keep", "covered_by": null, "reason": "Scope and privacy canary (other zone, instance and battle hidden with no coordinates leaked). Security-relevant, so kept."},
  {"name": "offline_one_sided_ignored_unknown_and_unplaced_identities_are_absent", "verdict": "keep", "covered_by": null, "reason": "Refusal and absence checks covering one-sided friendship, logout, ignore and missing profile. Security-relevant and not covered elsewhere."},
  {"name": "offline_requester_and_non_finite_registry_values_are_never_encoded", "verdict": "keep", "covered_by": null, "reason": "Hostile-value check: NaN and far-out registry positions are hidden and never encoded. Kept as a refusal check."},
  {"name": "online_friend_rows_open_the_atlas_gate_and_offline_rows_do_not", "verdict": "keep", "covered_by": null, "reason": "Pins the 74/1 Is_In_Static_Zone byte from login. Not covered by any other test I found; I did not inspect the social_lists.rs unit tests, so this is moderately confident."},
  {"name": "job_change_reaches_exactly_the_group_with_the_authenticated_guid", "verdict": "keep", "covered_by": null, "reason": "Only test of 40/15 fan-out, non-member refusal and no-op repeats."},
  {"name": "job_change_flag_survives_snapshots_and_dies_with_membership", "verdict": "keep", "covered_by": null, "reason": "Persistence and reset canary across 40/8 snapshots, leave and disconnect. Not covered elsewhere."},
  {"name": "ping_reaches_group_members_in_the_same_zone_and_instance_only", "verdict": "keep", "covered_by": null, "reason": "Scope check for group map ping; only test of group_map_ping fan-out."},
  {"name": "ping_refuses_nonmembers_bad_values_unplaced_and_ignoring_recipients", "verdict": "keep", "covered_by": null, "reason": "Refusal check: non-member, bad coordinates, unplaced sender and ignoring recipients."},
  {"name": "forged_sender_guid_in_a_ping_never_reaches_a_recipient", "verdict": "keep", "covered_by": null, "reason": "Security check that a forged guid in the body is ignored. Canary-style and unique."},
  {"name": "gateway_forwards_the_new_selectors_to_the_social_router", "verdict": "keep", "covered_by": null, "reason": "Source-text check of gateway.rs application_handler. I confirmed the arm at gateway.rs:511/514 lists 26/21 and 40/14|16, so the test passes. It is the only guard that these selectors reach the router. Brittle, but not redundant."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Nothing in the pack is a duplicate. The five similar files (player_trade, piece_088, npc_interaction, multiplayer, social_chat) cover trade, chat, NPC and multiplayer behaviour, not friend positions, group job change or group map ping. A repo-wide search found no other test file referencing parse_location_request, encode_friend_positions, friend_positions, group_changing_job or group_map_ping. Not checked: the unit tests inside src/social_lists.rs and tests/group_invite_expiry.rs, which could overlap the 74/1 atlas-gate test and the group-membership setup. The gateway test is source-text based and fragile; consider a behavioural routing test instead, but it is not removable now."}
]}
