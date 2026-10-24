<!-- fleet job=pin-audit id=tests-l052-staff-jobs-rs status=nothing_found turns=6 usd=0.0017 tokens(read,write,in,out)=[19857, 5713, 14, 1488] model=claude-haiku-5-5 -->
# tests/l052_staff_jobs.rs

No finding for `prototype/osfr-tools/tests/l052_staff_jobs.rs:364` (test `experience_paid_while_a_staff_job_is_worn_goes_to_the_real_job`).

The expected `200` is not read from a data file. The test sends `realm level 3`, and the handler in `prototype/osfr-tools/src/gameplay.rs:2756-2771` stores `(level - 1) * 100` experience for the active job. So 200 is the code formula applied to the test's own input (level 3). The `100` per level is a literal in code, not a field in `prototype/osfr-tools/data/content/*.json`. Retuning any data value would not change this assertion, so it is not a live-tuning violation under the stated rule.

Optional hardening, not required: if the 100-per-level step ever moves into data, the test should read it from that row rather than pin 200.
