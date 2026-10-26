<!-- fleet job=testaudit-infer id=free_revive-v1 status=done turns=3 usd=0.0044 tokens(read,write,in,out)=[30842, 21023, 8, 2877] model=claude-haiku-5-5 -->
# tests/free_revive.rs

{"file": "tests/free_revive.rs",
 "tests": [
  {"name": "world_knockout_is_held_and_offers_the_window_once", "verdict": "keep", "covered_by": null, "reason": "Only test of the EncounterEngine world knockout hold: one window, dead players not re-hit, refused attacks and begin while knocked out. Hostile-input/refusal coverage; piece_058 tests ReviveArbiter, a different path."},
  {"name": "the_window_carries_the_retail_paid_price", "verdict": "duplicate", "covered_by": "tests/free_revive.rs::world_knockout_is_held_and_offers_the_window_once", "reason": "Same knockout and 41/125 window; its 20-byte length, timer and cost checks are already asserted by world_knockout via window() equality (count == 1). Only the explicit byte-offset decode is extra, so it is near-redundant within this file."},
  {"name": "unanswered_knockout_is_revived_by_the_server", "verdict": "keep", "covered_by": null, "reason": "Server fallback timer (15 s) canary; no other test in the similar files drives the engine's tick-based fallback."},
  {"name": "free_revive_returns_to_the_checkpoint_at_full_health_with_grace", "verdict": "keep", "covered_by": null, "reason": "Free revive path through the engine with checkpoint, full health and grace window; only engine-level check of 41/122 free revive."},
  {"name": "replay_and_alive_requests_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Replay/refusal check that a repeat revive or an alive request changes nothing; security-style refusal, kept."},
  {"name": "paid_revive_is_refused_and_the_window_comes_back", "verdict": "keep", "covered_by": null, "reason": "Refusal check: engine holds no wallet so paid request is refused and window re-offered."},
  {"name": "paid_revive_charges_the_price_once_and_revives_in_place", "verdict": "keep", "covered_by": null, "reason": "Charge-once and in-place revive on the engine path; ReviveArbiter tests in piece_058 (paid_revive_charges_the_cost_once_and_keeps_the_spot) cover a different struct, so not superseded."},
  {"name": "paid_revive_below_the_price_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal below price with fallback still running; piece_058::paid_revive_below_cost_changes_nothing tests ReviveArbiter, not the engine, so keep."},
  {"name": "the_paid_price_comes_from_field_content", "verdict": "keep", "covered_by": null, "reason": "Content-data validation (ceiling, source marker, negative cost refused at load); unique to this file."},
  {"name": "client_supplied_ids_carry_no_authority_in_the_world", "verdict": "keep", "covered_by": null, "reason": "Hostile-input check that client header ids cannot pick the destination; security-type, kept."},
  {"name": "malformed_resume_is_rejected_without_mutation", "verdict": "keep", "covered_by": null, "reason": "Malformed-input refusal with no mutation; security-type, kept."},
  {"name": "a_knockout_saved_to_disk_wakes_up_on_reload", "verdict": "keep", "covered_by": null, "reason": "Persistence check on reload of a knocked-out save; persistence tests are not removable without an equal test."},
  {"name": "lost_instance_revives_through_the_existing_exit", "verdict": "keep", "covered_by": null, "reason": "Covers instance-loss revive via the 41/109-equivalent exit and replay refusals; multi-part refusal and persistence checks, not clearly covered elsewhere."},
  {"name": "developer_heal_hides_a_stale_window", "verdict": "keep", "covered_by": null, "reason": "Small but unique check that heal_full emits the 41/126 hide once; no equivalent found in the similar files."},
  {"name": "gateway_routes_resume_for_a_held_world_knockout", "verdict": "keep", "covered_by": null, "reason": "Gateway routing canary through login and tunnel; depends on private content fixture, not duplicated in similar files."},
  {"name": "gateway_paid_revive_charges_once_and_revives_in_place", "verdict": "keep", "covered_by": null, "reason": "Gateway-level charge-once canary; not covered by the engine-level or ReviveArbiter tests."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Mostly unique engine-level coverage of EncounterEngine's knockout/revive path. Similar tests in tests/piece_058.rs (ReviveArbiter unit: first_knockout_emits_one_window..., paid_revive_charges_the_cost_once..., paid_revive_below_cost_changes_nothing, safe_revive_is_free...) exercise a different struct and were judged parallel, not duplicate. tests/piece_037.rs::paid_revive_is_disabled_below_the_server_supplied_cost was seen only by name and not read, so overlap with paid_revive_below_the_price_changes_nothing is unverified. Only the_window_carries_the_retail_paid_price is a clear in-file duplicate candidate. Not read in depth: lines 560-735 (gateway helper bodies)."}
]}
