<!-- fleet job=testaudit-infer id=sanctuary_talk_spawn_placements-v1 status=done turns=5 usd=0.0032 tokens(read,write,in,out)=[38667, 11713, 12, 2678] model=claude-haiku-5-5 -->
# tests/sanctuary_talk_spawn_placements.rs

{"file": "tests/sanctuary_talk_spawn_placements.rs",
 "tests": [
  {"name": "every_placed_row_is_drawn_at_its_position", "verdict": "keep", "covered_by": null,
   "reason": "Only check that the two marker-selected sanctuary.json rows are legacy_data spawns drawn by NpcVisibility at their cited spawnNpcWithGuid transform, with the 35/2 AddNpc carrying the cited model and name ids. Sibling tests (snowhill_reference_placements::every_row_this_brief_placed_is_drawn_at_its_spawn_position, npc_reference_spawn_placements::placed_rows_match_the_cited_spawn_and_the_loader_draws_them) look similar but select different rows, so I could not name an equally strong test covering these rows. Could not read the sibling bodies at this tip to confirm."},
  {"name": "no_two_drawn_npc_rows_share_a_position", "verdict": "keep", "covered_by": null,
   "reason": "Whole-world 1 m duplicate latch over keyed rows against every drawn body, with a recorded KNOWN_CLOSE_PAIRS exception list. Likely overlaps snowhill_reference_placements::drawn_npc_rows_do_not_share_a_position and npc_reference_spawn_placements::no_two_drawn_regional_npc_rows_share_a_position, but those scope and exception handling could not be read, so it is kept under the conservative rule (duplicate-rule canary)."}
 ],
 "whole_file_removable": false,
 "confidence": 0.3,
 "notes": "The repo tip does not contain this file or its sibling files (read and search return 'not a file' / no matches for tests/sanctuary_talk_spawn_placements.rs, support/placement.rs and the sibling test names), so the verdicts rest on the pack excerpt and names only. The excerpt is truncated mid-way through the second test. Verify the sibling bodies (snowhill_reference_placements.rs, npc_reference_spawn_placements.rs, lakeshore_npc_placements.rs) before removing anything; the most likely real duplicates are the three per-slice 'drawn at its position' and '1 m apart' tests in those files."}
