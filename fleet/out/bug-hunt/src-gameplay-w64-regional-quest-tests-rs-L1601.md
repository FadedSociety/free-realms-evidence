<!-- fleet job=bug-hunt id=src-gameplay-w64-regional-quest-tests-rs-L1601 status=nothing_found turns=6 usd=0.0061 tokens(read,write,in,out)=[87380, 26845, 14, 3704] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs lines 1601-2400 of 2994

Window reviewed: `prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs` lines 1601-2400 (read in full).

No reportable defects. The whole file is compiled only for tests: `prototype/osfr-tools/src/gameplay.rs:5456-5457` declares `#[cfg(test)] mod w64_regional_quest_tests;`. Every line in the window is therefore test code, which the brief excludes from the defect list. The window's test functions (e.g. `medic_job_abilities_strike_heal_and_refuse`, `job_skills_unlock_at_their_level`, `refused_reload_all_keeps_behaviour_and_shared_field_state`, `activity_portal_refresh_is_throttled`, `live_equipment_and_job_changes_are_ready_for_neighbours`) only drive production APIs and assert on their output.

Items set aside because they are test-only:
- The helpers `i32_at` / `text_at` in `live_equipment_and_job_changes_are_ready_for_neighbours` (lines 2224-2232) index and `unwrap` without bounds checks. They run only on the server's own packets in a test and never see client input.
- Loose assertions such as `matches!(refusal(&missed), Some(285) | Some(288))` (line 1826) weaken a test but are not a production defect.

I did not open production code beyond the module declaration, because nothing in the window points to a production defect that I could tie to a line in it.
