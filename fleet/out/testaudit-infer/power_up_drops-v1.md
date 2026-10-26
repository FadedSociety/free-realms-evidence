<!-- fleet job=testaudit-infer id=power_up_drops-v1 status=done turns=3 usd=0.0055 tokens(read,write,in,out)=[33894, 25276, 8, 3912] model=claude-haiku-5-5 -->
# tests/power_up_drops.rs

{"file": "tests/power_up_drops.rs", "tests": [
{"name": "kill_spawns_a_pickup_actor_with_the_kind_model_at_the_kill", "verdict": "keep", "covered_by": null, "reason": "Only check that a kill spawns a pickup actor with the table's model at the kill position; no equivalent test found in power_ups.rs (which tests table parsing and roll logic, not spawning)."},
{"name": "pickup_actors_carry_no_kind_names", "verdict": "keep", "covered_by": null, "reason": "Canary tied to the T375 client-reader finding (empty name_string_id shows literal npc_name). Must stay."},
{"name": "kinds_use_their_own_models", "verdict": "keep", "covered_by": null, "reason": "Only test pinning per-kind model mapping in this file's path; not clearly covered elsewhere."},
{"name": "enemies_without_a_usable_table_drop_nothing", "verdict": "keep", "covered_by": null, "reason": "Negative path (no or unusable table yields no drop); not seen duplicated in the similar files."},
{"name": "an_unloaded_engine_drops_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal/unloaded-state check; keep."},
{"name": "walking_onto_the_big_heart_heals_from_the_server_position_and_asks_for_the_group", "verdict": "keep", "covered_by": null, "reason": "Pins heal from server position and group-heal request; only check of this path here."},
{"name": "the_small_heart_heals_only_the_player", "verdict": "keep", "covered_by": null, "reason": "Behavioural check distinct from big-heart group heal; keep."},
{"name": "energy_pickup_adds_energy_up_to_the_bar", "verdict": "keep", "covered_by": null, "reason": "Only check of energy pickup capping at the bar in this file's path; keep."},
{"name": "only_one_stored_kind_is_held_and_a_refused_pickup_stays_on_the_ground", "verdict": "keep", "covered_by": null, "reason": "Refusal check (one held kind, refused pickup stays); keep."},
{"name": "unclaimed_pickups_despawn_after_the_ttl_and_cannot_be_taken_late", "verdict": "keep", "covered_by": null, "reason": "Expiry/deadline-ordering check; keep."},
{"name": "a_refused_pickup_also_despawns_on_its_ttl", "verdict": "keep", "covered_by": null, "reason": "Expiry of refused pickup; distinct from the plain TTL test. Keep."},
{"name": "the_ground_holds_at_most_max_alive_pickups", "verdict": "keep", "covered_by": null, "reason": "Bound check on ground pickups. Could be argued to overlap with power_ups.rs bound tests, but it drives the engine cap; keep conservatively."},
{"name": "zoning_clears_pickups_but_not_the_held_power_up", "verdict": "keep", "covered_by": null, "reason": "Persistence/state-separation check; keep."},
{"name": "an_instance_bind_discards_ground_pickups_but_not_the_held_power_up", "verdict": "keep", "covered_by": null, "reason": "Scene-reload discard and held-state persistence; keep."},
{"name": "a_revive_or_same_instance_transfer_reload_discards_ground_pickups", "verdict": "keep", "covered_by": null, "reason": "Scene-reload discard on revive/transfer; keep."},
{"name": "a_bad_reload_keeps_the_previous_tables", "verdict": "keep", "covered_by": null, "reason": "Refusal check: bad reload leaves prior tables intact; keep."},
{"name": "shipped_enemy_content_only_names_shipped_tables", "verdict": "keep", "covered_by": null, "reason": "Content-integrity canary over shipped enemy data; power_ups.rs::shipped_file_loads_and_references_resolve checks power_ups.json internal references, not the enemy files, so not equivalent."},
{"name": "every_participant_gets_their_own_pickup_and_nobody_sees_anothers", "verdict": "keep", "covered_by": null, "reason": "Multi-participant personal-pickup and canary check; keep."},
{"name": "a_bystander_who_never_hit_the_enemy_gets_nothing", "verdict": "keep", "covered_by": null, "reason": "Security/refusal check for non-participants; keep."},
{"name": "only_recent_damage_counts_as_taking_part", "verdict": "keep", "covered_by": null, "reason": "Participation window boundary check; keep."},
{"name": "a_participant_who_left_the_field_loses_the_drop", "verdict": "keep", "covered_by": null, "reason": "Refusal check on departed participants; keep."},
{"name": "an_unclaimed_drop_lapses", "verdict": "keep", "covered_by": null, "reason": "Lapse-after-window check; keep."},
{"name": "the_group_multiplier_thins_shared_rolls_but_not_solo_ones_or_guaranteed_ones", "verdict": "keep", "covered_by": null, "reason": "Statistical multi-property check of the group multiplier; not duplicated elsewhere in the pack."},
{"name": "participation_settings_are_bounded", "verdict": "keep", "covered_by": null, "reason": "Bounds refusal check for participation settings. power_ups.rs::every_bound_rejects_a_bad_file may overlap in spirit, but the participation block is not confirmed there; keep conservatively."},
{"name": "roll_scaled_scales_chances_only", "verdict": "keep", "covered_by": null, "reason": "Tests roll_scaled, a different function from power_ups.rs roll tests (plain roll, determinism, distribution); keep."},
{"name": "pickups_do_not_follow_the_player_into_another_zone", "verdict": "keep", "covered_by": null, "reason": "Zone-boundary persistence check; keep."},
{"name": "big_hearts_from_one_kill_share_a_kill_key_so_the_group_heals_once", "verdict": "keep", "covered_by": null, "reason": "Group heal de-duplication canary; keep."},
{"name": "a_group_heal_restores_a_hurt_member_and_is_silent_at_full_health", "verdict": "keep", "covered_by": null, "reason": "Heal and silent-at-full-health check; keep."}
],
"whole_file_removable": false, "confidence": 0.6, "notes": "The similar-file pack was dominated by unrelated suites (kart, fishing, housing, coin store, trade); none drives power-up drops. The only real neighbour is tests/power_ups.rs (parsing/roll unit tests: every_bound_rejects_a_bad_file, roll_distribution, zero_chance_never_drops, guaranteed_drops_always_come_first), which may overlap on bounds and roll-scaling but was only checked by test name, not assertion. Given the instruction to be conservative, every test is kept. Candidates for a later, deeper comparison: participation_settings_are_bounded vs power_ups::every_bound_rejects_a_bad_file, and roll_scaled_scales_chances_only vs power_ups::roll_distribution_matches_chances_and_weights. No obsolete tests were found: nothing here pins behaviour a later task replaced. The file was last changed by F641 and the excerpt was truncated, so tests after the first 300 lines were read directly from the file."}
