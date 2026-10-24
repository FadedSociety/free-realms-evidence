<!-- fleet job=test-audit id=tests-content-npcs-rs-L1 status=done turns=3 usd=0.0044 tokens(read,write,in,out)=[12917, 15870, 8, 4485] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/content_npcs.rs lines 1-486 of 486

Window reviewed: `prototype/osfr-tools/tests/content_npcs.rs` lines 1-486. Two findings, both in the alias-collision and count assertions. The test is otherwise sound: the fixture directories it reads exist under `data/content`, nothing is `#[ignore]`d, and the `Scratch` directory is removed on drop.

- **[medium] prototype/osfr-tools/tests/content_npcs.rs:168 regional_npc_batch_and_resolved_job_references_validate - the "reference id maps to two NPCs" check (line 276) only fires when the colliding canonical id was seen earlier, so the result depends on file and record order.**
  - Why it cannot catch a regression: line 168 calls `reference_owner.insert(npc_id, npc_id)` with no collision check. If NPC A (processed first) lists alias `B`, the check at 276 sees `insert(B, A)` return `None`, so nothing fires. When NPC B is processed later, line 168 overwrites the owner back to `B` silently. A canonical id reused as another NPC's alias therefore passes whenever the alias-holder sorts first. The `canonical_ids` set (line 153-167) only covers canonical-vs-canonical duplicates, so it does not catch this either.
  - Fix: seed all canonical ids into `reference_owner` in a first pass, or at line 168 assert `reference_owner.insert(npc_id, npc_id).is_none()` after a pass that records aliases. Add a canary: a fixture where NPC A aliases NPC B's canonical id, with A listed first, must fail.

- **[low] prototype/osfr-tools/tests/content_npcs.rs:303 regional_npc_batch_and_resolved_job_references_validate - hard-coded totals (465 at 303, 1201 at 459, 655 at 470 and 475, 295 at 471, 170 at 472, 17/18 file counts at 133, 151, 306, 326) pin unrelated data.**
  - Why it cannot catch a regression: these totals change whenever any NPC, quest, or alias is added, even when the rule being tested still holds. They churn the test without testing the stated property (reference and job validity). The 465 check at 303 is also the same sum as 295 + 170 at 471-472, so it adds nothing new.
  - Fix: keep the structural invariant (`resolved + unresolved` covers every alias seen in the NPC files, and `db.npcs.len() == loader_npcs.len()`), and move the absolute counts into one clearly labelled data-inventory check, or drop the constants and keep only the consistency comparisons.

- **[low] prototype/osfr-tools/tests/content_npcs.rs:194 regional_npc_batch_and_resolved_job_references_validate - `tagged_fields.len() == npc_fields.len() - 2` pins the NPC record's field count, so any added field fails the test even when its source tag is present.**
  - Why it cannot catch a regression: the real rule is that every non-`source`/`field_sources` field has a tag, and the loop at 195-202 already checks exactly that. The count check fails on churn but adds no coverage.
  - Fix: remove the count assertion and keep the per-field loop at 195-202 (it already fails on any untagged field).
