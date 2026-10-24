<!-- fleet job=test-audit id=tests-content-npc-placement-rs-L1 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[8312, 9999, 8, 3854] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/content_npc_placement.rs lines 1-217 of 217

Window: `prototype/osfr-tools/tests/content_npc_placement.rs` lines 1-217. Two findings are firm, one is a weaker hole, and one is a low-severity pin.

- **[medium] prototype/osfr-tools/tests/content_npc_placement.rs:184 regional_npcs_have_unique_sourced_placements_and_captures_match_exactly - the final check compares `npc["capture_match"]["actor_id"]` with `captured["actor_id"]`, which is the same value the test already used to look up `captured` at lines 150-153.**
  - Why it cannot catch a regression: `captured` is selected with `captured["actor_id"] == capture_match.actor_id`, so this assertion is true by construction. A change that stopped the NPC from linking the right capture, or that linked it to the wrong one, would still pass, because `find` and this assert use the same source value. The position and rotation checks only compare against whatever `captured` was selected, so a wrong link would also pass them.
  - Fix: check the link against an independent key. For example, assert that the NPC's `capture_match.actor_id` equals an expected actor id taken from the startup snapshot or from a separate fixture. Alternatively, assert that the captured row's own identity (name or zone) agrees with the NPC's zone or name, which the code under test is supposed to record.

- **[low] prototype/osfr-tools/tests/content_npc_placement.rs:164-168 regional_npcs_have_unique_sourced_placements_and_captures_match_exactly - `assert_eq!` on `npc["position_w"].as_f64()` against `captured_position[3].as_f64()` compares two `Option<f64>` values, so `None == None` passes.**
  - Why it cannot catch a regression: if the generator stops writing `position_w` for a captured NPC (null), and the capture also has no W value, the check silently passes. The name's claim of an exact capture match is then not enforced for W.
  - Fix: first assert `npc["position_w"].as_f64().is_some()` and that `captured_position.len() == 4` (the code indexes [3] without checking). Then compare the two values with a tolerance or exact equality.

- **[low] prototype/osfr-tools/tests/content_npc_placement.rs:140-146 regional_npcs_have_unique_sourced_placements_and_captures_match_exactly - the name says "unique sourced placements", but the duplicate-position check only runs for sources starting with `reconstructed_`.**
  - Why it cannot catch a regression: a `captured` or `legacy_data` NPC placed exactly on top of another NPC's position passes unnoticed, and so does a captured NPC duplicating a reconstructed one. Nothing in the body reflects a "unique across all sources" claim.
  - Fix: either rename the test to say "reconstructed placements are unique", or insert `positions` for every source, and assert uniqueness only where the data is known to be unique (decide that explicitly per source class).

- **[low] prototype/osfr-tools/tests/content_npc_placement.rs:215 regional_npcs_have_unique_sourced_placements_and_captures_match_exactly - `assert_eq!(npc_count, 1_201)` pins an exact record total that changes whenever any NPC is added or removed, which is unrelated to the placement rules this test checks.**
  - Why it cannot catch a regression: it does not detect a placement bug. It fails on unrelated content additions and creates churn. The comment about T379 shows it is a deliberate pin, but it is still incidental to what the test is about.
  - Fix: remove the total, or move it to a dedicated content-count test. If it stays, assert a lower bound or the per-file set of record ids.

Checked and not reported: the `SCHEMA_VERSION` pin at line 31 is a real constant in `src/content.rs:12` and is used by the loader at `content.rs:496`. The `poi_anchor`, `legacy_data`, and unanchored branches (lines 75-146) do assert concrete values. The data directory and the `unanchored`/`captured` fields exist in the repo as the test expects, so the test does not skip.
