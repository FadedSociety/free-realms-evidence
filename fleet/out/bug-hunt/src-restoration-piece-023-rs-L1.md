<!-- fleet job=bug-hunt id=src-restoration-piece-023-rs-L1 status=nothing_found turns=5 usd=0.0046 tokens(read,write,in,out)=[39090, 21819, 12, 2965] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_023.rs lines 1-337 of 337

Reviewed `prototype/osfr-tools/src/restoration/piece_023.rs` lines 1-337 in full. I found no defect that meets the criteria, and I am not reporting any findings.

What I checked:

- **Decoder bounds (`decode_permissions`, 172-197):** `count` is rejected when negative or above `MAX_PERMISSION_ENTRIES` (4096) before the `count * 16` multiplication, so there is no overflow. The length check precedes `chunks_exact(16)`, and the `try_into().expect` calls operate on fixed-size slices, so they cannot panic. Allocation is capped by the 4096 bound.
- **Encoder (157-169):** the `entries.len() as i32` cast is safe because the length is capped at 4096 first.
- **Error decoder (205-213):** the length is checked before the 4-byte read, and trailing bytes are rejected.
- **Role logic (271-337):** the owner check runs first, and the first matching listed entry decides the role. `visitor_cap_reached` uses `>=`, which is correct for a cap. The owner is exempt from the cap as documented. The integer types are unsigned and only compared, so there is no arithmetic that can overflow.
- **Tests (`tests/piece_023.rs` 40-200):** the test vectors agree with the code and its doc comments.

Reach: the only callers of this module's API are in `tests/piece_023.rs` (via `#[path]` include). `grep` found no use from the server, the gateway, or `housing_service.rs`. Production housing access goes through `housing.rs:867` (`can_enter`) and does not call into this module. So none of these functions is currently reachable from a client packet. Any defect I might have raised would be latent, and I did not find one even as a latent defect.
