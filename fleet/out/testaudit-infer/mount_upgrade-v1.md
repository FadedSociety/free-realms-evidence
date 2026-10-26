<!-- fleet job=testaudit-infer id=mount_upgrade-v1 status=done turns=5 usd=0.0040 tokens(read,write,in,out)=[53952, 15428, 12, 2972] model=claude-haiku-5-5 -->
# tests/mount_upgrade.rs

{"file": "tests/mount_upgrade.rs",
 "tests": [
  {"name": "a_saddle_upgrades_an_owned_winged_ride", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end check of the 168/14 training path and its saved change. Nothing similar in the suite; mounts.rs, mount_roster.rs and mount_stats.rs cover roster bytes and stats, not training."},
  {"name": "a_repeat_upgrade_is_refused_and_consumes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a second training must be refused and consume nothing. No equivalent found elsewhere."},
  {"name": "refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal canary for the upgrade route (state and inventory unchanged). Same name as tests in station_cash.rs, job_level_quest.rs, sheep_watch_dungeon.rs and chat_settings.rs, but those drive other systems, so it is not a duplicate."},
  {"name": "malformed_upgrade_requests_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Hostile-input check on 168/14. Keep for safety."},
  {"name": "the_upgrade_survives_save_and_reload", "verdict": "keep", "covered_by": null, "reason": "Persistence check for the saved training. Not covered elsewhere."},
  {"name": "the_upgrade_request_is_a_row_and_an_item", "verdict": "keep", "covered_by": null, "reason": "Pins the dual row/item shape of the upgrade request; not clearly covered elsewhere."},
  {"name": "using_a_saddle_opens_the_upgrade_picker", "verdict": "keep", "covered_by": null, "reason": "Checks the T528 picker route (36/17 and BrowserV2:ShowUpgradableMounts). No other test covers this route."},
  {"name": "a_saddle_use_is_refused_when_not_owned_or_busy", "verdict": "keep", "covered_by": null, "reason": "Refusal check for the saddle use route. Keep."},
  {"name": "upgrade_item_data_is_bounded", "verdict": "keep", "covered_by": null, "reason": "Content-bound check on the upgrade allowlist; not clearly covered elsewhere."},
  {"name": "a_non_saddle_instance_is_left_to_its_own_route", "verdict": "keep", "covered_by": null, "reason": "Routing boundary check (non-saddle instances get no notice or picker). Keep as the only guard for that boundary."},
  {"name": "a_fully_consumed_saddle_cannot_train_a_ride", "verdict": "keep", "covered_by": null, "reason": "Refusal check tying the T527 and T528 saddle-holding rules together. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.3,
 "notes": "Low confidence because the file could not be read: 'read' returned 'not a file' for prototype/osfr-tools/tests/mount_upgrade.rs, and a search of the repo tip found no mount_upgrade.rs, no 168/14 or 79150 references, and no upgrade training in prototype/osfr-tools/src. Only a comment in src/mounts.rs (around line 1142) says is_upgraded awaits glide training. The verdicts above rest on the pack's names and doc lines, and the excerpt is cut off after the first test. The file appears to target a feature (T527/T528 saddle training) that is not in the tip, so it may be on a branch or pending. Nothing was marked removable: the similar mount files (mounts.rs, mount_roster.rs, mount_stats.rs) test roster bytes and stats, not training. The shared 'refusals_change_nothing' name in other files covers different systems. Verify on the branch that holds this file before any removal."}
]}
