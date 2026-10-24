<!-- fleet job=test-audit id=tests-game-store-rs-L1 status=done turns=5 usd=0.0042 tokens(read,write,in,out)=[26880, 13212, 12, 4644] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/game_store.rs lines 1-119 of 119

Window: `prototype/osfr-tools/tests/game_store.rs` 1-119. Code under test read: `src/game_store.rs` (read_document, save_document, save_pets_state, write_document) and `character_store.rs` `CharacterState::validate` (rejects non-finite components, so the NaN refusal at line 114 is real).

- **[medium] prototype/osfr-tools/tests/game_store.rs:45-48 version_one_migrates_without_changing_coordinates_and_corruption_is_preserved - the oversize-file case does not exercise the size cap.** The 1 MiB payload is `vec![b' '; MAX_SNAPSHOT_BYTES+1]`, which is whitespace only and is not valid JSON, so it fails in `serde_json::from_slice` regardless of the cap.
  - Why it cannot catch a regression: deleting or loosening the `bytes.len() > MAX_SNAPSHOT_BYTES` check in `read_document` (game_store.rs:158-160, and the `take(MAX+1)` read at 156) still returns `Err` for this input, so the test passes. The 1 MiB guard is never shown to be load-bearing.
  - Fix: make the oversize input valid JSON that only the cap rejects, e.g. a valid version-5 envelope (`{"schema_version":5,"character":{...}}`) followed by spaces up to `MAX_SNAPSHOT_BYTES+1` bytes. Assert the error message or kind contains the size text, so a removed cap makes the load succeed and the test fail.

- **[medium] prototype/osfr-tools/tests/game_store.rs:55-63 pet_state_uses_the_current_schema_constant - the name says "current" but the expected value is `PET_SCHEMA_VERSION` (6), not the current `SCHEMA_VERSION` (7); the expectation is also read from the code under test.**
  - Why it cannot catch a regression: changing `PET_SCHEMA_VERSION` to any value, or changing `save_pets_state` to write the same constant, still passes because both sides read the same constant. A pet save written with schema 7 instead of 6 would also match if the constant moved.
  - Fix: assert the literal `6` (the on-disk format number that read_document's `(Some(7 | 6 | 5 | 4 | 3), None)` arm accepts), and rename the test to say it pins schema 6 for pet saves. Lines 42 and 98 have the same constant-on-both-sides pattern for BASE and PET; literals there would make the on-disk version explicit.

- **[medium] prototype/osfr-tools/tests/game_store.rs:73-74 save_with_pets_writes_character_and_roster_in_one_document (doc at 69-72) - the doc says the write is atomic and that a crash between two writes must not split the state, but the test cannot observe atomicity.**
  - Why it cannot catch a regression: an implementation of `save_with_pets` that writes the character file and then the roster file in two `replace_bytes` calls would still produce the same final document, and the refused-NaN case (114-115) fails validation before any write. So the test would pass on a two-write implementation.
  - Fix: either narrow the name and doc to "the envelope holds character, roster and housing together and a refused save leaves the file unchanged", or add a check that exercises the single-replace path, for example asserting a refused pet-only or character-only failure leaves no temp or partial file, or a write-count/injected-failure seam in `replace_bytes`.

Lines 19-52 (except 45-48), 80-103 and 105-115 otherwise assert the values they name, and the refused-write byte comparison at 114-115 is meaningful because the roster passed differs from the one on disk.</result>
</invoke>
