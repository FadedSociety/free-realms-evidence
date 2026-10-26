<!-- fleet job=testaudit-infer id=ride_sources-v1 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[9579, 12138, 6, 1600] model=claude-haiku-5-5 -->
# tests/ride_sources.rs

{"file": "tests/ride_sources.rs",
 "tests": [
  {"name": "every_ride_is_sold_by_a_vendor_inside_the_price_bounds", "verdict": "keep", "covered_by": null, "reason": "Only test that checks every ride's Station Cash price is inside the policy bounds, that no ride remains coin-vendor stock or has coin prices, and that the ride catalogue count (89) and earn-only count (8) hold. station_cash.rs covers the world-entry rows and a few sample rides, not the full catalogue sweep."},
  {"name": "osfr_parity_rides_match_their_item_definitions", "verdict": "keep", "covered_by": null, "reason": "Unique check (T452) that each of the 35 added rides has one item whose client definition presents the ride's name and icon with item type 19. No similar file checks presentation data for these ids."},
  {"name": "osfr_parity_ride_evidence_names_its_real_source", "verdict": "keep", "covered_by": null, "reason": "Provenance check (T452 review) that evidence cites the correct source (client vs legacy) and that tint evidence carries (R). Unique to this file; it guards data provenance rather than behaviour, so it is not removable without a replacement."},
  {"name": "buying_each_ride_with_coins_grants_it", "verdict": "keep", "covered_by": null, "reason": "Despite the historical name, it buys every listed ride (81 listings) through the real order packet and checks exact wallet debit and ownership after each. station_cash.rs::order_debits_exact_price_and_grants_once and marketplace_owned_rides.rs::buying_a_ride_greys_it_out cover single orders, not the full sweep, so it is not clearly superseded. Conservative keep; a possible candidate for consolidation with station_cash world-entry tests if the batch needs trimming."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "All four tests are the only or broadest checks of their area. Overlap exists with tests/station_cash.rs (world_entry_store_rows_are_the_shipped_rides_at_their_scaled_prices, order_debits_exact_price_and_grants_once) and tests/marketplace_owned_rides.rs (buying_a_ride_greys_it_out_and_the_second_order_is_refused), but none is a strict superset. The file's historical names are intentionally retained per its header. Only the file's own content was read (test bodies and header); similar files were judged from the pack's test names, not their bodies, so confidence is moderate."}
