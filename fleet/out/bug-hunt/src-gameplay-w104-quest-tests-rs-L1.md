<!-- fleet job=bug-hunt id=src-gameplay-w104-quest-tests-rs-L1 status=nothing_found turns=4 usd=0.0022 tokens(read,write,in,out)=[21929, 10440, 10, 1310] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/w104_quest_tests.rs lines 1-440 of 440

No defects in `prototype/osfr-tools/src/gameplay/w104_quest_tests.rs` lines 1-440.

Why the window is out of scope:
- The module is declared `#[cfg(test)] mod w104_quest_tests;` at `prototype/osfr-tools/src/gameplay.rs:5462-5463`, so none of this code is compiled into the server binary.
- Every function in the window is a `#[test]` with `#[ignore = "private W104 scratch package; no native client"]` (for example lines 125-127, 138-140, 174-176, 243-245, 312-314, 352-354, 384-386, 416-418). The helpers `content()`, `game()`, `count()` and `stage()` (lines 13-123) exist only to support those tests.
- The rules exclude code in `#[cfg(test)]`, so the `unwrap()`s, the hard-coded fixtures and the `i32::MAX` grant at line 130 are not findings.

I did not follow any call into production code, because the window contains no production logic. The hooks it exercises (`grant_reward`, `handle_in_world`, `apply_type8`, `apply_craft`, `on_location`) are outside this window and were not reviewed here.
