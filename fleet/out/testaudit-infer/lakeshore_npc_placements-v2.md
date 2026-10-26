<!-- fleet job=testaudit-infer id=lakeshore_npc_placements-v2 status=blocked turns=4 usd=0.0025 tokens(read,write,in,out)=[26716, 11988, 10, 1556] model=claude-haiku-5-5 -->
# tests/lakeshore_npc_placements.rs

{"file": "tests/lakeshore_npc_placements.rs",
 "tests": [
  {"name": "every_lakeshore_legacy_row_is_drawn_at_its_position", "verdict": "keep", "covered_by": null, "reason": "Not verifiable: the file is absent at prototype/osfr-tools/tests/, and no test in the repo calls seen_from / shared_seen_from. The only shared-view placement check found is live_placements.rs::shared_view_sends_the_new_placement_once_through_the_revision, which does not cover every legacy_data Lakeshore row, so it is not a superseding match. Kept by the conservative rule (position and refusal-style canary coverage)."},
  {"name": "drawn_lakeshore_bodies_are_one_per_npc_and_a_metre_apart", "verdict": "keep", "covered_by": null, "reason": "Not verifiable: the file and its similar files (snowhill_reference_placements.rs, sanctuary_talk_spawn_placements.rs, npc_reference_spawn_placements.rs) are absent from the repo tests directory. The one-body-per-NPC and 1 m separation check cannot be compared, so it is kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.1,
 "notes": "Blocked. Checked at the current tip: tests/lakeshore_npc_placements.rs does not exist; neither does support/npc_visibility.rs (the helper module it includes), nor any function named seen_from, shared_seen_from in tests/. None of the five similar files exist at their stated paths, and their test names do not appear in the repo. Searches for the two test names returned nothing. The only overlapping-looking files in the repo are unrelated (e.g. npc_greetings_lakeshore_wilds.rs, fishing_guide_drawable.rs), and they test greetings and drawability rather than 35/2 position and separation. The pack appears to come from a different tip or branch. Both verdicts are keep by default, which is not a judged decision. Re-run against the tip that contains this file and its similar set before any removal."}
