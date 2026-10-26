<!-- fleet job=testaudit-infer id=mount_follow-v1 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[21072, 13054, 8, 1551] model=claude-haiku-5-5 -->
# tests/mount_follow.rs

{"file": "tests/mount_follow.rs",
 "tests": [
  {"name": "an_unmounted_player_keeps_the_sentinel_tail", "verdict": "keep", "covered_by": null, "reason": "Only test that pins the AddPc tail bytes of an unmounted player (sentinel guid 0, seat -1, queue -1) through PlayerRegistry::join. tests/mount_routing.rs checks MountService::view().tail() (the service value), not the bytes players.rs writes into AddPc, so it does not cover this path."},
  {"name": "a_viewer_who_arrives_later_gets_the_riders_mount_block", "verdict": "keep", "covered_by": null, "reason": "Only check that a late viewer's AddPc carries the rider's ride GUID, seat, queue and lift, and that the frame size and the other bytes are unchanged. The similar mount_routing test a_seated_rider_carries_the_mount_tail_and_the_ride_copies_its_moves asserts the service-side tail and the 168/2 Mount response, not the AddPc frame built in players.rs, so it is not a duplicate."},
  {"name": "setting_a_mount_sends_nothing_and_clearing_it_restores_the_sentinel", "verdict": "keep", "covered_by": null, "reason": "Covers that set_mount emits no packets, that the seated tail survives a leave-and-return of the rider, that clearing with MountTail::NONE restores the plain AddPc, and that an unknown session is ignored. No other file drives set_mount on the registry. The unknown-session check is weak on its own but is part of a unique path, so it is kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The five most similar files (housing_session, power_up_drops, fishing_entry, coin_store_siblings, sc_earnings) contain no mount tests and were not overlapping. The closest is tests/mount_routing.rs (a_seated_rider_carries_the_mount_tail_and_the_ride_copies_its_moves), which checks MountService and the Mount response rather than the players.rs AddPc bytes. tests/mount_stats.rs and tests/mount_roster.rs also use MountService, not PlayerRegistry::set_mount. Confidence is limited by not having read every mount file in full."}
