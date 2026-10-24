<!-- fleet job=test-audit id=tests-kart-gateway-rs-L1 status=done turns=9 usd=0.0087 tokens(read,write,in,out)=[114936, 28503, 20, 7979] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_gateway.rs lines 1-222 of 222

Window: `prototype/osfr-tools/tests/kart_gateway.rs` 1-222. Code under test read: `src/kart_gateway.rs` (load 223-300, accepts_close 449-461, rebuild_entry 499-527, begin 543-579, initialize 580-603) and `src/kart_entry.rs` (on_register 650-687, handle_inner 628-646).

- **[high] tests/kart_gateway.rs:127 entry_rebinds_known_slots_and_preserves_quaternion_and_return - the name's "rebinds known slots" is never checked: no assertion that the owned GUID reaches the vehicle attribute block or the progress racer rows.**
  - Why it cannot catch a regression: `rebuild_entry` (src/kart_gateway.rs:509-521) writes `owned` into `entry_vehicles[0].attribute_block[start..start+8]` and rewrites `progress.racer_guid` / `tail_0x29`. The test takes `started` from `handle_entry(&register(1))` (line 149) and only checks its length (150) and a 33/5 slice (151-152). Deleting the rebind loop, or writing the wrong GUID, leaves every assertion here green. The 33/11 vehicle frame (`started[1]`) and the 33/14 progress frames (`started[2..]`) are never inspected.
  - Fix: assert that `started` contains a `[33,0,<vehicle subtype>,0]` frame whose bytes at `vehicle_guid_offset` (+4 for the inner header, per the encoder) equal `1u64.to_le_bytes()`, and that each 33/14 frame carries racer_guid 1 at its GUID offset. Compare against literal `1u64`, not against values read back from the code.

- **[medium] tests/kart_gateway.rs:151-152 entry_rebinds_known_slots_and_preserves_quaternion_and_return - the 33/5 "register words" check is zero-versus-zero and cannot detect a missing echo.**
  - Why it cannot catch a regression: `on_register` (src/kart_entry.rs:676-677) overwrites `client_data[77..85]` with `register.word_8` and `word_12`. The fixture's `client_data` is `vec![0; 85]` (line 97) and `register(1)` (lines 120-125) sends zero words. So `data[81..89] == [0;8]` also holds if the copy is deleted or uses the wrong word, since the original bytes are already zero.
  - Fix: build the register with non-zero words (e.g. `word_8 = 0xA5A5_0001`, `word_12 = 0x5A5A_0002`) and assert `data[81..85]` and `data[85..89]`-equivalent bytes equal those literals. Also make the fixture `client_data` non-zero at 77..85 so an unchanged original cannot satisfy the check.

- **[medium] tests/kart_gateway.rs:209 original_close_is_bound_to_the_live_encounter_and_exact_width - "exact width" is only tested in the short direction, and the `-1` tail is never mutated.**
  - Why it cannot catch a regression: `accepts_close` (src/kart_gateway.rs:453-460) requires `inner.len() == 15` and `inner[7..15] == [255;8]`. The test only sends a 3-byte packet (line 219). Changing the check to `inner.len() < 15`, or dropping the `inner[7..15]` comparison, still passes every assertion, because the only mutation (line 217) changes the encounter word.
  - Fix: add `packet.push(0)` (16 bytes) and assert `is_err()`. Set one byte of `packet[7..15]` to 0 and assert `!accepts_close(...)` (or `is_err` for width). Keep the existing encounter-id mutation.

- **[low] tests/kart_gateway.rs:145-147 entry_rebinds_known_slots_and_preserves_quaternion_and_return - the "repeated" expectation re-applies the production transform to the code's own output.**
  - Why it cannot catch a regression: `repeated` is `init[0]` with `len-15..+4` zeroed, which is the same offset rule as `initialize` (src/kart_gateway.rs:600-601). If the production offset moved and the test's `- 15` were updated in step, or if both diverged in a way that still matches, nothing outside this test notices. It is a restatement, not an independent expectation.
  - Fix: assert the literal activity-id bytes. Check that `init[2][len-15..len-11] == [0;4]` and that `init[2]` and `init[0]` differ in exactly those 4 bytes.

- **[low] tests/kart_gateway.rs:132 entry_rebinds_known_slots_and_preserves_quaternion_and_return - "preserves quaternion" is checked on one component of a fixture value.**
  - Why it cannot catch a regression: only `scene.rotation[3] == 0.` (line 132) is asserted. The fixture rotation is `[0,0,1,0]` (line 61), so the x, y and z components, which are the actual quaternion, are never compared to `character()` or the content. Corrupting `rotation[0..3]` in `begin` passes.
  - Fix: assert `scene.rotation == [0.,0.,1.,0.]` (the literal fixture values) so any component change fails.

No `#[ignore]`, no early returns on missing fixtures, and the error-path tests at 160-206 do check state or `is_err` on real inputs.
