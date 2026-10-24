<!-- fleet job=bug-hunt id=src-restoration-piece-097-rs-L1 status=nothing_found turns=6 usd=0.0080 tokens(read,write,in,out)=[74267, 27861, 14, 7462] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_097.rs lines 1-593 of 593

No reportable defects in `prototype/osfr-tools/src/restoration/piece_097.rs` lines 1-593.

What I checked:

- **Panics on input.** `delimited_rows` (162-189) guarantees `fields.len() >= expected` before `parse_item_classes`, `parse_item_categories` and `parse_models` index `fields[0..=13]`, so the indexing is safe. `template_tokens` (294-306) slices only at ASCII `<`/`>` boundaries, so the byte slicing cannot split a UTF-8 char. `asset_names` (331) uses `unwrap_or_default` on an empty `&str`, which is fine. The only arithmetic is usize counters and `index + 1`. Nothing is recursive.
- **Column indices.** `Models.txt` index 2 is RACE_ID, index 13 is IS_VALID_FOR_PC, and index 1 is MODEL_FILE_NAME. This matches the header in the FreeRealms-Legacy, Sanctuary and Lxzxrus copies of `Models.txt`. `ItemClasses` index 5 is PROFILE_NAME_ID, which matches the test fixture at `tests/pieces/test_piece_041.py:250`.
- **Classification and expansion.** `classify_model`, `expand_race_gender` and the `analyze` match arms agree with the module docs and with `tests/piece_097.rs` (lines 78-120). `param1 > 0` is applied consistently in the coverage count (489) and the conflict list (540). `conflict_types` (533) requires `resolved > 0 && resolved < present`, which is what the doc describes.
- **Fallbacks.** `asset_names` falls back to column 2 when there is no `name` header, and `locale_ids` returns an empty set on malformed JSON. Both match the Python oracle (`scripts/pieces/piece_097.py:173-194`). The locale fallback is documented as deliberate, and it turns every name into a reported gap rather than a silent pass. Neither is a swallowed error that reports success.
- **Reach.** The inputs are preserved reference files read by an offline analysis tool. No client packet or save reaches this module, so none of the client-input categories apply.

Near-miss, not reported: the doc comment on `Findings::name_id_unset` (line 395) says "a positive or sentinel value that names nothing". The code (587) only puts `id <= 0` there. Positive unresolved ids go to `missing_name_ids` (588-590), and the test at `tests/piece_097.rs:192-193` expects that. The comment is misworded but the behaviour is consistent with the tests and has no downstream effect.
