<!-- fleet job=testaudit-infer id=vendor_sell-v3 status=done turns=3 usd=0.0043 tokens(read,write,in,out)=[29827, 19357, 8, 3258] model=claude-haiku-5-5 -->
# tests/vendor_sell.rs

{"file": "tests/vendor_sell.rs",
 "tests": [
  {"name": "native_sell_changes_exactly_one_stack_and_the_coin_balance", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end check of the native 165/5 sell at service layer: one stack changes, exact coin credit, 165/6 completion layout. Similar files list no equivalent."},
  {"name": "sale_completion_id_drives_buy_back", "verdict": "keep", "covered_by": null, "reason": "Checks the completion transaction id is the row the client sends back in 165/12. Overlaps the buy-back flow in coin_store_siblings (sell_then_buy_back_once_restores_the_stack_and_the_exact_coins), but that test asserts the restore, not the id linkage; not confirmed as same assertions, so keep."},
  {"name": "the_content_key_is_still_accepted_and_foreign_merchants_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal/security check on merchant ids; no equivalent confirmed elsewhere."},
  {"name": "sell_without_an_open_shop_or_out_of_range_is_refused_visibly", "verdict": "keep", "covered_by": null, "reason": "Refusal check (no open shop / range). Not read in full elsewhere; keep under refusal policy."},
  {"name": "malformed_sells_get_a_failure_reply_and_other_packets_stay_errors", "verdict": "keep", "covered_by": null, "reason": "Hostile/malformed input check; keep."},
  {"name": "every_item_refusal_leaves_state_untouched_with_a_canary_that_still_sells", "verdict": "keep", "covered_by": null, "reason": "Refusal plus canary check; keep."},
  {"name": "coin_cap_blocks_a_sale_without_taking_the_item", "verdict": "keep", "covered_by": null, "reason": "Refusal check for the coin cap; no equivalent confirmed; keep."},
  {"name": "replay_and_reload_cannot_pay_twice", "verdict": "keep", "covered_by": null, "reason": "Persistence/replay canary; keep."},
  {"name": "gateway_shop_list_is_the_client_readable_66_42", "verdict": "keep", "covered_by": null, "reason": "Client-layout check through gateway for the shop list. npc_interaction::coin_merchant_list_165_10_matches_the_same_row_reader_layout is related at service layer but does not drive the gateway; keep."},
  {"name": "gateway_native_sell_pays_once_saves_and_survives_a_reconnect", "verdict": "keep", "covered_by": null, "reason": "Gateway sell with persistence across reconnect; keep."},
  {"name": "gateway_refusals_answer_the_client_and_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check via gateway; keep."},
  {"name": "gateway_sell_replay_of_a_whole_stack_pays_once", "verdict": "keep", "covered_by": null, "reason": "Replay-pays-once canary for sell. coin_store_siblings::gateway_sell_then_buy_back_once_then_replays_pay_nothing covers replay of buy-back, not sell replay; not the same assertions, so keep."},
  {"name": "gateway_buy_then_sell_round_trip_from_the_native_window", "verdict": "keep", "covered_by": null, "reason": "Round trip buy then sell through one window; not shown to be duplicated elsewhere; keep."},
  {"name": "gateway_vendor_buy_debits_grants_and_replies", "verdict": "keep", "covered_by": null, "reason": "Vendor buy 165/4 gateway debit, grant and reply; npc_interaction::vendor_165_4_and_66_43_still_route is routing only, so not a superseding check; keep."},
  {"name": "gateway_vendor_buy_insufficient_coins_replies_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check; keep."},
  {"name": "gateway_vendor_buy_full_bag_replies_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check; coin_store_siblings::gateway_sc_full_bag_is_refused_atomically concerns station cash rides, not vendor buy; keep."},
  {"name": "gateway_vendor_buy_refusals_always_answer_with_66_44", "verdict": "keep", "covered_by": null, "reason": "Refusal reply-code check; keep."},
  {"name": "gateway_vendor_buy_reads_the_live_inventory_after_a_reward", "verdict": "keep", "covered_by": null, "reason": "Live-state canary for buy after reward; keep."},
  {"name": "gateway_bundle_failure_does_not_commit_a_vendor_buy", "verdict": "keep", "covered_by": null, "reason": "Atomicity/rollback check; coin_store_siblings::gateway_bundle_failure_rolls_back_buy_back_history covers buy-back rollback, a different path; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.4,
 "notes": "Low confidence: the pack's test bodies were truncated and the previous answer was itself cut off, so I read only parts of this file (about lines 600-884) and two overlapping coin_store_siblings tests. I did not read the service-layer refusal and coin-cap tests in full, nor the vendor-buy tests after line 884 beyond their names, so every verdict defaults to keep. Overlap is most plausible between the sell-replay and buy-back-replay tests and between the vendor routing tests in npc_interaction.rs; a full read of both files would be needed before removing anything. The file is clearly not removable as a whole: it holds the only native 165/5 sell and refusal coverage in the set."}
