<!-- fleet job=testaudit-infer id=field_reload_atomicity-v1 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[25609, 16892, 8, 2107] model=claude-haiku-5-5 -->
# tests/field_reload_atomicity.rs

{"file": "tests/field_reload_atomicity.rs",
 "tests": [
  {"name": "a_malformed_reload_leaves_every_field_structure_unchanged", "verdict": "keep", "covered_by": null, "reason": "Refusal and rollback check: a bad preset must leave spawners, encounter state, behaviours, dungeon content and the marker walk untouched. No other test in the similar files pins this combined rollback for battle reloads; field_battle_roster.rs::marker_collision_is_rejected_without_replacing_the_roster covers a different refusal (duplicate GUID) and checks only spawners and state."},
  {"name": "same_file_battle_reload_keeps_the_spawner_table", "verdict": "keep", "covered_by": null, "reason": "Successful-reload behaviour: same-file reload keeps spawners and consumes the open start screen. Not clearly covered elsewhere in the similar files; kept conservatively."},
  {"name": "a_battle_omitted_from_the_reload_file_is_dropped", "verdict": "keep", "covered_by": null, "reason": "Pins that a row omitted from the reload is removed along with its dungeon. Unique among the similar files; kept."},
  {"name": "a_reload_while_a_fight_is_active_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for both battle and enemy reloads during an active fight, asserting unchanged state and spawners. Refusal tests are kept."},
  {"name": "a_refused_enemy_reload_keeps_the_walk_and_attack_state", "verdict": "keep", "covered_by": null, "reason": "Refusal check that a malformed enemy file leaves walk set and attack cooldown intact, observed through tick replies. power_up_drops.rs::a_bad_reload_keeps_the_previous_tables covers pickup tables, not walk/attack state."},
  {"name": "a_successful_enemy_reload_despawns_before_it_respawns", "verdict": "keep", "covered_by": null, "reason": "Pins the 35/3 despawn ordering before respawn packets and the new position. No similar test checks this packet order; kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Excerpt was truncated, but I read the full file (480 lines) and compared the two closest overlaps (field_battle_roster.rs marker collision and enemy-reload spawner collision; power_up_drops.rs bad-reload test). Each test here checks a distinct refusal, rollback, or ordering behaviour, so none is a clear duplicate. Confidence is moderate because I did not read the full bodies of the similar tests in every file."}
