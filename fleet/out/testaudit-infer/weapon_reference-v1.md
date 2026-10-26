<!-- fleet job=testaudit-infer id=weapon_reference-v1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6950, 11703, 6, 968] model=claude-haiku-5-5 -->
# tests/weapon_reference.rs

{"file": "tests/weapon_reference.rs",
 "tests": [
  {"name": "every_weapon_and_attack_row_has_a_source", "verdict": "keep", "covered_by": null, "reason": "Only test that reads data/reference/weapons.json and attacks.json. It checks row count, schema version, source citations, and recomputes the power agreement flag from each row. No other test in the suite touches these tables (grep for weapons.json/attacks.json finds only this file). Its partial overlap with the similar files (piece_056, ride_sources, piece_065, piece_028, piece_008) is in unrelated domains."},
  {"name": "job_ability_multipliers_match_the_live_ratios", "verdict": "keep", "covered_by": null, "reason": "Only check that job_abilities.json damage multipliers agree with the wiki attack ratios. It also contains a canary that proves the checker flags a bad multiplier with no explanation. Other tests load job_abilities.json for behaviour (job_basic_attacks, opening_abilities, weapon_requirements, job_trainers), not for this ratio cross-check, and the canary is not repeated anywhere else."}
 ],
 "whole_file_removable": false,
 "confidence": 0.85,
 "notes": "Both tests cover reference data that no other test file validates, so nothing is redundant. The file is small (141 lines, two tests, no crate modules or shared helpers). The agent notes in notes/Autopilot/T635.md confirm the file was added with the reference build and that both tests pass. Neither test has a later task that replaced it. Confidence is lower because I only compared test names and grep results, not the full bodies of the similar files."}
