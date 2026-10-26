<!-- fleet job=testaudit-infer id=roles-v1 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[24311, 15466, 8, 2166] model=claude-haiku-5-5 -->
# tests/roles.rs

{"file": "tests/roles.rs",
 "tests": [
  {"name": "roles_allow_only_the_documented_commands", "verdict": "keep", "covered_by": null, "reason": "Pins the full builder/admin command matrix, including the refusal of non-admin use of admin commands. No other test in the similar files checks this matrix; it is the authoritative permission check."},
  {"name": "schema_one_accounts_load_as_players_and_save_as_schema_three", "verdict": "keep", "covered_by": null, "reason": "Persistence and migration canary for the legacy v1 fixture; no similar file asserts the v1 to v3 role migration."},
  {"name": "first_new_account_starts_as_player", "verdict": "keep", "covered_by": null, "reason": "Default-role security check (new accounts must not be elevated). Small, but not clearly covered elsewhere; kept conservatively."},
  {"name": "schema_two_rejects_missing_role_records", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a schema-2 document without role records must be rejected as InvalidData."},
  {"name": "only_admins_can_change_roles_and_changes_persist", "verdict": "keep", "covered_by": null, "reason": "Security check (non-admin role change denied with no state change) plus persistence round trip and NotFound refusal for unknown target. Not duplicated elsewhere by an equivalent assertion set."},
  {"name": "role_names_are_exact_and_closed", "verdict": "keep", "covered_by": null, "reason": "Hostile-input check: case-sensitive and unknown role names are refused by parse."},
  {"name": "moderators_run_only_the_moderation_commands", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the Moderator command set (mute/unmute/kick/ban/unban) and refusals of builder/admin commands for moderators. roles_allow_only_the_documented_commands does not cover the Moderator role at all."},
  {"name": "moderation_hierarchy_is_strict", "verdict": "keep", "covered_by": null, "reason": "Exhaustive 4x4 outranks matrix, including equal-rank refusals. The moderation tests in the gateway (l042_moderation) only exercise one admin-over-moderator case, so this is not superseded."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "All eight tests guard permissions, migration, or refusal behaviour, and I found no equal-strength test elsewhere that covers them. The most overlapping neighbour is tests/account.rs::moderation_and_uniqueness_share_the_folded_words, which uses a moderator role but tests name folding, not the command matrix. The gateway's l042_moderation.rs has one outranks case, which is weaker than moderation_hierarchy_is_strict. I did not read the full bodies of the gateway moderation or world-event tests, so a fuller comparison could change a verdict, but there was no evidence of a duplicate."}
