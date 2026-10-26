<!-- fleet job=testaudit-infer id=piece_017-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[10197, 13352, 6, 1643] model=claude-haiku-5-5 -->
# tests/piece_017.rs

{"file": "tests/piece_017.rs",
 "tests": [
  {"name": "recovery_boundary_reports_the_cancelled_run", "verdict": "keep", "covered_by": null, "reason": "Only Rust check that audit_recovery reports the cleared cooking run (ClearedRun with service, instance id and phase). No other test in the suite drives restoration::piece_017::audit_recovery. The Python twin in tests/pieces/test_piece_017.py tests a different implementation and is not a Rust duplicate."},
  {"name": "recovery_boundary_rejects_a_surviving_run", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a run that survives reload must be rejected. Security/refusal boundary, with no equivalent Rust test elsewhere."},
  {"name": "conservation_rejects_lost_materials", "verdict": "keep", "covered_by": null, "reason": "Refusal check that a material count drop on cancel is rejected. Conservation invariant, not covered elsewhere in Rust."},
  {"name": "conservation_rejects_a_cancel_reward", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal: a new item appearing on cancel (reward exploit) must fail. Only check of this path."},
  {"name": "conservation_rejects_wallet_and_equipment_changes", "verdict": "keep", "covered_by": null, "reason": "Refusal check for coin and equipment mutation during recovery. Two distinct assertions in one test; both needed."},
  {"name": "conservation_rejects_a_regressed_or_reused_attempt_counter", "verdict": "keep", "covered_by": null, "reason": "Canary/refusal for instance-id counter regression and reuse, which is persistence-relevant. Not covered by other suites for this module."},
  {"name": "conservation_accepts_a_fresh_attempt_replacing_a_stale_offer", "verdict": "keep", "covered_by": null, "reason": "Positive case that a fresh attempt may replace a stale offer, plus the stricter recovery contract. It is the only test pinning the stale-offer replacement rule."},
  {"name": "private_forging_abandon_restart_pair_conserves_materials", "verdict": "keep", "covered_by": null, "reason": "Ignored evidence test over private lab captures, acting as a canary that the reviewed evidence still conserves materials. Not redundant with the synthetic tests and cannot be run in the public suite."},
  {"name": "private_cooking_native_midround_disconnect_conserves_materials", "verdict": "keep", "covered_by": null, "reason": "Ignored evidence canary over the native mid-round disconnect capture. Checks instance-id and coin invariants on real data, which no synthetic test does."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The similar-file list (kart_service, housing_native, player_trade, piece_081, app_fuzz) shares only generic scaffolding and does not exercise restoration::piece_017 audit functions, so no superseding Rust test was found. The only parallel is the Python checker tests/pieces/test_piece_017.py, which covers the same contract in another language and was not treated as a Rust duplicate. Every test is a refusal, conservation, or canary check, so the conservative default is keep. Two ignored tests depend on private lab files and only run in the lab environment."}
