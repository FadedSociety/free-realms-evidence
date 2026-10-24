<!-- fleet job=note-refresh id=Content-Batch-Jobs status=done turns=14 usd=0.0229 tokens(read,write,in,out)=[424530, 61517, 30, 21873] model=claude-haiku-5-5 -->
# notes/Research/Content Batch Jobs.md

**Verdict:** badly stale. The schema-limit claims (`ContentDb` v1 rejects extra fields, `Job` has no name string ID, unlock or gear fields, `Quest` has no name, order or free-text objective field, job ability arrays are empty) still hold. The counts and the artifact/test description have drifted since later tasks (T247, T257, T281, F272, W104, W110) changed the data and the test.

**Corrections:**

1. `old:` The current schema could not serialize these free-text objectives as typed goals, so every JSON `objectives` array is empty.
   `new:` The current schema could not serialize these free-text objectives as typed goals, so most JSON `objectives` arrays are empty; a few quests now carry typed goals, for example the Adventurer quest at `quests/adventurer.json:349` and the `visit_position` goal in `quests/scavenger_hunt.json:9-30`.
   `why:` `repo:prototype/osfr-tools/data/content/quests/adventurer.json:349` and `repo:prototype/osfr-tools/data/content/quests/scavenger_hunt.json:9` are non-empty `objectives` arrays. The batch test also reads talk-objective NPCs at `repo:prototype/osfr-tools/tests/content_jobs.rs:93-96`.

2. `old:` The six serialized numeric grants are 3, 4, 16, 18, 13, and 1 coins (55 total), each in an Adventurer quest row.
   `new:` The quest files now carry 52 non-zero `coins` values across 14 quest files (Adventurer 20, Archer 2, Blacksmith 2, Brawler 6, Chef 1, Fisherman 2, Kart Driver 2, Medic 5, Miner 3, Ninja 1, Postman 1, Scavenger Hunt 1, Warrior 3, Wizard 3). Many Adventurer values are the W110 five-coin fallback marked `(R)`, for example `adventurer.json:12-18`. The 13 and 1 values from the original six are no longer present.
   `why:` `repo:prototype/osfr-tools/data/content/quests/adventurer.json:12,76,208,618,721`; `repo:prototype/osfr-tools/data/content/quests/*.json` (search for `"coins"`); `repo:prototype/osfr-tools/data/content/quests/chef.json:595` and `ninja.json:25,121` carry zero values.

3. `old:` | Adventurer | 58 | 55 | 6 | 58 / 18 / 45 |
   `new:` | Adventurer | 58 | 55 | 20 | 58 / 18 / 45 |
   `why:` `repo:prototype/osfr-tools/data/content/quests/adventurer.json` has 20 non-zero `"coins"` entries (lines 12 through 1569). The quest-row and C/V/W counts were not re-counted, and the other table rows are unverified.

4. `old:` Six quest `title_string_id` fields remain null with a reason in the record evidence: Adventurer "Another Day, Another Coin" (title not found), Medic "A Strong Supplement" (no title ID found), Miner "Speed Smelting" (no live title ID), and three Pet Trainer level rows (wiki-only titles).
   `new:` Sixteen quest `title_string_id` fields are null, with a reason in the record evidence: Blacksmith 2, Brawler 4, Medic 5 (for example "A Strong Supplement" at `medic.json:942-950`), Miner 1 (`miner.json:1493`, "Speed Smelting"), Pet Trainer 3, and Postman 1 (`postman.json:54`, "It's all in the Training"). Adventurer "Another Day, Another Coin" now carries `title_string_id` 5100416 (`adventurer.json:3953`), although its evidence tag at line 3973 still says null.
   `why:` `repo:prototype/osfr-tools/data/content/quests/blacksmith.json:1190,1643`; `brawler.json:2202,2251,2294,2339`; `medic.json:531,887,932,1287,1590`; `miner.json:1493`; `pet_trainer.json:400,717,980`; `postman.json:54`; `adventurer.json:3953`.

5. `old:` - `prototype/osfr-tools/data/content/quests/*.json` (17 files)
   `new:` - `prototype/osfr-tools/data/content/quests/*.json` (18 files: the 17 job files plus `scavenger_hunt.json`, a non-job quest file added by T247/F272)
   `why:` `repo:prototype/osfr-tools/data/content/quests/` lists 18 files; `repo:prototype/osfr-tools/tests/content_jobs.rs:82` asserts a count of 18; `repo:notes/Autopilot/T247.md`, `F272.md` (scavenger hunt added).

6. `old:` The test aggregates the 17 job files into a temporary root package, uses existing fixture zones and empty unrelated datasets, and creates temporary `(R)` NPC rows for the unresolved refs so `ContentDb::load` can validate the real jobs/quests and cross-references.
   `new:` The test aggregates all 18 quest files (17 job files plus `scavenger_hunt.json`) into a temporary root package, uses the fixture zones, builds a synthetic `items.json` from the quest-referenced item IDs, and leaves POIs, dungeons and minigames empty. It creates temporary `(R)` NPC rows for every referenced NPC (resolved or unresolved) so `ContentDb::load` can validate the real jobs/quests and cross-references.
   `why:` `repo:prototype/osfr-tools/tests/content_jobs.rs:26-42` (`referenced_items`), `:82` (18 files), `:141-151` (dataset writes), `:153-186` (rows created for `referenced_npcs`, not just unresolved ones).

7. `old:` The batch test confirms every job trainer and quest giver reference appears in this explicit list.
   `new:` The batch test confirms every job trainer, quest giver and talk-objective NPC reference is either resolved in `npcs/*.json` or appears in `npcs_unresolved.json`.
   `why:` `repo:prototype/osfr-tools/tests/content_jobs.rs:84-122` (resolved set plus `unresolved_ids`, with talk objectives included at lines 92-97).

**Unsure:**

- **Unresolved-reference counts (note line 40).** The file has 465-ish records, which I did not recount. `"name": null` appears 23 times in `repo:prototype/osfr-tools/data/content/npcs_unresolved.json`, not the 51 the note gives. `"zone": null` appears 20 times, not 236. The "no canonical zone" wording may map to a different field (`zone_reason`), so I did not correct it.
- **Loader wording (note line 48).** `ContentDb::load` still reads only a root `quests.json` (`repo:prototype/osfr-tools/src/content.rs:591-602`), so "the unchanged loader" is accurate for that loader. A separate split loader, `QuestEngine::from_split_content` (`repo:prototype/osfr-tools/src/quest_engine.rs:776-785`), reads `quests/` and `npcs/` and was not mentioned.
- **Test status (note line 55).** "passed (1 test, 0 failures)" was not re-run. `tests/content_jobs.rs` has one `#[test]`, and its assertions have changed since the note was written.
- **Quest totals (note line 36).** The table gives 651 quest rows. `repo:notes/Design/Build Ledger.md:86` says 653 quest records, and `repo:notes/Autopilot/F272.md:241` says 654 unique quest records. I did not count the rows.
- **Cited path.** `notes/Build Guides/Gameplay/Items and Inventory.md:143` exists and still lists the job profile IDs (Adventurer 1, Ninja 2, etc.), so that citation holds.
