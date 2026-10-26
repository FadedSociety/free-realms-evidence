<!-- fleet job=testaudit-infer id=coin_authoring-v1 status=blocked turns=7 usd=0.0054 tokens(read,write,in,out)=[97070, 20316, 16, 3774] model=claude-haiku-5-5 -->
# tests/coin_authoring.rs

{"file": "tests/coin_authoring.rs",
 "tests": [
  {"name": "place_binds_1950_and_a_reload_can_collect_it", "verdict": "keep", "covered_by": null, "reason": "Not audited: the file is not in the repo at prototype/osfr-tools/tests/coin_authoring.rs, so its assertions could not be compared."},
  {"name": "move_2115_repoints_2039_and_hides_the_old_guid", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "list_names_the_nearest_live_coin", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "unbind_removes_the_overlay_row_and_its_actor", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "moved_coin_is_hidden_from_a_player_who_collected_the_entry", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal test; kept by policy. Same-named tests exist in job_level_quest.rs, sheep_watch_dungeon.rs and station_cash.rs but they are not verified to match."},
  {"name": "a_second_session_sees_the_coin_after_its_poll", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "live_guids_are_unique_against_content_and_placements", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "an_oversized_overlay_is_refused_at_load", "verdict": "keep", "covered_by": null, "reason": "Security/refusal test; kept by policy."},
  {"name": "a_hostile_overlay_row_is_refused", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal test; kept by policy."},
  {"name": "a_failed_write_leaves_the_file_and_the_view", "verdict": "keep", "covered_by": null, "reason": "Persistence/refusal test; kept by policy."},
  {"name": "a_second_admin_writing_before_a_poll_keeps_the_first_row", "verdict": "keep", "covered_by": null, "reason": "Persistence test; kept by policy."},
  {"name": "moving_a_content_coin_removes_it_from_a_viewer_who_saw_it", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "moving_a_content_coin_removes_it_from_the_acting_session", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "a_live_row_moves_to_a_new_guid_and_keeps_its_replaces", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "unbinding_a_replacing_row_removes_it", "verdict": "keep", "covered_by": null, "reason": "Not audited: source missing."},
  {"name": "an_unbound_live_guid_is_never_reused", "verdict": "keep", "covered_by": null, "reason": "Canary/persistence test; kept by policy."},
  {"name": "a_damaged_overlay_is_refused_not_overwritten", "verdict": "keep", "covered_by": null, "reason": "Refusal test; kept by policy."},
  {"name": "an_unbound_guid_is_not_reused_in_an_overlay_without_a_counter", "verdict": "keep", "covered_by": null, "reason": "Compatibility/canary test; kept by policy."}
 ],
 "whole_file_removable": false,
 "confidence": 0.0,
 "notes": "The audit could not be performed. The pack names tests/coin_authoring.rs (created T525, changed F717), but the file does not exist at prototype/osfr-tools/tests/coin_authoring.rs in the repo tip. Read calls on it return 'not a file', and searches find no collection_coin_edits, next_guid, 'Placed coin', or 'realm coin' in the repo's src or tests. The 'realm coin place/move' command and the collection_coin_edits.json overlay do not appear to exist at the tip, so the file may have been removed or was never merged. The 'keep' verdicts are a default, not a finding. Please confirm whether the file or the feature exists on another branch before re-running this audit. The similar-file list also cites tests/kart_service.rs, tests/player_trade.rs, tests/kart_npc_entry.rs, tests/housing_service.rs and tests/fishing_entry.rs, which were not compared. Overlap candidates for the closest coin-adjacent feature are tests/live_placements.rs and tests/collection_coin_pickup.rs, which were not read."}
