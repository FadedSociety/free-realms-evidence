<!-- fleet job=test-audit id=tests-piece-091-rs-L1 status=done turns=9 usd=0.0095 tokens(read,write,in,out)=[146336, 31472, 20, 8289] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_091.rs lines 1-469 of 469

Reviewed `prototype/osfr-tools/tests/piece_091.rs` lines 1-469 against `src/restoration/piece_091.rs`. Nothing in the window is a tautology or a silent skip: the `#[path]` fixture exists, the sample values in `captain_zeus()` match the preserved `PacketSendSelfToClient.json` (Groom 82.37982, Unknown10 103980, TextureAlias "lightmark-chocolate"), and the hand-written byte offsets at lines 265-274 check out against `PetRecord::encode`. The findings below are the real gaps.

- **[medium] tests/piece_091.rs:408 utility_and_follow_requests_need_an_active_pet - the guid-mismatch refusal is checked only by its error, and the refused request carries the same `in_water: 1` already stored, so the state check cannot see a mutation.**
  - Why it cannot catch a regression: if `apply` wrote `state.in_water = in_water` (or any follow field) before calling `check_active_guid`, the refused `InWater { in_water: 1 }` would leave the stored value at 1 and the test would still pass; the test never reads `follow_state()` after line 410.
  - Fix: send the refused request with a different value (for example `in_water: 0`) and assert `session.follow_state().map(|s| s.in_water) == Some(1)` after the `GuidMismatch` error, plus the same check for the `CanGoLocation` position.

- **[medium] tests/piece_091.rs:465 roster_snapshot_round_trips_every_owned_pet - the duplicate-id case uses two identical `captain_zeus()` records and asserts only `roster_len() == 1`, so the documented "collapse to their first record" behaviour is not tested.**
  - Why it cannot catch a regression: an implementation that keeps the last duplicate, or that keeps whichever record it visits last, or dedups by something other than id, still yields length 1 with these inputs.
  - Fix: use two records with the same `unknown` but different `pet_name` (or `food`) and assert the surviving roster entry equals the first one, e.g. `CompanionSession::new(vec![a, b]).roster() == [a]` with `a != b`.

- **[low] tests/piece_091.rs:254 recorded_pet_record_round_trips_byte_exactly - the name promises a byte-exact round trip, but the body never decodes the encoded bytes and re-encodes them, and never compares against the recorded sample bytes.**
  - Why it cannot catch a regression: the test checks `decoded == record` and a few fixed offsets; a decode path that normalises a field (for example a string or flag) and an encode path that writes it differently in a way that still matches the struct compare would pass, and the claim of "byte exact" is not what is tested.
  - Fix: add `let (again, _) = PetRecord::decode(&encoded)?; assert_eq!(again.encode(), encoded);` (or rename the test to `recorded_pet_record_round_trips_through_its_own_layout`). If the byte-exact claim is wanted, also assert the encoding equals the sample's serialized bytes, which are not in the test today.

- **[low] tests/piece_091.rs:126 recovered_packet_family_uses_the_client_base_opcode - the `PET_PACKET_SUBTYPES.len() == 35` pin is a count on a fixed-size array that churns when any subtype row is renamed or added and says nothing about the opcode the test is named for.**
  - Why it matters: this is an over-pinned incidental detail; adding a reviewed subtype row fails the opcode test for an unrelated reason.
  - Fix: drop the count assertion (the array's type already fixes the length) or move it into a dedicated table-size test; keep the opcode and name checks here.
