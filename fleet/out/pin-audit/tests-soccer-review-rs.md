<!-- fleet job=pin-audit id=tests-soccer-review-rs status=nothing_found turns=2 usd=0.0013 tokens(read,write,in,out)=[1806, 7681, 6, 607] model=claude-haiku-5-5 -->
# tests/soccer_review.rs

No findings for `prototype/osfr-tools/tests/soccer_review.rs` line 179 (`clock_rejects_non_finite_and_out_of_order_samples`).

The expected value 151.412 is not read from a data file. It is the fixture input the test itself sends on line 177: `game_time(151.412, 60.622)`. Line 179 only checks that the clock stored the sample the test just fed in. Retuning any file under `data/content` cannot change it. The `151.412` in the code comments and in `search` results comes from captured fixtures, not from the gameplay data. The arguments in lines 166–173 are also test-local inputs.

No edit is needed.
