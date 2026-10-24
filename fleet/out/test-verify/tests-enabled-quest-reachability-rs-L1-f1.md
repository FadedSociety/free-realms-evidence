<!-- fleet job=test-verify id=tests-enabled-quest-reachability-rs-L1-f1 status=done turns=8 usd=0.0098 tokens(read,write,in,out)=[137842, 33422, 18, 8403] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/enabled_quest_reachability.rs:850

**Verdict:** `confirmed`

**Evidence:**

- **The named test has no job_level input.** `graded_target_kinds_fail_on_a_scratch_tree` (lines 850-1007) runs the clean fixture and canaries A-F. None of them patch or add a `job_level` objective. The canaries touch `complete_dungeon` (A), `finish_minigame` (B, F), `collect_item`/`equip_item` (C), `craft_recipe` (D) and `gather_resource` (E). The `defeat`, `reach_poi`, `interact_actor` and `job_level` kinds have no canary.
- **The fixture has no job_level objective.** `quest_catalogue_fixture.rs:121-168` (`fixture_objectives`) builds the FIXTURE_QUEST objectives from `talk_to_npc` plus six kinds: `collect_item`, `equip_item`, `craft_recipe`, `finish_minigame`, `complete_dungeon`, `gather_resource`. There is no `job_level`. The claim's wording "the fixture contains only a talk_to_npc objective" is slightly off, since FIXTURE_QUEST carries those six extra objectives. The conclusion still holds.
- **The job_level check is reached from one place only.** `job_level_violation` (lines 418-450) is a private method on `Catalogue`, so no other test file can call it. `target_violations` reaches it through `every_talk_target_and_visit_point_resolves` (line 604) on the shipped tree. The only shipped `job_level` objective is `data/content/quests/warrior.json` (`id` 3150005, `enabled: true`, `profile_id: 32`, `level: 5`). That input is valid.
- **Mutations that the file cannot see.** Each of these leaves every test in the file green:
  - Deleting `rank == level` (line 442). Valid shipped content still passes.
  - Deleting `profile <= 0 ||` or the `1..=20` guard (line 429). Valid shipped content still passes.
  - Deleting the `job_level` match arm (line 393). Nothing else checks it.
  - Making `job_level_violation` return early. The shipped objective still passes.
  - The module-doc claim (lines 17-20) that job_level is "proved" is therefore not backed by any negative case.
- **The same gap applies to `defeat` and `reach_poi`.** No canary exists, and the shipped tree is valid for both, so deleting those arms also passes.

I looked for another route to catch these regressions and found none. `job_level_quest.rs` tests the quest's runtime behaviour, not this audit's private helper. The Profiles loader is reached only through the audit's own check, so it cannot stand in for these canaries.

**Minimal fix:**

- Add a valid `job_level` objective to `fixture_objectives()` as a control. Use a profile in `reference_content()` and level 5.
- Add canaries that patch it to an absent profile (e.g. 9999), to level 0 or 21, and to a `defeat` with `count = 0` and a `reach_poi` with `poi_id = 0`. Each should assert exactly one violation that names the kind.
- Alternatively, rename the test to match its five-kind scope. The fixture-based fix is the stronger option.
