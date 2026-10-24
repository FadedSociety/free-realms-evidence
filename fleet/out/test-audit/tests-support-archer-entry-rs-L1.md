<!-- fleet job=test-audit id=tests-support-archer-entry-rs-L1 status=done turns=5 usd=0.0061 tokens(read,write,in,out)=[39689, 20814, 12, 6177] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/support/archer_entry.rs lines 1-407 of 407

Window reviewed: `prototype/osfr-tools/tests/support/archer_entry.rs` lines 1-407 (full file). No `#[ignore]`, no early-return fixture skips, and no assertion that restates its own computation. Most assertions compare content JSON against literal ids and locale constants, and the helpers they call (`release_end_screen`, `finish_quest`, `counts`, `pending_turnin`) assert against game state. The findings below are the weaker spots.

- **[medium] prototype/osfr-tools/tests/support/archer_entry.rs:226-239 assert_enabled_archer_chapter_records - "every objective needs provenance" / "every reward needs provenance" only checks that each `source` array is non-empty.**
  - Why it cannot catch a regression: a `source` of `["placeholder"]`, or a source that points at a file or line that does not exist, still passes. Removing a real citation and replacing it with a dummy string keeps the check green.
  - Fix: resolve each source entry against its target (for example, require the locale or legacy id it cites to exist in the content tables, or require a known source-kind enum value) and assert on that, not just on non-emptiness.

- **[low] prototype/osfr-tools/tests/support/archer_entry.rs:85-91 learn_archer - the message says the Archer starter outfit "must be complete", but the only check is `switched.changed`.**
  - Why it cannot catch a regression: if select_job starts returning `changed == true` while the starter outfit is incomplete or missing, nothing here inspects the outfit, so the assertion and its message both still pass. The message claims a check that is not made.
  - Fix: after `select_job(ARCHER)`, assert the starter outfit items for profile 35 are present in inventory (or equipped), or reword the message to match what is actually asserted.

- **[low] prototype/osfr-tools/tests/support/archer_entry.rs:402-406 - the final `runtime_guids.len() == 3` check repeats the duplicate test already done by `insert` at lines 377-380.**
  - Why it cannot catch a regression: it is redundant rather than wrong. It adds no coverage, and it fails only in cases the per-recruit assertion already catches. The redundancy does not hide a gap, but it suggests the loop's intent (one distinct actor per recruit) is stated twice without a stronger check.
  - Fix: keep one check. Either drop the final count, or assert that the set equals the expected three runtime GUIDs derived from the bindings.

Not reported: the 49/13 byte offsets and the locale ids (22083, 22075, 9701, 77038, 77036) are in comments and constants, and the test checks the end text against `PATH_END_TEXT`/`OATH_END_TEXT`. The locale lookup did not confirm 22083 and 22075, so their accuracy as text ids is unverified. The step-4 comment at lines 128-129 is not checked by any assertion.
