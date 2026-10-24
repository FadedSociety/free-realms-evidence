<!-- fleet job=test-audit id=tests-spine-rules-rs-L1 status=done turns=4 usd=0.0037 tokens(read,write,in,out)=[18324, 11826, 10, 4056] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/spine_rules.rs lines 1-177 of 177

Window: `prototype/osfr-tools/tests/spine_rules.rs` 1-177. Two real gaps in the ratchet, plus one low-severity note.

- **[high] prototype/osfr-tools/tests/spine_rules.rs:130 spine_rules_only_ratchet_down - the test trusts whatever numbers are in `spine_rules.ceilings` and never checks that the file was not edited upward.**
  - Why it cannot catch a regression: a builder raises `hub:src/gameplay.rs 5515` to `5700` (or any `busy_outside_occupation`/`hex_outside_trace`/`plain_fs_write` value) in `spine_rules.ceilings`, then adds the growth. `values` is still `<= ceilings`, the keys match, and the test passes. The only "only down" enforcement is the `SPINE_RATCHET_LOWER` path at 159-176, which runs after integration, not as a gate.
  - Fix: compare the ceilings file to the committed baseline, for example `git show HEAD:prototype/osfr-tools/tests/spine_rules.ceilings` (or a checked-in copy), and fail if any ceiling exceeds its baseline value (999999 "not measured yet" excepted). Alternatively, assert the file's bytes match a hash pinned in the test, so an edit forces an explicit review. Also rename the test if this is left out, since "only ratchet down" is not what it proves today.

- **[medium] prototype/osfr-tools/tests/spine_rules.rs:92 measure (busy_outside_occupation, line 117; hex_outside_trace, line 112) - the exemption uses `Path::ends_with(filename)`, so every file named `occupation.rs` or `trace.rs` anywhere under `src` is exempt, not just the designated module.**
  - Why it cannot catch a regression: a builder adds `src/forging/occupation.rs` (or `src/bin/x/trace.rs`) containing `Forging::active` or `:02x}` and the count skips it. Current counts stay at their ceilings and the test stays green while the busy/hex rule is broken.
  - Fix: match the exact relative path (e.g. `path.ends_with("src/gameplay/occupation.rs")` and `path.ends_with("src/trace.rs")`, or compare against `root.join(...)` canonicalized), and add a canary that the exempt file exists so a rename cannot silently zero the rule. Grep `src/gameplay.rs:1030` and `src/recipe_book.rs:364` show busy terms outside occupation.rs and are counted, so the rule is live; only the suffix exemption is the hole.

- **[low] prototype/osfr-tools/tests/spine_rules.rs:126-129 spine_rules_only_ratchet_down - the `panic = "abort"` guard is an exact substring match on the manifest.**
  - Why it cannot catch a regression: `panic="abort"` (no spaces), `panic = 'abort'`, or a `[profile.release]` override written in a different form passes the check, so the isolation boundary in `contain` can be silently disabled.
  - Fix: parse the manifest as TOML (or normalise whitespace and quotes) and assert that no `panic` key under any `[profile.*]` equals `"abort"`.

No findings for is_ok-only assertions or ignored/early-return tests in this window: there is no `#[ignore]`, and missing hub files or the ceilings file panic via `unwrap`. The counts at 104, 108 and 112 are not over-pinned, since they are ceilings compared with `>`, not exact values.
