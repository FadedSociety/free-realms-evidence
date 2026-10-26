<!-- fleet job=testaudit-infer id=npc_greetings_merry_vale_stillwater_remaining-v1 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[8327, 16847, 6, 1736] model=claude-haiku-5-5 -->
# tests/npc_greetings_merry_vale_stillwater_remaining.rs

{"file": "tests/npc_greetings_merry_vale_stillwater_remaining.rs",
 "tests": [
  {"name": "every_recovered_blank_row_is_bound_or_recorded", "verdict": "keep", "covered_by": null, "reason": "Drift guard: fails when a drawable row is blank without a recorded reason. Unique to this slice's BLANK_WITH_REASON table; no other file checks this set."},
  {"name": "each_new_greeting_is_the_npcs_own_first_person_line", "verdict": "keep", "covered_by": null, "reason": "Checks the 17 new bindings' hashes, dat lines, first-person marker, source-note provenance and no id reuse across all bindings. Covers new rows only; the similar T316 file checks different rows with a different table, so not a duplicate."},
  {"name": "the_new_greetings_are_26_3_bodies", "verdict": "keep", "covered_by": null, "reason": "Drives the real 26/8 -> 26/9 -> Talk path and the in-world router for five new rows. The similar T316 test covers other rows (9000000222 etc.), so it is not the same assertion set."},
  {"name": "the_t316_bindings_and_other_regions_are_unchanged", "verdict": "keep", "covered_by": null, "reason": "Pins T316's bindings, pre-existing owned rows and other-region samples, plus an exact owned-file binding set. Likely overlaps npc_greetings_merry_vale_stillwater.rs::the_existing_greetings_and_other_regions_are_unchanged, but I did not read that test body, so I keep it (conservative). Low-cost candidate for later pruning if that test is confirmed to assert the same ids."},
  {"name": "two_players_see_the_same_line_and_a_blank_stays_blank", "verdict": "keep", "covered_by": null, "reason": "Covers two-session isolation, a refused choice leaving the menu usable (refusal check), and a blank control sending no body. Refusal and hostile-input checks are kept by rule; the similar files' two-player tests use other rows."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Only the first 200 lines of the similar T316 file and the tail of this file were read, so overlap claims are based on test names and doc lines. The likeliest removable overlap is the_t316_bindings_and_other_regions_are_unchanged versus npc_greetings_merry_vale_stillwater.rs::the_existing_greetings_and_other_regions_are_unchanged; verifying that needs its body. Not verified: the middle of this file (lines 200-560) and the similar files' bodies beyond their test names."}
