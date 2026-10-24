<!-- fleet job=test-audit id=tests-kart-pad-repair-guys-rs-L1 status=done turns=6 usd=0.0075 tokens(read,write,in,out)=[81840, 24077, 14, 7343] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_pad_repair_guys.rs lines 1-571 of 571

Window: `prototype/osfr-tools/tests/kart_pad_repair_guys.rs` lines 1-571. Three findings, all confirmed by reading the test body and the helpers it calls (`click`, `choose`, `menu`, `talk_body` at lines 109-154; `movie.rs` / `gameplay.rs` around 4276-4305 for the busy path).

- **[medium] tests/kart_pad_repair_guys.rs:418-455 two_players_see_the_same_actor - the "closing the first must leave the second's menu selectable" check never tests the second session's menu state after the close.**
  - Why it cannot catch a regression: after `first.handle_in_world(&[26,0,4,0], ...)` at line 440, the test calls `click(&mut second, ...)` again at line 443. That click re-opens a fresh menu, so the second session's menu is never checked as still open after the close. A change where the first session's close clears or disables the second session's open dialogue would still pass, as long as a new click works. The comment's claim is therefore not exercised.
  - Fix: capture `state_bytes(&second)` (or the second's menu/actor state) before the first session's close and assert it is byte-identical after the close. Then choose option 0 from the menu opened at line 423 without re-clicking. That fails if the close touches the second session, and the re-click cannot hide it.

- **[medium] tests/kart_pad_repair_guys.rs:526-571 a_busy_player_is_refused_and_the_menu_is_not_opened - the refusal the name claims is never identified, and there is no unblocked control.**
  - Why it cannot catch a regression: in production the busy gate answers `Ok` with a `chat::system(movie.blocked_message())` reply (gameplay.rs:4294). The test only checks that no 26/9 menu and no 26/3 body appear, plus unchanged state. Any silent no-op would pass, including one caused by an unrelated failure to resolve the NPC. The test also never shows that the same click succeeds when the Mining run is not active; it relies on other tests for that.
  - Fix: assert that `refused.replies` contains the chat packet for `mining::Movie::Mining.blocked_message()` (the "Close the mining game before changing jobs, equipment or interacting." text), and add a paired click on the same actor with no mining state that does produce a 26/9 menu, so the busy result is shown to be the cause.

- **[low] tests/kart_pad_repair_guys.rs:223 both_repair_guys_are_drawable_at_their_legacy_positions - `assert_ne!(content_key, 0)` compares a constant from `ACTORS` (literal 9_000_001_989 / 9_000_002_048) with 0 and cannot fail.**
  - Why it cannot catch a regression: the value is a hard-coded literal, so the check does not depend on any loaded content. It adds no coverage beyond the later `record["npc_id"] == content_key` assertion.
  - Fix: delete it, or replace it with an assertion on the loaded data, e.g. `extra["content_key"].as_u64().is_some_and(|k| k != 0)`, so it tests the content and not the constant.</result>
</invoke>
