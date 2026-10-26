<!-- fleet job=testaudit-infer id=player_radial-v1 status=done turns=3 usd=0.0044 tokens(read,write,in,out)=[32556, 21367, 8, 2863] model=claude-haiku-5-5 -->
# tests/player_radial.rs

{"file": "tests/player_radial.rs",
 "tests": [
  {"name": "select_builds_a_one_entry_menu_for_the_target", "verdict": "keep", "covered_by": null, "reason": "Only test that pins the full select-menu byte layout (header, target guid, no auto-select, row id/icon/label, name, trailer). player_trade.rs uses helper menu_rows() and checks rows, not the wire bytes, so it is not an equal check."},
  {"name": "forged_own_guid_field_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Hostile-input check: the reply must ignore the claimed own guid. Nothing else in the suite drives this path."},
  {"name": "every_refusal_sends_nothing_and_leaves_no_menu", "verdict": "keep", "covered_by": null, "reason": "Refusal check across SelfTarget, NotVisible, Malformed and NotInWorld that also asserts no menu is left. Keep as the refusal guard."},
  {"name": "malformed_requests_are_rejected_without_panics", "verdict": "keep", "covered_by": null, "reason": "Truncation, overlong and wrong-subcommand fuzz on the select packet. Robustness and hostile-input check; keep."},
  {"name": "reach_limit_is_tunable_and_bounded", "verdict": "keep", "covered_by": null, "reason": "Tunable reach boundary and with_reach rejection of non-finite or non-positive values. Not covered elsewhere."},
  {"name": "name_is_bounded_and_utf8_safe", "verdict": "keep", "covered_by": null, "reason": "Bounds the name at 64 bytes and keeps it valid UTF-8. Hostile-input check with no equivalent in the similar files."},
  {"name": "inspect_choice_sends_the_public_look_only", "verdict": "keep", "covered_by": null, "reason": "Main Inspect success path with the parser for the wire layout, the one-shot menu and the private-value canary. Keep."},
  {"name": "inspect_carries_every_stat_the_window_reads", "verdict": "keep", "covered_by": null, "reason": "Regression guard for a client crash (stat list must have more than 37 entries, including the empty-look case). Keep as a canary."},
  {"name": "replay_and_foreign_choices_do_not_inspect", "verdict": "keep", "covered_by": null, "reason": "Replay, foreign-guid and wrong-width refusals that must not read the look. Security/refusal check."},
  {"name": "stale_target_at_choice_time_reveals_nothing", "verdict": "keep", "covered_by": null, "reason": "Target leaves, walks out of reach, or changes instance before choice; the look must never be read. Security check. player_trade covers reach on its own path, not this radial choice."},
  {"name": "missing_or_invalid_look_is_refused", "verdict": "keep", "covered_by": null, "reason": "Validation of every BadLook case (slot range, duplicate slot, record id, length, profile and item count caps). Refusal and hostile-input check."},
  {"name": "stop_inspect_closes_idempotently_and_is_strict", "verdict": "keep", "covered_by": null, "reason": "Strict close-packet validation and idempotent close. Only test of stop_inspect here."},
  {"name": "reset_clears_menu_and_inspect", "verdict": "keep", "covered_by": null, "reason": "Only checks reset() clears menu and inspect state. Small, but not clearly covered elsewhere; keep."},
  {"name": "a_new_selection_replaces_the_open_menu", "verdict": "keep", "covered_by": null, "reason": "Fail-closed behaviour: a refused follow-up selection closes the old menu. Refusal check; keep."},
  {"name": "no_public_look_means_no_menu_and_hidden_targets_are_never_asked", "verdict": "keep", "covered_by": null, "reason": "Canary that the look source is never consulted for refused targets and that no look means no menu. player_trade.rs asserts NoLook only indirectly, via a busy target, so this is not superseded."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "All 14 tests are keep. The file is the only dedicated suite for PlayerRadial's select, choose and stop_inspect paths. The similar files (player_trade.rs, the closest one) reuse PlayerRadial only as a helper for trade menus; they check menu rows through helpers and do not cover the Inspect wire layout, the stale-target or reach guards, or the stop_inspect strictness. Overlap is limited to a few NoLook and Inspect-row assertions in player_trade.rs (around lines 301-332), which is not equal in strength. Within-file, no test is a strict subset of another. Other similar files (kart_service, coin_store_siblings, fishing_entry, app_fuzz) do not exercise the radial path. Confidence is 0.8 because I did not read the full player_trade.rs file, only the first trade-menu tests."}
