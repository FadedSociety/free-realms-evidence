<!-- fleet job=testaudit-infer id=login_broker-v1 status=done turns=3 usd=0.0043 tokens(read,write,in,out)=[28203, 21485, 8, 2608] model=claude-haiku-5-5 -->
# tests/login_broker.rs

{"file": "tests/login_broker.rs",
 "tests": [
  {"name": "login_gateway_address_follows_the_lan_rule", "verdict": "keep", "covered_by": null, "reason": "Security/refusal check on gateway address exposure (public and private gateways refused without --allow-lan); no other file runs the osfr-login binary with --gateway validation."},
  {"name": "broker_refuses_public_wildcard_and_private_without_allow_lan", "verdict": "keep", "covered_by": null, "reason": "Refusal check on the credential broker bind address (public, wildcard, private without --allow-lan). Unique to this file; no other test asserts the 'credential broker binds loopback' message."},
  {"name": "private_broker_bind_admits_private_peers_and_keeps_failure_limits", "verdict": "keep", "covered_by": null, "reason": "Security review test for LAN bind, failure lockout and IP burst limits; #[ignore]d but is the only LAN-bind admission check. Keep."},
  {"name": "broker_good_signature_wrong_key_wrong_server_and_no_enumeration", "verdict": "keep", "covered_by": null, "reason": "Security check: wrong key, wrong server id and unknown/keyless handles all return the same generic refusal (no enumeration). Only test of the AUTH2 broker proof path."},
  {"name": "tokens_route_to_distinct_native_accounts_replay_fails_and_peers_stay_live", "verdict": "keep", "covered_by": null, "reason": "Replay refusal and token-to-account routing across real UDP processes; includes store-unchanged and no-lingering-lock canary. No equivalent in-process test found."},
  {"name": "ban_and_unban_apply_while_login_runs", "verdict": "keep", "covered_by": null, "reason": "L042 blocker test: moderation writes applied to a live login process. login.rs::ban_blocks_login_until_expiry checks ban in-process only, not against a running login service, so not superseded."},
  {"name": "a_held_store_lock_does_not_stop_login_or_the_character_list", "verdict": "keep", "covered_by": null, "reason": "Canary that login and reads do not take the store writer lock (L042 third review). login.rs::only_saves_wait_for_the_store_lock is related but in-process; this is the process-level check. Keep."},
  {"name": "loopback_dev_login_without_account_store_still_works", "verdict": "keep", "covered_by": null, "reason": "Dev-path canary for login without an account store. The membership byte assertion overlaps login.rs::login_reply_carries_account_membership_in_the_byte_the_client_reads, but the no-store login path is only checked here. Conservatively kept."},
  {"name": "account_lockout_unknown_lockout_ip_budget_and_malformed_replies_are_generic", "verdict": "keep", "covered_by": null, "reason": "Security check: lockout after failures, generic replies for unknown accounts, IP budget refill. Unique to the AUTH2 broker path."},
  {"name": "slow_broker_peer_cannot_block_native_login_and_expires", "verdict": "keep", "covered_by": null, "reason": "Availability/DoS check: a stalled TCP broker peer must not block UDP login and must be dropped. Unique."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "All 10 tests exercise the real osfr-login process over sockets (AUTH2 broker, LoginUdp_6, gateway/LAN gate, store lock). No similar file (login.rs, vendor_sell.rs, coin_store_siblings.rs, multiplayer.rs, kart_service.rs) drives the AUTH2 broker or the osfr-login binary flags, so no test is clearly superseded or duplicate. Closest overlaps are login.rs ban/membership/lock tests, but they are in-process and were judged weaker. I only sampled login.rs by name and grep, not by reading its bodies, so the partial overlaps (ban, membership byte, store lock) deserve a look if the suite is trimmed. The ignored LAN test is lead-only and counts toward review runs."}
]}
