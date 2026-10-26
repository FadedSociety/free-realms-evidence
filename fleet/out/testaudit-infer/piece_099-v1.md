<!-- fleet job=testaudit-infer id=piece_099-v1 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[8649, 18551, 6, 2179] model=claude-haiku-5-5 -->
# tests/piece_099.rs

{"file": "tests/piece_099.rs",
 "tests": [
  {"name": "trade_vocabulary_is_pinned_to_the_supplied_client_and_community_sources", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the 18-row trade sub-opcode table (family 59); no similar file covers trade vocabulary."},
  {"name": "trade_commands_round_trip_the_recovered_client_wire", "verdict": "keep", "covered_by": null, "reason": "Unique encode/parse byte vectors for the six trade client-to-server commands plus malformed-wire refusals (wrong family, truncated, trailing bytes); no overlapping test elsewhere."},
  {"name": "grouping_intents_match_the_recovered_activity_launch_table", "verdict": "keep", "covered_by": null, "reason": "Partly overlaps tests/piece_020.rs::activity_launch_sub_opcodes_match_the_recovered_class_table, but it additionally checks this harness's GroupRequest-to-wire mapping and RECOVERED_TABLE ordering, which piece_020 does not cover. Conservative keep."},
  {"name": "party_case_is_deterministic_and_compares_identical", "verdict": "keep", "covered_by": null, "reason": "Tests the scenario runner's determinism and digest comparison, a harness behaviour not exercised by the piece_020 registry tests."},
  {"name": "activity_case_launches_an_instance_and_refuses_a_non_member", "verdict": "keep", "covered_by": null, "reason": "Refusal check (non-member enter, late cancel after launch). Registry-level behaviour is similar to tests/piece_020.rs::duplicate_and_non_member_requests_are_rejected and membership_mutation_after_launch_is_rejected, but this asserts through the harness log and wire; kept conservatively as a refusal check."},
  {"name": "comparison_reports_the_first_divergence_for_each_stream", "verdict": "keep", "covered_by": null, "reason": "Unique test of the compare() divergence ordering across log, launch and state streams."},
  {"name": "trade_case_records_the_silent_drop_on_the_real_gateway", "verdict": "keep", "covered_by": null, "reason": "Canary: pins that recovered trade traffic is currently dropped by the real gateway. Must not be removed while the gap stands."},
  {"name": "scenario_validation_rejects_malformed_scripts", "verdict": "keep", "covered_by": null, "reason": "Hostile/malformed-input refusal checks on scenario validation; no equivalent elsewhere."},
  {"name": "replies_belong_to_the_log_stream_not_just_the_state", "verdict": "keep", "covered_by": null, "reason": "Not inspected in full (lines 200-250 unread), but it is a distinct stream-ownership check of the harness; keep by default."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "The file is mostly a harness test for a candidate module with trade-family coverage found nowhere else in the similar set. The closest overlap is grouping_intents_match_the_recovered_activity_launch_table and activity_case_launches_an_instance_and_refuses_a_non_member against tests/piece_020.rs (launch table, membership refusals). I kept them conservatively. No test was marked removable. I did not read piece_099.rs lines 200-250 or the similar test files piece_043/045/065/011, so the last verdict and the overlap checks against those are unverified."}
