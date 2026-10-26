<!-- fleet job=testaudit-infer id=mount_roster-v1 status=done turns=4 usd=0.0045 tokens(read,write,in,out)=[49343, 23401, 10, 2221] model=claude-haiku-5-5 -->
# tests/mount_roster.rs

{"file": "tests/mount_roster.rs",
 "tests": [
  {"name": "world_entry_sends_the_owned_ride_roster", "verdict": "keep", "covered_by": null, "reason": "Only test that pins the exact 168/5 world-entry roster bytes (row fields, pet 53/5 beside it, empty roster for no rides). tests/mount_bots.rs waits for a 168/5 only end-to-end and does not decode its rows, so it does not cover this."},
  {"name": "grants_send_the_roster_once_and_nothing_else_does", "verdict": "keep", "covered_by": null, "reason": "Asserts the roster is sent exactly once per ride change and that non-ride grants, repeat grants and idle ticks send nothing. This is a no-duplicate guard that no other file in the set checks."},
  {"name": "summon_put_away_and_refusal_rosters_leave_nothing_for_the_sync", "verdict": "keep", "covered_by": null, "reason": "Covers summon, put-away and refused-summon rosters and asserts the following sync adds no second roster. The refusal branch is a refusal check. Only tests/mount_wired.rs and tests/mount_stats.rs touch settle_mounts, and neither asserts these roster contents."},
  {"name": "a_new_session_sends_the_roster_again_at_world_entry_and_nothing_before", "verdict": "keep", "covered_by": null, "reason": "Pins the new-session resend and the absence of any roster before world entry. Not seen elsewhere in the compared files."},
  {"name": "losing_the_ride_item_puts_the_ride_away", "verdict": "duplicate", "covered_by": "tests/mount_stats.rs (ride item traded away, T424 put-away in settle_mounts, around lines 282-288)", "reason": "Same trade-away path and put-away assertion as the ride-item-traded-away case in mount_stats.rs. Low confidence: I read only the comment and the call site there, not the full assertions, so the match is not verified line by line."},
  {"name": "a_scaled_dragon_stays_out_while_another_of_its_items_is_owned", "verdict": "keep", "covered_by": null, "reason": "Service-level check for multi-item ownership of the Scaled Dragon ride, using the real mounts.json catalogue. Not found in the compared files. Its doc notes Gameplay cannot host these items, so no Gameplay-level equivalent exists."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The similar files returned by the pack (housing, kart, station cash, coin store) are not about rides and overlap by name only. The real ride neighbours are tests/mount_wired.rs, tests/mount_stats.rs, tests/mounts.rs and tests/mount_routing.rs. I checked only grep hits and a few call sites in them, not their full assertions, so the verdicts above are conservative. Only the trade-away test has a candidate duplicate. Confirm it against mount_stats.rs before removing it."}
