<!-- fleet job=testaudit-infer id=trade_unavailable-v1 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[10688, 11835, 6, 1577] model=claude-haiku-5-5 -->
# tests/trade_unavailable.rs

{"file": "tests/trade_unavailable.rs",
 "tests": [
  {"name": "accepted_invite_reply_is_closed_with_sub_5_only", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the sub 3 accept reply (sub 5 close) in the unavailable path; no other file calls unavailable_replies."},
  {"name": "declined_invite_reply_needs_no_answer", "verdict": "keep", "covered_by": null, "reason": "Sole check that a declined invite gets no reply; unique to this unavailable path."},
  {"name": "cancel_closes_the_window_with_sub_5", "verdict": "keep", "covered_by": null, "reason": "Sole check of the sub 7 cancel close reply in the unavailable path."},
  {"name": "accept_lock_unlock_offer_item_and_offer_coins_get_status_then_close", "verdict": "keep", "covered_by": null, "reason": "Sole check of the status-then-close reply for subs 6, 8, 9, 10; the active-session tests in player_trade.rs exercise a different path (live sessions), not this unavailable reply."},
  {"name": "replies_carry_only_the_session_id_never_request_fields", "verdict": "keep", "covered_by": null, "reason": "Canary/no-echo check on reply bytes; security-relevant and not checked elsewhere."},
  {"name": "replays_are_identical_and_stateless", "verdict": "keep", "covered_by": null, "reason": "Statelessness/replay check; partly overlaps the no-echo test but asserts a distinct property (determinism over 50 replays). Kept conservatively."},
  {"name": "the_idle_session_sentinel_gets_no_reply", "verdict": "keep", "covered_by": null, "reason": "Refusal check for the 0xFFFFFFFF sentinel; unique to this file."},
  {"name": "wrong_body_length_gets_no_reply", "verdict": "keep", "covered_by": null, "reason": "Refusal of trailing bytes and every truncated prefix; hostile-input check, kept."},
  {"name": "server_to_client_subs_and_unknown_subs_get_no_reply", "verdict": "keep", "covered_by": null, "reason": "Refusal sweep over all non-request subs; hostile-input check, kept."},
  {"name": "other_families_get_no_reply", "verdict": "keep", "covered_by": null, "reason": "Refusal of other family headers and empty input; kept."},
  {"name": "hostile_bytes_never_panic_or_amplify", "verdict": "keep", "covered_by": null, "reason": "Fuzz-style no-panic and no-amplification check; canary-type robustness test, kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file is the only consumer of trade::unavailable_replies in the repo (grep finds no other test or src caller), so no other test file drives this path. The similar files (player_trade.rs, coin_store_siblings.rs, kart_service.rs, fishing_entry.rs, npc_interaction.rs) exercise live trade sessions and other systems, not the not-offered reply path. Minor internal overlap (replays vs no-echo, wrong-length vs hostile bytes) was judged distinct enough to keep. No test is removable."}
