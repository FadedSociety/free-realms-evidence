<!-- fleet job=testaudit-infer id=style_cards-v1 status=done turns=4 usd=0.0041 tokens(read,write,in,out)=[47078, 20400, 10, 2131] model=claude-haiku-5-5 -->
# tests/style_cards.rs

{"file": "tests/style_cards.rs",
 "tests": [
  {"name": "request_decoders_take_exact_lengths", "verdict": "keep", "covered_by": null, "reason": "Only test of decode_request in the suite; it checks exact-length refusals (short, long, wrong opcode, wrong family), which are hostile-input refusal checks."},
  {"name": "skin_tone_card_is_record_1", "verdict": "keep", "covered_by": null, "reason": "Only check that the skin-tone card maps to record 1 and applies to the look; no other test file uses StyleCard."},
  {"name": "hair_card_is_record_2", "verdict": "keep", "covered_by": null, "reason": "Only check of the hair card rule (record 2) and its apply path."},
  {"name": "hair_colour_card_is_record_3_with_its_tint", "verdict": "keep", "covered_by": null, "reason": "Only check of record 3 and the tint being applied."},
  {"name": "eye_colour_card_is_record_4_with_its_tint", "verdict": "keep", "covered_by": null, "reason": "Only check of record 4 and eye tint."},
  {"name": "model_customization_card_is_record_5", "verdict": "keep", "covered_by": null, "reason": "Only check of record 5 for beard and pixie wings, including the apply path."},
  {"name": "face_paint_card_is_record_6", "verdict": "keep", "covered_by": null, "reason": "Only check of record 6 and face paint apply."},
  {"name": "wings_card_is_record_7", "verdict": "keep", "covered_by": null, "reason": "Only check of record 7 (wings) rule."},
  {"name": "face_type_card_is_record_0", "verdict": "keep", "covered_by": null, "reason": "Only check of record 0 (face type) rule."},
  {"name": "clean_shaven_is_empty_string_without_lookup", "verdict": "keep", "covered_by": null, "reason": "Pins the empty-string special case with no mapping lookup; unique behaviour."},
  {"name": "ineligible_cards_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check: wrong gender, wrong model, unsupported slot, unknown mapping, and the 'refusal changes nothing' invariant. Must keep."},
  {"name": "customization_data_round_trips", "verdict": "keep", "covered_by": null, "reason": "Round-trip of the 35/65 encoder against the identity path; no other file exercises customization_data."},
  {"name": "portrait_ids_are_the_first_four_self_data_ids", "verdict": "keep", "covered_by": null, "reason": "Listed in the pack (doc describes a canary for portrait id order), but it is NOT present in the file on disk (472 lines, last test is customization_data_round_trips). Cannot judge its body; kept by default. Pack and file disagree."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "No other test file in tests/ references StyleCard, customization_change, customization_data or style_cards::decode_request, so nothing is superseded or duplicated. The five similar files were chosen by generic shared-score (housing, earnings, NPC, kart, housing session) and share no style-card path. The pack reports 504 lines and a portrait test, but the repository file is 472 lines and has no portrait test; the pack may be stale relative to the tip. Recheck before any removal."}
