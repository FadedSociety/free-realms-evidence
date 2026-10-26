<!-- fleet job=testaudit-infer id=npc_greetings_highroad_farnum-v1 status=done turns=2 usd=0.0033 tokens(read,write,in,out)=[8159, 18174, 6, 1900] model=claude-haiku-5-5 -->
# tests/npc_greetings_highroad_farnum.rs

{"file": "tests/npc_greetings_highroad_farnum.rs",
 "tests": [
  {"name": "every_edited_row_has_resolved_client_provenance", "verdict": "keep", "covered_by": null, "reason": "Checks provenance for the seven Highroad/Farnum rows (hash, locale line, speaker guide row, quest giver/intro). Sister file tests/npc_greetings_merry_vale_stillwater.rs has the same test shape, but over different NPC ids, lines and guides, so it does not drive the same assertions on the same rows. Not a duplicate."},
  {"name": "highroad_and_farnum_rows_send_their_greeting_in_26_3", "verdict": "keep", "covered_by": null, "reason": "Dispatch-path check that these rows' greeting ids reach the 26/3 body through Gameplay::handle_in_world. The sister files cover other regions with the same mechanism, not these rows. Only check of this row set's wire behaviour."},
  {"name": "a_zero_or_missing_greeting_falls_back_to_no_body", "verdict": "keep", "covered_by": null, "reason": "Fallback/no-bypass guard, a behaviour check. tests/npc_greetings_merry_vale_stillwater.rs::a_zero_or_missing_greeting_falls_back_to_no_body is similar in purpose but uses a different control row and fixture. Kept conservatively (refusal-type check)."},
  {"name": "the_t246_rows_and_all_other_regions_are_unchanged", "verdict": "keep", "covered_by": null, "reason": "Regression guard that the T246 bindings and the other regions' top-level values stay put. It is a canary for other slices overwriting bindings. Sister files carry similar 'unchanged' tests but over different row sets, so it is not clearly superseded."},
  {"name": "the_content_stays_within_the_loader_bounds", "verdict": "keep", "covered_by": null, "reason": "Loader bounds check (NpcVisibility spawn counts, max rows). Not covered by the sister tests' assertions on these two files."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "This file is one of a family of per-region greeting suites (merry_vale_stillwater, seaside_briarwood, lakeshore_wilds, job_hubs, sanctuary) built from the same template by T315-T317 and later edits. Each file pins different rows, so their assertions differ in data even when test names match. I only read the file's first ~530 lines and the sister file's first 300, so I did not verify the tail of the file (the change-guard and bounds bodies) line by line. The closest redundancy is the zero/missing-greeting fallback test versus the merry_vale file's version, and the 'unchanged' guard versus the sister files' versions; consolidating those would be a harness-level change, not a removal from this file. No test is marked removable."}
]}
