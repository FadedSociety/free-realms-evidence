<!-- fleet job=test-audit id=tests-npc-greetings-starting-road-rs-L1 status=done turns=7 usd=0.0072 tokens(read,write,in,out)=[81219, 23982, 16, 6769] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/npc_greetings_starting_road.rs lines 1-370 of 370

Window reviewed: `tests/npc_greetings_starting_road.rs` 1-370, with `tests/common/npc_greetings.rs` 1-200 and the code under test (`src/npc_interaction.rs` 190-200, 898; `data/content/npcs/farnum_farmstead.json` 1674-1760).

- **[medium] prototype/osfr-tools/tests/npc_greetings_starting_road.rs:283 `missing_or_zero_greeting_still_falls_back_to_an_empty_body` - the name claims a zero greeting falls back to an empty body, but only the missing-key case (`BLANK`) is ever exercised.**
  Why it cannot catch a regression: `BLANK` (9500000269, `farnum_farmstead.json:1674`) has no `greeting_string_id` key at all, so serde's `#[serde(default)] Option<u32>` yields `None`. The loader passes the value through unchanged (`npc_interaction.rs:898`, `body_string_id: npc.greeting_string_id`), so an explicit `"greeting_string_id": 0` becomes `Some(0)`. A change or regression that stores 0 would still pass: line 287 only sees `None`, and the gameplay check at lines 315-319 compares a 26/3 body of `0`, which is the same bytes whether the service had `None` or `Some(0)`.
  Fix: add an in-memory or temp-dir fixture NPC with `"greeting_string_id": 0` and assert `service_talk_body(...) == None` (and that the menu's Talk context has `body_string_id == None`). Alternatively, rename the test to drop "or_zero" and state that only the missing-key case is covered.

- **[low] prototype/osfr-tools/tests/npc_greetings_starting_road.rs:232-239 `the_starting_road_npcs_have_recovered_greetings` - the source check uses substring matching, so it accepts ids that only contain the expected number.**
  Why it cannot catch a regression: `evidence.contains("40")` for `line 40` also matches `line 400`, and `contains("101014")` matches `1010140`. A source that cites the wrong row or a longer id still passes.
  Fix: match delimited tokens (for example, a regex `line {n}\b` and `(?<!\d){id}(?!\d)`), or check the exact `"{guide} line {n}"` string the content generator writes.

- **[low] prototype/osfr-tools/tests/npc_greetings_starting_road.rs:323 `the_content_rows_stay_bounded_and_sourced` - the name and the comment at 346 claim a row-count or shape bound, but the body only checks file byte sizes and UTF-8.**
  Why it cannot catch a regression: a change that adds or drops rows, or breaks the shape of rows that still parse, passes. The `let _ = service();` call only panics if the loader fails, and its result is discarded, so it asserts no row count.
  Fix: either rename the test to say it bounds byte size and evidence text, or assert the expected row count per file (for example, `npc_records(file).len()` against a constant) and check that each edited row still has the keys the first test checks.

- **[low] prototype/osfr-tools/tests/npc_greetings_starting_road.rs:181-185 `the_starting_road_npcs_have_recovered_greetings` - the "greeting reused" check only compares the 16 new rows against each other, not against the 19 `EXISTING_GREETINGS`.**
  Why it cannot catch a regression: a new row that reuses an existing W126 greeting id (for example 80 or 24940) passes. The assertion message reads as a global uniqueness rule. The current data has no overlap, so this is a gap in coverage rather than a failing case today.
  Fix: also insert the `EXISTING_GREETINGS` ids into `greeting_ids` before the loop, or change the message to say "reused within this slice" if sharing is intended.
