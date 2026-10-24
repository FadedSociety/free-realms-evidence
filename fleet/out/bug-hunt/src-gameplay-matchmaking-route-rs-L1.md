<!-- fleet job=bug-hunt id=src-gameplay-matchmaking-route-rs-L1 status=nothing_found turns=6 usd=0.0037 tokens(read,write,in,out)=[30960, 14516, 14, 3105] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/matchmaking_route.rs lines 1-34 of 34

Window `prototype/osfr-tools/src/gameplay/matchmaking_route.rs` lines 1-34 (the whole file) reviewed, plus the callee chain it depends on (`matchmaking::handles`, `Listings::from_activities`, `matchmaking::route`, `Packet141`/join constants, `read_u16`/`read_u32`/`check_count`). No defect I can tie to a line and show reachable from client input.

Checked specifically:
- `handle_matchmaking` (line 15-17): `handles()` requires `len >= 3` before `read_u16(inner, 0)`, so the family read cannot go out of bounds. Other handlers in `route` index `inner[2]` only after that gate.
- Join path (`matchmaking.rs:1303-1311`, reached via line 20): the body is length-checked against `JOIN_BODY_PREFIX` (0x10) and the queue id is read at 0x0c through the bounds-checked `read_u32`. The result is a refusal only; no queue, character or session state is written, and the handler takes `&self`. The refusal text is a constant (`matchmaking.rs:1229`), so no client text is echoed.
- Reply sizing: `Listings::from_activities` is built from the server's activity catalogue, not from the packet, and `check_count` caps rows. `queue_stats` sizes its vectors from `rows.len()`, not from client counts.
- Error paths (lines 18-19, 20-21): a malformed packet becomes `invalid(...)`, which the caller propagates. That is the documented intent and it does not partially apply anything.

The only error path I noticed that a client can't trigger is a catalogue with a zero or duplicate battle id, which would make every matchmaking packet fail. That is a server-data problem, not a remote-input defect, so I did not report it.
