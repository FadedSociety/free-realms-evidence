<!-- fleet job=test-audit id=tests-s6-characterization-rs-L1 status=done turns=7 usd=0.0073 tokens(read,write,in,out)=[97079, 27574, 16, 5825] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/s6_characterization.rs lines 1-688 of 688

Window: `prototype/osfr-tools/tests/s6_characterization.rs` lines 1-688. Four findings, ordered by severity.

- **[high] prototype/osfr-tools/tests/s6_characterization.rs:635 `reward_count_excludes_rented_items` - the test only exercises `count_definition_owned`, a helper defined in this same file (line 40), and never touches production reward code.**
  - Why it cannot catch a regression: production's reward and rental filters (e.g. `src/gameplay/crafting.rs:329`, `:500`, `src/inventory.rs:1000`) are never called. Those could start counting rented stacks and this test would still pass. It is also the only test in the file that is not `#[ignore]`d, so it is the only one that runs on the integrator, and it verifies a copy of the logic instead of the code.
  - Fix: drive the production path that grants or counts rewards (for example the crafting/gathering reward count function used by `gathering_payout.rs` or `crafting.rs`) with a rented and an owned stack of definition 21785, and assert the owned-only total. Alternatively, delete the test and rely on the ignored packet-path tests.

- **[medium] prototype/osfr-tools/tests/s6_characterization.rs:413 `ability_request_is_the_clients_24_byte_mode_zero_form` - the name says the request "must parse", but the only assertion is that `handle_at` returns `Ok`.**
  - Why it cannot catch a regression: `src/abilities.rs:821-835` (`unsupported_cast`) answers a well-formed mode-0 cast on an unserved bar or slot with a failure packet, not an error. If a change routed every valid mode-0 cast to that refusal, `handle_at` would still return `Ok` and the test would pass. Nothing checks that the cast was served.
  - Fix: assert on the outcome, for example that `out.replies` contains no 36/10 failure packet, or that the ability's energy, cooldown or target-damage state changed, in addition to the `Ok`.

- **[low] prototype/osfr-tools/tests/s6_characterization.rs:426 `ability_request_is_the_clients_24_byte_mode_zero_form` - `assert_eq!(attack.len(), 24)` checks the length of a vector the test has just built from literals.**
  - Why it cannot catch a regression: the assertion is true by construction and does not depend on any production code. It only documents the size.
  - Fix: remove it, or replace it with a check against the encoder in `src/restoration/piece_046.rs:292`, which is the production 24-byte form.

- **[low] prototype/osfr-tools/tests/s6_characterization.rs:337 `smelting` arm of `prepare_terminal` - `assert_eq!(ready.replies.len(), 6)` pins a reply count that depends on the content's phase count.**
  - Why it cannot catch a regression: a change that adds or removes an unrelated reply (for example an extra notice) breaks this test even when the terminal behaviour under test is unaffected. This is churn rather than a missed bug.
  - Fix: assert that the `OnDataComplete` reply is present, or derive the expected count from the loaded `smelting.json` phases, rather than hard-coding 6.
