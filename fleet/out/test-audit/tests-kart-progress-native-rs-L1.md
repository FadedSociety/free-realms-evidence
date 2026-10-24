<!-- fleet job=test-audit id=tests-kart-progress-native-rs-L1 status=done turns=5 usd=0.0057 tokens(read,write,in,out)=[34819, 18300, 12, 6074] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_progress_native.rs lines 1-404 of 404

Window `prototype/osfr-tools/tests/kart_progress_native.rs` lines 1-404, checked against `prototype/osfr-tools/src/kart_progress_native.rs` (decode/encode at 202-257, `results_row_finished` at 287, `results_screen_trigger` at 296). Most of the window holds up. I hand-checked the `FINISH_HEX` bytes for 61.5, 58.25 and 179.75 and they match. The signed-boundary predicate cases (lines 259-264) and the agreement loop (266-274) are correct for the implemented wrapping semantics. The ignored capture test has a reason string and no silent early return.

- **[low] tests/kart_progress_native.rs:187-189 refuse_nan_flags_only_the_two_natively_checked_fields - the "other three floats are kept verbatim" claim is checked only with `is_nan()` on two of the three fields, and the third (total time at 0x25) is never inspected.**
  - Why it cannot catch a regression: `decode_progress` could start rewriting the NaN payload bits of 0x1d, 0x21 or 0x25 (for example canonicalising to `f32::NAN`) and this test would still pass, because `is_nan()` stays true. The `total_time_bits` field is not touched at all, so a change that altered only that field would also pass.
  - Fix: assert `decoded.unknown_1d_bits == 0x7fc0_0001`, `decoded.best_lap_bits == ...` and `decoded.total_time_bits == ...` with non-canonical NaN payloads, using `assert_eq!` on the bits rather than `is_nan()`.

- **[low] tests/kart_progress_native.rs:311-317 private_capture_roundtrips_all_progress_frames - exact file counts (9358 / 7 / 0) are pinned to one private, unversioned lab directory.**
  - Why it is churn: the test is about byte-exact codec round-tripping and the frame-level distribution checks. Any change to the lab archive (adding or pruning captures) fails it even when the codec is correct. The count is incidental to what the test claims to prove. This is only relevant when the test is run manually with `--ignored`.
  - Fix: keep the lower bounds (`>= 9358`) or move the counts into the lab report that describes the capture, and keep the distribution assertions at 379-386 as the substantive checks.
