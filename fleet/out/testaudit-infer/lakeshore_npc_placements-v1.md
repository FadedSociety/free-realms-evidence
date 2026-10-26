<!-- fleet job=testaudit-infer id=lakeshore_npc_placements-v1 status=blocked turns=7 usd=0.0031 tokens(read,write,in,out)=[46674, 11815, 16, 2274] model=claude-haiku-5-5 -->
# tests/lakeshore_npc_placements.rs

{"file": "tests/lakeshore_npc_placements.rs",
 "tests": [
  {"name": "every_lakeshore_legacy_row_is_drawn_at_its_position", "verdict": "keep", "covered_by": null, "reason": "Could not locate the file or any comparison file in the repo, so no superseding test could be confirmed. Kept by default. It appears to be the only check that each legacy_data Lakeshore row reaches a player at its own position in both update and shared_view, and it has a non-vacuity assert."},
  {"name": "drawn_lakeshore_bodies_are_one_per_npc_and_a_metre_apart", "verdict": "keep", "covered_by": null, "reason": "Could not locate the file or the similar files (snowhill_reference_placements.rs::drawn_npc_rows_do_not_share_a_position, sanctuary_talk_spawn_placements.rs::no_two_drawn_npc_rows_share_a_position, npc_reference_spawn_placements.rs::no_two_drawn_regional_npc_rows_share_a_position) to compare. Those names suggest overlap on the 1 m separation check, but the one-body-per-NPC check is specific to this file. Kept by default."}
 ],
 "whole_file_removable": false,
 "confidence": 0.1,
 "notes": "Blocked. The target file tests/lakeshore_npc_placements.rs does not exist in the repo (searches for its test names and for the excerpt's helpers found nothing under prototype/osfr-tools/tests). None of the five similar files (snowhill_reference_placements.rs, sanctuary_talk_spawn_placements.rs, npc_reference_spawn_placements.rs, and two others) exist at those paths either, and their test names did not match anything in the tests directory. Both verdicts are therefore keep by default and are based only on the pack's excerpt and doc lines, not on the source. Also not verified: whether support/npc_visibility.rs exposes seen_from, shared_seen_from, and content_key as the excerpt uses them. The three placement files named as similar probably overlap heavily with each other and should be audited together once they can be found. Rerun this audit against the correct tip or branch."}
