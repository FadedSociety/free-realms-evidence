<!-- fleet job=testaudit-infer id=harvesting_reward_catalogue-v1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[24181, 16046, 8, 1692] model=claude-haiku-5-5 -->
# tests/harvesting_reward_catalogue.rs

{"file": "tests/harvesting_reward_catalogue.rs",
 "tests": [
  {"name": "real_package_missing_bundle_definitions_refuse_gameplay_load", "verdict": "keep", "covered_by": null, "reason": "Refusal check: the shipped region-111 config must make Gameplay::load refuse when bundle definitions 2885/2890 are missing from the inventory. The only test that drives the gameplay.rs:1019 'harvesting reward definition ... is not in the loaded inventory' guard; no other test in the suite matches that message."},
  {"name": "wrong_or_late_output_definition_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check with hostile input: unknown definitions in first and fourth output slots must be named in the error. Nothing else in tests/ exercises per-slot validation of harvesting outputs at load."},
  {"name": "valid_definitions_load_and_legacy_save_bytes_stay_compatible", "verdict": "keep", "covered_by": null, "reason": "Positive load path plus backward-compatibility of a legacy GameplayState without harvesting (serialization round-trip byte-equal). Not found as an equivalent elsewhere; conservative keep. Could be a candidate for consolidation with inventory.rs/persistence tests if someone audits those, but not proven redundant."},
  {"name": "refused_load_preserves_the_caller_state_and_content_bytes", "verdict": "keep", "covered_by": null, "reason": "Persistence/refusal canary: a refused load must neither mutate the caller's state nor rewrite harvesting.json. Unique in the suite; never mark removable."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Searched tests/ for 'reward definition', 'harvesting reward definition' and 'unknown reward definition'. The only other hit is tests/field_battle_roster.rs:1185, which concerns a different inventory path. The harvesting_* siblings (harvesting.rs, harvesting_review.rs, harvesting_border.rs, harvesting_lifecycle.rs) write content and check the farm ids (2885, 2887, 2890, 2877) but do not assert the Gameplay::load refusal, so no superseding test was found. The file's 'created_by'/'last_changed_by' are both T034, and T608 lists it as a strengthen-tests target, which argues for keeping it. Similar-file scores were computed from the pack and not re-verified in depth."}
