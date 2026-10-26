<!-- fleet job=testaudit-infer id=startup_snapshot-v1 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[7066, 10223, 6, 1050] model=claude-haiku-5-5 -->
# tests/startup_snapshot.rs

{"file": "tests/startup_snapshot.rs",
 "tests": [
  {"name": "empty_snapshot_serializes_as_typed_json_and_loads", "verdict": "keep", "covered_by": null, "reason": "Only test that writes an empty StartupSnapshot to disk as JSON and reloads it via StartupSnapshot::load, pinning schema_version 1 and the 23 NPC spawn / 2 effect-tag defaults. Other files (gateway, bot_smoke, shared_world_membership, app_fuzz) only pass StartupSnapshot::empty() into Gateway and never exercise the file load path, so it is not clearly covered elsewhere."},
  {"name": "exports_typed_snapshot_to_lab_and_matches_all_45_builders", "verdict": "keep", "covered_by": null, "reason": "The only test of StartupSnapshot::export_from_reference and of the 2470 quick-chat / 149 POI / 23 spawn counts against the private reference. It is #[ignore]d and needs OSFR_GATEWAY_REFERENCE, so it does not run on the merge suite, but it is the sole check of this path and removing it would lose the only reference-capture validation. The notes (D010, F140) record it being run manually with --ignored."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Two tests, no helpers, no crate modules beyond startup_snapshot and gateway. Nothing redundant found. The ignored export test costs nothing on the default run. Its name says '45 builders' but it asserts 2470/149/23 counts, which is a minor naming mismatch, not a redundancy."}
