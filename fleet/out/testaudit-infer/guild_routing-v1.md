<!-- fleet job=testaudit-infer id=guild_routing-v1 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[25771, 19160, 8, 2540] model=claude-haiku-5-5 -->
# tests/guild_routing.rs

{"file": "tests/guild_routing.rs",
 "tests": [
  {"name": "two_bots_create_invite_accept_and_chat", "verdict": "keep", "covered_by": null, "reason": "End-to-end create/invite/accept/chat path across two identities; no similar guild test file exists in the repo to supersede it."},
  {"name": "relog_roster_survives_a_gateway_restart", "verdict": "keep", "covered_by": null, "reason": "Persistence across restart is the only check of roster reload in the suite; persistence tests are not removable without an equal replacement."},
  {"name": "non_members_forged_guids_and_bad_names_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Security/refusal check (forged guids from non-members change nothing)."},
  {"name": "oversize_and_invalid_names_are_refused", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check for guild names; no equivalent found elsewhere."},
  {"name": "control_characters_in_the_motd_are_refused_without_change", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check on MOTD text; only MOTD sanitising test found (world_notice.rs covers a different feature)."},
  {"name": "malformed_and_member_location_requests_are_answered_with_silence", "verdict": "keep", "covered_by": null, "reason": "Refusal/silence check for malformed input; keep as the only guild-side check."},
  {"name": "declined_and_timed_out_invites_carry_the_actor_name", "verdict": "keep", "covered_by": null, "reason": "Asserts 129/27 and 129/28 notification layout with actor name; unique to this file."},
  {"name": "forged_accept_is_silent_and_keeps_the_pending_invite", "verdict": "keep", "covered_by": null, "reason": "Refusal check that the pending row survives a forged accept; partly overlaps a_refused_request_changes_no_persisted_state_even_when_the_sweep_runs but asserts different behaviour (the correct accept still joins)."},
  {"name": "abandoned_invites_are_reclaimed_after_the_grace_window", "verdict": "keep", "covered_by": null, "reason": "Covers grace-window expiry and reclaim timing; unique in repo for guilds."},
  {"name": "an_expired_invite_does_not_block_a_new_one", "verdict": "keep", "covered_by": null, "reason": "Store-level re-invite after expiry; small, but the only check of that rule. Conservatively kept; could later be folded into abandoned_invites_are_reclaimed_after_the_grace_window."},
  {"name": "leader_quit_encodes_leave_and_succession_never_a_demotion", "verdict": "keep", "covered_by": null, "reason": "Checks status codes 3/4 and absence of 5 on leader quit; unique succession coverage."},
  {"name": "a_timed_out_accept_changes_no_persisted_state", "verdict": "keep", "covered_by": null, "reason": "Persistence no-change check (file bytes and dirty flag). Partly overlapping with a_refused_request_changes_no_persisted_state_even_when_the_sweep_runs (same invariant on a different refusal path), so not removable."},
  {"name": "a_refused_request_changes_no_persisted_state_even_when_the_sweep_runs", "verdict": "keep", "covered_by": null, "reason": "Refusal plus runtime-sweep invariant; it also checks the stale row reclaim, which no other test in the file asserts in this combination."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The pack's five similar files (player_trade, kart_service, social_lists, kart_npc_entry, housing_service) are other domains; none drives the guild service, and a grep of tests/ found no other GuildService test file. Overlap is only internal: the two persistence no-change tests (a_timed_out_accept..., a_refused_request...) share an invariant, and an_expired_invite_does_not_block_a_new_one is a narrower store-level version of the reclaim behaviour in abandoned_invites_are_reclaimed_after_the_grace_window. I did not read the src/guilds.rs unit tests, so unit-level duplicates were not checked; confidence is limited for that reason. No obsolescence found: the file's recovered-layout notes cite current client readers, and no later task replaced these behaviours in the pack."}
