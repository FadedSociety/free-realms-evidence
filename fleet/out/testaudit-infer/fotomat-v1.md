<!-- fleet job=testaudit-infer id=fotomat-v1 status=done turns=5 usd=0.0035 tokens(read,write,in,out)=[49212, 17137, 12, 1724] model=claude-haiku-5-5 -->
# tests/fotomat.rs

{"file": "tests/fotomat.rs",
 "tests": [
  {"name": "fotomat_answers_self_and_visible_players", "verdict": "keep", "covered_by": null, "reason": "Only positive check of the 156/2 -> 156/3 reply shape and the self/visible/far/elsewhere visibility rule. No similar file in the pack exercises fotomat; the similar files (player_trade, coin_store_siblings, chess_route, warpstone_travel, social_lists) cover other subsystems."},
  {"name": "fotomat_refuses_without_reply", "verdict": "keep", "covered_by": null, "reason": "Refusal and hostile-input test (bad family/subtype, trailing bytes, truncated bodies, malformed 115 CRC shapes). Security/refusal checks are kept unless an equal test is named; none found."},
  {"name": "login_time_request_is_handled_or_dropped_cleanly", "verdict": "keep", "covered_by": null, "reason": "Only test driving the login-time pre-Loaded gateway path with trace and snapshot-unchanged assertions; it is skipped when the private lab reference is absent, so it is not replaceable by a public test. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.3,
 "notes": "Low confidence because the search tools could not reach the osfr-tools Rust sources or the fotomat_routing module named in the doc line, so no fotomat-specific overlap could be checked. The five similar files share no fotomat behaviour (shared_score 4-6 is from helper or generic structure). The 115 CRC assertions and the login-time test may overlap a gateway-level test not visible here; a follow-up check of fotomat_routing and the gateway tests is advised before any removal. Note the excerpt cut off before the end of the login-time test (the 'Without an identity or' tail), which was not reviewed."}
