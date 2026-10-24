<!-- fleet job=bug-hunt id=src-gameplay-w64-regional-quest-tests-rs-L2401 status=nothing_found turns=5 usd=0.0039 tokens(read,write,in,out)=[46445, 20158, 12, 1809] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs lines 2401-2994 of 2994

No defects reported for `prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs` lines 2401-2994.

Why nothing qualifies:

- The whole module is test-only. `prototype/osfr-tools/src/gameplay.rs:5456-5457` declares `mod w64_regional_quest_tests;` behind `#[cfg(test)]`. Every function in the window is a `#[test]` fn (2402, 2476, 2529, 2563, 2633, 2666, 2787, 2861). The brief excludes code in `#[cfg(test)]`, so panics, `unwrap`s, and fixture-driven assertions here are expected behaviour, not server defects.
- The `unwrap`s and indexing in the window (for example `p[4..8]`, `p[28..32]`, `screen[18..22]`) read packets the test builds itself or receives from the engine under test. A failing one is a test failure, not a remote crash.
- The test-side `Scratch`, `std::fs` and temp-directory helpers (2685-2781) are test fixtures, so their cleanup and atomicity behaviour does not reach production code.

I did not trace any production function that these tests exercise beyond what the window shows, since the brief limits review to this window.
