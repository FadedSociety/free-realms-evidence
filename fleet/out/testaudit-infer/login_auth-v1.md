<!-- fleet job=testaudit-infer id=login_auth-v1 status=done turns=4 usd=0.0037 tokens(read,write,in,out)=[42432, 16623, 10, 2394] model=claude-haiku-5-5 -->
# tests/login_auth.rs

{"file": "tests/login_auth.rs",
 "tests": [
  {"name": "credential_failure_lockout_recovery_success_reset_and_unknown_capacity", "verdict": "keep", "covered_by": null, "reason": "Lockout threshold, 60s recovery, success reset and unknown-hash capacity bound on LoginFailures; the only direct test of this limiter. Security refusal check, and the sibling broker lockout test goes through the network path, not this struct."},
  {"name": "good_signature_returns_a_one_use_ascii_session_bound_to_the_account", "verdict": "keep", "covered_by": null, "reason": "Happy path plus one-use redemption and token format at the module level; only direct check of redeem binding to account id."},
  {"name": "wrong_key_and_replayed_challenge_are_refused_even_after_failure", "verdict": "keep", "covered_by": null, "reason": "Refusal and replay check: a failed verify must not consume a good later login, and a used challenge cannot be replayed. Security check."},
  {"name": "signature_is_bound_to_server_handle_and_nonce", "verdict": "keep", "covered_by": null, "reason": "Transcript-binding security check; independently builds the message and rejects each altered field."},
  {"name": "expiry_is_exactly_sixty_seconds_for_challenges_and_tokens", "verdict": "keep", "covered_by": null, "reason": "Exact expiry boundary for challenges and tokens; no equivalent elsewhere in the suite."},
  {"name": "table_caps_refuse_growth_and_expired_entries_free_capacity", "verdict": "keep", "covered_by": null, "reason": "Capacity refusal and expiry-freed capacity; bounded-growth check unique to this file."},
  {"name": "malformed_lengths_and_malleated_signature_are_refused_without_panicking", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check for lengths and non-canonical signature; security canary."},
  {"name": "revoked_keys_disable_pending_challenges_and_tokens", "verdict": "keep", "covered_by": null, "reason": "Revocation must disable outstanding tokens and challenges; security refusal check. login_broker covers ban/unban only, not key revocation."},
  {"name": "handles_are_bounded_and_unknown_accounts_fail_generically", "verdict": "keep", "covered_by": null, "reason": "Handle validation and generic failure for unknown accounts; refusal check. Broker no-enumeration test is at the network layer and does not test handle bounds."},
  {"name": "weak_keys_and_bad_signatures_never_create_tokens", "verdict": "keep", "covered_by": null, "reason": "Low-order key rejection via validate_public_key and no token from bad signatures; security check."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Audited against the similar files only by name. login_broker.rs (broker_good_signature_wrong_key_wrong_server_and_no_enumeration, account_lockout_unknown_lockout_ip_budget_and_malformed_replies_are_generic) overlaps some behaviour, but it drives the network broker, not LoginAuth or LoginFailures directly, so I did not mark anything superseded. I did not read the bodies of login_broker.rs or bot_broker_login.rs to confirm assertion strength. The crate's src/login_auth.rs has no unit tests, so nothing here duplicates an in-crate test. No task metadata was provided (created_by and last_changed_by are null)."}
