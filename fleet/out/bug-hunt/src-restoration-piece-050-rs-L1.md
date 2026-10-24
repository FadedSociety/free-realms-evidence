<!-- fleet job=bug-hunt id=src-restoration-piece-050-rs-L1 status=done turns=6 usd=0.0088 tokens(read,write,in,out)=[71190, 28086, 14, 9125] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_050.rs lines 1-636 of 636

Reviewed `prototype/osfr-tools/src/restoration/piece_050.rs` lines 1-636 in full. Only one defect survived verification. Everything else I checked is either safe or not reachable.

**Finding**

- **[low] `prototype/osfr-tools/src/restoration/piece_050.rs:308` (and the same pattern at :369 in `classify_custom_name`) - the duplicate check claims case-insensitive comparison, but `eq_ignore_ascii_case` folds only ASCII, while the name window (`name_characters_valid`, line 329-334, via `char::is_alphabetic`) admits non-ASCII letters.**
  - **Failure scenario:** an existing character is "Éva Vale". A new request for "éva Vale" (or "ÉVA VALE" vs "Éva Vale") passes `name_shape_valid`, because `é` is alphabetic. `eq_ignore_ascii_case` treats `É` (U+00C9) and `é` (U+00E9) as different bytes, so no duplicate is found and the function returns `NameResultCode::Available`. The result is two live characters whose names differ only by the case of a non-ASCII letter.
  - **Reach:** the doc comment at line 294 ("Compared case-insensitively") and the test table at `tests/piece_050.rs:161` (`"Éva"` is accepted) show non-ASCII names are intended to be valid. The duplicate check is therefore the only place this case folding happens. The module is not yet registered in the live server: `notes/Reviews/*.json` says the lead still has to register `pub mod piece_050;`. The impact is latent until it is wired in. The live account store folds with `to_lowercase()` (`account_store.rs:594`), so this is also inconsistent with the production path.
  - **Fix:** compare with Unicode folding, for example `name.to_lowercase() == display.to_lowercase()` (and the same in `classify_custom_name`), or `to_lowercase` both sides before the `any` check.

**Checked and dropped**

- `Slice::take`, `string`, `u8`–`u64`: bounds are checked with `checked_add` and `filter` before slicing. The length prefix is checked against `max` before `take`, so there is no panic and no oversized allocation.
- `NameCheckRequest::decode`, `NameCheckReply::decode`, `CharacterDeleteReply::decode`: the payload length is bounded by the buffer through `take`, and trailing bytes are rejected.
- `NameCatalogue::parse`: `fields[0..2]` are guarded by the `len() < 3` check. The `parse` on `fields[2]` maps errors. Only resource files reach this, not client input.
- `NameCatalogue::resolve`/`definition`: the client-supplied definition id is looked up in a BTreeMap and returns an error on a miss. Nothing panics. Typed names pass through on the custom path (`(false, None)`), but that is by design, and no production caller exists yet to rely on it. The reliance is a wiring concern, not a defect in this window.
- `classify_custom_name` length and combined rules: the order of the checks is consistent with the doc comment. Blank parts map to the short codes (blank whitespace-only parts map to `Invalid`, a cosmetic doc gap I did not report).
- `delete_decision`: the doc mentions a "coordinated" gameplay save, but the function takes only a bool. This is a doc/caller issue and is not a behavioural defect in this window.
- `put_string` `as u32` truncation: encode-side only, with server-generated strings.

No `high` or `medium` defect is supported by the code in this window.
