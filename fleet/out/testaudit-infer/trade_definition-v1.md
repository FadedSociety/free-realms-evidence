<!-- fleet job=testaudit-infer id=trade_definition-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[7146, 9590, 6, 770] model=claude-haiku-5-5 -->
# tests/trade_definition.rs

{"file": "tests/trade_definition.rs",
 "tests": [{"name": "no_trade_and_max_stack_come_from_the_definition_row", "verdict": "keep", "covered_by": null, "reason": "Only test that drives Inventory::trade_flags directly with synthetic definition rows: NO_TRADE set/unset (byte +44), max_stack <=0 mapped to uncapped, a too-short row (id 8) yielding no entry, and an unknown id yielding None. Other files use trade_flags only indirectly (battle_prize_bag_preflight, field_battle_roster, vendor_stock_coverage, field_battle_fixture) or check one real catalogue ride row (station_cash::bought_ride_catalogue_row_is_no_trade), none of which pin the short-row or unknown-id refusal or the uncapped mapping. Not removable."}],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Single-test file; no created_by/last_changed_by metadata in the pack. The short-row and unknown-id cases are refusal-style checks, so kept per the conservative rule. Trade-gate behaviour in src/trade.rs is tested in player_trade.rs and trade.rs, but those drive the gate, not the definition-row reader."}
