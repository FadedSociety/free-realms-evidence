<!-- fleet job=testaudit-infer id=mystery_chest_gameplay-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[24249, 14287, 8, 1394] model=claude-haiku-5-5 -->
# tests/mystery_chest_gameplay.rs

{"file": "tests/mystery_chest_gameplay.rs",
 "tests": [
  {"name": "private_confirmation_atomic_grant_replay_and_disk_restore", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end check of the Check-then-Confirm grant on real content, with replay refusal and save/restore persistence. The closest test, tests/app_fuzz.rs::t3_pending_chest_survives_malformed_use_and_valid_reward_cannot_replay, covers replay on synthetic content (chest 910190) and does not check the grant, the disk round-trip, or the real item ids."},
  {"name": "private_missing_key_forged_item_and_malformed_requests_conserve_everything", "verdict": "keep", "covered_by": null, "reason": "Refusal and hostile-input check (missing key, forged instance ids, truncated requests) asserting state conservation. No equivalent found elsewhere; app_fuzz.rs uses different content and ids."},
  {"name": "private_failed_reward_allocation_rolls_back_both_consumptions", "verdict": "keep", "covered_by": null, "reason": "Rollback check: a failed grant must leave chest and key intact. Atomicity is a security/persistence property; no other test in the repo exercises this path."},
  {"name": "private_confirmation_is_cleared_on_session_reset", "verdict": "keep", "covered_by": null, "reason": "Checks that reset_session clears the pending confirmation. No other chest test covers reset; the generic reset tests (encounter_job_skills, fishing_entry, derby_route) cover other systems."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "All four tests are #[ignore]d and need the private Mystery Chest package (OSFR_CHEST_CONTENT), so they only run in that environment. The overlap with tests/app_fuzz.rs (chest replay, pending confirmation, t3_ and finding_1_ tests) is partial: those use synthetic content and different definition ids, so they do not drive the same real-content path. No test was marked removable. Recommend a look at whether the private package is ever run in CI, since if it is not, the file's value is limited to manual runs."}
