<!-- fleet job=testaudit-infer id=startup_world-v1 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[10210, 14801, 6, 1656] model=claude-haiku-5-5 -->
# tests/startup_world.rs

{"file": "tests/startup_world.rs",
 "tests": [
  {"name": "mapped_world_content_reproduces_capture_and_exports_typed_rows", "verdict": "keep", "covered_by": null, "reason": "Only byte-oracle check of the startup world sections against the private capture (quick chat, POIs, 23 NPCs, journal, welcome, MOTD). It is #[ignore]d without OSFR_GATEWAY_REFERENCE, but no other file replays these captures, so it is not clearly covered elsewhere."},
  {"name": "synthetic_quick_chat_row_changes", "verdict": "keep", "covered_by": null, "reason": "Checks that a changed quick-chat field changes the built bytes and parses back. No other test file drives build_quick_chat directly; the only other reference is a comment or an import. Conservative keep."},
  {"name": "synthetic_poi_position_and_name_change", "verdict": "keep", "covered_by": null, "reason": "Round-trip and change check for POI name and position fields. Only this file calls build_points_of_interest, so nothing else covers it."},
  {"name": "synthetic_npc_actor_transform_flags_and_lists_change", "verdict": "keep", "covered_by": null, "reason": "Covers AddNpc actor, transform, flags and nested attachment/effect/variable lists in one round trip. Many other files use build_add_npc or parse_add_npc as a helper, but none assert this full field set. Keep, since it is the widest AddNpc field check."},
  {"name": "synthetic_journal_rows_change", "verdict": "keep", "covered_by": null, "reason": "Change and round-trip check on journal definition rows. quest_engine.rs calls build_journal_definitions in src, but no test file asserts this field-level behaviour."},
  {"name": "synthetic_welcome_rows_and_flag_change", "verdict": "keep", "covered_by": null, "reason": "Covers the welcome flag and nested rows and their round trip. No other test file calls build_welcome_screen."},
  {"name": "synthetic_motd_strings_change", "verdict": "keep", "covered_by": null, "reason": "Small change check on MOTD string fields. It is weak, but no other test covers build_motd, so it is kept by the conservative rule."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Checked with a search: no other tests/ file calls the build_* functions for quick chat, POI, journal, welcome or MOTD. Most other files only use build_add_npc or parse_add_npc as fixture helpers. The similar files (startup_catalogues, startup_selfdata) cover other startup sections, not these. The synthetic tests are fairly weak (change-detection plus parse-back), so a later consolidation could fold them into a unit test in src/startup_world.rs, but no test elsewhere is equally strong, so none is marked removable. I did not read the src unit tests, so duplication with in-crate tests is unverified."}
