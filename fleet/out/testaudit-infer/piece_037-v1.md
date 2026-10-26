<!-- fleet job=testaudit-infer id=piece_037-v1 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[24065, 14373, 8, 2349] model=claude-haiku-5-5 -->
# tests/piece_037.rs

{"file": "tests/piece_037.rs", "tests": [
{"name": "medic_identity_is_the_recovered_client_wield_type", "verdict": "keep", "covered_by": null, "reason": "Pins recovered identity constants (wield 14, stat ids, ability and effect ids). Only test of these constants; no other file includes src/restoration/piece_037.rs."},
{"name": "first_aid_ladder_is_the_recovered_five_rank_text", "verdict": "keep", "covered_by": null, "reason": "Unique check of the five-rank heal ladder and its out-of-range None cases; no other file exercises first_aid_heal."},
{"name": "heal_accepts_self_group_member_and_ally_targets", "verdict": "keep", "covered_by": null, "reason": "Positive target rule for heal; only test of target_allowed for Heal in the repo."},
{"name": "heal_rejects_opponents_and_knocked_out_targets", "verdict": "keep", "covered_by": null, "reason": "Refusal check (hostile target, knocked-out target); must be kept."},
{"name": "damage_accepts_only_opponents", "verdict": "keep", "covered_by": null, "reason": "Refusal check for damage against friendlies; unique in repo."},
{"name": "revive_accepts_only_knocked_out_friendlies", "verdict": "keep", "covered_by": null, "reason": "Refusal and acceptance matrix for revive including self-revive refusal; unique in repo."},
{"name": "damage_on_a_knocked_out_opponent_keeps_no_recovered_restriction", "verdict": "keep", "covered_by": null, "reason": "Records an explicit open point (canary against inventing a restriction); keep."},
{"name": "knocked_out_actors_cannot_use_abilities", "verdict": "keep", "covered_by": null, "reason": "Refusal check for knocked-out actors plus recovered denial string; unique in repo."},
{"name": "energy_cost_is_reported_with_the_recovered_denial_string", "verdict": "keep", "covered_by": null, "reason": "Energy refusal check and denial string; unique in repo."},
{"name": "paid_revive_is_disabled_below_the_server_supplied_cost", "verdict": "keep", "covered_by": null, "reason": "Boundary check on paid revive cost; unique (the piece_058 paid-revive tests cover a different module's ledger, not this offer predicate)."},
{"name": "overworld_offer_matches_the_two_button_dialog", "verdict": "keep", "covered_by": null, "reason": "Pins the two-button offer and label strings; unique in repo."},
{"name": "encounter_offer_counts_down_without_a_coin_option", "verdict": "keep", "covered_by": null, "reason": "Pins the encounter countdown offer with no coin option; unique in repo."},
{"name": "revive_events_match_the_recovered_client_commands", "verdict": "keep", "covered_by": null, "reason": "Maps choices to the recovered FR_event commands; unique. piece_058 tests a separate respawn packet, not this mapping."},
{"name": "post_revival_invulnerability_declares_two_effects", "verdict": "keep", "covered_by": null, "reason": "Single constant pin of the recovered effect count (22111/22112); only check, keep."},
{"name": "ability_denials_carry_no_client_text_when_none_was_recovered", "verdict": "keep", "covered_by": null, "reason": "Asserts absence of client text for denials without recovered strings; a distinct negative check, keep."}
],
"whole_file_removable": false, "confidence": 0.8, "notes": "All 15 tests exercise the pure rules in src/restoration/piece_037.rs, which no other test file in the repo includes or drives (the only other hits are the same file). The similar files (piece_058 respawn/revive ledger, piece_036 wizard casting, kart/power-up/piece_046) test different modules, so no superseded or duplicate verdicts are supported by the pack. Nothing is obsolete: the file pins recovered original values and is itself a #[path] include awaiting registration. Similar-file names were judged by name only; I did not open their bodies, so overlap with piece_058 (revive semantics) is plausible in intent but not proven at assertion level. Recommend no removal."}
