<!-- fleet job=testaudit-infer id=field_camp_separation-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[9147, 14602, 6, 1286] model=claude-haiku-5-5 -->
# tests/field_camp_separation.rs

{"file": "tests/field_camp_separation.rs",
 "tests": [
  {"name": "no_field_camp_shares_ground_with_a_band_more_than_two_levels_away", "verdict": "keep", "covered_by": null, "reason": "Only test that checks pairwise spacing of every shipped field actor across bands more than two levels apart, using leash + aggro + chase margin. The similar files (field_camps_high_band, field_camps_elite_band, field_enemy_level_camps) check their own band populations and rewards, not cross-band separation. Not clearly covered elsewhere; kept conservatively."},
  {"name": "low_difficulty_battle_markers_are_clear_of_higher_bands", "verdict": "keep", "covered_by": null, "reason": "Unique check that difficulty 1-2 battle markers and the giver-to-world-enemy walks (F621) stay clear of higher-band camps. It is the only test that reads the opening giver positions and encounters.json walks. The fixture-vs-production drift it cannot see is a note, not a reason to remove it."},
  {"name": "a_level_three_player_at_each_starter_camp_is_hit_only_by_its_own_band", "verdict": "keep", "covered_by": null, "reason": "Behavioural canary that drives the real shared-field tick from each of the 12 W102 starter centres and asserts only starter-band attackers hit, at the authored scaled damage. It is the only test here that exercises live hit packets. Similar files check populations and rewards, not hit attribution."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "All three tests are distinct, and no similar file was shown to assert the same cross-band separation, low-level walk, or starter hit attribution. I read only the tail of the file and did not open field_camps_elite_band.rs or field_enemy_level_camps.rs to compare assertions line by line, so a partial overlap with those files is possible. The low-level walk test takes its opening givers from tests/fixtures/quests/opening.json, not shipped content, so it can drift from production; that is a fidelity risk, not a redundancy. Lower confidence reflects that comparison gap."}
