<!-- fleet job=test-audit id=tests-piece-062-rs-L1 status=done turns=5 usd=0.0059 tokens(read,write,in,out)=[41355, 20414, 12, 5954] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_062.rs lines 1-225 of 225

Reviewed `prototype/osfr-tools/tests/piece_062.rs` lines 1-225 against `prototype/osfr-tools/src/restoration/piece_062.rs` (all 534 lines). Most assertions are real pins against independently written literals, and `advance`, `ability`, `attack_timing` and `validate` behave as the tests expect. The gaps below are where a plausible regression still passes.

- **[medium] tests/piece_062.rs:155 attack_timing_table_matches_the_original_actor_definition - the clip binding of each attack slot is never asserted, although the name says the table matches the actor definition.**
  - Why it cannot catch a regression: the `cases` tuple holds only slot, contact and interrupt. `row.clip` is never read. `validate()` (src/restoration/piece_062.rs:493-497) only checks clip for slots that an `ABILITIES` row names, which is `com_cast_01..03`. So swapping the clip for `com_h2h_attack_01..04` (src lines 165-186, e.g. flick <-> kick) or any other `ATTACK_TIMINGS` clip string would pass every test in this file.
  - Fix: add the expected clip to each case, e.g. `("com_h2h_attack_02", 0.7820, None, "necronomicus_com_h2h_attack_flick.gr2")`, and `assert_eq!(row.clip, clip)`.

- **[medium] tests/piece_062.rs:191 portal_objectives_record_eight_original_targets - only the first and last of the eight objectives are checked.**
  - Why it cannot catch a regression: portals 2-7 (src/restoration/piece_062.rs:344-351, locale ids 5100671/73/75/77/79/81) are never compared. A typo or swap in the middle entries passes, and `validate()` only checks the portal numbering, not the locale ids. The name says "record eight original targets", which the body does not establish.
  - Fix: `assert_eq!(PORTAL_OBJECTIVES, &[(1, 5100669), (2, 5100671), (3, 5100673), (4, 5100675), (5, 5100677), (6, 5100679), (7, 5100681), (8, 5100683)]);`

- **[low] tests/piece_062.rs:198 barks_keep_their_measured_durations_without_inventing_a_cue_pairing - the middle bark and middle dialogue cue are not checked.**
  - Why it cannot catch a regression: `DIALOGUE_CUES[1]` (`DIA_Necronomicus_Not_So_Fast`, 5100652) and `BARK_RECORDINGS[1]` (`DX_NECRONOMICUS_NOT_SO_FAST.mp3`, 2.136 s; src lines 400-403) are never touched. Changing the file name or duration of that bark, or its cue text, passes. The second duration is also unchecked against its 5e-3 tolerance.
  - Fix: assert the cue and text id of `DIALOGUE_CUES[1]`, and the asset and `seconds` (about 2.136 within 5e-3) of `BARK_RECORDINGS[1]`, alongside the existing checks.

- **[low] tests/piece_062.rs:221 unrecovered_server_timing_stays_a_gap - the test checks two of the five "not recovered" flags and nothing else.**
  - Why it cannot catch a regression: the `src` doc (lines 36-38) says `PHASE_HEALTH_THRESHOLDS_RECOVERED`, `PORTAL_ENTITY_IDS_RECOVERED` and `CUE_TO_RECORDING_RECOVERED` must stay false, and that the checker fails if any is flipped. Here only `SERVER_ABILITY_TIMING_RECOVERED` and `GR2_CLIP_DURATION_DECODED` are asserted, and `CUE_TO_RECORDING_RECOVERED` is asserted only in the barks test. Flipping `PHASE_HEALTH_THRESHOLDS_RECOVERED` or `PORTAL_ENTITY_IDS_RECOVERED` passes this test. The assertions are on constants, so this is a canary, not behavioural coverage.
  - Fix: assert all five flags false in this test, or move the check to where the doc says the checker enforces it, and make the doc match.

- **[low] tests/piece_062.rs:108 ability_rows_keep_their_recovered_slots_and_effects - the effect bindings in `SLOT_EFFECT_BINDINGS` are only partly checked.**
  - Why it cannot catch a regression: `SLOT_EFFECT_BINDINGS[0]` (`ground_pound` effect, `com_cast_01`) and the `effect` field of `[2]` (`magic_beam`) are never asserted; only the `instance` of `[2]` and `effect`/`instance` of `[1]` are. Changing `[0].effect` or `[2].effect` passes. The name "slots and effects" covers these bindings.
  - Fix: assert `SLOT_EFFECT_BINDINGS` in full, e.g. `assert_eq!(SLOT_EFFECT_BINDINGS[0].effect, "ground_pound")` and `assert_eq!(SLOT_EFFECT_BINDINGS[2].effect, "magic_beam")`, or compare the whole slice.

No `#[ignore]` or early-return skips in this window. The `boss_identity` literals are external pins rather than values derived from the code under test, so they are not reported.
