<!-- fleet job=test-audit id=tests-field-reload-atomicity-rs-L1 status=done turns=5 usd=0.0041 tokens(read,write,in,out)=[42074, 16713, 12, 3262] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/field_reload_atomicity.rs lines 1-480 of 480

One finding in lines 1-480 (the other tests in this window pin real state: `engine.state()`, `battle_spawners()`, `behaviour()`, the tick replies, and the pending battle).

- **[low] prototype/osfr-tools/tests/field_reload_atomicity.rs:430 a_refused_enemy_reload_keeps_the_walk_and_attack_state - the refusal is only checked as `!error.is_empty()`, so any error at all satisfies it.**
  - Why it cannot catch a regression: the bad file is meant to fail the level check (`level` 21, `field.rs:188`, which returns `"invalid field enemy"`). If a regression made `reload_field_enemies` fail for some other reason (missing file, schema or parse error, a wrong `staged` path), the test would still pass. The walk and attack state assertions after it would also still hold, because nothing was applied.
  - Fix: assert the specific message, for example `assert!(error.contains("invalid field enemy"), "{error}");`. Optionally, also check that the error is not a missing-file or parse error by asserting `error_kind()` or the message together with the level-21 cause.

Nothing else in the window looked like a cannot-fail or skipped test. The byte offsets in the 445 test (lines 466-476) are the wire format under test, not incidental details.
