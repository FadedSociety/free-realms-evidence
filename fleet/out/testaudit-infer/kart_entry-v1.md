<!-- fleet job=testaudit-infer id=kart_entry-v1 status=done turns=3 usd=0.0049 tokens(read,write,in,out)=[32861, 26434, 8, 2567] model=claude-haiku-5-5 -->
# tests/kart_entry.rs

{"file": "tests/kart_entry.rs",
 "tests": [
  {"name": "gate_defaults_off_and_refuses_without_any_reply_or_state", "verdict": "keep", "covered_by": null, "reason": "Refusal check: the default-off gate must send no reply and leave state untouched. Only test of the Disabled gate at the handler level."},
  {"name": "unhandled_subtypes_and_missing_context_are_inert_refusals", "verdict": "keep", "covered_by": null, "reason": "Hostile/unknown subtype and no-context refusals; no other file drives KartEntryHandler directly."},
  {"name": "malformed_register_and_frame_widths_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Malformed-input refusal with exact error variants and no phase change. Byte-width checks are only exercised here at unit level."},
  {"name": "spoofed_session_is_refused_and_reported", "verdict": "keep", "covered_by": null, "reason": "Security refusal (foreign session) with exact ForeignSession payload; kept per the refusal rule."},
  {"name": "stale_replay_and_closed_session_are_refused", "verdict": "keep", "covered_by": null, "reason": "Replay and closed-session refusal; security-relevant, no equivalent found elsewhere."},
  {"name": "register_emits_the_ordered_start_bundle", "verdict": "keep", "covered_by": null, "reason": "Pins the ordered 33/9 start bundle byte-for-byte; the core contract check for this handler."},
  {"name": "player_state_requires_started_phase_and_matching_session", "verdict": "keep", "covered_by": null, "reason": "Phase ordering and foreign-session refusal on the join path; unique to this handler."},
  {"name": "race_ready_requires_joined_phase", "verdict": "keep", "covered_by": null, "reason": "Phase-gate refusals for on_race_ready; unique coverage of the streaming transition."},
  {"name": "scene_frame_preserves_rotation_w_zero_through_the_zone_codec", "verdict": "keep", "covered_by": null, "reason": "Canary for the rotation w=0 behaviour through the zone codec (explicitly pinned against the encounter writer's 1.0)."},
  {"name": "content_bounds_are_refused", "verdict": "keep", "covered_by": null, "reason": "Long list of bound and validation refusals for content; hostile-input checks with no equivalent in the similar files, which test gateway-level behaviour."},
  {"name": "context_bounds_are_refused", "verdict": "keep", "covered_by": null, "reason": "Zero-id, NaN-rotation and double-open refusals; security/refusal check."},
  {"name": "typed_decoders_match_the_recovered_layouts", "verdict": "keep", "covered_by": null, "reason": "Pins the recovered field layouts and the shared inner opcode with the racing family. Not clearly covered elsewhere; kept conservatively."},
  {"name": "private_content_package_format_round_trips_and_is_strict", "verdict": "keep", "covered_by": null, "reason": "Serde round-trip plus unknown-field refusal for the content package; strictness check."},
  {"name": "private_capture_reencodes_the_full_entry_bundle", "verdict": "keep", "covered_by": null, "reason": "Ignored private canary against pinned capture hashes; cannot be run in the public suite and has no substitute, so keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Nothing in the repo's other test files drives the kart_entry module's KartEntryHandler directly (grep for kart_entry|KartEntryHandler under prototype/osfr-tools finds only src consumers, app_fuzz constant reads, and the gateway/npc paths). The similar files (kart_service.rs, kart_npc_entry.rs, housing_service.rs, soccer_service.rs, coin_store_siblings.rs) test gateway and service behaviour above this handler, so they do not supersede these unit-level checks at the same level. Within-file overlap exists (register replay appears in register_emits_the_ordered_start_bundle and stale_replay_and_closed_session_are_refused) but each asserts different things. I did not read the full similar-file bodies or the tail of this file past line 765, so the private capture test's remaining assertions are unverified. No test was found obsolete: no later task in the pack replaced this handler's behaviour."}
]}
