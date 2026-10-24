<!-- fleet job=bug-hunt id=src-restoration-piece-091-rs-L1 status=nothing_found turns=7 usd=0.0096 tokens(read,write,in,out)=[128393, 34385, 16, 7967] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_091.rs lines 1-785 of 785

## Window: `prototype/osfr-tools/src/restoration/piece_091.rs` lines 1-785

No reportable defect in this window. I read all 785 lines and checked the callers.

**Reach.** The module is not compiled into the server. `notes/Research/Pieces/091 Pets and companions.md:19` says it is "Not registered in `src/lib.rs`", and `notes/Autopilot/F114.md:100` calls it "a separate, unrouted reference codec". The only consumer is `prototype/osfr-tools/tests/piece_091.rs:35-37`, which `#[path]`-includes it. The live pet route is `src/pets.rs` (`PetRequest::decode` at pets.rs:1027 and 1107), which is a different type. So no client packet reaches `PetRequest::decode`, `PetRecord::decode`, or `CompanionSession::apply` in the running server.

**Checked and not defects:**
- **Panics on client bytes.** `PetRequest::decode` indexes only after exact length checks: subtype 4 at lines 206-224 (len 5 and len 1), subtype 32 at 226, subtype 26 at 239 (len 17, so `body[16]` and the `index*4+3` reads are in range), subtype 28 at 261. The `word` closure at 197-204 is only called after those checks. `Reader::take` (507-518) uses `checked_add` and bounds-checks. `Reader::string` (544-557) and `count` (534-542) bound the length or count against the remaining body before use. `from_utf8` returns an error, not an unwrap.
- **Unbounded allocation.** `Vec::with_capacity(trick_count)` (419), `guid_count` (434) and `item_count` (439) are capped by `count(element_size)`, which requires `count * element_size <= remaining`. The `count * 37` product cannot overflow a 64-bit `usize`. It could overflow on a 32-bit target, but the server is 64-bit and the module is unrouted, so I did not report it.
- **Atomicity.** Every `CompanionSession` method validates before it mutates. `apply` (716-751) calls `check_active_guid` before `get_or_insert`. `summon`, `recall` and `forced_dismiss` have no fallible step after their state writes.
- **Trust.** The owned-pet check happens in `summon` (672), and the non-zero guid check happens in `summon` (675). Follow and interaction traffic is checked against the active guid (`check_active_guid`, 775-784). No value in this file grants items, coins or a price.
- **Doc and test contradictions.** The subtype table, the `PetRequest::decode` refusal of unrecovered layouts (270), and the `summon`/`recall`/`interact` rules match their doc comments and the tests in `tests/piece_091.rs` (lines 360-469).

**Noted but not reported (not a defect that can be tied to a reachable input):**
- `F114.md:100-103` says the live route no longer accepts the one-byte forced-dismiss body, but this file still decodes it as `ForcedDismiss` (lines 215-216). The note records this as a known artifact of the unrouted codec.
- `apply` (line 723) ignores `item_id` for `SummonByItemId`. Ownership is still checked on `pet_id`, and the live route handles subtype 32 separately in `pets.rs:1098`.
- Client-sent `ForcedDismiss` (line 725) is accepted without a guid check. The effect is limited to dismissing the sender's own pet.
