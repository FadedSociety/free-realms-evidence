<!-- fleet job=pin-audit id=tests-fishing-review-rs status=nothing_found turns=3 usd=0.0012 tokens(read,write,in,out)=[4945, 6296, 8, 681] model=claude-haiku-5-5 -->
# tests/fishing_review.rs

No findings in `prototype/osfr-tools/tests/fishing_review.rs` for the screened lines 289, 291 and 299.

The expected values are not read from any data file. They are the test's own fixture. `distinctive_result_body()` (fishing_review.rs:98) writes the floats literally into the byte buffer: `1.25f32` at line 107 (`at_38`), `2.5f32` at line 109 (`at_40`) and `3.75f32` at line 119 (`at_7c`). The asserts check that the decoder reads those same fixture bytes back in order. Retuning any fishing data file cannot change them, so they are not tunable-number pins. No change is needed.
