<!-- fleet job=testaudit-infer id=field_enemy_budget-v1 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[6622, 8532, 6, 996] model=claude-haiku-5-5 -->
# tests/field_enemy_budget.rs

{"file": "tests/field_enemy_budget.rs",
 "tests": [
  {"name": "starter_enemies_and_camps_stay_inside_the_final_era_budget", "verdict": "keep", "covered_by": null, "reason": "The only test in the suite that checks the (R) time-to-knock-out budget for starter field enemies and starter camps, measured from the live engine (player health after set_player_job, hits from attack_processed). The similar files pin content identity, loader bounds, banding, separation and shared-state behaviour, not the combat-time floor. Nothing else drives this path with these assertions, so it is not superseded or duplicate. Bounds check, not a redundant copy."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Single test, created and last changed by T398. Its doc describes the budget as tunable bounds, so a later retuning of combat_scale.json or the budget constants would legitimately break it; that is a maintenance cost, not redundancy. The nearest file, tests/field_enemy_level_camps.rs (T245/T699), pins level bands, GUIDs, loader bounds and balance rows for the same content but does not assert time-to-knock-out. Searching the repo for the budget constants and the 'knocks out' assertion found no other test with these floors. Not checked: whether tests/field_camp_separation.rs or the power_up_drops suite compute player-kill timing in a way that overlaps; the excerpts I saw do not."}
