<!-- fleet job=bug-hunt id=src-abilities-rs-L1 status=nothing_found turns=9 usd=0.0167 tokens(read,write,in,out)=[238444, 45922, 20, 17153] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/abilities.rs lines 1-800 of 1008

No reportable defects in `prototype/osfr-tools/src/abilities.rs` lines 1-800 (read in full, plus 799-860 to finish `definition_reply` and `unsupported_cast`).

What I checked and why each is not a defect:

- **Client-reachable parsers (the only paths a remote player reaches from this window).**
  - `parse_definition_request` (785-790) requires an exact 8-byte inner message; no panic.
  - `definition_reply` (799-811) short-circuits on `m.len() == 160` before `m[4..8]`, so no out-of-bounds index; `id <= 0` is rejected; a forged id returns `None`.
  - `unsupported_cast` (821-837) uses `get(at..at+4)` for each word, so a short packet returns `Err`, not a panic. The `try_into().unwrap()` is on an exact 4-byte slice. Length is checked against 24 or 32 by mode. The served predicate (mode 0, bar 1, slot 0..=7) matches its doc comment and the gateway caller at gameplay.rs:4630.
  - `gameplay.rs:4622-4630` calls these with `inner` and does not mutate state before them.
  - `equipped_weapon_matches` (27-69) uses `row.get(44..48)` and `row.get(52..56)`, so it is bounds-safe and fails closed. Its inputs are server-side equipment state and catalogue values.
- **`use_ability` and its helpers (32-570).**
  - `validate_definition` runs first, so the `expect("catalogue validated")` calls in `apply_one` (669-717) cannot fire.
  - Every mutation (energy, cooldown, casting) happens after all fallible checks, so there is no mutate-then-fail.
  - Subtractions and additions use saturating ops or are bounded by validated ranges.
  - The cooldown boundary (`now_ms < until`) and the tick expiry (`now_ms >= expires`) match their comments.
  - The `unreachable!("validated target")` arm is consistent with `validate_use` returning `MissingTarget` when the target is `None`.
- **`JobEffect::valid` (132-164).** Range checks with inverted bounds (e.g. `500..=duration_ms` when duration < 500) return `false` rather than panic.
- **Catalogue loading (223-335).** Size is capped via `take(MAX+1)`, abilities and effects are capped, and duplicate ids are rejected.
- **`tick_effects` (735-748).** Removal is bounded by the catalogue-sized active-effect map.

Reach note: a grep of `src/` shows `use_ability` has no production caller. Its only src caller is `enemies.rs:554` `use_ability_on_enemy`, which is called only from tests. The live job-ability path goes through `encounter/skills.rs`, outside this window. So the combat-resolution logic in this range is not reachable from a client packet today. Two authored-data nits I noticed but did not report because they need a malformed catalogue and have no reachable path: `Heal` has no `health > 0` guard (apply_one 694-704), and `apply_effects_to_one` ignores `recipient`.
