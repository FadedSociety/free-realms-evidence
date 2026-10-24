<!-- fleet job=bug-hunt id=src-progression-extras-rs-L1601 status=nothing_found turns=9 usd=0.0077 tokens(read,write,in,out)=[94218, 23071, 20, 7686] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/progression_extras.rs lines 1601-1686 of 1686

Reviewed `prototype/osfr-tools/src/progression_extras.rs` lines 1601-1686 (plus callers in `handle_claim_request`, `definitions_response`, `issue_server_grant`, `from_saved`, `list_response`, and `rewards::apply_grant`). No defect I could tie to a line and show reachable from a client packet or save.

Checked and dropped:
- `parse_definitions_request` (1602-1616): length checks run before any index. `count <= MAX_CLAIM_ITEMS` short-circuits before `count * 4`, so no overflow. `bytes[..2]` and `bytes[2..4]` are safe because `len >= 12` is checked first. Duplicate ids are accepted, and the comment at `definitions_response` (1303-1305) documents that as intended.
- `encode_claim_array` (1618-1633): `MAX_PACKET_BYTES - 9` cannot underflow (the constant is 1 MiB). The size bound leaves room for the 5-byte `list_response` header and the 9-byte `handle_claim_request` header, so the packet stays within the bound.
- `merge_grants` (1635-1659): `grants[1..]` is safe because `first` already errors on an empty slice. Coins and per-profile XP use `checked_add`. Items and display rows are bounded by at most 256 server-issued pending grants, each validated by `issue_server_grant`/`from_saved`. The merge is built on a local clone, so a failure leaves no state changed. Dropping the non-first grants' display header fields is display-only, not a defect under the criteria.
- `claim_grant_key` (1661-1675): ids come from `handle_claim_request`, which rejects duplicates and unknown ids before this call. Sorting fixed-width u64s gives an injective byte string, so distinct id sets yield distinct keys.
- `promotional_packet` (1679-1686): the `body.len() <= MAX_PACKET_BYTES` check ignores the 4-byte header, so the total can exceed the bound by 4 bytes. However, the only callers are in `tests/progression_extras.rs`, and the body is server-serialized, not client input. Not reachable as a defect.

`handle_claim_request` (1216-1290) also has no mutation before a fallible step: `records` is computed before the pending/claimed/trackers mutation, and nothing after that mutation can fail.
