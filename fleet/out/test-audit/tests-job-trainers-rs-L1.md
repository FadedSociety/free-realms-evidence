<!-- fleet job=test-audit id=tests-job-trainers-rs-L1 status=done turns=6 usd=0.0103 tokens(read,write,in,out)=[101700, 36821, 14, 9418] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/job_trainers.rs lines 1-1200 of 1696

Window: `prototype/osfr-tools/tests/job_trainers.rs` lines 1-1200. Read against `src/profiles.rs` (`load_trainers` 242-279, `learn` 283-300).

- **[medium] prototype/osfr-tools/tests/job_trainers.rs:383 malformed_trainer_files_are_refused_at_load - the "oversize" case writes 65,537 spaces, which fail JSON parsing, so the error does not come from the size bound.**
  - Why it cannot catch a regression: `load_trainers` (profiles.rs:249) checks `bytes.len() > 65_536` before parsing, but `serde_json::from_slice` on whitespace-only input also returns Err (EOF). Deleting or loosening the size check at profiles.rs:249 still leaves this assertion green, because the file still fails to parse.
  - Fix: write a valid `job_trainers.json` (`{"schema_version":1,"trainers":[...]}`) padded past 65,536 bytes, for example with a long `source` string or trailing whitespace after a valid document, and assert `is_err()`. Also add the boundary case: a valid document of exactly 65,536 bytes must load. Then removing the size check fails the test.

- **[low] prototype/osfr-tools/tests/job_trainers.rs:502-506 service_refusals_change_nothing - the comment says the forged row is "refused without a panic or a change", but nothing compares state after `learn`.**
  - Why it cannot catch a regression: the body only asserts `Err(LearnDenied::Unavailable)`. If `learn` mutated `unlocked` or `experience` before returning that error, the test would still pass. The same test does compare state in the other refusal cases (lines 488 and 494), so this one is inconsistent with its own comment.
  - Fix: take `let before = profiles.state().clone();` before the call and add `assert_eq!(profiles.state(), &before);` after it.

- **[low] prototype/osfr-tools/tests/job_trainers.rs:1068 without_the_content_file_nobody_offers_a_job - the `fs::remove_file(content.0.join(...)).ok()` line is a no-op and does not do what its comment implies.**
  - Why it cannot catch a regression: `content` already had its trainer file removed at line 1058, so this call does nothing. The `with` gateway at 1066-1071 is not affected by it either. The absent-file behaviour is actually covered at 1073-1076, which is valid. The stray line misleads a reader into thinking the file is removed after the gateway is built, which the test never exercises.
  - Fix: delete line 1068 and its comment. If the intent was "removed after load still yields no offers", remove the file from `with.0` after `gateway_at` and assert that the existing gateway still offers, since trainers are read at load time (confirm in gateway load code before relying on this).

No other defects found in the window. The content-row, malformed-row, service-level, and gateway-level assertions I checked compare against independently loaded state or explicit expected values, and the refusal tests compare full `gameplay_json` snapshots.
