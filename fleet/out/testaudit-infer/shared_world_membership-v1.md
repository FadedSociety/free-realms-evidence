<!-- fleet job=testaudit-infer id=shared_world_membership-v1 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[45749, 23073, 10, 2128] model=claude-haiku-5-5 -->
# tests/shared_world_membership.rs

{"file": "tests/shared_world_membership.rs",
 "tests": [
  {"name": "two_bot_socket_membership_and_transfer", "verdict": "keep", "covered_by": null,
   "reason": "Only end-to-end two-socket test of party join, child-instance isolation for movement/say/quick-chat, cross-instance party and tell, forged encounter rejection with byte-identical save check, and same-scene reunion. The similar files cover shared HP (shared_field_state::two_bot_socket_shared_hp_route) and observer death (shared_field_interest), not membership. It also contains refusal and persistence checks that should not be removed."},
  {"name": "chat_scope_derives_zone_and_position_from_the_live_registry", "verdict": "keep", "covered_by": null,
   "reason": "Sole check that Say range, Yell instance scope and other-zone Yell are derived from the live world registry after real realm goto moves. No similar file asserts chat scope. Not a duplicate, so keep."},
  {"name": "conversions_cap_and_ready_mismatch", "verdict": "keep", "covered_by": null,
   "reason": "Refusal and cap checks: negative and overflowing instance ids are rejected, a ready mismatch is refused, NaN pose is refused with state unchanged, the 16-child encounter cap and InstanceIdsExhausted are enforced. Only tests/world.rs covers mark_zone_ready, and it does not cover the cap or NaN refusal. Unverified whether src/world.rs unit tests (around line 1614) cover the exhaustion case; if they do, only that sub-assertion would be redundant. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Pack excerpt was truncated, so I read the three test bodies directly (lines 250-760) and did not read the rest of the file or the other similar files' assertion bodies. Only the names of the similar files were compared, so the 'not covered elsewhere' calls are based on names and grep hits, not a full assertion comparison. Every test here is a membership, scope or refusal check, so none qualifies for removal under the conservative rule. The fixture's per-test wait and content loading are a runtime cost, not a redundancy, and are out of scope for this audit."}
