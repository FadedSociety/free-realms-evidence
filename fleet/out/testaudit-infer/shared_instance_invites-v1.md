<!-- fleet job=testaudit-infer id=shared_instance_invites-v1 status=done turns=4 usd=0.0030 tokens(read,write,in,out)=[31206, 12650, 10, 2235] model=claude-haiku-5-5 -->
# tests/shared_instance_invites.rs

{"file": "tests/shared_instance_invites.rs",
 "tests": [
  {"name": "a_grouped_start_invites_the_member_and_only_accept_enters_the_run", "verdict": "keep", "covered_by": null, "reason": "Could not read the test body (file not present at repo tip); the doc describes the only end-to-end two-socket check of the 41/102 invite and the accept-enters-run path, so it is not shown to be covered elsewhere."},
  {"name": "an_accept_rechecks_the_party_and_the_go_gates_after_the_invite", "verdict": "keep", "covered_by": null, "reason": "Refusal/recheck behaviour (accept after party or Go gate changed sends nothing); a refusal check that cannot be matched to an equally strong test without reading the body."},
  {"name": "a_refused_accept_leaves_the_invite_answerable", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a refused accept must leave the invite pending. Keep by the conservative rule."},
  {"name": "the_world_sweep_voids_an_invite_when_a_player_or_the_run_goes_away", "verdict": "keep", "covered_by": null, "reason": "Cleanup/sweep behaviour on departure; not verified as covered elsewhere, so kept."},
  {"name": "an_ungrouped_or_ineligible_player_gets_no_invite", "verdict": "keep", "covered_by": null, "reason": "Refusal check for ineligible players; kept by the conservative rule."}
 ],
 "whole_file_removable": false,
 "confidence": 0.2,
 "notes": "The file tests/shared_instance_invites.rs does not exist in the repository at tip (read and search both return nothing for it or its test names), so the test bodies could not be compared against the similar files (player_trade, multiplayer, guild_routing, shared_field_state, playtest_gateway_smoke). Verdicts are therefore all keep by default. Its helpers (common/group_invite_wire.rs, common/field_battle_fixture.rs) exist and are used by other files (group_invite_expiry.rs, shared_world_membership.rs, social_lists.rs). Overlap with shared_world_membership.rs and group_invite_expiry.rs is plausible for the family-40 invite plumbing but was not verified. Re-run this audit against the branch that contains the file before removing anything."}
