<!-- fleet job=testaudit-infer id=sanctuary_named_npcs-v1 status=done turns=7 usd=0.0051 tokens(read,write,in,out)=[83280, 22100, 16, 3041] model=claude-haiku-5-5 -->
# tests/sanctuary_named_npcs.rs

{"file": "tests/sanctuary_named_npcs.rs",
 "tests": [
  {"name": "every_reference_row_is_drawn_once", "verdict": "keep", "covered_by": null, "reason": "Only test that checks all 109 reference_data rows against their extras bodies (unique spawn_guid/content_key, rotation-yaw vs heading, exactly one drawn actor, model and name ids). Other NpcVisibility::load users check their own NPCs, not this T470/T506 set."},
  {"name": "held_back_rows_stay_undrawn", "verdict": "keep", "covered_by": null, "reason": "Negative check: held-back and duplicate rows must stay undrawn. Refusal-style guard; no equivalent found in the other NpcVisibility tests."},
  {"name": "gulsh_is_the_cave_seller", "verdict": "keep", "covered_by": null, "reason": "Pins name-collision choice (Gulsh, Cragara, Tiger) and a terrain-grounded height check for Gulsh; specific to this file's data, not found elsewhere."},
  {"name": "a_click_works_where_she_stands_and_not_at_her_old_guess", "verdict": "keep", "covered_by": null, "reason": "Range-check canary: the click succeeds at the new placement and fails at the old guess. Security-style refusal check; body not readable in the pack so no removal is justified."},
  {"name": "lakeshore_merchants_and_dewey_stand_in_their_towns", "verdict": "keep", "covered_by": null, "reason": "Location assertions for the T506 moves (Lakeshore merchants, Skye, Dewey); documented regression for the POI-guess bug. Not shown to be duplicated."},
  {"name": "two_sessions_both_see_her", "verdict": "keep", "covered_by": null, "reason": "Checks per-session visibility is built independently from shared content. Could overlap with multiplayer-style visibility tests, but no named equivalent was verified, so kept conservatively."},
  {"name": "the_visibility_cap_keeps_neighbours_in_view", "verdict": "keep", "covered_by": null, "reason": "Guards the nearest-64 cap so no neighbour within 30 m drops out of view. Distinct invariant; kept."},
  {"name": "the_reference_tag_names_the_commit", "verdict": "keep", "covered_by": null, "reason": "Provenance canary that the REF tag names Sanctuary-main@10f129e. Cheap and not clearly covered elsewhere; kept conservatively."}
 ],
 "whole_file_removable": false,
 "confidence": 0.3,
 "notes": "Limited review: prototype/osfr-tools/tests/sanctuary_named_npcs.rs is not present in the repo tree (read and search both returned nothing), and the pack excerpt cuts off before the bodies of most tests. Verdicts rest on test names, doc lines and the file header. The five similar files (housing_service, multiplayer, vendor_sell, power_up_drops, piece_056) are in unrelated domains and give no superseding candidates. Several other tests call NpcVisibility::load (e.g. world.rs, npc_greetings_sanctuary.rs, priced_vendors_drawable.rs), so a body-level comparison of the visibility tests, especially two_sessions_both_see_her and the_visibility_cap_keeps_neighbours_in_view, is the next step before any removal."}
