<!-- fleet job=testaudit-infer id=gameplay-v1 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[6547, 10253, 6, 950] model=claude-haiku-5-5 -->
# tests/gameplay.rs

{"file": "tests/gameplay.rs",
 "tests": [
  {"name": "private_complete_loop_reward_once_atomic_bundle_and_fresh_restore", "verdict": "keep", "covered_by": null, "reason": "Single #[ignore]d private end-to-end oracle covering quest accept, enemy kills, reward-once on duplicate completion, rollback of a mixed bundle containing an invalid equip, and fresh-restore from disk. It combines refusal, atomicity, persistence and canary checks. Similar private files (smelting_gameplay.rs, kart_gameplay.rs, forging_gameplay.rs, mystery_chest_gameplay.rs) exercise other job loops (smelting, racing, forging, chest), not the realm quest/combat loop with the bundle-rollback check, so no equally strong test elsewhere was found. economy_review.rs uses 'realm quest accept 900001' only as a setup step and does not assert the full reward-once and restore sequence."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file is one ignored test that needs private reference, content and capture env vars, so it does not run in normal suite runs. It has no obvious duplicate. Other private loop tests have analogous structure but different job paths. Kept conservatively. I did not read the full bodies of the similar files, so the coverage judgement rests on test names and the grep of quest-accept usage."}
