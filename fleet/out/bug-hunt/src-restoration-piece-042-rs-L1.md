<!-- fleet job=bug-hunt id=src-restoration-piece-042-rs-L1 status=done turns=6 usd=0.0068 tokens(read,write,in,out)=[82439, 27954, 14, 4895] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_042.rs lines 1-751 of 751

Reviewed `prototype/osfr-tools/src/restoration/piece_042.rs` lines 1-751 in full. The window is recovered metadata tables plus pure helpers. I found one defect, and it is low severity. I found no panic, unbounded growth, or client-trust issue reachable from a packet or save.

- **[low] prototype/osfr-tools/src/restoration/piece_042.rs:729-750 - `validate_locale` says it checks that "every referenced id must resolve", but it only loops over `TEXT_CLAIMS` and never looks at `REFERENCE_IDS`.**
  - **Failure scenario:** The locale export drops a referenced row, for example 387947 "level 5 achievement line" or 19323 "mail sorting tutorial top". `validate_locale` still returns `Ok(())`, so a caller relying on the Rust validator alone would believe the references resolve. The unit test at `tests/piece_042.rs:150-156` only removes a quoted claim (387932), so it does not catch this.
  - **Reach:** No production caller exists. `validate_locale` is called only from `tests/piece_042.rs:133,137,152`. The module is also not registered in `src/restoration/mod.rs`, so no client packet or save can reach it. The Python checker `scripts/pieces/piece_042.py:425-429` does check references (`MissingLocaleEntry`), which limits the practical impact.
  - **Fix:** Add a loop after the `TEXT_CLAIMS` loop: `for row in REFERENCE_IDS { if lookup(row.string_id).map_or(true, |s| s.trim().is_empty()) { return Err(ProgressionError::MissingLocalizedText { profile_id: row.profile_id, string_id: row.string_id }); } }`. Also add a test that drops one reference id.

Checked and ruled out:
- `SOCCER_TUTORIAL_PICKUP_ICONS` omits `SoccerTutIcon0003`. This is intentional: `ScriptsBase.lua:25829` spawns only 0001, 0002 and 0004.
- `soccer_tutorial_advance`, `level_gate`, `unlocked_level_gates` and `milestone_reached` have no production callers, and all index-free `u8` comparisons cannot panic.
- `validate()` arithmetic (`(index + 1) as u8` over 7 entries) and the ascending checks are sound.
