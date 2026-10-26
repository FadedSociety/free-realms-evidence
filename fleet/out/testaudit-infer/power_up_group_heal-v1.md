<!-- fleet job=testaudit-infer id=power_up_group_heal-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[17222, 11705, 8, 1477] model=claude-haiku-5-5 -->
# tests/power_up_group_heal.rs

{"file": "tests/power_up_group_heal.rs",
 "tests": [
  {"name": "a_kill_gives_its_group_heal_once", "verdict": "keep", "covered_by": null, "reason": "Only direct test of World::claim_group_heal's once-per-kill dedupe (second claim None, next ms and other enemy Some). power_up_drops::big_hearts_from_one_kill_share_a_kill_key_so_the_group_heals_once exercises the same key through the tick/drop layer, not the World ledger, so it does not drive the same path with the same assertions."},
  {"name": "the_same_kill_id_in_two_instances_heals_each_group_once", "verdict": "keep", "covered_by": null, "reason": "Unique check that the instance is part of the kill identity (same guid+ms in a child instance is a separate kill). Nothing elsewhere asserts this; it guards cross-instance isolation."},
  {"name": "a_picker_without_a_committed_place_claims_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check: no committed place yields None and consumes nothing (F182 fixed the instance-0 default). Only test of this refusal at the World level."},
  {"name": "the_memory_is_bounded", "verdict": "keep", "covered_by": null, "reason": "Only check of the 256-entry eviction bound on the ledger (memory must not grow forever). Canary-like; no equivalent elsewhere."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Small, focused file testing the World-level group-heal ledger directly. Similar files (power_up_drops.rs) test the same feature end-to-end via tick/drop rather than claim_group_heal itself; their overlap is partial (different layer), so nothing is marked superseded. No test here is redundant."}
