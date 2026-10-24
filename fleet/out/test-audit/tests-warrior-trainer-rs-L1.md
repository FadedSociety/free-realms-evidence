<!-- fleet job=test-audit id=tests-warrior-trainer-rs-L1 status=done turns=5 usd=0.0076 tokens(read,write,in,out)=[55661, 28532, 12, 7039] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/warrior_trainer.rs lines 1-674 of 674

Window reviewed: `prototype/osfr-tools/tests/warrior_trainer.rs` lines 1-674 (whole file). Most assertions are real: the reload test compares full gameplay JSON, the refusal tests compare byte-exact saves, and the rank/learn checks run through the production `Profiles::learn`. The findings below are the gaps I could confirm.

- **[medium] tests/warrior_trainer.rs:598-610 and 649-653 `warrior_unlock_survives_reload` - the "package with starter items must equip the outfit" branch never runs in this repo, so the equip assertions are dead code.**
  - Why it cannot catch a regression: `starter_items` reads `profiles.json` from the copied content dir and returns empty when the file is absent. The bundled `data/content` has no `profiles.json`, per the provenance note in `scripts/fixtures/starter_items.json`. The test therefore always takes the `starter.is_empty()` branch. A change that stops granting or equipping the starter outfit on a populated package (the `else` branch: `equipped > 0`, no "unavailable" text, no duplicate outfit on re-learn) would still pass. The `profiles.json` file is copied into the temp dir only if the reference content has one; I did not confirm that.
  - Fix: build the temp content with a test-owned `profiles.json` that has `starter_items["32"]` set to a real item id, and assert the populated branch unconditionally. Keep the empty branch as a separate test, and do not branch on whatever file happens to be present.

- **[medium] tests/warrior_trainer.rs:656-674 `non_warrior_trainers_do_not_offer_warrior` - the name says "trainers" (plural), but only the Blacksmith (`SMITH`) is checked.**
  - Why it cannot catch a regression: a change that makes any other non-Dewey trainer (e.g. Archer, Medic, or a row whose profile is Warrior) also offer "Become a Warrior" would pass, because only one NPC is clicked.
  - Fix: load every row from `trainers(&content)` where `npc != DEWEY`, click each, and assert that its menu has no `BECOME_A_WARRIOR` option. Or rename the test to say it covers only the Blacksmith.

- **[low] tests/warrior_trainer.rs:519, 524, 579 `refused_learn_changes_nothing` - the forged-option, other-NPC and out-of-range `choose` calls discard their result with `let _ =`.**
  - Why it cannot catch a regression: the state comparison would still pass if the gateway returned `Err` (an io error) or a reply that should not be sent, such as an "already known" line or a success line that is not committed. The reply is never checked, only the save document.
  - Fix: unwrap the result and assert the refusal text (or assert `!changed` / `!gameplay_changed`) for each of the three cases, so the test proves the refusal, not only the absence of a change.

- **[low] tests/warrior_trainer.rs:382 `dewey_is_drawable_and_has_a_warrior_trainer_row` - the source-text check pins prose and ids ("412471", "5100388", "Level 20 Brawler", "(R)") in the trainer's documentation string.**
  - Why it cannot catch a regression: it is not a behaviour check. Rewording the documentation, or changing the client gate id that the row cites, breaks the test without any change to what Dewey does. The actual requirement (a Warrior row that cites the guide) is only partly covered by `Warrior.md`.
  - Fix: assert the structured fields (profile, job, label, requirement) that the loader uses, and check the source only for the guide name, or drop the prose needles.
