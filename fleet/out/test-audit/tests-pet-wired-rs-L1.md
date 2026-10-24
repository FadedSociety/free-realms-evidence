<!-- fleet job=test-audit id=tests-pet-wired-rs-L1 status=done turns=5 usd=0.0045 tokens(read,write,in,out)=[30804, 13584, 12, 5002] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/pet_wired.rs lines 1-268 of 268

Window `prototype/osfr-tools/tests/pet_wired.rs` 1-268. Three findings; the rest of the window (roster listing, summon/seen/dismiss, foreign-request no-mutation, gateway actor clear) checks literal bytes or state and I found no defect there.

- **[medium] prototype/osfr-tools/tests/pet_wired.rs:128 `removal_packet` (used at :153 and :207) - the expected removal frame is built by calling the production `pet_removal_packet`, so the helper compares the code under test with its own output.**
  Why it cannot catch a regression: `pets.rs:1684` builds `[35,0,3,0,1,0] + actor LE + [0;17]`. If someone changes that opcode, subtype, or padding, both sides change together and `removal_packet` still returns true. The only removal-shape check in the file is the gateway test at :265, and it covers only the first six bytes, not the actor or trailing bytes.
  Fix: compare against a literal frame in the test, e.g. `let mut want = vec![35,0,3,0,1,0]; want.extend(actor.to_le_bytes()); want.extend([0;17]);`, so a change to `pet_removal_packet` fails the test.

- **[medium] prototype/osfr-tools/tests/pet_wired.rs:198 `zoning_dismisses_without_persisting_the_actor_and_reload_keeps_roster` - the name claims zoning does not persist the actor, but the test never saves after `settle_pets`, so the reload passes trivially.**
  Why it cannot catch a regression: the file at `save.path` is the one written by `Save::new()` (before any summon). `settle_pets` (gameplay.rs:2139) only changes in-memory `self.pets`, so the reload assertions at :213-215 hold even if the dismissed active actor were written to disk by `save_pet_roster`/`save_to`. Nothing in the test is a write-then-reload of the post-zoning state.
  Fix: after line 208, call `game.save_pet_roster(&save.path).unwrap()`, read the JSON, and assert the active-pet field is absent or cleared (matching the schema `pets.rs` writes). Then reload and assert `pet_view(1).is_none()`. Alternatively, rename the test to drop the "without persisting the actor" claim.

- **[low] prototype/osfr-tools/tests/pet_wired.rs:233-239 `an_accepted_name_is_written_to_the_top_level_pet_payload` - the reload only checks that a 53/5 roster packet exists, not that the name survived.**
  Why it cannot catch a regression: the 53/5 roster packet is sent whatever the roster contents, so a `save_pet_roster` that drops the name on the reload path would still pass. The name is checked only in the raw JSON at :231, not after a round trip through `load_pet_roster`.
  Fix: after `reloaded.load_pet_roster(&save.path)`, assert `reloaded.pet_view(1).unwrap()` carries name "Admiral Ace" (or inspect the roster's name field through the wire reply), so the reload depends on the renamed value.</result>
