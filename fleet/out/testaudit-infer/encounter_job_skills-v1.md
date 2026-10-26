<!-- fleet job=testaudit-infer id=encounter_job_skills-v1 status=done turns=4 usd=0.0049 tokens(read,write,in,out)=[46881, 21587, 10, 3399] model=claude-haiku-5-5 -->
# tests/encounter_job_skills.rs

{"file": "tests/encounter_job_skills.rs",
 "tests": [
  {"name": "unbuffed_critical_damage_keeps_existing_integer_rounding", "verdict": "keep", "covered_by": null, "reason": "Pins x1.5 crit rounding-down on an odd basic hit; no other test in the sampled files asserts this integer rounding path."},
  {"name": "self_heal_clamps_and_scales_with_the_existing_hp_curve", "verdict": "keep", "covered_by": null, "reason": "Checks heal clamping at max HP and the cooldown reply bytes; no equivalent self-heal assertion found in sampled files."},
  {"name": "area_damage_hits_each_in_radius_once_and_honours_target_limit", "verdict": "keep", "covered_by": null, "reason": "Only direct check of max_targets cap for area_damage in this file; shared_field_state.rs uses area_damage in a broader scenario but does not assert the cap in isolation (not verified line by line)."},
  {"name": "dot_ticks_on_deadlines_and_does_not_consume_basic_swing_gate", "verdict": "keep", "covered_by": null, "reason": "Asserts DoT deadline timing and that DoT does not consume the basic attack gate; field_enemies_runtime.rs only checks DoT clearing, not this timing contract."},
  {"name": "stun_stops_attacks_and_movement_until_exact_expiry", "verdict": "keep", "covered_by": null, "reason": "Exact-expiry boundary (1900 blocked, 2000 free). field_enemies_runtime.rs stun checks are clear/respawn-oriented, not the expiry boundary."},
  {"name": "target_vitals_debuff_only_increases_damage_on_its_target_and_expires", "verdict": "keep", "covered_by": null, "reason": "Checks the debuff affects only its target and expires; a scope/refusal-style check not duplicated in sampled files."},
  {"name": "critical_buff_affects_chance_and_damage_and_clears_on_job_change", "verdict": "keep", "covered_by": null, "reason": "Asserts crit buff clears on job change, a distinct behaviour from reset/knockout paths."},
  {"name": "pure_dot_arms_an_arena_and_stops_at_victory_without_repeating_rewards", "verdict": "keep", "covered_by": null, "reason": "Reward-once and victory-stop persistence/canary-style check; not reviewed in full (body truncated in pack) so kept by default."},
  {"name": "buff_changes_damage_and_mitigation_then_expires_without_stacking", "verdict": "keep", "covered_by": null, "reason": "Non-stacking refusal-style assertion on buffs; kept conservatively."},
  {"name": "invalid_range_cooldown_and_unavailable_summon_do_not_spend_or_damage", "verdict": "keep", "covered_by": null, "reason": "Refusal check: invalid range, cooldown and unavailable summon spend nothing. Security/refusal category; kept."},
  {"name": "knockout_clears_skill_effects", "verdict": "keep", "covered_by": null, "reason": "Knockout path with revive and 8 s grace; field_enemies_runtime.rs covers kill-respawn, evade-completion and reload clearing but not the player knockout/revive path."},
  {"name": "reset_session_clears_skill_effects", "verdict": "keep", "covered_by": null, "reason": "Only sampled test that calls EncounterEngine::reset_session and checks effect clearing; not covered by the field_enemies_runtime clear tests."},
  {"name": "medic_wins_using_skills", "verdict": "keep", "covered_by": null, "reason": "Per-job end-to-end win via job bar across ladder levels; thin wrapper over job_wins. Possibly overlaps battle_catalogue_audit.rs (not inspected), so kept conservatively."},
  {"name": "warrior_wins_using_skills", "verdict": "keep", "covered_by": null, "reason": "Same job_wins path as medic; per-profile coverage. Possible overlap with battle_catalogue_audit.rs not verified."},
  {"name": "wizard_wins_using_skills", "verdict": "keep", "covered_by": null, "reason": "Same job_wins path; per-profile coverage. Possible overlap with battle_catalogue_audit.rs not verified."},
  {"name": "ninja_wins_using_skills", "verdict": "keep", "covered_by": null, "reason": "Same job_wins path; per-profile coverage. Possible overlap with battle_catalogue_audit.rs not verified."},
  {"name": "brawler_wins_using_skills", "verdict": "keep", "covered_by": null, "reason": "Same job_wins path; per-profile coverage. battle_catalogue_audit.rs uses BRAWLER at max level, overlap possible but not confirmed."},
  {"name": "archer_wins_using_skills", "verdict": "keep", "covered_by": null, "reason": "Same job_wins path; per-profile coverage. Possible overlap with battle_catalogue_audit.rs not verified."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Searched for overlap in other test files. The DoT, stun, and clear-on-reset/respawn scenarios have partial overlap in field_enemies_runtime.rs (kill_then_respawn_forgets_skill_effects, evade_completion_forgets_skill_effects, reload_field_enemies_forgets_skill_effects), but those assert clearing rather than the timing or expiry boundaries, so they are not marked superseded. The six job_wins tests are thin wrappers around one helper; they could be consolidated into a single parameterised test, but battle_catalogue_audit.rs was not inspected and may cover the same job-bar wins. Full bodies of the last test (pure_dot_arms_an_arena...) and buff_changes_damage... were not read in full; verdicts there are conservative. Confidence is low-moderate because only a partial comparison was done."}
]}
