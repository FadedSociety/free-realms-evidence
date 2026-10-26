<!-- fleet job=testaudit-infer id=kart_gateway-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[9943, 13731, 6, 1601] model=claude-haiku-5-5 -->
# tests/kart_gateway.rs

{"file": "tests/kart_gateway.rs",
 "tests": [
  {"name": "entry_rebinds_known_slots_and_preserves_quaternion_and_return", "verdict": "keep", "covered_by": null, "reason": "Pins the full entry sequence (scene id, quaternion, return position, status bytes, race start packet layout). Only test in the repo that drives KartGateway::begin/initialize/handle_entry/exit byte-for-byte. tests/kart_gameplay.rs exercises restore via supports_location but not these byte-level replies."},
  {"name": "duplicate_begin_and_malformed_register_leave_state_unchanged", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a second begin and a truncated register packet must error and leave state unchanged. Not found elsewhere with the same assertions."},
  {"name": "active_snapshot_roundtrip_and_content_binding", "verdict": "keep", "covered_by": null, "reason": "Persistence check: snapshot roundtrip plus refusal when content changes under an active snapshot. tests/kart_gameplay.rs restores a gateway (line ~669) but does not check the content-binding refusal; keep for persistence/security."},
  {"name": "bad_proven_slots_and_spawn_refused_before_entry", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal of out-of-range proven slots, bad spawn byte and mismatched progress tail. Security/refusal check; keep."},
  {"name": "absent_optional_content_and_missing_required_content", "verdict": "keep", "covered_by": null, "reason": "Covers the optional-absent (None) path and required-missing (error with an active snapshot) refusal. Small, not clearly duplicated; keep."},
  {"name": "original_close_is_bound_to_the_live_encounter_and_exact_width", "verdict": "keep", "covered_by": null, "reason": "Refusal check: close packet must match the live encounter id, must be exact width, and is refused after exit. accepts_close is only called from src/gameplay.rs; no other test drives it. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Audit is shallow: I compared by name and grep for KartGateway call sites, not by reading tests/kart_gameplay.rs or tests/bundle_activity_content.rs assertions in full. The similarity list (kart_service.rs, etc.) concerns weapons, gates and racing, not gateway entry/close, so no superseded or duplicate match was found. Possible overlap worth checking later: kart_gameplay.rs around lines 669 and 1225 (restore and corrupt-snapshot refusal) against active_snapshot_roundtrip_and_content_binding. Nothing here is obsolete; no task metadata (created_by/last_changed_by are null)."}
