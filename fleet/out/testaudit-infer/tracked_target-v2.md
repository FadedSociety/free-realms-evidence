<!-- fleet job=testaudit-infer id=tracked_target-v2 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[28493, 16695, 8, 2716] model=claude-haiku-5-5 -->
# tests/tracked_target.rs

{"file": "tests/tracked_target.rs",
 "tests": [
  {"name": "active_pin_has_the_recovered_47_14_layout", "verdict": "keep", "covered_by": null, "reason": "Pure encoder canary with a synthetic pin; checks field offsets directly. w64 covers only one talk pin's bytes."},
  {"name": "no_pin_is_the_four_byte_clear", "verdict": "keep", "covered_by": null, "reason": "Clear-packet canary; w64 take_me_there_pin_follows_the_selected_quest only checks it via gameplay."},
  {"name": "talk_and_interact_objectives_point_at_the_npc", "verdict": "keep", "covered_by": null, "reason": "Interact branch not covered elsewhere; talk branch is only partly covered by w64."},
  {"name": "kill_objectives_point_at_the_field_enemies_home", "verdict": "superseded", "covered_by": "src/gameplay/w64_regional_quest_tests.rs::kill_objective_pins_its_field_enemy", "reason": "Same KillActorKind path asserted end to end: guid bytes and position bytes against field_enemies.json home. Checked in source; w64 asserts at least as much."},
  {"name": "reach_poi_and_visit_position_use_their_own_geometry", "verdict": "keep", "covered_by": null, "reason": "ReachPoi and VisitPosition geometry not found in other tests."},
  {"name": "dungeon_objectives_point_at_their_battle_marker", "verdict": "keep", "covered_by": null, "reason": "CompleteDungeon to battle marker not found in other tests."},
  {"name": "a_battle_only_kill_points_at_its_battle_marker", "verdict": "superseded", "covered_by": "src/gameplay/w64_regional_quest_tests.rs::a_battle_only_kill_objective_pins_its_battle_marker", "reason": "Same kind 930096 to battle-96 marker path; w64 checks guid, position and zone 0 bytes. Checked in source."},
  {"name": "a_field_enemy_still_wins_over_a_battle_marker", "verdict": "superseded", "covered_by": "src/gameplay/w64_regional_quest_tests.rs::kill_objective_pins_its_field_enemy", "reason": "w64 uses kind 930050, which has both a field home and a battle, and asserts the field home guid and position. Same precedence check through the full path."},
  {"name": "unknown_battles_and_battle_kinds_pin_nothing", "verdict": "keep", "covered_by": null, "reason": "Negative lookup for unknown encounter and kind ids; not covered elsewhere."},
  {"name": "objectives_without_a_known_place_locate_nothing", "verdict": "keep", "covered_by": null, "reason": "Broad no-guess table over many kinds; w64 an_objective_without_a_known_place_sends_no_pin covers one gather step only."},
  {"name": "a_position_that_is_not_finite_is_never_sent", "verdict": "keep", "covered_by": null, "reason": "Hostile-input check: NaN and infinities are never sent."},
  {"name": "only_the_selected_quests_open_objectives_are_tracked", "verdict": "keep", "covered_by": null, "reason": "Unit-level selection and refusal rules (no selection, no open objectives, unlocated objective). Not covered at this level elsewhere; not verified line by line because the previous answer was truncated here."},
  {"name": "a_place_in_another_zone_is_not_pinned", "verdict": "keep", "covered_by": null, "reason": "Zone-gating check for tracked_pin; not verified elsewhere, so kept."},
  {"name": "the_tracker_sends_changes_clears_and_nothing_else", "verdict": "keep", "covered_by": null, "reason": "Send-once, clear-once and silence behaviour of Tracker. Not found elsewhere."},
  {"name": "a_new_session_sends_the_pin_again", "verdict": "keep", "covered_by": null, "reason": "Reconnect behaviour: tracker state is not persisted. Kept as a persistence-style check."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Three tests are superseded by w64_regional_quest_tests.rs (kill field home, battle-only kill, field-beats-battle); I checked those w64 bodies in source. The w64 tests are inside src/, not tests/, so they are not separate test binaries but do run in the suite. The pack's previous_answer was truncated after only_the_selected_quests, so the verdicts for the last four tests were reached independently and not checked against a prior answer. The file's unit-level checks on the encoder, the negative lookups and the tracker are not duplicated, so the file should stay."}
