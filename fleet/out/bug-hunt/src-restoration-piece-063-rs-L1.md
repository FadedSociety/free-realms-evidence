<!-- fleet job=bug-hunt id=src-restoration-piece-063-rs-L1 status=nothing_found turns=5 usd=0.0048 tokens(read,write,in,out)=[36867, 18066, 12, 4351] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_063.rs lines 1-376 of 376

Window `prototype/osfr-tools/src/restoration/piece_063.rs` lines 1-376 (whole file) read in full. No defect I could tie to a line and show reachable from client input or a save.

What I checked:
- `parse_minigame_header` (l.140-151): the length guard (`< MINIGAME_HEADER_LEN`, 13) runs before every index, and `bytes[13..]` is safe after it. No panic.
- `has_duplicates` (l.373-376), `open` (l.236-272), `finish` (l.278-301), `pending` (l.304-313), `claim` (l.317-335), `completed` (l.343-349): no unwrap on client data. The two `expect("run checked above")` calls (l.290, l.332) are guarded by a `get` on the same key just before, so they are internal invariants, not client-reachable.
- Atomicity: every refusal in `open`, `finish` and `claim` returns before any mutation. `finish` sets `run.finished` and inserts into `finished` with no fallible step between them. `claim` inserts into `claimed` only on the success path. No half-applied state.
- Replay: `finish` refuses a second completion (l.287-289), `open` refuses a finished id forever (l.252-254), and `claim` refuses a second claim per player (l.329-331). These match the doc comments.
- Header layout: 1 + 3×4 = 13 bytes, matching the doc's `u8 sub | i32 state | i32 group | i32 game`.

Reach: the module is not registered in the crate. `grep` for `piece_063` and `DungeonRewardLedger` under `src/` finds only its own file (the `#[path]`/`pub mod` integration is a pending lead step, as in the sibling pieces). Nothing in the server calls `open`, `finish`, `claim` or `parse_minigame_header` yet. Without a caller, no client packet reaches these functions.

Things I considered and dropped:
- No cap on `participants` length or on the number of runs in `runs`/`finished`. The inputs come from the caller, not from a packet, and no client path reaches `open` today. This is a risk for the integration step, not a present defect.
- `RewardBundle` (coins, items) is caller-supplied by design, per the module doc, so it is not client-trusted here.
- `completed` returns the full roster regardless of claims. This matches the doc comment ("Every member whose completion was recorded").

Recommendation for integration (not a finding): when the 39/46 handler is wired, the player id passed to `claim` must come from the session, not the packet, and `finish`'s `actor` likewise. Neither check exists in this file, so the wiring step must add them.
