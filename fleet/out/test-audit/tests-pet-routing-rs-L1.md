<!-- fleet job=test-audit id=tests-pet-routing-rs-L1 status=done turns=5 usd=0.0075 tokens(read,write,in,out)=[60729, 24070, 12, 7833] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/pet_routing.rs lines 1-818 of 818

Reviewed `prototype/osfr-tools/tests/pet_routing.rs` lines 1-818 against `src/pets.rs` (`PetService::handle`, `handle_with_inventory`, `insert_pet`/`MAX_PETS`) and `src/bin/osfr_gateway/pet_wire.rs`. Most tests are sound: the summon/dismiss, refusal, roster-cap, save/reload and speed tests compare against independent constants or pre-action snapshots, and the `summon_by_item` second argument is a tint, so the "wrong tint" test name is accurate. Three findings:

- **[medium] pet_routing.rs:443 a_selected_name_updates_only_the_active_pet_and_refusals_change_nothing - the name claims "updates only the active pet", but the test owns exactly one pet (`owned_pet` at line 446), so no other pet exists to be wrongly renamed.**
  - Why it cannot catch a regression: a rename implementation that writes the name to every pet in the roster, or to the first pet rather than `active.pet_id`, still passes, because the only pet is both active and the one checked at lines 461, 489 and 509. `rename_selected(active.pet_id, ...)` in `pets.rs:1055` is never shown to ignore other pets.
  - Fix: adopt a second pet (`adopt_vendor_grant(2, ...)`), summon only the first, rename, and assert the second pet's `name` is unchanged, along with the first's being "Admiral Ace". Or rename the test to drop the "only the active pet" claim.

- **[low] pet_routing.rs:622-649 decode_pet_list (used by the reload test at line 551 and the adoption test at line 334) - the favourite, utility, item and string fields are read and then discarded or only checked for finiteness, so the decoded value is never compared.**
  - Why it cannot catch a regression: the four per-record floats are only checked with `is_finite()` (line 622), and the `pet.items`, `pet.favorites` and `pet.utilities` vectors (lines 633, 645-648) are never asserted. A server change that writes wrong favourite or utility dwords, or a wrong item row, still passes, because only consumption length and id, species, name and tricks are checked.
  - Fix: assert the expected favourite and utility dwords (for a freshly adopted pet, the zeros or the `pets.rs` defaults), assert `pets[0].items` and the float values against the values `pets.rs` writes, and assert the second string and flags explicitly rather than just reading them.

- **[low] pet_routing.rs:392 an_owned_adoption_item_can_create_and_summon_a_roster_pet - the inventory check is `after < before`, which passes for any decrease, including one that consumes two certificates or a stack the grant did not touch.**
  - Why it cannot catch a regression: a redemption that consumes two items, or consumes more than one unit per adoption, still satisfies `after < before`. The test name claims a single adoption, and the adjacent test at line 311 shows the exact pattern (`2 - pet`) already used in this file.
  - Fix: assert `after == before - 1` (or the exact expected count) so that a double-consumption or wrong-stack change fails.
