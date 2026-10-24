<!-- fleet job=bug-hunt id=src-inventory-v2-fixes-rs-L1 status=nothing_found turns=3 usd=0.0024 tokens(read,write,in,out)=[7488, 9120, 8, 2383] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/inventory_v2_fixes.rs lines 1-121 of 121

Reviewed `prototype/osfr-tools/src/inventory_v2_fixes.rs` lines 1-121 in full. No defect in this window that I could tie to a line and show is reachable from client input or a save.

What I checked:
- `encode_definition_batch_v2` (35-90): `record[..4]` is guarded by `len < 4` (43-45), so `try_into().unwrap()` at 46 cannot panic. Non-positive ids are rejected both for definitions (47-49) and owned ids (61-63). Duplicate ids with differing bytes are rejected (50-53). Missing owned ids return an error (64-72). Length and count use `checked_add` and `i32::try_from` (74-80), so overflow is handled. No mutation happens before a fallible step, so there is no atomicity problem. The framing (length = 4 + record bytes, count, then records) matches the client reader `FUN_00a3db70`, which reads the count from the first dword after the length and bounds the batch by the length.
- `encode_item_update_v2` (106-121): an encoder with no arithmetic or indexing on untrusted input, so no panic path. Field order matches the doc comment.
- Callers: `coin_shop.rs:670/681` pass an empty owned-id slice, which skips the coverage check. That is by design for those paths and is outside this window. `inventory.rs:625` passes server-side owned ids. I did not find a client-controlled path into either encoder from this file.

Observations outside my window, not reported as findings: the notes say `InventoryItem` only carries a 32-bit last-cast field, so the 38/3 integration is incomplete. That is a caller-side concern, not a defect in these lines.
