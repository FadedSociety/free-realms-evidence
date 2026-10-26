<!-- fleet job=testaudit-infer id=piece_034-v1 status=done turns=3 usd=0.0046 tokens(read,write,in,out)=[32580, 24712, 8, 2357] model=claude-haiku-5-5 -->
# tests/piece_034.rs

{"file": "tests/piece_034.rs",
 "tests": [
  {"name": "recovered_ability_packet_ids_are_the_original_values", "verdict": "keep", "covered_by": null, "reason": "Pins the recovered opcode/denial constants for the Ninja path. Wizard file tests/piece_036.rs pins similar opcodes but for its own constants and no other file exercises NinjaProgression, so not a duplicate."},
  {"name": "a_corrupt_or_incomplete_catalogue_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check on hostile/corrupt input (bad JSON, wrong schema_version, zero damage, empty cooldown_source). No equivalent test elsewhere."},
  {"name": "a_foreign_weapon_cannot_be_equipped", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a Wizard wand must not equip on the Ninja. Only Ninja-module test of UnknownWeapon."},
  {"name": "a_weapon_tier_needs_its_recovered_rank", "verdict": "keep", "covered_by": null, "reason": "Refusal check on the rank gate (RankTooLow) plus positive unlock at rank 5. No other file covers Ninja equip rank."},
  {"name": "the_training_sword_resolves_the_recovered_ability_pair", "verdict": "keep", "covered_by": null, "reason": "Only check that the 75091 weapon maps to basic 2154 / special 2050 in the Ninja toolbar."},
  {"name": "an_unmapped_weapon_falls_back_to_the_basic_only", "verdict": "keep", "covered_by": null, "reason": "Fallback behaviour for Ninja. tests/piece_036.rs::an_unmapped_weapon_falls_back_to_the_bare_hand_basic_only is the same shape but for the Wizard toolbar and a different module, so it does not drive the same path."},
  {"name": "a_non_ninja_profile_cannot_cast", "verdict": "keep", "covered_by": null, "reason": "Refusal check on profile gating; no equivalent Ninja test elsewhere."},
  {"name": "the_basic_recast_window_refuses_a_second_cast", "verdict": "keep", "covered_by": null, "reason": "Canary for the 600 ms recast window (the RED/GREEN recast fix recorded in notes). Refusal of stale timestamp. Wizard recast test covers a different module."},
  {"name": "the_special_has_no_invented_recast", "verdict": "keep", "covered_by": null, "reason": "Guards against fabricating an unrecovered cooldown; a security-style negative check."},
  {"name": "energy_is_spent_once_and_regenerates", "verdict": "keep", "covered_by": null, "reason": "Energy spend, refusal at zero energy and regeneration for the Ninja pool; no other Ninja coverage."},
  {"name": "a_refused_cast_does_not_change_the_state", "verdict": "keep", "covered_by": null, "reason": "Explicit 'changes nothing on refusal' invariant; refusal check, keep."},
  {"name": "denial_packets_use_the_recovered_string_ids", "verdict": "keep", "covered_by": null, "reason": "Pins the exact wire bytes for denial payloads and the no-fabricated-payload refusal for RankTooLow."},
  {"name": "start_casting_packet_matches_the_recovered_wire", "verdict": "keep", "covered_by": null, "reason": "Byte-exact wire check for the Ninja start-casting packet; unique to this module."},
  {"name": "the_cast_state_survives_a_restart", "verdict": "keep", "covered_by": null, "reason": "Persistence check: cooldown survives a restart. Persistence tests are not removable without an equal equivalent; none named."},
  {"name": "the_emitted_ninja_catalogue_validates", "verdict": "keep", "covered_by": null, "reason": "End-to-end validation of the emitted catalogue. It is env-gated and returns early when OSFR_PIECE_034_CATALOGUE is unset, so by default it asserts nothing; the research notes record it was run with the variable set (green-final.log). Keep, but it is the weakest test in the file when the env var is absent."}
 ],
 "whole_file_removable": false,
 "confidence": 0.85,
 "notes": "No other test file in the repo references NinjaProgression or the piece_034 module, so no test here is superseded or duplicated. The most similar file, tests/piece_036.rs, covers the Wizard module with the same structure (packet ids, toolbar fallback, recast window, energy, denials, restart), but drives different code, so it is not a covering test. Nothing is obsolete: the work-item notes show the recast enforcement was added in this same item (RED then GREEN), not replaced by a later task. Minor caveat: the last test silently passes without the environment variable."}
