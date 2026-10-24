<!-- fleet job=bug-hunt id=src-restoration-piece-085-rs-L1 status=nothing_found turns=6 usd=0.0079 tokens(read,write,in,out)=[75306, 26293, 14, 7799] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_085.rs lines 1-570 of 570

## Window: `prototype/osfr-tools/src/restoration/piece_085.rs` lines 1-570

No defect I could tie to a reachable client or save input. Nothing submitted as a finding.

**Reach is the main reason.** This file is not part of any server build path. Its only `#[path]` inclusion is `prototype/osfr-tools/tests/piece_085.rs:41-43`. The live trade code is `prototype/osfr-tools/src/trade.rs` (`offer_item` at :456, `offer_coins` at :523, `validate_offer_item` at :1200), so no packet can reach `TradeSession` or `WireFrame::decode` here.

**Checked and cleared (in case another window revisits them):**
- `WireFrame::decode` (:167-180): the empty check precedes `bytes[0]`, `bytes.get(1)` guards the code byte, and `bytes[2..]` is safe because the `get(1)` succeeded so `len >= 2`.
- `TradeOffer::from_frame` (:271-281) and `TradeUpdateLock::from_frame` (:301-309): the length checks (12 and 5) precede the `try_into().unwrap()` and index reads, so they cannot panic.
- `complete` (:441-514): every fallible step (lock/confirm revision checks, `remove_item`, `remove_coins`) runs on cloned plans before `*host = host_plan; *guest = guest_plan;` at :507-508. Atomicity holds.
- `remove_item` and `remove_coins` (:221-244): they check before subtracting, so no underflow.
- `offer_item` / `offer_coins` (:386-408): `count == 0` / `coins == 0` are rejected. The revision bump is u64 and cannot realistically overflow.
- `confirm` and `complete` stale-lock logic (:422-453): a lock or confirmation is valid only when recorded at the current revision, and any offer change bumps the revision.

**Observations below the reporting bar (not defects as shown):**
- `add_item` / `add_coins` (:216-236) use `saturating_add` after the sender's side has already been debited in `complete`. Coins or items can vanish if a receiver's total exceeds `u32::MAX`. Reaching that needs an implausibly large balance, and this path is test-only.
- `SideOffer.items` (:326-329) has no cap on distinct guids per offer, so repeated `offer_item` calls grow the map. This is also unreachable from a packet here; the live `trade.rs` path is where a cap would matter.
- Doc/behaviour mismatch at :343: "offers may change until both sides lock" disagrees with the code, which allows changes at any time and invalidates locks. The test at `tests/piece_085.rs:246-269` matches the code, so this is documentation only.
