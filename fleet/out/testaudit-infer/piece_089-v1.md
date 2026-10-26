<!-- fleet job=testaudit-infer id=piece_089-v1 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[24075, 16007, 8, 2752] model=claude-haiku-5-5 -->
# tests/piece_089.rs

{"file": "tests/piece_089.rs",
 "tests": [
  {"name": "subopcode_table_matches_client_constructors", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the group family (40), field offset, and the 15-row sub-opcode table against the shipped client constructors; the sibling social_lists.rs uses family 40 subs 1-5 only and does not check the full table or the 10/12/18 rejections."},
  {"name": "parses_invite_frame_header_and_keeps_body_opaque", "verdict": "keep", "covered_by": null, "reason": "Only check of the header parser's field extraction and the opaque-body guarantee for this unit; no equivalent header-level test found in other files."},
  {"name": "rejects_other_families_and_unknown_subopcodes", "verdict": "keep", "covered_by": null, "reason": "Refusal check for foreign family and unknown sub-opcode at the parser level; keep as a refusal test."},
  {"name": "rejects_malformed_envelope", "verdict": "keep", "covered_by": null, "reason": "Hostile/malformed input refusal (length mismatch, truncated header); keep per refusal rule."},
  {"name": "invite_accept_and_leader_membership", "verdict": "keep", "covered_by": null, "reason": "Happy-path lifecycle on PartyRegistry (pending is not membership, accept adds member, leader kept). Similar flow exists in social_lists::group_invite_accept_capacity_kick_leader_leave_and_disband but through the social service API, not this registry, so not the same path."},
  {"name": "duplicate_accept_and_uninvited_accept_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal checks (AlreadyInParty, NoPendingInvite); keep."},
  {"name": "invite_rejects_self_duplicate_and_cross_party_members", "verdict": "keep", "covered_by": null, "reason": "Multiple refusal checks on invite; keep. social_lists::refused_group_invites_leave_membership_and_pending_invites_unchanged is a related refusal test but drives the service layer."},
  {"name": "capacity_counts_members_and_open_invites", "verdict": "keep", "covered_by": null, "reason": "Capacity reservation by open invites is a distinct rule; keep."},
  {"name": "decline_releases_the_slot", "verdict": "keep", "covered_by": null, "reason": "Checks decline frees capacity and rejects declining without invite; keep."},
  {"name": "only_the_leader_kicks_and_never_self", "verdict": "keep", "covered_by": null, "reason": "Authorization refusal (NotLeader, SelfTarget); keep."},
  {"name": "leaving_member_is_not_re_addable_while_invited_elsewhere", "verdict": "keep", "covered_by": null, "reason": "Re-invite after leave lifecycle edge case, not covered by other files; keep."},
  {"name": "leader_leave_transfers_to_the_oldest_member", "verdict": "keep", "covered_by": null, "reason": "Unique succession rule (oldest member becomes leader); keep."},
  {"name": "last_member_leave_disbands_and_drops_open_invites", "verdict": "keep", "covered_by": null, "reason": "Disband and open-invite cleanup on last leave; persistence/cleanup check, keep."},
  {"name": "disconnect_transfers_leadership_then_disbands", "verdict": "keep", "covered_by": null, "reason": "Disconnect path with idempotent Absent outcome; disconnect cleanup is a state-cleanup check, keep. Related to social_lists::client_autorefuse_group_answer_declines_and_disconnect_cleans_state but a different layer."},
  {"name": "capacity_must_allow_a_pair", "verdict": "keep", "covered_by": null, "reason": "Constructor guard for capacity 0 and 1 (InvalidCapacity); small but the only check of this refusal."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "The file is a unit-level model of PartyRegistry (included via #[path] from src/restoration/piece_089.rs), not an integration of the crate, so the similar files exercise the same rules through a different service API (social_lists.rs group tests, which use family-40 packets and the social service). Overlap is conceptual (invite/accept/leave/kick/disconnect), not the same driven path with the same assertions, so nothing is marked superseded or duplicate. The excerpt was truncated mid-test; the remaining tests were read directly from the file tail (lines 235-296). Confidence is moderate because the similar-file comparison was limited to social_lists.rs group tests and the other similar files were not read."}
]}
