<!-- fleet job=testaudit-infer id=style_card_preview-v1 status=done turns=5 usd=0.0045 tokens(read,write,in,out)=[50061, 21616, 12, 2661] model=claude-haiku-5-5 -->
# tests/style_card_preview.rs

{"file": "tests/style_card_preview.rs",
 "tests": [
  {"name": "customization_data_at_world_entry", "verdict": "keep", "covered_by": null, "reason": "Pins the 35/65 world-entry byte layout through the real Gateway and checks it is not re-sent on replayed loads, ticks or location reports. The only check of that gateway path found; tests/style_cards.rs::customization_data_round_trips is a codec round trip, not the gateway entry path."},
  {"name": "preview_reaches_self_only_and_saves_nothing", "verdict": "keep", "covered_by": null, "reason": "Preview is a persistence/security-style check (self-only delivery, nothing saved). No equivalent 42/11 gateway test found in the repo; the 42/11 preview is not exercised elsewhere in tests/ (only station_cash, lot_deeds and housing previews, which are different request types)."},
  {"name": "refused_previews_send_nothing_and_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check, which must be kept. Decoder-level refusals exist in tests/style_cards.rs::request_decoders_take_exact_lengths, but that does not test the gateway's send-nothing/change-nothing behaviour, so it is not an equivalent test."},
  {"name": "customization_data_after_relog_has_the_new_look", "verdict": "keep", "covered_by": null, "reason": "Persistence check that the 35/65 data after a relog reflects the saved look. Not clearly covered elsewhere; kept conservatively."}
 ],
 "whole_file_removable": false,
 "confidence": 0.3,
 "notes": "Low confidence. The pack's file path could not be read at the repo tip: read returned 'not a file' for prototype/osfr-tools/tests/style_card_preview.rs, and searches for its test names only matched the excerpt's own text in notes. I could only check the excerpt and the first 250 lines of tests/style_cards.rs (its helpers and decoder tests). I found no 42/11 gateway preview test in tests/ beyond station_cash/lot_deeds/housing previews, which are different request types. The possible overlap with tests/style_cards.rs gateway 35/65 tests (style_cards.rs line 212 reads 35/65 too) was not verified, so a duplicate verdict may exist there. Defaulted to keep per the conservative rule; re-audit with the file present before removing anything."}
