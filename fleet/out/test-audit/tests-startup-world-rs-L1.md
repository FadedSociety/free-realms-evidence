<!-- fleet job=test-audit id=tests-startup-world-rs-L1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[9314, 8374, 8, 2299] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/startup_world.rs lines 1-262 of 262

Window: `prototype/osfr-tools/tests/startup_world.rs` lines 1-262. Two findings, both in the synthetic round-trip tests. The ignored capture oracle (line 35) has a reason, has no early return, and does not skip silently. I did not confirm the 2470 count or the other capture-specific pins as problems.

- **[medium] prototype/osfr-tools/tests/startup_world.rs:249 synthetic_motd_strings_change - the name says the strings change, but only `first_string` is mutated and checked, so `second_string` is never verified.**
  - Why it cannot catch a regression: `build_motd` writes `second_string` (src/startup_world.rs:535) and `parse_motd` reads it (src/startup_world.rs:543), but the test never changes or asserts it. A change that drops `second_string` from the output, or swaps the two strings on parse, still leaves `original != changed` (the first string differs) and still passes the `first_string` assertion.
  - Fix: mutate `second_string` in the changed value too (or add a third case), then assert `parsed.second_string == "second-changed"` (or the new value) alongside `parsed.first_string`.

- **[medium] prototype/osfr-tools/tests/startup_world.rs:153 synthetic_npc_actor_transform_flags_and_lists_change - the name says the lists change, but the attachment and effect-tag lists are never mutated, and their contents are never compared, only their lengths.**
  - Why it cannot catch a regression: `attachments` and `effect_tags` are only length-checked (lines 186-187). A parse or build bug that scrambles or zeroes `model_name`, `texture_alias`, `tint_id`, `composite_effect_id`, `slot`, or the effect-tag fields would still pass, because the lengths stay 1 and the changed value still differs in actor_id/position. The `original != changed` check is satisfied by the scalar edits alone.
  - Fix: after parsing, assert `parsed.attachments[0] == row.attachments[0]` (or compare each string/int field), and mutate an attachment field (e.g. `changed_row.attachments[0].slot += 1`) so the list change is actually exercised and checked.
