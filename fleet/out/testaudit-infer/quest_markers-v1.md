<!-- fleet job=testaudit-infer id=quest_markers-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[42581, 15767, 10, 2498] model=claude-haiku-5-5 -->
# tests/quest_markers.rs

{"file": "tests/quest_markers.rs",
 "tests": [
  {"name": "giver_shows_available_after_add_npc", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the 35/2-before-35/10 ordering for both the per-player and shared-field paths; no similar marker-order assertion found in the similar files."},
  {"name": "accept_moves_the_marker", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end check that accepting clears the giver's '!' and shows the turn-in marker; the similar files drive quest accept but do not assert 35/10 or 35/11 marker packets."},
  {"name": "turn_in_clears_and_unlocks", "verdict": "keep", "covered_by": null, "reason": "Covers the hand-in clear, next-giver unlock and packet ordering before the dialogue close; no equivalent marker assertion elsewhere in the pack."},
  {"name": "refused_accept_changes_no_marker", "verdict": "keep", "covered_by": null, "reason": "Refusal check (forged 49/2 changes nothing: no marker packet, unchanged revision and saved state). Must be kept per refusal rule."},
  {"name": "players_see_their_own_markers", "verdict": "keep", "covered_by": null, "reason": "Per-player isolation check: one player's accept must not touch another's state or revision. Security-style isolation, keep."},
  {"name": "reconnect_recomputes_markers", "verdict": "keep", "covered_by": null, "reason": "Persistence/reload check that markers are recomputed after a serialized reload; body beyond the excerpt was not readable, so kept conservatively."},
  {"name": "idle_pass_sends_nothing", "verdict": "keep", "covered_by": null, "reason": "Negative check that an unchanged pass emits no packets; body not fully readable, kept conservatively."},
  {"name": "job_switch_settles_markers_in_its_own_packet", "verdict": "keep", "covered_by": null, "reason": "Documents job-as-eligibility ordering inside one packet plus a refused request moving nothing; not covered by the similar files."},
  {"name": "extra_spawn_marker_uses_the_runtime_guid", "verdict": "keep", "covered_by": null, "reason": "Guards that the marker uses the runtime guid rather than the template id; distinct from the similar files' assertions. Body not fully readable."},
  {"name": "revision_moves_only_when_quest_state_does", "verdict": "keep", "covered_by": null, "reason": "Canary on the marker revision counter; unique to this file, kept."},
  {"name": "old_startup_snapshots_still_load_the_renamed_add_npc_field", "verdict": "keep", "covered_by": null, "reason": "Backward-compatibility persistence check for an old snapshot field name; must be kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The file path tests/quest_markers.rs could not be read from the repo (read and grep both returned 'not a file' / no matches for the later test names), so the bodies of reconnect_recomputes_markers, idle_pass_sends_nothing, extra_spawn_marker_uses_the_runtime_guid, revision_moves_only_when_quest_state_does and old_startup_snapshots_still_load_the_renamed_add_npc_field were not inspected; verdicts rest on the pack's names and doc lines. Related shared_npc_view and update_npc_visibility coverage exists in brawler_job_chain.rs, brawler_mongo_chain.rs, live_placements.rs and collection_coin_pickup.rs, but those assert object visibility, not 35/10 or 35/11 marker packets, so no duplicate was confirmed. Re-run with the file present to verify the kept verdicts, especially the unread tests."}
