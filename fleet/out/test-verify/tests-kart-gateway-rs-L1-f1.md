<!-- fleet job=test-verify id=tests-kart-gateway-rs-L1-f1 status=done turns=8 usd=0.0072 tokens(read,write,in,out)=[102718, 24225, 18, 6263] model=claude-haiku-5-5 -->
# high: tests/kart_gateway.rs:127

**Verdict:** `confirmed`

**Evidence:** I could not refute the claim. Walking the test against the mutation "delete the rebind loop in `rebuild_entry`" (src/kart_gateway.rs:514-521, or the write at 512-513), every assertion in `entry_rebinds_known_slots_and_preserves_quaternion_and_return` (tests/kart_gateway.rs:127-159) still passes:

- Line 131 `begin` succeeds. Without the loop, `KartEntryHandler::new` (src/kart_entry.rs:497-514) still accepts the content: racer_guid 123 is nonzero and unique, and the vehicle block is nonempty.
- Lines 132-135 check the scene quaternion and the `begin` reply bytes. Neither depends on the rebind.
- Lines 136-147 check `initialize()`. It returns `details`, `enter`, `ready` and `status`. None of these carries the vehicle block or progress rows (src/kart_gateway.rs:580-603).
- Line 148 `handle_entry(&register(123))` is empty. Without the rebind, `own_session(123)` against `context.session == 1` returns `ForeignSession`, which `handle_entry` maps to `Ok(Vec::new())`, so the assertion still holds.
- Line 149 `handle_entry(&register(1))` succeeds. `own_session` checks only `context.session`, which `begin` sets to 1 (src/kart_gateway.rs:558), not the rebound rows. The on_register path (src/kart_entry.rs:650-687) emits config, one vehicle, client data and one progress frame, so `started.len() == 4` at line 150 holds.
- Line 151-152 check only the 33/5 frame's bytes 81..89 against zeros. The register words are zero and the client data is copied verbatim, so the rebind does not affect them.

A wrong-GUID mutation (for example writing `old` instead of `owned`) is also invisible for the same reasons. The test never reads `started[1]` (33/11) or `started[2..]` (33/14). Load-time ownership proof (src/kart_gateway.rs:281-290) runs on the unmodified content before `begin`, so it does not catch this either.

**Correction to the suggested fix:** the offset `+4` is wrong. `encode_inner` emits a 4-byte header (src/kart_entry.rs:421-427). The 33/11 body is `u32 name_len | name | f32 | attribute_block` (src/kart_entry.rs:176-182). The GUID therefore sits at `4 + 4 + body_asset.len() + 4 + vehicle_guid_offset` in `started[1]`. The 33/14 GUID is at payload offset 0 (`PROGRESS_GUID_OFFSET = 0x00`, src/kart_progress_native.rs:59), so it sits at frame bytes `4..12` in each of `started[2..]`. Derive the vehicle offset from the fixture's `body_asset` length rather than hard-coding it.

**Minimal fix:** after line 149, assert `started[1][4 + 4 + "test.cdt".len() + 4..][..8] == 1u64.to_le_bytes()` (or equivalently use the computed attribute offset), and assert `started[2..]` each have `[4..12] == 1u64.to_le_bytes()`.
