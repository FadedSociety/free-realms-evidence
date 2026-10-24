<!-- fleet job=test-audit id=tests-field-enemies-bot-rs-L1 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[2303, 4151, 6, 1878] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/field_enemies_bot.rs lines 1-98 of 98

Reviewed `prototype/osfr-tools/tests/field_enemies_bot.rs` lines 1-98. Most of the window holds up. The `#[ignore]` has a reason, and missing `W105_GATEWAY` or `W105_REFERENCE` makes the test panic through `unwrap` rather than pass silently. The leash assertion at line 73 and the final assertion at lines 91-94 both compare against the test's own `home` constant, not against the code under test. The loop cannot pass without the actor leaving home past 10 m and returning within 0.05 m, and it fails at the 25 s deadline otherwise.

- **[low] prototype/osfr-tools/tests/field_enemies_bot.rs:96 field_enemy_leashes_on_the_wire - The PASS line reports "Studio disabled", but nothing in the test checks that.**
- **Why it cannot catch a regression:** The only assertions are the leash distance, the max-radius and return checks, and the wire packets for GUID 131000102001. If Studio were enabled, or the `realm god` / `realm reload` setup stopped disabling it, the test would still pass and print the same PASS text, so the summary overstates what was verified.
- **Fix:** Either drop "Studio disabled" from the PASS message, or assert the precondition directly, for example by checking the response to the setup commands in lines 37-50, which currently only waits for `family: 15, sub: Some(3)` and does not inspect the payload.
