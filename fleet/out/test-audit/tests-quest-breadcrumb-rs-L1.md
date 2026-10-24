<!-- fleet job=test-audit id=tests-quest-breadcrumb-rs-L1 status=done turns=5 usd=0.0062 tokens(read,write,in,out)=[47478, 21857, 12, 6031] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/quest_breadcrumb.rs lines 1-469 of 469

Window reviewed: `prototype/osfr-tools/tests/quest_breadcrumb.rs` lines 1-469. Read against `src/quest_journal.rs` (`handle`/`breadcrumb` at 96-137, `load_crosswalk` at 161-204, `translate` at 208-215). No `#[ignore]` and no fixture-dependent early returns. The loader and `translate` assertions are not tautological, and the refusal tests compare full engine state, so the main paths are sound. Findings:

- **[medium] tests/quest_breadcrumb.rs:453 `a_listed_id_for_a_quest_already_done_or_held_changes_nothing` - the name promises the "already done" case, but the body only exercises an Active (held) quest and never sets a quest to Completed.**
  - Why it cannot catch a regression: `breadcrumb()` in `quest_journal.rs:118` only special-cases `Active`. A change that drops or breaks the Completed guard (for example, one that re-offers a finished quest, or sends a fresh `QuestInfo` for it) would still pass, because no Completed quest is ever built.
  - Fix: after accepting 10, complete it through the engine's normal path (or fixture state with `QuestStatus::Completed`), then call `start(&mut engine, &crosswalk, 1807)` and assert no offer (`offered(..) == None`), no reward, `!outcome.changed`, and `assert_eq!(engine.state(), &before)`.

- **[low] tests/quest_breadcrumb.rs:442 `a_full_quest_log_refuses_the_start_and_says_so` - the comment says the limit notice is "the only thing sent", but the assertion is `outbound.contains(...)`, which allows any other messages.**
  - Why it cannot catch a regression: an extra outbound message (for example a stray `QuestInfo` or a reward-display message next to the limit notice) still passes `contains`, so the "only" claim is never checked.
  - Fix: assert the exact vector, e.g. `assert_eq!(outcome.outbound, vec![OutboundMessage::Quest(QuestMessage::QuestLimit { member: true })])`.

- **[low] tests/quest_breadcrumb.rs:160 `every_shipped_row_names_its_points_and_says_how_it_was_decided` - the name says rows "name their points", but the body never checks `poi_ids` or `poi_name`; it only checks `source` tags.**
  - Why it cannot catch a regression: a shipped row with `poi_ids: []` or an empty `poi_name` would pass, since the loader's checks at `quest_journal.rs:180-190` are only exercised by the synthetic `malformed_*` file, not by the shipped content.
  - Fix: in the loop, assert `!row["poi_ids"].as_array().unwrap().is_empty()` and `!row["poi_name"].as_str().unwrap().is_empty()`, or rename the test to drop "names its points".

- **[low] tests/quest_breadcrumb.rs:320 doc comment on `crosswalk()` - it says "1807..1813 map to 10..13", but the fixture maps only 1807..1811 to 10..14 (line 322), and 1812-1814 are not in the map.**
  - Why it cannot catch a regression: this is comment drift, so it is not a missed bug. It misleads the next reader about which ids are refusal cases. The actual refusal cases are 1808-1810 (lines 412-414).
  - Fix: change the comment to "1807..1811 map to 10..14; 1812 and 1813 are unmapped and 1814 is unmapped". Check the wording against the fixture.

- **[low] tests/quest_breadcrumb.rs:87 and 94-95 `the_shipped_crosswalk_loads_and_points_at_real_quests` - exact content counts (`rows.len() == 18`, `points.len() == 43`) are pinned, though the test is about the crosswalk pointing at real quests.**
  - Why it cannot catch a regression: it is churn, not a missed bug. Adding a legitimate breadcrumb row or POI to the shipped JSON fails this test even when the new row is valid, and the comment at line 94 ties the number to a startup snapshot that must be kept in sync by hand.
  - Fix: drop the two count asserts and keep the real checks (the id-set equality at line 80 and the per-row `catalogue.contains` at line 131). If the 43 count is a deliberate content guard, say so in the test name or move it to a dedicated snapshot test.

Checked and not reported: the malformed-crosswalk `is_err()` loop (194-237) is guarded by the positive case in `unmapped_rows_are_kept_out_of_the_map` (187-191), which asserts `Ok` with the same `record`/`file` helpers. The `after the window` checks in 369-394 compare full state and are not tautological.
