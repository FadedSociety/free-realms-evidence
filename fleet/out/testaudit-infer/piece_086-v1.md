<!-- fleet job=testaudit-infer id=piece_086-v1 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[10230, 15444, 6, 1694] model=claude-haiku-5-5 -->
# tests/piece_086.rs

{"file": "tests/piece_086.rs",
 "tests": [
  {"name": "recovered_coin_wire_constants_match_the_supplied_packet_enums", "verdict": "keep", "covered_by": null, "reason": "Only check of the piece_086 wire section/opcode constants; the module is used only by this file, so nothing else pins them."},
  {"name": "recovered_client_rows_match_scriptsbase", "verdict": "keep", "covered_by": null, "reason": "Pins the ScriptsBase data-source row numbers for the recovered currency rows; no other test file references piece_086 row constants."},
  {"name": "the_two_recovered_currencies_have_distinct_scopes_and_grants", "verdict": "keep", "covered_by": null, "reason": "Asserts the coin vs Station Cash scope and grant split, a refusal-style invariant (Station Cash not gameplay-grantable); no equivalent elsewhere."},
  {"name": "producers_classify_currency_direction_and_evidence", "verdict": "keep", "covered_by": null, "reason": "Full producer classification table for this module; unique to piece_086 types."},
  {"name": "audit_accepts_the_local_producers_once_each", "verdict": "keep", "covered_by": null, "reason": "Positive audit path and totals for the piece_086 audit; only test of that function."},
  {"name": "audit_rejects_a_replayed_source_instance", "verdict": "keep", "covered_by": null, "reason": "Replay/duplicate refusal check; security-type test with no equal elsewhere."},
  {"name": "audit_rejects_negative_and_above_wire_range_amounts", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal (negative and oversized amounts); keep."},
  {"name": "audit_rejects_an_unkeyed_source", "verdict": "keep", "covered_by": null, "reason": "Zero-instance refusal check; keep."},
  {"name": "account_wallet_funding_is_the_only_station_cash_source", "verdict": "keep", "covered_by": null, "reason": "Invariant that Station Cash has a single source; a canary-style check of the economy split. Also checks mixed-currency accounting."},
  {"name": "coin_ledger_refuses_overflow_and_overdraw", "verdict": "keep", "covered_by": null, "reason": "Overflow/overdraw refusal on CoinLedger; the sibling coin-store tests exercise a different store path and do not drive this ledger type."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "All ten tests are kept. The file is the only test target that drives the piece_086 module (CoinLedger, audit, producer table, ScriptsBase row constants), so no other file supersedes or duplicates its assertions. The similar files (piece_043, coin_store_siblings, piece_011, station_cash, piece_073) test other modules; coin_store_siblings and station_cash touch coin/Station Cash behaviour, but through different code paths and not the piece_086 constants or ledger. The file's module is pulled in by #[path] include, which is a lead-owned integration item, not a redundancy. Confidence is moderate because I did not read the similar files' bodies line by line."}
