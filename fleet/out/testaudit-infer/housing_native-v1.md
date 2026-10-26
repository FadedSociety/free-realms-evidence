<!-- fleet job=testaudit-infer id=housing_native-v1 status=done turns=3 usd=0.0042 tokens(read,write,in,out)=[28681, 19277, 8, 2914] model=claude-haiku-5-5 -->
# tests/housing_native.rs

{"file": "tests/housing_native.rs",
 "tests": [
  {"name": "fixture_asset_bytes_follow_the_client_reader_order", "verdict": "keep", "covered_by": null, "reason": "Pins the byte-level client reader order (model, selection, definition, aliases, tint). housing_service.rs only decodes FixtureAsset via the round trip and does not assert the layout; no other file checks it."},
  {"name": "place_round_trip_length_and_subtype", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the 42-byte Place length and subtype 2 through both the body and dispatch APIs."},
  {"name": "place_rejects_truncation_trailing_and_non_finite", "verdict": "keep", "covered_by": null, "reason": "Refusal check: every truncation, trailing bytes and non-finite floats must be rejected. No equivalent elsewhere."},
  {"name": "update_empty_round_trip_is_227_bytes", "verdict": "keep", "covered_by": null, "reason": "Pins the 227-byte empty FixtureUpdate layout and subtype 40. Overlaps every_subtype_uses_the_same_explicit_family_boundary only in round-trip, but the length pin is unique."},
  {"name": "update_populated_round_trip_variable_paths", "verdict": "keep", "covered_by": null, "reason": "Round trip of the variable-length paths (actions with key != id, npc guids, unknown guids). Not clearly covered elsewhere."},
  {"name": "update_rejects_oversize_counts_strings_and_lengths", "verdict": "keep", "covered_by": null, "reason": "Security check: oversize counts and declared lengths must not allocate or decode. Canary against hostile input; keep."},
  {"name": "update_rejects_invalid_utf8_raw_bools_and_trailing", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal: invalid UTF-8, non-0/1 raw bools and trailing bytes. Keep."},
  {"name": "update_rejects_non_finite_instance_fields", "verdict": "keep", "covered_by": null, "reason": "Refusal of NaN scale on both encode and decode paths. Keep."},
  {"name": "remove_round_trip_and_bounds", "verdict": "keep", "covered_by": null, "reason": "Round trip plus truncation and trailing refusal for FixtureRemove (10 bytes). Keep."},
  {"name": "house_info_round_trip_and_bool_policy", "verdict": "keep", "covered_by": null, "reason": "Pins the HouseInfo bool policy. housing_service.rs edit_mode test uses HouseInfo only at the service level, so the codec-level bool policy is not duplicated."},
  {"name": "zone_data_follows_native_pair_between_the_second_and_third_words", "verdict": "keep", "covered_by": null, "reason": "Pins ZoneData byte layout and snapshot placement after factory_plot_id. Unique layout check."},
  {"name": "instance_list_rows_carry_the_snapshot_after_factory_plot_id", "verdict": "keep", "covered_by": null, "reason": "Pins InstanceList row layout. lot_deeds.rs and world_reload_startup.rs decode InstanceList but do not assert the snapshot offset; keep."},
  {"name": "placement_denied_is_one_string_and_refuses_trailing", "verdict": "keep", "covered_by": null, "reason": "Refusal of trailing bytes, invalid UTF-8 and oversize message. housing_service.rs only checks the decoded message text, not these refusals."},
  {"name": "dispatch_rejects_empty_and_unknown_subtype", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal of empty and unknown subtype in the dispatcher. Keep."},
  {"name": "inner_remove_framing_has_one_family_and_one_subtype", "verdict": "keep", "covered_by": null, "reason": "Pins the explicit 127 family prefix plus subtype 41 bytes and that body and inner APIs are not interchangeable. The every_subtype test covers round trip only, not these exact bytes."},
  {"name": "inner_framing_refuses_wrong_family_truncation_double_prefix_and_trailing", "verdict": "keep", "covered_by": null, "reason": "Refusal check for wrong family, double prefix and truncation at every cut. Keep."},
  {"name": "every_subtype_uses_the_same_explicit_family_boundary", "verdict": "keep", "covered_by": null, "reason": "Cross-subtype check that every packet gets the same 127 family boundary. Not duplicated by any other file's test."},
  {"name": "private_housing_corpus_round_trips_through_registered_codec", "verdict": "keep", "covered_by": null, "reason": "Ignored private-corpus canary (requires OSFR_HOUSING_CAPTURE_DIR). Keep; it cannot be replaced by public tests."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Every test is a codec-level byte-layout, refusal or canary check on the housing_native module. The similar files (zone_transition, housing_service, housing_session, lot_deeds, world_reload_startup) exercise these codecs through service or session paths and assert decoded values, not the byte layouts or hostile-input refusals. No test is redundant with a named equal-or-stronger test, so none is marked removable. Lines 200-250 were not read in full; verdicts there rest on test names and the excerpt."}
