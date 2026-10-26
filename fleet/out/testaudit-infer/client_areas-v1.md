<!-- fleet job=testaudit-infer id=client_areas-v1 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[12209, 19225, 6, 1860] model=claude-haiku-5-5 -->
# tests/client_areas.rs

{"file": "tests/client_areas.rs",
 "tests": [
  {"name": "enable_and_disable_packets_are_the_readers_eleven_bytes", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the 11-byte opcode-89 wire layout against the client reader (u16 opcode, i32 id, u8 bool, i32 ms); no other test in the repo references ClientAreas or set_area."},
  {"name": "season_windows_are_inclusive_wrap_the_year_and_follow_the_offset", "verdict": "keep", "covered_by": null, "reason": "Only test of season window inclusivity, year wrap, leap day and UTC offset handling; the notes record it as the canary that caught a year-wrap bug."},
  {"name": "world_ready_sends_the_pad_and_the_season_areas_only_in_season", "verdict": "keep", "covered_by": null, "reason": "Sole check of world-ready packet contents in and out of season, and that nothing is persisted across reload."},
  {"name": "every_shipped_season_is_active_inside_its_window_and_not_outside", "verdict": "keep", "covered_by": null, "reason": "Sole check of every shipped season's window against the real content file, including required season names."},
  {"name": "a_season_without_client_areas_gates_by_date_and_switches_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal/no-op behaviour for seasons with no areas; no equivalent elsewhere."},
  {"name": "an_event_toggle_reports_elapsed_time_and_unknown_ids_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for unknown ids plus elapsed-time reporting; not covered elsewhere."},
  {"name": "season_changes_report_each_boundary_once_even_with_a_clock_going_back", "verdict": "keep", "covered_by": null, "reason": "Once-only boundary reporting and clock-regression behaviour; unique to this file."},
  {"name": "an_event_and_a_season_sharing_an_area_keep_it_on_while_either_holds_it", "verdict": "keep", "covered_by": null, "reason": "Shared-area hold logic; unique to this file."},
  {"name": "missing_content_means_no_areas_and_malformed_content_names_the_file", "verdict": "keep", "covered_by": null, "reason": "Hostile/malformed content refusal table (about 17 cases) plus missing-file behaviour; no other coverage."},
  {"name": "every_content_area_is_a_client_area_the_client_ships_disabled", "verdict": "keep", "covered_by": null, "reason": "Cross-checks content ids against the client's FabledRealmsAreas.xml; no other test does this. It reads a lab path, so it may skip or fail where the lab extract is absent."}
 ],
 "whole_file_removable": false,
 "confidence": 0.85,
 "notes": "The similar-file pack (fishing_entry, housing_session, coin_store_siblings, kart_service, kart_npc_entry) has no overlapping client-area coverage; a repo-wide search for ClientAreas, set_area, world_ready_packets and is_season_active finds uses only in this file and the gateway binary, with no other test driving these paths. No test is redundant. Caveat: every_content_area... depends on lab/extracted, outside the repo test data, so its portability should be checked, though that is a robustness issue rather than a redundancy one."}
