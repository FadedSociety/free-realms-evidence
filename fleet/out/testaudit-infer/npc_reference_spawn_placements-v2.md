<!-- fleet job=testaudit-infer id=npc_reference_spawn_placements-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[9291, 9650, 6, 1175] model=claude-haiku-5-5 -->
# tests/npc_reference_spawn_placements.rs

{"file": "tests/npc_reference_spawn_placements.rs",
 "tests": [
  {"name": "placed_rows_match_the_cited_spawn_and_the_loader_draws_them", "verdict": "keep", "covered_by": null, "reason": "Checks the T698-marked rows against their cited FabledRealms.lua spawn line (position, heading, model id) and that NpcVisibility::load draws them. No equally strong test was found that covers this brief's marker-scoped rows. The sibling snowhill and sanctuary files cover other row sets."},
  {"name": "no_two_drawn_regional_npc_rows_share_a_position", "verdict": "keep", "covered_by": null, "reason": "The earlier duplicate verdict is withdrawn. It cited tests/snowhill_reference_placements.rs::no_two_drawn_regional_npc_rows_share_a_position, which the pack does not list. The pack lists drawn_npc_rows_do_not_share_a_position in that file instead. The name was not verified in the repository, so the claimed equivalence is unproven. Kept conservatively."}
 ],
 "whole_file_removable": false,
 "confidence": 0.3,
 "notes": "The file tests/npc_reference_spawn_placements.rs and the Snowhill file are not in the repo checkout (search for the test names returned nothing; read reports the path is not a file). The test bodies beyond the excerpt could not be inspected, so no removal can be justified. The previous duplicate verdict cited a test name that does not match the pack's listing and was retracted. Verify against a checkout that contains the file before any removal. Lakeshore's drawn_lakeshore_bodies_are_one_per_npc_and_a_metre_apart is lakeshore-scoped and was not compared."}
