<!-- fleet job=test-audit id=tests-support-quest-catalogue-fixture-rs-L1 status=nothing_found turns=4 usd=0.0032 tokens(read,write,in,out)=[21897, 12627, 10, 2729] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/support/quest_catalogue_fixture.rs lines 1-418 of 418

Reviewed `prototype/osfr-tools/tests/support/quest_catalogue_fixture.rs` lines 1-418 in full. This file contains no `#[test]` functions and no assertions. It is a support module that writes a scratch split-content tree (quests, NPCs, jobs, inventory, item catalogue, recipes, field battles) for the tests in `tests/enabled_quest_reachability.rs`. The audit checks I could make against it found nothing that would let a test pass vacuously:

- **Defect variants do what their names say.** Each `Defect` arm writes exactly one broken record. `MissingGiver` omits the NPC `FIXTURE_MISSING_GIVER` from `npcs/fixture.json` (lines 411-416). `WrappedTitle` uses `u32::MAX` (line 305). `EmptyReward` uses `json!([])` (line 319). `DisabledPrerequisite` adds the disabled blocker record (lines 337-346). `MissingPrerequisite` points at an id that is never written (line 356). `VisitGeometry` passes the caller's position and radius through (lines 365-366).
- **Scratch directories do not collide.** `Scratch::new` removes and recreates `t314-{name}` (lines 55-61). Every `fixture("…")` call site in `enabled_quest_reachability.rs` uses a distinct name, including the loop-driven `visit-*` names at lines 1014-1029. Parallel tests therefore do not share a directory.
- **Cleanup is real.** `Drop` removes the directory (lines 68-72), so the fixture does not leak state between runs.
- **Fixture rows resolve.** The item and recipe rows (lines 400-401) cover the `FIXTURE_ITEM` and `FIXTURE_RECIPE` references, and the battle, minigame and gather targets are written or referenced as the comments describe. I did not find a graded kind whose target is missing from the fixture, which would have made a canary pass by absence.

No finding meets the criteria for this window. The test bodies that consume these defects live outside my window (for example `enabled_quest_reachability.rs:735-1035`), and I did not audit them.
