<!-- fleet job=note-refresh id=Windows-Atomic-Save-Reader-Compatibility status=done turns=12 usd=0.0105 tokens(read,write,in,out)=[230078, 36408, 26, 7356] model=claude-haiku-5-5 -->
# notes/Research/Windows Atomic Save Reader Compatibility.md

**Verdict:** minor drift. The code claims all match the tip. Only the closing status sentence is stale: the review and native follow-up it calls pending were recorded as done later on 2026-10-08.

**Corrections:**

- `old:` Independent review and fresh native acceptance under observer reads remain pending.
  `new:` Independent review passed: 12 focused atomic-save checks, full ordinary suite 153 passed, release c642323 (MODLOG.md:334; `notes/Reviews/Native Forging Cancellation Restart 181038.md:13`). Native Forging 181715 then completed 18 chains, 5 hammers and the Cleetus turn-in on the retry build (`notes/Tasks.md:88`). The record does not say whether an observer reader was attached during that native run, so "under observer reads" stays unproven.
  `why:` MODLOG.md:334 and :336; notes/Tasks.md:88 (marked [x]); notes/Reviews/Native Forging Cancellation Restart 181038.md:13.

**Checked and holding (no change):**

- `character_store::replace_bytes` (src/character_store.rs:106) writes and `sync_all`s a unique temp file in the same directory (`create_temporary`, :158). It drops the handle, then calls `fs::rename` through `replace_bytes_with` (:110–141).
- Retry rule: `cfg!(windows)`, raw OS error 5 or 32, `retries < 20`, `sleep(25ms)`. That is 500 ms total, and other errors return immediately (:121–136).
- An uncommitted temp file is removed on drop (:149–156). Permanent denial propagates.
- The shared primitive is used by character saves (:102), `game_store.rs:183`, and `identity.rs:197`.
- Tests: `tests/character_store.rs` has 8 `#[test]` functions, two of them `#[cfg(windows)]` (the transient reader at :181 and the permanent denial at :214). `tests/game_store.rs:20` is the migration/corruption test.

**Unsure:**

- `three library tests pass`: I found the in-crate `injected_replacement_failure_preserves_the_previous_file` (src/character_store.rs:196–220) but could not confirm a count of three.
- The proof files `../lab/reports/windows-atomic-save-retry-proof.json` and `prove-windows-atomic-save-retry.py` are not in the repo, so I could not check them.
- Only Windows runs exercise the two `cfg(windows)` tests. I could not confirm from this tip that they were run on Windows.
- The note's "Eight character-store tests … pass" can only be confirmed as eight functions in the file, not as an executed pass count.
