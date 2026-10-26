<!-- fleet job=testaudit-infer id=piece_021-v1 status=done turns=2 usd=0.0036 tokens(read,write,in,out)=[12236, 19908, 6, 2057] model=claude-haiku-5-5 -->
# tests/piece_021.rs

{"file": "tests/piece_021.rs",
 "tests": [
  {"name": "catalogue_accepts_recovered_rows_and_pins_schema", "verdict": "keep", "covered_by": null, "reason": "Only test that pins the schema version and row count of the property catalogue; no other test file drives src/restoration/piece_021.rs."},
  {"name": "a_property_without_a_recovered_channel_refuses_every_channel", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a property with no channel refuses all four channels and changes no balance or ownership. Unique to this module."},
  {"name": "catalogue_rejects_a_member_price_that_is_not_the_recovered_discount", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal of a corrupted member price. tests/piece_083.rs has a member-price check, but it exercises a different module (coin store), so it is not the same path."},
  {"name": "catalogue_rejects_unknown_schema_and_duplicate_deed_items", "verdict": "keep", "covered_by": null, "reason": "Refusal checks for unsupported schema version and a deed item shared by two properties. No equivalent elsewhere."},
  {"name": "marketplace_purchase_charges_once_and_ownership_is_once_only", "verdict": "keep", "covered_by": null, "reason": "Currency accounting plus once-only ownership and debit proposal. Unique to piece_021 acquisition."},
  {"name": "non_member_pays_the_regular_price", "verdict": "keep", "covered_by": null, "reason": "Checks the regular-price branch of the marketplace charge; the only test of that branch in this module."},
  {"name": "insufficient_station_cash_leaves_ownership_and_balance_untouched", "verdict": "keep", "covered_by": null, "reason": "Refusal that changes nothing. Unique to this module."},
  {"name": "membership_claim_is_free_once_only_and_member_gated", "verdict": "keep", "covered_by": null, "reason": "Member-gate refusal plus once-only claim and no debit. Unique to this module."},
  {"name": "starter_grant_is_once_per_character_and_migration_is_explicit", "verdict": "keep", "covered_by": null, "reason": "Once-per-character grant and explicit migration grant; persistence-relevant ownership rule with no equivalent elsewhere."},
  {"name": "unknown_property_and_unsupported_channel_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal checks for unknown property and unsupported channel, both changing no balance."},
  {"name": "bonus_grant_is_free_and_once_only", "verdict": "keep", "covered_by": null, "reason": "Free and once-only bonus grant; unique to this module."},
  {"name": "an_ownerless_request_is_rejected_without_mutation", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal (owner 0) that must not mutate state."},
  {"name": "corrupted_catalogue_bytes_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal of non-JSON input. Cheap, but no other test in the suite drives this loader."},
  {"name": "real_recovered_catalogue_loads_and_charges_the_recorded_prices", "verdict": "keep", "covered_by": null, "reason": "Ignored by default (needs private lab corpus); checks the real 31-row extract. Not run in normal suite, so not a removal candidate."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file tests src/restoration/piece_021.rs, a module included via #[path] and not yet registered in src/lib.rs. No other test file in the pack or in a repo search drives that module, so nothing is superseded or duplicated. The only near-overlap is tests/piece_083.rs (member price formula, coin store), a different module and path. The real-catalogue test is #[ignore]d and opt-in. Once the lead registers the module and drops the include, the file should be reviewed again for overlap with any housing tests. Created_by and last_changed_by are null in the pack, so no obsolescence by later task could be checked."}
