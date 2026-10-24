<!-- fleet job=test-audit id=tests-pets-rs-L1 status=done turns=6 usd=0.0052 tokens(read,write,in,out)=[62649, 18219, 14, 4619] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/pets.rs lines 1-615 of 615

Window: `prototype/osfr-tools/tests/pets.rs` lines 1-615. Read in full, plus `src/pets.rs` (summon guard at 885-896, `advance_roster` decay at 1530-1552, `PetContent::definition` at 235-248) to confirm behaviour.

- **[medium] prototype/osfr-tools/tests/pets.rs:519-527 species_catalog_has_field_sources_and_resolved_or_unresolved_item_ids - the final `resolved + unresolved == sum of adoption_source lengths` check cannot fail.**
  - Why it cannot catch a regression: every adoption entry in the loop (lines 485-504) increments exactly one of the two counters on every path, so the sum equals the iteration count by construction. Changing how `item_ids` is resolved, dropping an item from the catalogue, or mis-classifying a row still passes, because the counters only ever sum to the loop count.
  - Fix: assert against an independent expectation, e.g. a hard-coded count of rows whose `store_item_id` resolves in `startup.json`, or assert that every `store_item_id` that is present in `item_ids` is counted as resolved (`resolved_item_ids == expected_resolved`), so a change to the resolution logic is detected.

- **[medium] prototype/osfr-tools/tests/pets.rs:402-420 minigame_busy_rule_rejects_summon_without_mutation - the name promises "without mutation", but the only state check is `active_pet_id() == None`.**
  - Why it cannot catch a regression: the body never snapshots the pet. A change in the summon path that mutates the pet before returning the busy error (for example, advancing `updated_at`, changing `needs`, `position`, or `equipment`, or writing the roster) still passes, since `active_pet_id` stays `None`. The guard at `src/pets.rs:894` happens to be first, which is why the test passes today, but the test would not detect it moving.
  - Fix: take `let before = service.pet(pet_id).unwrap().clone();` (or serialize the roster via `save_to` and read the bytes) before the rejected call, then assert `service.pet(pet_id).unwrap()` equals `before` after the error, in addition to the `active_pet_id` check.

- **[low] prototype/osfr-tools/tests/pets.rs:596-599 client_pet_bindings_exist_and_species_ids_are_unique - the final `species_ids.len() == species.len()` check is redundant and cannot fail on its own.**
  - Why it cannot catch a regression: `assert!(species_id > 0 && species_ids.insert(species_id))` at line 557 already fails on any duplicate, and the set is only filled there, so the set size always equals the row count when the loop completes. The "unique" claim is therefore carried by line 557 alone, and the end-of-test assertion adds nothing.
  - Fix: keep the line 557 check, and drop or re-base the final assertion on an independent figure (for example, a pinned expected species count, or the count of rows whose `species_id` is present in `PetContent::bundled()`), so it can fail when rows are added or dropped without updating the test.

- **[low] prototype/osfr-tools/tests/pets.rs:611 every_bound_pet_model_has_a_models_txt_id - the hard-coded `models.len() == 26` is an incidental count.**
  - Why it is churn, not a missed bug: any content edit that adds or removes a bound species (or a model-less row) breaks this test even when every model still has a `Models.txt` id, which is the property the test name claims. The count is about the catalogue size, not the id lookup.
  - Fix: assert `models` is non-empty and keep the `model_id(model) > 0` loop, or move the count into a separate content-size test with a clear name.
