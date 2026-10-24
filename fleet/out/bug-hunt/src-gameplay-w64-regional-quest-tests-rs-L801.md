<!-- fleet job=bug-hunt id=src-gameplay-w64-regional-quest-tests-rs-L801 status=nothing_found turns=4 usd=0.0045 tokens(read,write,in,out)=[28145, 22633, 10, 2859] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs lines 801-1600 of 2994

## Window: `prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs` lines 801-1600

No defects in this window. Every line in it is test code, so it is outside the scope the brief sets.

- **Scope:** `prototype/osfr-tools/src/gameplay.rs:5456-5457` declares `#[cfg(test)] mod w64_regional_quest_tests;`. The window contains only `#[test]` functions and their helpers: `tracked_pins`, `select_packet`, `spawned_actors`, `offer_test_game`, and the rest. None of it is in production code, so the "code in `#[cfg(test)]`" exclusion applies to the whole window.
- **What I read:** lines 801-1600 in full, plus lines 1-40 and the `gameplay.rs` module declaration. The window covers claim/watch replies (45/x), the ordered goal and rearm tests, the take-me-there pin, the kill-objective pin, the Samantha end-screen and reconnect flow, developer offer variants, and the troll-summoner battle.
- **Non-defect observations (test code, so excluded):**
  - The comment at lines 1288-1289 says "6-byte header, 20-byte end-screen ids and 69-byte bundle keep the 99-byte total", but 6+20+69 = 95. The asserted length of 99 is right; only the comment's arithmetic is off.
  - Several test helpers use `unwrap` on fixture data (for example lines 1057-1058 and 1050-1051). These are test-only and read bundled content, not client input.
- **Production paths:** the tests exercise production code (`handle_in_world`, `on_location`, `update_npc_visibility`, `Gameplay::load`, the encounter `attack` path, and so on), but those functions are defined outside this window and I did not review them. Reviewing them would be a different window.
