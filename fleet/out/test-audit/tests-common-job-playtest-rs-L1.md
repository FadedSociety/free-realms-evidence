<!-- fleet job=test-audit id=tests-common-job-playtest-rs-L1 status=nothing_found turns=7 usd=0.0042 tokens(read,write,in,out)=[56422, 14721, 16, 3652] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/job_playtest.rs lines 1-127 of 127

Reviewed `prototype/osfr-tools/tests/common/job_playtest.rs` lines 1-127 (a helper module, not a test file; it has no `#[test]` functions). No finding in the five reportable categories.

What I checked against the code under test:

- **`hits_from` (l.87-96) offsets are correct.** `attack_processed` in `src/encounter.rs:3015-3036` writes a 4-byte header, then attacker GUID (4..12), attacker again (12..20), target (20..28), and the damage `i32` at 28..32. The helper's `[28..32]` read matches. The helper is not a tautology: it reads a field from the packet rather than recomputing the value.
- **`bar_ids` (l.103-127) layout is correct.** `src/opening_abilities.rs:335-453` writes `36,0,5,0`, then profile id, then slot count 8 (matching the `assert_eq!(..., 8)` at l.106). A type-3 entry is 10 `i32` values plus a trailing byte, which is 41 bytes as the decoder expects. An empty slot is a single `0` `i32` (4 bytes). The final `assert_eq!(at, toolbar.len())` pins the whole packet to the layout, so it can fail.
- **Install helpers (l.17-82)** only add definitions or outfits when the id or job key is absent. That matches their doc comments. The starter grant is not pre-decided here.

Minor observations, below the reporting bar, so not filed:

- `bar_ids` panics on toolbar kind 1. Its doc says "kinds 1/3 are 41 bytes", but only kind 3 is decoded. This fails loudly rather than passing, and the server only emits kind 0 and kind 3 in the paths I read.
- `hits_from` indexes `packet[28..32]` after a `starts_with` check without a length guard. A truncated 32/7 packet would panic rather than be filtered. This is a loud failure, not a silent pass.
