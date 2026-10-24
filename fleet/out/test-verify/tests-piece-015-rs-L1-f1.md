<!-- fleet job=test-verify id=tests-piece-015-rs-L1-f1 status=done turns=5 usd=0.0082 tokens(read,write,in,out)=[55083, 29040, 12, 7988] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_015.rs:129

**Verdict:** `confirmed` (narrowed; the claim's wording "any change to the parser, launch_mode, or counts" is too broad, but the real-data gap it names is real).

**Evidence:**

- **The early return is live in this repo.** `lab_resources()` (piece_015.rs:46-56) joins `CARGO_MANIFEST_DIR/../../lab/working/...`. The repo root listing has no `lab/`, and `.gitignore:28` ignores `/lab/`, so a clean checkout never has it. Lines 130-133 (`let Some(resources) = ... else { eprintln!; return; }`) therefore make the test pass without asserting anything.
- **The skip exemption does not apply.** The fixture is not in `repo`, so the "fixture-gated early return where the fixture exists in repo" carve-out does not cover this test.
- **Nothing else reaches this module against shipped data.** `src/restoration/piece_015.rs` is not registered in `lib.rs` (its own header, line 17). A search of `tests/` finds no other reference to `MiniGameData` or `piece_015`. The synthetic tests (lines 58-126) are the only other coverage.
- **The synthetic tests do catch generic breakage.** Examples: `counts()` must equal (2,2,1,2) on the fixtures; type 8 must map to Flash and type 9 to Native; undeclared type 999 must map to Undeclared; and the duplicate-ID and short-row errors are pinned. So a generic logic error (swapped mode, off-by-one IS_FLASH column, wrong fixture count) is caught without the lab. The claim is therefore wrong to say that *any* change to these functions passes.
- **Regressions that only show on the real corpus pass.** The 783/22/20/610 totals and the 139 (Flash) and 802 (Undeclared) lookups are asserted only at lines 144-149, which never run. Concrete example: a change that dedupes group links by (group, game) would leave all synthetic fixtures unchanged, since they have no duplicate links, and would change the real 610 count. Nothing in the gate would catch it.
- **Not a refutation via CRLF.** The header claims CRLF tolerance. `str::lines()` already strips `\r\n`, so the `trim_end_matches('\r')` at line 103 is not a real-data-only regression vector, and I am not relying on it.

**Minimal fix:** on the gate, fail instead of returning early, e.g. `let Some(resources) = lab_resources() else { if std::env::var_os("OSFR_REQUIRE_LAB").is_some() { panic!("lab resources required") } else { return } };`. Alternatively, commit the four hash-pinned tables under `tests/fixtures/` and assert their SHA-256 plus the 783/22/20/610 counts so the check never depends on the gitignored lab.
