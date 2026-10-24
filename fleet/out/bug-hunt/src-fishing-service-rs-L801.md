<!-- fleet job=bug-hunt id=src-fishing-service-rs-L801 status=nothing_found turns=23 usd=0.0322 tokens(read,write,in,out)=[948207, 71831, 48, 27431] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/fishing_service.rs lines 801-1600 of 1623

No reportable defect in `prototype/osfr-tools/src/fishing_service.rs` lines 801-1600 after reading the window and the callers it depends on.

Checked and cleared:

- **settle_catch unwraps and indexing (885-1022).** `tracked.session.actor().unwrap()` is safe. The reel path requires `session.actor() == Some(actor)` (line 731), and `Session::cancel` only sets the phase to Idle, so the binding survives. `item_definitions[&(key, grade)]` (936) is safe. `choose_grade` only returns a grade whose `bound` flag came from `contains_key` on the same key. `bind_item_definition` (442) only stores positive ids.
- **Atomicity in settle_catch.** Nothing is mutated before a fallible step except `paid.entry(guid)`, which is harmless. The cap is checked before `apply_grant`, which works on a clone. On failure it escapes. `cap_record`, `tracked.rewards`, `attempt` and `session.cancel` all run only after success, with no `?` after them.
- **Cap logic (1025-1049, 1433-1466).** The Hour ledger is bounded: it is pruned, then checked against the limit (at most 3,600) before each push. A disabled or absent cap never records. `restore_hour_history` (494) rejects oversized or unsorted input. Session counts reset on disconnect, which matches "login session". Config validation prevents a zero or absent limit when enabled.
- **Overflow and division.** `select_species` uses `checked_add` and rejects a zero total before `%`. `choose_grade` rejects a zero total before `%`. The lure `u64` multiplication cannot overflow for `u32` inputs. `saturating_*` is used for time and score. `unit` and the mix functions are fine.
- **validate_cast (1234).** Finiteness is checked first. Distance overflow to infinity is rejected by the max check.
- **FishingSpots::parse (1502).** Size is capped at 64 KiB before parsing. Spot count is capped at 16. NPC ids are checked for zero and duplicates. Item values are checked for sign and for at least one positive size. Payout rows are checked for count, order and ceilings.
- **Doc versus code.** The `CatchCap`, `CapWindow`, `choose_grade`, `cap_record` and `is_lifecycle` doc comments match the code.

Considered and dropped (cannot show from this window):

- `select_species` (1260-1273) returns `Err` when no fish in an area is at the player's level or total weight is zero. In `Cast` (outside the window, lines 772-774), `session.request` and `cast_sequence` are mutated before that `?`, which could leave the phase stuck at Casting. This only happens if some shipped area has no fish with `minimum_level` ≤ 1. I did not verify every area roster against `fishing.json`, so I did not report it.
- The `advance()` call at line 752 mutates timers before later `?` returns (outside the window). That needs a client to send Cast during an active attempt, and the effect is a dropped bobber update rather than a payout.
- `applied_grant_keys` duplicate handling in `apply_grant` (rewards.rs:104) could pay nothing for a repeated key. Instance ids are monotonic per service and the reward state is not persisted, so I could not reach a repeat.
