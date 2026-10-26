<!-- fleet job=testaudit-infer id=piece_075-v1 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[9522, 13407, 6, 1374] model=claude-haiku-5-5 -->
# tests/piece_075.rs

{"file": "tests/piece_075.rs",
 "tests": [
  {"name": "mailbox_catalogue_keeps_the_recovered_addresses_and_models", "verdict": "keep", "covered_by": null, "reason": "Only test of the piece_075 mailbox catalogue (23 actors, NameId, model ids, spawn data, address lookup). No other test file references mailbox_by_address, MAILBOXES or the piece_075 module; the similar files (piece_037, piece_031, piece_076) cover different recovery modules."},
  {"name": "delivery_activities_stay_on_the_recovered_client_rows", "verdict": "keep", "covered_by": null, "reason": "Only check of the DELIVERY_ACTIVITIES client-row table (ids, names, string ids, live flag, activity types). No overlap found in other test files."},
  {"name": "route_text_claims_keep_the_recovered_route_lines", "verdict": "keep", "covered_by": null, "reason": "Only check of ROUTE_TEXT_CLAIMS hash-to-text pairs; not exercised elsewhere in the suite."},
  {"name": "delivery_notification_matches_the_client_lua", "verdict": "keep", "covered_by": null, "reason": "Pins the notification string id 388255 and icon 1237 against the client Lua; a canary for the recovered constants. Nothing else in the suite checks them."},
  {"name": "delivery_run_validates_targets_and_completion_without_inventing_a_route", "verdict": "keep", "covered_by": null, "reason": "Refusal checks (duplicate delivery AlreadyDelivered, UnknownTarget on deliver and on start) plus completion state; the only exercise of DeliveryRun. Refusal behaviour, so kept."},
  {"name": "route_membership_order_and_timer_stay_reported_gaps", "verdict": "keep", "covered_by": null, "reason": "Canary asserting the explicit gap flags (membership, order, packets not recovered; timer None) and validate() passes. Guards against inventing values; kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Self-contained #[path] include of src/restoration/piece_075.rs; no other test file drives this module (checked by search for piece_075 symbols, DeliveryRun, mailbox_by_address, ROUTE_TEXT_CLAIMS). Similar-file scores were from shared vocabulary only. The notes reference a Python checker (tests/pieces/test_piece_075.py) that is not a Rust test and is out of scope. Not reviewed: the src module contents beyond the grep hits, and the excerpt's numeric values were not re-verified against the client tables."}
