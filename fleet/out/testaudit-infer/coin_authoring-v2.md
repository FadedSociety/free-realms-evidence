<!-- fleet job=testaudit-infer id=coin_authoring-v2 status=blocked turns=3 usd=0.0033 tokens(read,write,in,out)=[26775, 14712, 8, 2453] model=claude-haiku-5-5 -->
# tests/coin_authoring.rs

{"file": "tests/coin_authoring.rs",
 "tests": [
  {"name": "place_binds_1950_and_a_reload_can_collect_it", "verdict": "keep", "covered_by": null, "reason": "Could not compare assertions: the file is not in the repo at prototype/osfr-tools/tests/coin_authoring.rs (read and search both return nothing). Kept by default."},
  {"name": "move_2115_repoints_2039_and_hides_the_old_guid", "verdict": "keep", "covered_by": null, "reason": "Source missing; kept by default."},
  {"name": "list_names_the_nearest_live_coin", "verdict": "keep", "covered_by": null, "reason": "Source missing; kept by default."},
  {"name": "unbind_removes_the_overlay_row_and_its_actor", "verdict": "keep", "covered_by": null, "reason": "Source missing; kept by default."},
  {"name": "moved_coin_is_hidden_from_a_player_who_collected_the_entry", "verdict": "keep", "covered_by": null, "reason": "Source missing; kept by default."},
  {"name": "refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check; kept by policy."},
  {"name": "a_second_session_sees_the_coin_after_its_poll", "verdict": "keep", "covered_by": null, "reason": "Source missing; kept by default."},
  {"name": "live_guids_are_unique_against_content_and_placements", "verdict": "keep", "covered_by": null, "reason": "Uniqueness invariant; kept by policy."},
  {"name": "an_oversized_overlay_is_refused_at_load", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal; kept by policy."},
  {"name": "a_hostile_overlay_row_is_refused", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal (model id must fit i32); kept by policy."},
  {"name": "a_failed_write_leaves_the_file_and_the_view", "verdict": "keep", "covered_by": null, "reason": "Persistence/refusal check; kept by policy."},
  {"name": "a_second_admin_writing_before_a_poll_keeps_the_first_row", "verdict": "keep", "covered_by": null, "reason": "Persistence check; kept by policy."},
  {"name": "moving_a_content_coin_removes_it_from_a_viewer_who_saw_it", "verdict": "keep", "covered_by": null, "reason": "Visibility behaviour; source missing, kept by default."},
  {"name": "moving_a_content_coin_removes_it_from_the_acting_session", "verdict": "keep", "covered_by": null, "reason": "Visibility behaviour; source missing, kept by default."},
  {"name": "a_live_row_moves_to_a_new_guid_and_keeps_its_replaces", "verdict": "keep", "covered_by": null, "reason": "Source missing; kept by default."},
  {"name": "unbinding_a_replacing_row_removes_it", "verdict": "keep", "covered_by": null, "reason": "Source missing; kept by default."},
  {"name": "an_unbound_live_guid_is_never_reused", "verdict": "keep", "covered_by": null, "reason": "Canary/persistence invariant; kept by policy."},
  {"name": "a_damaged_overlay_is_refused_not_overwritten", "verdict": "keep", "covered_by": null, "reason": "Refusal check (no overwrite of unreadable overlay); kept by policy."},
  {"name": "an_unbound_guid_is_not_reused_in_an_overlay_without_a_counter", "verdict": "keep", "covered_by": null, "reason": "Legacy-overlay guard against GUID reuse; kept by policy."}
 ],
 "whole_file_removable": false,
 "confidence": 0.1,
 "notes": "Blocked: prototype/osfr-tools/tests/coin_authoring.rs does not exist in the repo (read returns 'not a file'; search for test names returns no matches). The only copies are in the audit pack data (quest-lines/testaudit-packs.json), which has the names, doc lines and excerpt but not the test bodies, so assertions cannot be compared against the similar files (kart_service, player_trade, kart_npc_entry, housing_service, fishing_entry). Every verdict is keep by default. The file's own doc lines name the coin tests as security/refusal/persistence checks, which supports keeping them. Re-run once the file is present in the repo to get real superseded/duplicate verdicts. The earlier partial answer for this file also said 'source missing' and is not a verified audit."}
