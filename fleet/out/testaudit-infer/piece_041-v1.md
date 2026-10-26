<!-- fleet job=testaudit-infer id=piece_041-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[9519, 13267, 6, 1723] model=claude-haiku-5-5 -->
# tests/piece_041.rs

{"file": "tests/piece_041.rs",
 "tests": [
  {"name": "recovered_job_identity", "verdict": "keep", "covered_by": null, "reason": "Only Rust check pinning the recovered driver job name/description ids and validate(); no other test file drives piece_041 (its Python twin tests/pieces/test_piece_041.py is a different harness, not a Rust test)."},
  {"name": "activity_binds_job_and_original_wire", "verdict": "keep", "covered_by": null, "reason": "Sole check of DriverActivity -> job / lobby game type / tunnel opcode binding; no equivalent elsewhere in the suite."},
  {"name": "progression_rejects_non_driving_jobs", "verdict": "keep", "covered_by": null, "reason": "Refusal check (non-driving job 1 rejected). Its final assertion repeats the job() accessor check, but it is not a duplicate of any other file."},
  {"name": "wrong_activity_is_rejected_without_mutation", "verdict": "keep", "covered_by": null, "reason": "Refusal check that a wrong-job outcome changes nothing; must be kept."},
  {"name": "validated_outcomes_credit_exactly_once", "verdict": "keep", "covered_by": null, "reason": "Once-only credit (persistence/replay) contract; security-relevant, keep."},
  {"name": "distinct_outcomes_accumulate_and_unpriced_finish_credits_zero", "verdict": "keep", "covered_by": null, "reason": "Accumulation and zero-star unpriced finish behaviour; no other file covers this ledger."},
  {"name": "star_award_is_a_single_byte", "verdict": "keep", "covered_by": null, "reason": "Boundary/canary on the 255 star cap for a single byte award; keep."},
  {"name": "max_rank_credits_but_does_not_advance", "verdict": "keep", "covered_by": null, "reason": "Max-rank credit behaviour plus member/non-member rank caps; unique to this module."},
  {"name": "unlock_tables_cover_the_recovered_ranks", "verdict": "keep", "covered_by": null, "reason": "Pins recovered unlock table rows and counts; the only check of these tables in Rust."},
  {"name": "gear_class_and_part_class_constants_are_recovered", "verdict": "keep", "covered_by": null, "reason": "Recovered constant pinning; not replicated in any other Rust test file."},
  {"name": "captured_vehicles_match_the_recovered_catalogue_rows", "verdict": "keep", "covered_by": null, "reason": "Pins the six captured vehicle rows; sole check of CAPTURED_VEHICLES."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The five similar files (piece_032, 056, 048, 046, 040) cover different work items and modules; none exercises DriverProgression, DriverActivity or CAPTURED_VEHICLES, so no cross-file superseding or duplicate was found. Within-file overlap is minor (progression_rejects_non_driving_jobs repeats a job() check; recovered_job_identity overlaps driver_job lookups), but these are cheap and not worth removing. The file is the only Rust test target for src/restoration/piece_041.rs, so removing it would lose coverage. Constant-pinning tests are brittle to recovery updates but are intentional for this work item."}
