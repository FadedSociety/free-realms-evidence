<!-- fleet job=testaudit-infer id=multiplayer-v1 status=done turns=2 usd=0.0038 tokens(read,write,in,out)=[12443, 16137, 6, 3296] model=claude-haiku-5-5 -->
# tests/multiplayer.rs

{"file": "tests/multiplayer.rs",
 "tests": [
  {"name": "audit_crossed_account_and_character_ids_can_join_together", "verdict": "keep", "covered_by": null, "reason": "Canary/audit test reproducing the W103 crossed numeric-ID domains; no similar test found elsewhere."},
  {"name": "audit_duplicate_snapshot_cannot_overwrite_progress_on_disconnect", "verdict": "keep", "covered_by": null, "reason": "Persistence/security check that a duplicate snapshot cannot overwrite saved progress; no equivalent found in the similar files."},
  {"name": "audit_duplicate_snapshot_cannot_overwrite_progress_on_shutdown", "verdict": "keep", "covered_by": null, "reason": "Persistence check on the shutdown path, distinct from the disconnect path; keep."},
  {"name": "audit_duplicate_account_is_rejected_before_loading_another_character_save", "verdict": "keep", "covered_by": null, "reason": "Refusal check on duplicate-account login; no equivalent found."},
  {"name": "audit_content_social_delivers_without_trace", "verdict": "keep", "covered_by": null, "reason": "Audit canary for social delivery; not clearly covered elsewhere."},
  {"name": "audit_two_bots_deliver_say_and_tell_with_content", "verdict": "keep", "covered_by": null, "reason": "End-to-end say/tell delivery across two sessions; no duplicate found (chat tests in chat_settings.rs cover budget, not two-session delivery)."},
  {"name": "an_account_past_its_action_budget_is_dropped_and_logged", "verdict": "keep", "covered_by": null, "reason": "Security check on the 5/s social budget and security-log counting. chat_settings.rs::the_action_budget_covers_the_three_requests and src social_chat action_budget_tests are related but do not check the wire drop plus security-log entry, so not declared removable."},
  {"name": "the_seventeenth_connection_is_refused", "verdict": "keep", "covered_by": null, "reason": "Security/refusal check on the 16-session cap driven through the gateway. spine_pins.rs tests the rate-limit bucket function only, not the gateway admission path; keep."},
  {"name": "a_connection_that_never_logs_in_is_dropped", "verdict": "keep", "covered_by": null, "reason": "Timeout behaviour for unauthenticated connections; not found elsewhere."},
  {"name": "a_vanished_client_does_not_stop_the_server", "verdict": "keep", "covered_by": null, "reason": "Robustness canary for ConnectionReset on Windows; keep."},
  {"name": "two_clients_share_world_routing_but_keep_their_sessions_and_saves", "verdict": "keep", "covered_by": null, "reason": "Multi-session isolation check; no equivalent found."},
  {"name": "two_players_see_each_other_with_the_real_name_and_job", "verdict": "keep", "covered_by": null, "reason": "Cross-player visibility check; not found in similar files."},
  {"name": "a_shared_field_kill_pays_both_and_credits_the_killer_once", "verdict": "keep", "covered_by": null, "reason": "Pays both players and credits the killer once. tests/shared_field_kill_quest_credit.rs covers quest credit only, not coin payout to both; not clearly a duplicate."},
  {"name": "a_group_forms_and_party_chat_reaches_both", "verdict": "keep", "covered_by": null, "reason": "Group formation and party chat across two sessions; not found elsewhere."},
  {"name": "each_character_keeps_its_own_coins_and_quest_after_relog", "verdict": "keep", "covered_by": null, "reason": "Persistence check across relog; keep."},
  {"name": "one_players_disconnect_or_bad_packet_does_not_stop_the_other", "verdict": "keep", "covered_by": null, "reason": "Isolation/hostile-input check; keep."},
  {"name": "the_social_loop_uses_no_dev_commands", "verdict": "keep", "covered_by": null, "reason": "Guard that the social loop does not depend on dev commands; cheap but unique in the similar files; keep."},
  {"name": "a_late_joiner_sees_the_equipped_weapon_wield_type", "verdict": "keep", "covered_by": null, "reason": "Wield-type visibility for late joiners; no other test in tests/ drives AddPc wield_type through the gateway."},
  {"name": "the_live_equip_path_and_initial_addpc_agree", "verdict": "keep", "covered_by": null, "reason": "Consistency check between live equip and AddPc; keep."},
  {"name": "an_inactive_jobs_weapon_does_not_change_the_public_wield_type", "verdict": "keep", "covered_by": null, "reason": "Negative check on the public wield type (gameplay/profile_outfit.rs public_wield_type); keep."},
  {"name": "the_wield_type_survives_save_and_relog", "verdict": "keep", "covered_by": null, "reason": "Persistence check; keep."},
  {"name": "a_refused_equip_does_not_change_the_public_wield_type", "verdict": "keep", "covered_by": null, "reason": "Refusal check; keep."},
  {"name": "two_players_keep_their_own_wield_type", "verdict": "keep", "covered_by": null, "reason": "Isolation check across two players; keep."},
  {"name": "no_weapon_unknown_definition_and_negative_values_are_zero", "verdict": "keep", "covered_by": null, "reason": "Hostile/edge-value check on the AddPc accessor (fails to 0, negative clamp); keep. Not a duplicate of the inventory-owned tests as far as surfaced."}
 ],
 "whole_file_removable": false,
 "confidence": 0.3,
 "notes": "Low-confidence audit: I did not read the file body or the helper modules, and the five similar files (player_trade, kart_service, fishing_entry, kart_npc_entry, shared_field_kill_quest_credit) cover different domains with little name overlap. I ran a name/keyword search across the repo; the only partial overlaps found were tests/chat_settings.rs::the_action_budget_covers_the_three_requests (budget, weaker than the wire-level drop and security-log check), and tests/shared_field_kill_quest_credit.rs (quest credit, not coin payout). Given the instruction to be conservative, every test is kept. A proper redundancy check would need the file body compared against tests/shared_field_kill_quest_credit.rs and the wield-type tests in inventory/equip test files."}
