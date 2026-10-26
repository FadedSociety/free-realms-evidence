<!-- fleet job=testaudit-infer id=halloween_dance_off-v1 status=blocked turns=6 usd=0.0029 tokens(read,write,in,out)=[47602, 10653, 14, 2236] model=claude-haiku-5-5 -->
# tests/halloween_dance_off.rs

{"file": "tests/halloween_dance_off.rs",
 "tests": [
  {"name": "every_id_resolves_against_the_client", "verdict": "keep", "covered_by": null, "reason": "Gates every id in the shipped halloween_dance_off row against the client tables; the only such check for this row. Not verified against other files, since the file is not in the repo tree."},
  {"name": "the_six_rounds_alternate_sides_and_every_song_area_goes_off_once", "verdict": "keep", "covered_by": null, "reason": "Drives the real WorldEvents::tick through the full run and pins the area on/off order, dancer sides and boombox sparks. No equivalent found in the similar files by name. Not confirmed by reading their bodies."},
  {"name": "each_ending_names_its_winner_leaves_one_cake_and_no_actor_behind", "verdict": "keep", "covered_by": null, "reason": "Checks both endings' lines, reward, cake and actor cleanup. Likely the only check of the ending outcome, but not verified."},
  {"name": "stopping_early_switches_the_song_off_and_removes_every_actor", "verdict": "keep", "covered_by": null, "reason": "Possible overlap with tests/bruce_concert.rs::stopping_a_concert_early_turns_the_music_off_and_removes_bruce (same shape, different event). Not superseded because the actors and content differ, and the bodies could not be read. Kept under the conservative rule."},
  {"name": "the_dance_off_runs_every_half_hour_in_season_and_not_after_it", "verdict": "keep", "covered_by": null, "reason": "Schedule sweep in and out of season. Similar in intent to tests/client_areas.rs season tests, but those check area gating, not this event's schedule. Kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.2,
 "notes": "Blocked: tests/halloween_dance_off.rs and tests/bruce_concert.rs do not exist at the repo path (read returned 'not a file'; name searches for the test names and 'dance_off' found nothing in prototype/osfr-tools). Only the pack excerpt was available, and it is truncated after the third test, so the verdicts rest on test names and doc lines alone and are not verified. Nothing was marked removable. Re-run with the file present, comparing the body of stopping_early_switches... against bruce_concert's stopping test and the schedule test against client_areas.rs season tests."}
