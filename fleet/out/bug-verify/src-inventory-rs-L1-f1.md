<!-- fleet job=bug-verify id=src-inventory-rs-L1-f1 status=done turns=7 usd=0.0071 tokens(read,write,in,out)=[72046, 22311, 16, 7109] model=claude-haiku-5-5 -->
# medium: `src/inventory.rs:701-704`

**Verdict:** confirmed (narrower than claimed, and lower severity)

**Severity if confirmed:** low. The effect is a wrong tint on a worn piece, and the granted copy is left unequipped. No items, coins, crash or save corruption follow, so the "medium" rating overstates it.

**Evidence**

- *Module tree (step 1):* `lib.rs` has `pub mod gameplay;`, `pub mod gateway;`, `pub mod identity;`, `pub mod inventory;`. `gameplay.rs:50` has `mod jobs;`. The code is live, not test-only.
- *The defect is real:* `inventory.rs:692-704`. `equip_owned_definition` finds `.find(|i| i.definition_id == definition_id)` with no tint check, then calls `equip(item.id, ..., None)`. `grant_with_tint` (`inventory.rs:997-1005`) matches on `tint`, so a tint-0 grant can create a new instance next to an existing tint-5 one. `validate_state` (`inventory.rs:715-731`) allows that, since it only checks id uniqueness.
- *Reachable copies:* a tinted copy can come from the store, `coin_shop.rs:946` (`grant_with_tint(0, sale.item_id, wanted, sale.tint)`).
- *Reach, narrowed:*
  - `jobs.rs:56` is the real case. With `reuse_owned == false` (`jobs.rs:47-56`), the code grants `grant(0, definition, 1)` and then calls `equip_owned_definition`, which can pick the older tinted copy. This path is reached with `false` from `gameplay.rs:4832-4835` (`apply_opening` `unlock_profiles`) and `npc.rs:876`.
  - `gameplay.rs:5256-5259` (`apply_identity`) is also real: it does `grant_with_tint(0, def, 1, tint_id)` then `equip_owned_definition(def, 1)`. It runs once per character, guarded by `identity_fingerprint`.
  - `jobs.rs:47` (`reuse_owned == true`) is intended to reuse whatever is owned, so it is not a mismatch.
  - `jobs.rs:105` (`ensure_outfit`) grants only when no instance of the definition exists (`jobs.rs:99-104`). Nothing was just granted, so it cannot pick a different instance from "the one just granted". It is at most the same ambiguity when duplicates already exist.
- *Consequence:* `equip` (`inventory.rs:1215-1273`) writes the chosen item's tint into the reply and the visible attachment (`write_attachment(..., item.tint, ...)`). So the wrong tint is shown, and the granted copy stays in the bag, unequipped.

**Corrected fix:** the claimed fix is sound. Give `equip_owned_definition` a tint parameter and match on `definition_id && tint`. Call it with `0` at `jobs.rs:56` (after `grant(0, …)`, a tint-0 instance is guaranteed to exist), and with `attachment.tint_id` at `gameplay.rs:5259`. Leave `jobs.rs:47` and `jobs.rs:105` on the first-owned behaviour, or pass `0` there deliberately. Do not describe `jobs.rs:105` as a grant-mismatch case.
