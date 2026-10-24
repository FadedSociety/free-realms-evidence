<!-- fleet job=bug-hunt id=src-kart-rewards-rs-L1 status=nothing_found turns=7 usd=0.0100 tokens(read,write,in,out)=[80105, 31204, 16, 10672] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/kart_rewards.rs lines 1-350 of 350

No reportable defects in `prototype/osfr-tools/src/kart_rewards.rs` lines 1-350 after reading the window in full and the callers and dependencies it relies on.

What I checked:

- **Grant authority and price check (252-290):** the award comes only from `RaceSession::claim_reward` on a staged `RaceSession::restore` of the live session's snapshot. It must equal the registry row for the session's own speedway, or the call fails with `ScheduleNotRegistered`. `RaceSession::restore` (`kart_racing.rs:639-698`) accepts every coherent live finished session, so the snapshot round-trip does not refuse legitimate payouts. The `coins == 0 && xp == 0` check at 288 is unreachable because `validate()` rejects empty rows, but it is harmless.
- **Atomicity (292-346):** all mutation goes to clones (`staged_inventory`, `staged_profiles`, `staged_race`). Every fallible step (`checked_add` filters, `grant_coins`, `add_experience`, `reward_bundle_toast`) runs before the three infallible commit assignments at 335-337. A refusal leaves the live session, wallet and XP unchanged, including `reward_claimed`. The gateway (`kart_gateway.rs:724-765`) also stages its own copy and discards it on error.
- **Overflow (213-231, 300-322):** coin and XP overflow are checked in the same way as `Inventory::grant_coins` (`inventory.rs:852-873`) and `Profiles::add_experience` (`profiles.rs:309-329`). Values are range-checked against `i32::MAX` before `as i32` casts at 228-229. `experience_packets` (`profiles.rs:333-363`) uses `1 + xp/100` on a `u32`, which cannot overflow, and clamps rank to 20.
- **Toast layout (224-243):** I counted the pushes. Coins sit at inner offset 4, XP at 8, kind at 16, source and player GUIDs at 40 and 48, and the total is 72 bytes. This matches the doc comments.
- **Client trust:** the only client-derived values are the session's own state (validated in `restore`) and the registry (built from content in `kart_gateway.rs:357-374`). No packet field supplies an amount, price or guid.
- **Registry construction (102-117):** `new()` validates every row and rejects duplicates. `starter_defaults()` skips `validate()`, but its rows are all non-zero and within range. `RewardRegistration` derives `Deserialize`, but no code path deserializes it.

Non-defects noted: the doc on `RewardRegistration::reconstructed` (line 57) says zero values "may not" occur, but the function does not enforce that. `new()` does, and no caller bypasses it, so this is a doc nit only.
