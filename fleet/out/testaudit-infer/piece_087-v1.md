<!-- fleet job=testaudit-infer id=piece_087-v1 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[11667, 16527, 6, 2438] model=claude-haiku-5-5 -->
# tests/piece_087.rs

{"file": "tests/piece_087.rs",
 "tests": [
  {"name": "family_and_sub_opcodes_match_the_client_and_the_supplied_server", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the recovered friend family/sub-opcode table against client constructors and the supplied server enum; no equivalent elsewhere in the suite."},
  {"name": "command_sub_opcodes_match_the_client_constructors", "verdict": "keep", "covered_by": null, "reason": "Unique pin of the recovered command sub-opcode table (14-30) for restoration::piece_087; not asserted in any other file."},
  {"name": "roster_field_sets_match_the_client_lua_datasource", "verdict": "keep", "covered_by": null, "reason": "Unique check of the 18 FriendsList_DS fields and 13 UI columns against ScriptsBase.lua; no other test reads these constants."},
  {"name": "friend_list_encodes_the_inferred_layout_byte_for_byte", "verdict": "keep", "covered_by": null, "reason": "Byte-exact layout pin for the INFERRED friend-list encoding; the only byte-level check of this restoration encoder. The production src/social_lists.rs encoder is a different code path."},
  {"name": "friend_list_round_trips_offline_rows", "verdict": "keep", "covered_by": null, "reason": "Round-trip with offline rows for the restoration decoder; the only such test for this module."},
  {"name": "friend_list_rejects_malformed_bodies", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check (truncated, trailing, oversized count, non-finite, overlong name); must be kept."},
  {"name": "client_requests_decode_from_the_recovered_opcodes_only", "verdict": "keep", "covered_by": null, "reason": "Refusal of unrecovered opcodes on the request decoder; unique to this module."},
  {"name": "notifications_encode_with_the_family_and_sub_header", "verdict": "keep", "covered_by": null, "reason": "Header check for notification encoding in this module; not covered elsewhere."},
  {"name": "add_requests_validate_identity_and_permissions", "verdict": "keep", "covered_by": null, "reason": "Permission/identity refusal check on the restoration FriendRegistry; security-relevant and not duplicated by tests/social_lists.rs, which drives src/social_lists.rs."},
  {"name": "accepting_a_request_makes_the_roster_mutual", "verdict": "keep", "covered_by": null, "reason": "Core lifecycle behaviour of the restoration registry; only test of this path."},
  {"name": "declining_and_timing_out_leave_no_friendship", "verdict": "keep", "covered_by": null, "reason": "Refusal-style lifecycle check on the restoration registry; not a duplicate of social_lists.rs tests because the module under test differs."},
  {"name": "only_the_addressed_recipient_may_answer_a_request", "verdict": "keep", "covered_by": null, "reason": "Authorization refusal check; must be kept."},
  {"name": "removal_requires_an_existing_friendship_and_notifies_both_sides", "verdict": "keep", "covered_by": null, "reason": "Refusal and fan-out check for removal in this module; kept conservatively."},
  {"name": "presence_changes_only_reach_friends", "verdict": "keep", "covered_by": null, "reason": "Privacy/fan-out boundary check; kept conservatively."},
  {"name": "position_requests_return_only_local_friends_and_reject_bad_input", "verdict": "keep", "covered_by": null, "reason": "Hostile-input and scope refusal check; tests/friend_positions.rs covers the production SocialService, not this restoration registry."},
  {"name": "rename_is_bounded_and_notifies_friends", "verdict": "keep", "covered_by": null, "reason": "Bounds check on rename plus notification; unique to this module."},
  {"name": "deliveries_recover_the_decoded_notification", "verdict": "keep", "covered_by": null, "reason": "Round-trip of Delivery to decoded Notification; only test of this path."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "The pack's similar-file list (coin_store, housing, npc_interaction, piece_091, piece_046) shares no friend tests. Targeted search found friend tests in tests/social_lists.rs (friend_request_accept_remove_and_all_client_result_codes, friend_decline_timeout_duplicate_and_login_logout_presence) and tests/friend_positions.rs, which drive the production src/social_lists.rs SocialService, not src/restoration/piece_087.rs. Those are a plausible overlap in behaviour (accept/decline/remove/positions) but a different code path, so I did not mark any test superseded or duplicate. A reviewer who accepts that the restoration module is a parallel implementation could justify consolidating the lifecycle tests against social_lists.rs; that judgement needs the full file and the registry source, which were not in the pack. The file's header says it is a #[path] include meant to be temporary until 'pub mod piece_087' is registered; if that registration lands, the include-only shape could be reconsidered."}
