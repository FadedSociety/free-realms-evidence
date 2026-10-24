<!-- fleet job=test-audit id=tests-bot-smoke-rs-L1 status=done turns=6 usd=0.0071 tokens(read,write,in,out)=[77851, 24580, 14, 6450] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/bot_smoke.rs lines 1-544 of 544

Window `prototype/osfr-tools/tests/bot_smoke.rs` 1-544 read in full. Read `src/bin/osfr-bot.rs` (run_step 610-650, run 668-680, wait_for 571-587, matches_family 226-231) to check the assertions. Most of the window holds up: the expectation and timeout paths return real errors, `wait_for` times out with `Err`, and the `#[ignore]` attributes carry reasons. Two findings:

- **[medium] tests/bot_smoke.rs:350 script_parser_accepts_every_step - the name claims every step kind is parsed, but only steps[0], steps[3] and steps[6] are checked (lines 355-368).**
  - Why it cannot catch a regression: `parse_script(...).unwrap()` only proves nothing errors. A change that maps `wait 50` to the wrong duration, drops the direction from `move 1 2 3`, mangles the `raw 0f000100` bytes, turns `expect-text hi there` into the wrong text, or makes `quit` parse as something else would still pass, because steps 1, 2, 4, 5, 7, 8 and 9 are never compared.
  - Fix: assert the full vector with `assert_eq!(steps, vec![Chat(..), Wait(50), Move(..), Ability{0,1}, Ability{2,77}, Raw(vec![0x0f,0,1,0]), Expect{15,Some(1),Some(900)}, Expect{12,None,None}, ExpectText("hi there".into()), Quit])`. Check that `Step` derives `PartialEq` and `Debug`, which it does, since the existing assertions compare steps.

- **[medium] tests/bot_smoke.rs:378 bot_logs_in_to_single_save_gateway_and_chats - the chat check rests on `expect 15 1`, and that match is loose, so the test can pass without the chat echo arriving.**
  - Why it cannot catch a regression: `matches_family` (osfr-bot.rs:226-231) also accepts any message whose byte at index 2 equals the sub-value, so `expect 15 1` (line 386) is satisfied by any unrelated message with byte 2 == 1. Separately, `move` and `attack` (line 386) have no expectation at all. A gateway that drops the chat echo, or ignores move and attack, still passes, provided some message carries that byte. The only other assertion (line 394-397) checks that family 12 arrived, which `login()` already waits for.
  - Fix: give the echo an exact expectation. Either tighten `matches_family` so `sub` matches only the parsed sub-field, or assert on the echoed text with `expect-text hello bot` immediately after `chat hello bot`. Add an assertion on the reply to `move`/`attack`, or drop the claim from the name.

- **[low] tests/bot_smoke.rs:372 script_parser_accepts_every_step - `steps.len() == 10` (line 355) and the exact 24-byte `ability_request` layout (lines 372-374) pin incidental detail.**
  - Why it is a churn risk, not a missed bug: adding a script line to the fixture string, or changing the ability request framing, breaks this test even though its concern is parsing.
  - Fix: keep the per-step equality from the first finding and drop the bare length check. Keep the 36/10 opcode bytes, since those are the protocol behaviour the comment cites.
</result>
