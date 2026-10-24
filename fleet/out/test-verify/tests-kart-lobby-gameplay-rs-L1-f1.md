<!-- fleet job=test-verify id=tests-kart-lobby-gameplay-rs-L1-f1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[8808, 10966, 8, 2850] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/kart_lobby_gameplay.rs:143

**Verdict:** `confirmed`

**Evidence:** I could not refute the claim. The oversized case never reaches the size check's meaningful outcome.

- Test, `tests/kart_lobby_gameplay.rs:141-149`: the oversized input is `vec![b' '; 256 * 1024 + 1]`, which is whitespace only. The only assertions are `assert!(Gameplay::load(&fixture.0, None).is_err())` (line 147) and that the file bytes are unchanged (line 148). Neither checks the error kind or message.
- Code, `src/gameplay.rs:1048-1059`: with the cap, the reader takes at most `MAX_LOBBY_CONTENT + 1` bytes, then `if bytes.len() > MAX_LOBBY_CONTENT { return Err(invalid("kart lobby content exceeds 256 KiB")) }` runs at line 1056. Without the check (or without the `.take` bound, which still reads 256 KiB+1 bytes here), the code reaches line 1059, `serde_json::from_slice(&whitespace)`. That returns an EOF parse error, so `Gameplay::load` still returns `Err`.
- Walk-through with the cap deleted: line 143's input → parse error → line 147 `is_err()` passes → line 148 bytes unchanged passes. The test stays green.
- A grep for `exceeds 256 KiB`, `256 * 1024` and `MAX_LOBBY_CONTENT` across `prototype/osfr-tools` finds no test asserting the cap message. So the suite as a whole does not pin this cap, not just this test.

The claim's mechanism is accurate. The other cases in the window (the 102/1 opt-in, the truncated and trailing-bytes requests, `deny_unknown_fields` on `guess`) were not part of this challenge and I did not re-verify them.

Note: the test is `#[ignore]`d with a stated reason (private campaign input). That is not the defect here. The defect is that when it does run, its assertions would pass with the cap removed.

**Minimal fix:** Make the oversized payload valid JSON that exceeds only the cap (e.g. the five empty tables plus a `"pad"` string sized so the total is 256*1024+1 bytes), and assert the message, e.g. `assert!(Gameplay::load(&fixture.0, None).unwrap_err().to_string().contains("exceeds 256 KiB"))`. The exact-error check needs confirming against how `invalid(...)` renders in `Gameplay::load`'s error type, which I did not check.
