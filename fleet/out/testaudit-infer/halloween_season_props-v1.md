<!-- fleet job=testaudit-infer id=halloween_season_props-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[20662, 10995, 8, 1722] model=claude-haiku-5-5 -->
# tests/halloween_season_props.rs

{"file": "tests/halloween_season_props.rs",
 "tests": [
  {"name": "the_twelve_halloween_rows_are_tagged_and_leave_only_when_the_season_is_over", "verdict": "keep", "covered_by": null, "reason": "Only test that drives NpcVisibility::retain_in_season over the shipped table plus the 12 archived Halloween rows; asserts the over-season drops exactly the tagged rows and keeps live rows. A repo search for retain_in_season / load_in_season_at under tests/ finds no other caller. client_areas.rs covers is_season_active windows, a different API, so it does not supersede this."},
  {"name": "an_unknown_season_fails_naming_the_row_and_drops_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check: an unknown season must error naming the row and change nothing. No equivalent assertion found elsewhere in tests/."},
  {"name": "loading_for_play_follows_the_shipped_season_dates", "verdict": "keep", "covered_by": null, "reason": "Pins NpcVisibility::load_in_season_at against the shipped Halloween dates at fixed clocks (in and out of season), including the cake content-key map. Not found elsewhere; client_areas.rs tests date windows on a different type."},
  {"name": "a_row_naming_a_season_the_content_lacks_fails_the_load", "verdict": "keep", "covered_by": null, "reason": "Load-time refusal for a season the content does not define; a refusal check with no equivalent found. The body was truncated in the pack, so the assertion detail is unverified."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Could not read the full file: the read tool reported 'not a file' for the path and a repo grep for the test names found nothing, so the file may sit at another path or be uncommitted. The excerpt was also cut off mid-way through the last test. Verdicts rest on the excerpt and on searches of tests/ for retain_in_season, load_in_season_at and Halloween. client_areas.rs (T457/T659) and piece_051.rs mention Halloween but test different APIs (season windows and enemy model names). The file header says T468 retired these rows and world.rs never reads the archive, so the tests cover a dormant path. That is not obsolescence, because the NpcVisibility season filter is still exercised. Conservative keep on all four."}
]}
