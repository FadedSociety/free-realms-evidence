<!-- fleet job=testaudit-infer id=power_up_use-v1 status=done turns=6 usd=0.0071 tokens(read,write,in,out)=[115464, 31343, 14, 3959] model=claude-haiku-5-5 -->
# tests/power_up_use.rs

{"file": "tests/power_up_use.rs",
 "tests": [
  {"name": "a_held_power_up_uses_its_own_key_once_and_restores_the_job_bar", "verdict": "keep", "covered_by": null, "reason": "Only test of the bar-1 slot-2 key path: pickup places the kind on slot 2, use consumes it once and restores the authored bar. No other file drives power-up use (grep found none)."},
  {"name": "the_f1_pickup_point_hits_the_co_located_mid_camp_wolf", "verdict": "keep", "covered_by": null, "reason": "Pins the T415 re-scope: F1 cast reaches no actor beyond two levels of the starter, MID-F1 hit leaves it alive and drops nothing. Unique geography/level assertion."},
  {"name": "the_flame_wave_burn_ticks_and_a_repeat_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Covers the burn tick and the refusal of a repeat use. Only burn coverage in the suite; body lines 584-600 were not reviewed in detail."},
  {"name": "a_level_fifteen_flame_wave_uses_the_tier_one_basic_once", "verdict": "keep", "covered_by": null, "reason": "F263 blocker regression for single application of the weapon scale; a double-multiply bug would only show here."},
  {"name": "a_difficulty_five_battle_scales_the_flame_wave_by_its_tier", "verdict": "keep", "covered_by": null, "reason": "F263 blocker: indexes damage_by_tier by battle tier, not player level. Distinct from the level-15 test (different battle tier path)."},
  {"name": "a_shielded_summoner_is_not_stunned_by_earth_shard", "verdict": "keep", "covered_by": null, "reason": "F263 finding 4 canary for the shield-blocks-stun rule; no equivalent elsewhere."},
  {"name": "a_shielded_summoner_is_not_burned_by_flame_wave", "verdict": "keep", "covered_by": null, "reason": "F263 finding 4: no burn while shielded, then the shield drops. Distinct from the stun test (burn vs stun)."},
  {"name": "earth_shard_stuns_an_enemy_and_the_stun_expires", "verdict": "keep", "covered_by": null, "reason": "Only stun and stun-expiry check for Earth Shard in the suite."},
  {"name": "super_shield_blocks_damage_for_its_window_then_expires", "verdict": "keep", "covered_by": null, "reason": "Shield window and expiry plus the HUD effect-tag byte layout. Unique."},
  {"name": "super_shield_blocks_instance_damage_for_its_window_then_expires", "verdict": "keep", "covered_by": null, "reason": "F263 finding 7: instanced-fight mitigation path, distinct from the shared-field shield test."},
  {"name": "a_use_request_with_nothing_held_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check: empty key changes nothing. Refusal tests are kept by policy."},
  {"name": "a_knocked_out_player_keeps_the_power_up_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check for a knocked-out player; kind stays held and state is unchanged."},
  {"name": "a_held_power_up_is_session_state_and_a_reconnect_clears_it", "verdict": "keep", "covered_by": null, "reason": "Persistence/design check (kind never saved). Persistence test; not covered elsewhere in this form."},
  {"name": "the_shared_field_route_uses_the_same_key_and_consumes_once", "verdict": "keep", "covered_by": null, "reason": "Shared-field route for the same power-up; distinct from the in-world route tests."},
  {"name": "a_shared_field_use_skips_an_enemy_outside_the_senders_interest", "verdict": "keep", "covered_by": null, "reason": "F263 finding 6 security/interest-set check; unique."},
  {"name": "a_derby_return_keeps_the_held_power_up_on_its_slot", "verdict": "keep", "covered_by": null, "reason": "F263 blocker: derby return must resend the bar with the held kind. Unique."},
  {"name": "held_power_up_survives_weapon_change", "verdict": "keep", "covered_by": null, "reason": "Listed in the pack (T521) but NOT found in the current file: grep for the name returned no match. Cannot classify on the body; conservatively keep. Either the pack is stale or the test was dropped in the T521 change, which should be checked."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "No other test file drives the held power-up use path (flame wave, earth shard, super shield, shared-field use, derby return); the only overlap is the drop/held-state tests in tests/power_up_drops.rs (zoning_clears_pickups_but_not_the_held_power_up, an_instance_bind_discards_ground_pickups_but_not_the_held_power_up), which cover pickup persistence rather than use. No superseded, duplicate or obsolete verdicts found. Discrepancies: the pack says 1079 lines and lists held_power_up_survives_weapon_change (T521), but the file on disk is 1027 lines and that test is absent; the pack's metadata may be stale. The file's lines 1-300 (helpers and fixture setup) and lines 584-600 (burn test body) were not read in full, so the burn test verdict rests on its name and doc comment. Confidence is moderate for that reason."}</result>
