<!-- fleet job=testaudit-infer id=smelting_gameplay-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[20540, 11971, 8, 1355] model=claude-haiku-5-5 -->
# tests/smelting_gameplay.rs

{"file": "tests/smelting_gameplay.rs",
 "tests": [
  {"name": "older_gameplay_snapshot_defaults_absent_smelting_state", "verdict": "keep", "covered_by": null, "reason": "Same body as tests/forging_gameplay.rs::older_gameplay_snapshot_defaults_absent_forging_state, but it asserts the smelting field is absent (state.smelting.is_none()), a different field. Cheap, unique to smelting, and it guards the back-compat/no-change-on-roundtrip property. Could be folded into a shared parametrised test, but not a removable duplicate."},
  {"name": "private_mining_smelting_reward_atomic_once_restore_and_cancel", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end check of the smelting job: gating (unaccepted goal, missing inputs, remote spoof, wrong class, exhausted goal), atomic rollback on malformed bundle, once-only reward, persistence round-trip, restart cancel without consumption, and bad-packet refusals. Security/refusal and persistence checks with no equivalent elsewhere. Note it is #[ignore] and needs private reference content."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file is smelting-specific and the forging/cooking/mining siblings cover different recipes and resources, so the big test is not superseded. The only overlap is the snapshot-default test, which is a near-copy of the forging one and could be consolidated later into a single parametrised check across all craft states. Not a removal candidate on its own. Existing 'older_*' tests across files are the same pattern, so a shared helper is a possible cleanup, not a deletion."}
