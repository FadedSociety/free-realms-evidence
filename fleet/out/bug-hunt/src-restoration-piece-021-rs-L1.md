<!-- fleet job=bug-hunt id=src-restoration-piece-021-rs-L1 status=nothing_found turns=6 usd=0.0064 tokens(read,write,in,out)=[49670, 23044, 14, 6125] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_021.rs lines 1-408 of 408

## piece_021.rs lines 1-408: no reachable defect found

I read the whole window (1-300 and 301-408) and the call sites that matter, and found nothing that meets the defect rules.

**Reach.** `PropertyAcquisition`, `AcquisitionRequest` and `set_station_cash` have no production callers. `search` finds them only in `prototype/osfr-tools/tests/piece_021.rs` (included via `#[path]`) and in the notes. `notes/Research/Pieces/021 Property acquisition.md` says the module is not yet registered in `src/lib.rs`. No packet handler, save loader or client-facing path reaches `acquire` or `from_json`, so none of the client-input defects apply to this window today.

**Checked and cleared:**
- `acquire` (235-330): every fallible check (owner, property lookup, already-owned, channel, membership, starter flag, price lookup, balance) runs before the first mutation at 309-319. The `MembershipClaim && !members_only` branch at 259 cannot fire, because `validate_property` (381) rejects that combination at load. `available - charge` (311) cannot underflow because `charge > available` is refused at 301.
- `validate_property` (333-408): the duplicate-deed check spans properties through the shared `deeds` map, and the within-property check uses `local`. The duplicate-id check runs before insert. A failure mid-load aborts the whole catalogue, so no partial state escapes.
- The `member` flag (267, 290) is a request field, and the module checks nothing against membership. That is a trust point only if a future caller passes client input unverified. The module's own doc comments put this with the lead's economy layer, so I did not report it.

**Not reported (not client-reachable):**
- `validate_property`:373, `price.regular * (100 - MEMBER_DISCOUNT_PERCENT)` is an unchecked u64 multiply. For `regular` above about 2.0e17 it overflows, which panics in debug builds. The input is the local recovered catalogue file, not client or save data, and no production loader exists.
- The discount floor at 373 accepts `regular` 1 to 11 with `member` 0. No such row exists, and the check is catalogue-data policy, not a defect.
