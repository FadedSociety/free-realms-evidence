<!-- fleet job=test-verify id=tests-combat-rs-L1-f1 status=done turns=5 usd=0.0038 tokens(read,write,in,out)=[23366, 13210, 12, 3814] model=claude-haiku-5-5 -->
# high: tests/combat.rs:244

**Verdict:** `confirmed` (the conclusion holds; the stated mechanism and the proposed fix need correction).

**Evidence:**

- Test fixture (`tests/combat.rs:17-44`): `Content::new()` creates `temp_dir()/osfr-combat-test-<pid>-<n>` and writes only `npc.bin` and `combat.json` inside it. Nothing is written to the parent (`temp_dir()`).
- Guard-deleted mutation (remove `combat.rs:104-109`): at line 258, `Combat::load` reaches `directory.join(path)` at line 110 with `path = "../npc.bin"`. That resolves to `temp_dir()/npc.bin`, which the test never creates. `fs::read` at line 110 returns `NotFound`, and `load` returns `Err` via `?`. The assertion `assert!(Combat::load(&content.0, None).is_err());` at `tests/combat.rs:258` is therefore still satisfied. The test passes under the mutation.
- No other test in `prototype/osfr-tools` references `template_file`, `local filename`, or traversal (grep across the crate), so nothing else pins the guard.

**Corrections to the claim:**

- The claim says the second load "fails on the hash mismatch (`combat.rs:111`)". That is wrong. Without the guard, the code reads `../npc.bin`, not the corrupted `npc.bin`, so line 111 is never reached. The corruption at line 247 is irrelevant to the escape assertion. The failure is an I/O error at line 110.
- The proposed fix (rewrite `npc.bin` with valid bytes) is not sufficient on its own. With the guard deleted, the traversal still reads a missing file in the parent and errors. The fix that actually works is the message assertion: `Combat::load(...).unwrap_err().to_string()` must contain `"combat template must be a local filename"` (`combat.rs:108`). Under the guard-deleted mutation the message would be the OS "No such file" error, so the assertion fails. Restoring `npc.bin` is optional.

**Minimal fix:** at `tests/combat.rs:258`, replace `assert!(Combat::load(&content.0, None).is_err());` with `assert!(Combat::load(&content.0, None).unwrap_err().to_string().contains("local filename"));`. The line-249 corruption check can stay, but it should also assert `contains("hash mismatch")`.
