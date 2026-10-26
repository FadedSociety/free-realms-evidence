<!-- fleet job=testaudit-infer id=piece_063-v1 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[10240, 14966, 6, 1583] model=claude-haiku-5-5 -->
# tests/piece_063.rs

{"file": "tests/piece_063.rs",
 "tests": [
  {"name": "original_capture_frames_decode_with_the_recovered_minigame_header", "verdict": "keep", "covered_by": null, "reason": "Only test asserting the recovered sub|state|group|game header against the three retail capture frames for family 39, including the 13-byte truncation refusal. tests/piece_020.rs::original_capture_frames_decode_with_the_recovered_family_widths reuses one 39/7 frame but only checks family widths, not the header fields, so it does not supersede this."},
  {"name": "reward_sub_opcodes_match_the_client_constructors_and_the_pinned_enums", "verdict": "keep", "covered_by": null, "reason": "Pins the 22/45/46/68 reward sub-opcode table, class names and flow directions, plus unknown-sub refusals. The sibling piece_020 sub-opcode test covers the launch family (175), a different enum, so nothing equivalent is elsewhere."},
  {"name": "party_finish_grants_completion_and_one_parcel_per_eligible_member", "verdict": "keep", "covered_by": null, "reason": "Only test of the party-completion policy: any member finishes, each eligible member gets an independent parcel. No equivalent in the similar files (their domains are groups, karts, vendors, social lists)."},
  {"name": "duplicate_and_replayed_finish_are_rejected_without_extra_grants", "verdict": "keep", "covered_by": null, "reason": "Replay and double-payout refusal (AlreadyFinished, re-open of a finished instance, double claim). Security/refusal check with no equally strong test elsewhere; kept."},
  {"name": "ineligible_and_unfinished_requests_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check: no claim before finish, stranger refused, unknown run refused. Kept as a refusal check."},
  {"name": "malformed_rosters_are_refused_at_open", "verdict": "keep", "covered_by": null, "reason": "Hostile/malformed input refusal at open (empty roster, duplicate participant, zero instance, reopen). Kept."},
  {"name": "run_state_snapshot_reports_completions_and_claims", "verdict": "keep", "covered_by": null, "reason": "Asserts the state() snapshot shape and claimed/finished fields. Not a duplicate of the sibling snapshot tests in other domains; kept conservatively as the only check of this module's snapshot."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Every test drives the piece_063 reward ledger, which no other similar file exercises. The only overlap found is the shared 39/7 capture frame in tests/piece_020.rs, which checks different properties. No test is redundant, so the whole file should stay."}
