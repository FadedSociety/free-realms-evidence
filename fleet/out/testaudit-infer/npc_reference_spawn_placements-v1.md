<!-- fleet job=testaudit-infer id=npc_reference_spawn_placements-v1 status=done turns=8 usd=0.0043 tokens(read,write,in,out)=[69413, 15326, 18, 3417] model=claude-haiku-5-5 -->
# tests/npc_reference_spawn_placements.rs

{"file": "tests/npc_reference_spawn_placements.rs",
 "tests": [
  {"name": "placed_rows_match_the_cited_spawn_and_the_loader_draws_them", "verdict": "keep", "covered_by": null, "reason": "Checks the T698-marked rows against their cited FabledRealms.lua spawn line (position, heading, model id) and that NpcVisibility::load draws them. The sibling snowhill_reference_placements.rs::every_row_this_brief_placed_is_drawn_at_its_spawn_position uses the same idea but over a different zone set (Snowhill rows), so this is not a full duplicate. Kept conservatively; the marker scan is shared with the Sanctuary/Snowhill briefs, so a partial overlap on any shared zone file is possible."},
  {"name": "no_two_drawn_regional_npc_rows_share_a_position", "verdict": "duplicate", "covered_by": "tests/snowhill_reference_placements.rs::no_two_drawn_regional_npc_rows_share_a_position", "reason": "Same name and same global scan: every drawn regional NPC row in content/npcs is checked for no two within 1 m. It is not scoped to this brief's rows, so the Snowhill copy asserts the same property over the same data. Its assertions are the same, so it adds only redundant runtime."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Only the excerpt, the two test names and the similar-file metadata were readable. The repository checkout does not contain this file (search found no npc_reference_spawn_placements.rs under prototype/osfr-tools/tests), so the bodies of the test functions past the excerpt were not inspected, and the snowhill/sanctuary test bodies were not compared line by line. The duplicate verdict rests on matching names and the global scope of the test; confirm the assertions before removing. Lakeshore's drawn_lakeshore_bodies_are_one_per_npc_and_a_metre_apart is lakeshore-scoped and was not treated as a duplicate."}
